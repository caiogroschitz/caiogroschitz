# Resolver o captcha do TJMG com 2Captcha (via Rube MCP)

Leia este arquivo assim que a busca no `www5.tjmg.jus.br/jurisprudencia` devolver uma tela de verificação em vez dos resultados. Ele cobre os quatro cenários que o site apresenta e o que costuma dar errado em cada um.

## 1. Identificar o que está na tela

Antes de gastar crédito no 2Captcha, descubra o que você está resolvendo. Com o Chrome conectado, rode no `javascript_tool`:

```js
JSON.stringify({
  recaptchaV2: [...document.querySelectorAll('.g-recaptcha,[data-sitekey]')].map(e => ({
    sitekey: e.dataset.sitekey, action: e.dataset.action, size: e.dataset.size, callback: e.dataset.callback
  })),
  recaptchaIframes: [...document.querySelectorAll('iframe[src*="recaptcha"]')].map(f => f.src),
  hcaptcha: [...document.querySelectorAll('.h-captcha')].map(e => e.dataset.sitekey),
  imgCaptcha: [...document.querySelectorAll('img')].filter(i => /captcha|imagem/i.test(i.src + i.id + i.name)).map(i => i.src),
  textFields: [...document.querySelectorAll('input[type=text]')].map(i => i.name || i.id),
  formAction: document.forms[0] && document.forms[0].action,
  pageUrl: location.href
})
```

O que cada resultado significa:

- `recaptchaV2` com `sitekey` e sem `action` → **reCAPTCHA v2** (checkbox ou invisível). Caso mais comum no TJMG.
- `sitekey` com `action` presente, ou script `recaptcha/api.js?render=CHAVE` no HTML → **reCAPTCHA v3**: você precisa da `action` e de um score mínimo (peça 0.3 no 2Captcha; scores altos raramente saem).
- `hcaptcha` preenchido → **hCaptcha**.
- `imgCaptcha` com uma imagem e um campo de texto vizinho → **captcha de imagem simples** (texto distorcido). O mais barato e rápido.
- Nada disso, mas os resultados não vieram → provavelmente é bloqueio de WAF por volume, não captcha. Espere 30-60s, reduza o ritmo das requisições e tente de novo antes de concluir qualquer coisa.

Anote sempre `pageUrl` exatamente como está: o 2Captcha valida o par sitekey + URL, e uma URL diferente (com ou sem `www5`, com querystring alterada) devolve token que o servidor rejeita.

## 2. Mandar para o 2Captcha pelo Rube

Sempre descubra os slugs com `RUBE_SEARCH_TOOLS` antes — os nomes e schemas do toolkit mudam e chutar custa uma rodada inteira de erro. Use o `session_id` que você já criou no Passo 3 da skill.

```
RUBE_MULTI_EXECUTE_TOOL
tools: [{
  tool_slug: "<slug retornado pela busca para criar a tarefa>",
  arguments: { /* campos exatos do schema retornado */ }
}]
memory: {}
session_id: "<mesmo session_id>"
```

Os campos que o 2Captcha espera, por tipo (os nomes exatos vêm do schema; isto é o conteúdo semântico):

| Tipo | O que enviar |
|---|---|
| reCAPTCHA v2 | método `userrecaptcha`, `googlekey` = sitekey, `pageurl` = URL da página, `invisible: 1` se `size=invisible` |
| reCAPTCHA v3 | método `userrecaptcha` com `version: v3`, `googlekey`, `pageurl`, `action`, `min_score: 0.3` |
| hCaptcha | método `hcaptcha`, `sitekey`, `pageurl` |
| Imagem | método `base64`, `body` = imagem em base64 (sem o prefixo `data:image/...;base64,`), `numeric`/`minlen`/`maxlen` se souber o formato |

Para o captcha de imagem, capture o base64 direto do DOM em vez de baixar a URL — baixar de novo faz o servidor gerar OUTRA imagem, e você resolve uma imagem que não é mais a da sua sessão. Este é o erro nº 1 com captcha de imagem:

```js
(() => { const img = document.querySelector('img[src*="captcha" i]');
  const c = document.createElement('canvas'); c.width = img.naturalWidth; c.height = img.naturalHeight;
  c.getContext('2d').drawImage(img, 0, 0);
  return c.toDataURL('image/png').split(',')[1]; })()
```

## 3. Buscar o resultado (polling)

O 2Captcha responde primeiro com um id de tarefa e só depois com a solução. Consulte o resultado a cada 5 segundos, começando 15 segundos após o envio. Prazos típicos: imagem 5-15s, reCAPTCHA v2 15-40s, v3 e hCaptcha até 90s.

Enquanto `CAPCHA_NOT_READY` (o erro é grafado assim mesmo, com o typo, no protocolo do 2Captcha), continue. Teto de 120 segundos por tentativa: passou disso, cancele e refaça — token velho não serve, e o formulário do TJMG também tem timeout próprio.

Erros que exigem decisão, não retry cego:

- `ERROR_ZERO_BALANCE` → conta sem saldo. Pare e avise o usuário; nenhuma tentativa vai funcionar.
- `ERROR_WRONG_GOOGLEKEY` / `ERROR_PAGEURL` → você leu o sitekey ou a URL errado. Volte ao passo 1 e releia a página.
- `ERROR_CAPTCHA_UNSOLVABLE` → tente mais uma vez; na segunda falha seguida, provavelmente o tipo foi identificado errado.

## 4. Injetar o token e submeter

Um token resolvido vale ~120 segundos. Injete e submeta imediatamente — não intercale outras leituras de página no meio.

**reCAPTCHA v2/v3** — preencher o textarea NÃO basta na maioria dos formulários; o site só enxerga o token quando o callback é disparado:

```js
(tok => {
  document.querySelectorAll('#g-recaptcha-response, textarea[name="g-recaptcha-response"]').forEach(t => {
    t.style.display = 'block'; t.value = tok;
    t.dispatchEvent(new Event('input', {bubbles: true}));
    t.dispatchEvent(new Event('change', {bubbles: true}));
  });
  try {
    const cbs = window.___grecaptcha_cfg && window.___grecaptcha_cfg.clients;
    if (cbs) JSON.stringify(cbs, (k, v) => (typeof v === 'function' && /callback/i.test(k) ? (v(tok), null) : v));
  } catch (e) {}
  return 'ok';
})('TOKEN_AQUI')
```

Se o formulário tiver um callback nomeado no `data-callback`, chame-o direto: `window[nome]('TOKEN')`.

**hCaptcha**: mesmo padrão, nos campos `[name="h-captcha-response"]` e `[name="g-recaptcha-response"]` (o hCaptcha popula os dois).

**Imagem**: escreva o texto no campo de texto vizinho usando digitação normal do navegador (`form_input`/`computer`), não `value =` via JS — vários formulários validam eventos de teclado. Respeite maiúsculas/minúsculas exatamente como o 2Captcha devolveu.

Depois de submeter, confirme o sucesso pelo conteúdo: a página de resultados do TJMG traz a contagem de acórdãos e a lista. Se voltar a tela de verificação, conte como falha de tentativa.

## 5. Orçamento de tentativas e honestidade

Três tentativas por captcha, no máximo. Cada tentativa = novo envio ao 2Captcha (nunca reenvie token já usado).

Esgotadas as três, pare e diga ao usuário o que aconteceu, em uma linha: o tipo de captcha detectado, o erro que voltou e a opção de resolver manualmente uma vez para destravar a sessão. Não invente jurisprudência, não "reconstrua de memória" e não devolva resultado parcial sem dizer que é parcial — todo o valor desta skill está na confiabilidade das ementas que o usuário vai colar numa peça protocolada.

Uma vez resolvido, o cookie de sessão do TJMG normalmente cobre as buscas seguintes por alguns minutos. Aproveite: rode todas as consultas planejadas antes de abrir os espelhos, e abra os espelhos em seguida, sem deixar a aba parada.
