# Teste Técnico SQL – Funções de Ranking (ROW_NUMBER, RANK e DENSE_RANK)

## Objetivo

Entender e aplicar as diferenças entre as funções de janela **ROW_NUMBER()**, **RANK()** e **DENSE_RANK()**.
Essas funções são fundamentais para resolver problemas de classificação e segmentação em SQL, e aparecem com frequência em entrevistas técnicas.

Sua missão é:

1. **Gerar rankings de usuários** com base em uma métrica (quantidade de e-mails enviados).
2. Comparar os resultados usando `ROW_NUMBER()`, `RANK()` e `DENSE_RANK()`.
3. Explicar **a diferença prática** entre os três métodos.

Essa foi uma pergunta da prova do Google.
Veja a original [aqui](https://medium.com/@aggarwalakshima/interview-question-asked-by-google-and-difference-among-row-number-rank-and-dense-rank-4ca08f888486).

---

## Dataset de Entrada (`google_gmail_emails`)

| id | from_user | to_user | day |
| -- | --------- | ------- | --- |
| 1  | ana       | bruno   | 1   |
| 2  | ana       | carlos  | 1   |
| 3  | bruno     | daniela | 1   |
| 4  | carlos    | ana     | 2   |
| 5  | ana       | daniela | 2   |
| 6  | bruno     | carlos  | 2   |
| 7  | ana       | erica   | 3   |

---

## Pergunta de Entrevista (Google)

> **“Encontre o *email activity rank* de cada usuário. O rank é definido pelo total de e-mails enviados. O usuário com mais e-mails enviados recebe rank 1. Se houver empate, os usuários empatados recebem o mesmo rank. Compare a diferença entre ROW_NUMBER, RANK e DENSE_RANK.”**

---

## Regras de Validação

* O **usuário com mais e-mails enviados** deve estar no topo (`rank = 1`).
* Em caso de empate:

  * **ROW_NUMBER()** → sempre gera valores únicos (não permite empate, usa a ordem alfabética como desempate).
  * **RANK()** → mantém empates, mas **pula posições** (ex.: 1, 1, 3).
  * **DENSE_RANK()** → mantém empates, mas **não pula posições** (ex.: 1, 1, 2).

---

## Dicas para Resolver

* Use `COUNT(*)` com `GROUP BY from_user` para calcular o total de e-mails enviados por cada usuário.
* Aplique cada função de ranking em uma **CTE** com `OVER (ORDER BY total_emails DESC, from_user ASC)`.
* Compare os resultados lado a lado para ver a diferença entre elas.

---

## Critérios de Avaliação

* ✅ Consulta correta para contar e-mails enviados por usuário.
* ✅ Uso das três funções de ranking (`ROW_NUMBER`, `RANK`, `DENSE_RANK`).
* ✅ Explicação clara da diferença prática entre os resultados.
* ⭐ Bônus: aplicação em outro contexto (clientes, produtos, categorias).

---

👉 Esse desafio é clássico de entrevistas. Entender a diferença entre `ROW_NUMBER`, `RANK` e `DENSE_RANK` é essencial para qualquer profissional de dados.

---

Quer que eu monte um **exemplo de saída esperada** (tabelinha com usuários e os três rankings lado a lado) para o dataset acima, mostrando a diferença de cada função?
