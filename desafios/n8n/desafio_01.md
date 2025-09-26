# Teste Técnico n8n – Agente Financeiro (Telegram + Google Sheets + ChatGPT)

## Resolução

Recomendo que você assista ao vídeo abaixo somente após tentar entender e resolver o desafio sozinho:

[https://www.youtube.com/watch?v=E3V31nWF0Ws&t=3388s](https://www.youtube.com/watch?v=E3V31nWF0Ws&t=3388s)

## Objetivo

Você deve criar um **agente no n8n** que converse via **Telegram** e seja capaz de:

1. **Classificar a mensagem recebida** automaticamente como:

   * **Registro de despesa** (ex.: “gastei R$180 no Uber ontem”)
   * **Consulta de despesas** (ex.: “quanto eu gastei ontem?”)

2. **Executar a ação correspondente**:

   * **Registro**: extrair **data, valor, descrição, categoria, projeto, forma de pagamento**; gravar no **Google Sheets**; responder no Telegram com uma confirmação curta.
   * **Consulta**: interpretar filtros (ex.: ontem/hoje/semana/mês, categoria, projeto, forma de pagamento), **consultar o Google Sheets**, calcular total ou listar itens e responder no Telegram com um **resumo analítico**.

---

## Dataset de Entrada (Google Sheets)

Crie a planilha **Financeiro** com a aba **`lancamentos`** contendo as colunas:

```
id | data(YYYY-MM-DD) | descricao | categoria | projeto | forma_pagamento | valor | origem
```

* `data` no formato **YYYY-MM-DD**
* `valor` número decimal positivo
* `origem` pode ser “bot”

**Mensagens exemplo (para testes):**

**Registro**

* “Gastei R$180 com Uber para uma reunião do projeto CRM. Paguei no Pix hoje de manhã.”
* “Assinei o Figma por R$99 para o projeto de redesign do app. Pagamento com cartão ontem.”
* “Almoço com cliente do projeto Jornada, R$150. Dinheiro.”

**Consulta**

* “Quanto eu gastei ontem?”
* “Me mostra quanto gastei com cartão?”
* “Quais foram as despesas no projeto CRM?”

---

## Regras de Validação

* **Classificação** deve retornar apenas duas intenções: **INSERIR** ou **CONSULTAR**.
* **Registro**:

  * Se a data não for informada, usar **hoje**; se disser “ontem”, subtrair 1 dia.
  * Converter valores com vírgula para decimal (ex.: “32,90” → 32.90).
  * Categoria/projeto/forma de pagamento podem ter um **padrão** (“Outro” / “Geral” / “Não informado”) se ausentes.
* **Consulta**:

  * Converter períodos relativos (ontem/semana/mês) em datas exatas.
  * Responder **uma frase** clara e humana (ex.: “Você teve 3 despesas ontem, total de R$ 245,90.”).
  * Em listagens, limitar a **até 5 itens**.

---

## Dicas para Resolver

* **Entrada**: use **Telegram Trigger** para capturar a mensagem.
* **Classificação de intenção**: **OpenAI Chat Model + Text Classifier** para decidir INSERIR/CONSULTAR.
* **Ramo INSERIR**:

  * Um segundo passo de **extração** (LLM) para estruturar `data, valor, …`.
  * **Google Sheets → Append Row** para gravar na aba `lancamentos`.
  * **Telegram → Send Message** com confirmação curta (tom humano).
* **Ramo CONSULTAR**:

  * Um **planner** (LLM) para transformar a pergunta em **filtros** (período/categoria/projeto/forma).
  * **Google Sheets → Read** e **Filter/Code/Calculator** para somar/contar/listar.
  * **Telegram → Send Message** com resumo analítico.
* **Guardrails**: manter o escopo **financeiro**, responder educadamente quando a mensagem não for compreensível e sempre usar datas corretas (ontem ≠ hoje).
* **Credenciais**: configurar **OpenAI**, **Google Sheets (OAuth)** e **Telegram Bot**.

---

## Extra (Opcional)

* **Memória** simples do usuário (nome/projeto recorrente) para personalizar respostas.
* **KPIs** em uma segunda aba (contagem por categoria/projeto, soma mensal).
* **Comando /ajuda** no Telegram com exemplos de uso.
* **Filtro por forma de pagamento** (ex.: “com cartão”, “Pix”).

---

## Critérios de Avaliação

* ✅ Fluxo completo e estável: Telegram → Classificar → (Inserir | Consultar) → Resposta no Telegram
* ✅ Escrita/leitura corretas no **Google Sheets**
* ✅ Respostas **claras, curtas e humanas**
* ✅ Regras de validação aplicadas (datas/valores/limites)
* ⭐ Bônus: memória, KPIs, filtros adicionais e organização dos nós (nomes e comentários)
