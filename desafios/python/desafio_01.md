# Teste Técnico Python – Acelera Jornada de Dados

## Objetivo

Você recebeu um arquivo chamado `funcionarios.csv` com informações de colaboradores de uma empresa.

Sua missão é:

1. **Validar os dados** de cada registro.
2. **Calcular o bônus final** de cada funcionário válido usando a fórmula:

```
BONUS_BASE = 1000
bonus_final = BONUS_BASE + salario * bonus_percentual
```

3. **Gerar relatórios**:

   * `relatorio_individual.csv`: somente registros válidos com o cálculo de `bonus_final`.
   * `erros.csv`: registros inválidos com o motivo do erro.
   * `kpis.json`: métricas agregadas, contendo:

     * quantidade de funcionários por área
     * média de salário por área
     * bônus total geral
     * top 3 funcionários com maior bônus final

---

## Dataset de Entrada (`funcionarios.csv`)

```csv
id,nome,area,salario,bonus_percentual
1,Ana Souza,Vendas,4500,0.1
2,Bruno Lima,TI,7000,0.05
3,Carla Mota,Financeiro,0,0.2
4,Daniel 9,TI,5200,0.1
5,,RH,3800,0.15
6,Elisa Prado,Financeiro,6100,-0.05
7,Fernando Dias,Vendas,4800,0.07
8,João Silva,Operações,5300,abc
9,Maria Alves,TI,6100,0.12
10,Pedro Santos,Operações,5100,0.08
```

---

## Regras de Validação

* **Nome**: não pode estar vazio e não pode conter números.
* **Área**: deve estar entre `Vendas`, `TI`, `Financeiro`, `RH`, `Operações`.
* **Salário**: número positivo ou zero.
* **Bônus percentual**: número entre `0` e `1` (inclusive).

---

## Dicas para Resolver

* **Leitura de CSV**: `csv.DictReader`
* **Laços e condições**: `for`, `while`, `if/elif/else`
* **Conversão de tipos**: `int()`, `float()`
* **Tratamento de erros**: `try/except`
* **Manipulação de strings**: `.strip()`, `.isdigit()`
* **Ordenação**: `sorted()` para encontrar top 3 bônus
* **Exportação de arquivos**:

  * CSV: `csv.DictWriter`
  * JSON: `json.dump()`

---

## Extra (Opcional)

Se quiser, você pode resolver parte do desafio com **pandas**:

```python
import pandas as pd

df = pd.read_csv("funcionarios.csv")

# cálculo direto
df["bonus_final"] = 1000 + df["salario"] * df["bonus_percentual"]

# agregações
media_por_area = df.groupby("area")["salario"].mean()
```

---

## Critérios de Avaliação

* ✅ Validação correta das regras
* ✅ Geração dos arquivos solicitados (`relatorio_individual.csv`, `erros.csv`, `kpis.json`)
* ✅ Clareza e organização do código
* ✅ Uso de boas práticas de Python (tratamento de erros, laços, condições)
* ⭐ Bônus: uso de bibliotecas como **pandas** para simplificar etapas