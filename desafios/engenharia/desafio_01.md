# Teste Técnico Engenharia de Dados – Docker + Airflow (ETL Bitcoin)

## Objetivo

Criar uma **pipeline ETL** com **Airflow (em Docker)** que coleta o **preço do Bitcoin** a cada **15 minutos** e salva os resultados em uma camada persistente.

A pipeline deve conter as etapas:

1. **Extrair**: consultar a API da Coinbase:

   * `https://api.coinbase.com/v2/prices/spot`

2. **Transformar**:

   * Capturar os campos: `valor`, `criptomoeda`, `moeda`
   * Adicionar um campo `timestamp` (data/hora da coleta).

3. **Carregar**:

   * Gravar em **uma dessas opções**:

     * **CSV particionado** por data (`data/bitcoin/dt={{ ds }}/btc.csv`)
     * **S3/MinIO** (`s3://crypto/bitcoin/dt={{ ds }}/btc.csv`)
     * **Postgres** (Render ou Supabase) em tabela `bitcoin_dados` com colunas:
       `id, valor, criptomoeda, moeda, timestamp`.

---

## Requisitos Técnicos

* **Airflow rodando via Docker** (webserver, scheduler, metadata DB).
* Criar um **DAG com 3 tasks** (`extract`, `transform`, `load`).
* **Agendamento**: `schedule_interval="*/15 * * * *"` (a cada 15 minutos).

---

## Dicas

* Teste primeiro seu código Python localmente (como no script que você montou).
* Transforme cada função (`extrair`, `tratar`, `salvar`) em uma **task do Airflow** com `PythonOperator`.
* Para salvar em **Postgres** no Airflow, crie uma **Connection** (`Conn Id: bitcoin_pg`) com credenciais.
* Para CSV, monte um volume no Docker (`./data:/opt/airflow/data`).
* Para S3/MinIO, configure credenciais no Airflow Connections (`aws_default`).

---

## Extra (Opcional)

* Adicionar checagens de qualidade (ex.: valor > 0, moeda = "USD").
* Publicar a DAG no GitHub e deixar pronta para rodar com `docker compose up`.

---

## Critérios de Avaliação

* ✅ DAG funcional e agendada a cada 15 minutos.
* ✅ Extração correta da API da Coinbase.
* ✅ Transformação com `timestamp` adicionado.
* ✅ Persistência (CSV, S3 ou Postgres).
* ✅ Logs claros no Airflow.
* ⭐ Bônus: checks de qualidade, integração com S3/Postgres, DAG bem documentada no README.

---

👉 Esse desafio mostra que o candidato sabe **usar Docker, orquestrar no Airflow, lidar com API externa e persistir dados** — ou seja, cobre o ciclo básico de **engenharia de dados JR**.