# Teste Técnico Python 02 – Acelera Jornada de Dados

## Contexto

Este desafio **evolui o Desafio 01**. Agora você vai aplicar **funções** e **logs** — dois pilares essenciais na **engenharia de dados** (manutenção, observabilidade e depuração).

## Objetivo

Transformar a solução do `funcionarios.csv` em uma **ETL modular** com **logs estruturados (loguru)**:

1. **Ingestão**

   * Ler `funcionarios.csv`.
   * Registrar em log: início, fim, caminho do arquivo e **quantidade de linhas lidas**.

2. **Transformação**

   * Validar cada registro (mesmas regras do Desafio 01).
   * Calcular `bonus_final` para válidos usando:

     ```
     BONUS_BASE = 1000
     bonus_final = BONUS_BASE + salario * bonus_percentual
     ```
   * Registrar em log: **válidos x inválidos**, principais motivos de erro e um **resumo dos Top 3 bônus**.

3. **Salvamento**

   * Gerar:

     * `relatorio_individual.csv` (válidos + `bonus_final`)
     * `erros.csv` (inválidos + `motivos`)
     * `kpis.json` (qtd por área, média de salário por área, bônus total, top 3 bônus)
   * Registrar em log: **arquivos gerados**, caminhos e **linhas gravadas**.

---

## Estrutura esperada (esquemático)

```
etl_funcionarios/
├─ ingestion.py   # funções de leitura
├─ transform.py   # validações + cálculo do bônus + KPIs (funções puras)
├─ save.py        # funções de escrita CSV/JSON
├─ main.py        # orquestra ingest → transform → save e configura o loguru
└─ requirements.txt
```

---

## Regras de Validação (mesmas do Desafio 01)

* **Nome**: não vazio e sem números.
* **Área**: uma de `Vendas`, `TI`, `Financeiro`, `RH`, `Operações`.
* **Salário**: número ≥ 0.
* **Bônus percentual**: número em `[0, 1]`.

---

## Dicas para Resolver

* Escreva **funções pequenas e reutilizáveis** (ex.: `parse_row`, `validate_row`, `compute_bonus`, `build_kpis`).
* Configure o **loguru** para console **e** arquivo (`logs/etl_{data}.log`) com rotação.
* Logue **contagens por etapa** (lidas, válidas, inválidas, escritas), **tempo** e **amostras de erros**.
* Organize saídas em `./output/` e mantenha nomes claros dos arquivos.

---

## Critérios de Avaliação

* ✅ **Evolução clara** do Desafio 01 com **módulos**: `ingestion`, `transform`, `save`, `main`.
* ✅ Uso consistente de **funções** (sem lógica “espalhada” no `main`).
* ✅ **Logs com loguru**: úteis, legíveis e com informações de progresso/erros.
* ✅ Saídas corretas: `relatorio_individual.csv`, `erros.csv`, `kpis.json`.
* ⭐ Bônus: métricas de tempo no log, contagem por motivo de erro, mensagens de log padronizadas.

> Meta: demonstrar que você sabe **estruturar** uma ETL simples e **torná-la observável** — competências fundamentais para quem segue para engenharia de dados.
