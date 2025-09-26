# Teste Técnico AWS – Streamlit no EC2 com Kaggle + S3

### Objetivo

Criar um **dashboard em Streamlit** que rode em uma instância **EC2** e utilize um dataset baixado do **Kaggle** como fonte de dados, armazenando e lendo os arquivos a partir de um **bucket S3**.

### Tarefas

1. Escolher **um dataset do Kaggle** (ex.: Bitcoin, Netflix, World Happiness).
2. Subir o dataset bruto para um bucket S3 (`s3://acelera-dados/<dataset>`).
3. Criar um app **Streamlit** que:

   * Leia os dados do S3 (via `boto3`).
   * Mostre **KPIs** básicos.
   * Exiba pelo menos **1 gráfico interativo** (linha, barras ou dispersão).
   * Permita **upload de CSV** → salva no mesmo bucket/prefixo em `uploads/`.
4. Colocar o app no ar em uma instância **EC2** (porta 8501).

### Dataset

#### 🔹 1. **Bitcoin Historical Data**

👉 [Bitcoin Historical Data – Kaggle](https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data)

* **Colunas**: Date, Open, High, Low, Close, Volume, Market Cap
* **O que fazer no Streamlit**:

  * KPI: preço médio diário, volume total
  * Gráfico de **linha** do preço de fechamento ao longo do tempo
  * Upload de um CSV atualizado → grava no S3

---

#### 🔹 2. **Netflix Movies and TV Shows**

👉 [Netflix Movies and TV Shows – Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)

* **Colunas**: title, director, cast, country, date_added, release_year, rating, duration, listed_in
* **O que fazer no Streamlit**:

  * KPI: total de títulos, número de países, ano mais comum
  * Filtro interativo por **country** e **release_year**
  * Gráfico de barras por categoria/ano

---

#### 🔹 3. **World Happiness Report**

👉 [World Happiness Report – Kaggle](https://www.kaggle.com/datasets/unsdsn/world-happiness)

* **Colunas**: Country, Region, Happiness Score, GDP per Capita, Freedom, Generosity, etc.
* **O que fazer no Streamlit**:

  * KPI: país mais feliz, média global
  * Gráfico de dispersão GDP vs Happiness Score
  * Upload de CSV → novo ranking gravado no S3

### Requisitos

* Usar **IAM Role** na EC2 (sem chaves hardcoded).
* App acessível em `http://<EC2_PUBLIC_IP>:8501`.
* Código versionado no GitHub com `README.md` explicando setup.

### Critérios de Avaliação

* ✅ Streamlit funcionando no EC2
* ✅ Leitura/escrita no S3
* ✅ KPIs e gráficos corretos
* ✅ Upload → salva no bucket
* ⭐ Bônus: filtros interativos, presigned URL para download, dashboard visual caprichado