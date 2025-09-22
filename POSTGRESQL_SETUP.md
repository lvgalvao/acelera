# 🚀 Configuração do PostgreSQL (Supabase)

Este guia explica como configurar a conexão direta com PostgreSQL para o projeto Jornada de Dados.

## 📋 Pré-requisitos

1. Conta no [Supabase](https://supabase.com)
2. Python 3.8+ instalado
3. Dependências instaladas: `pip install -r requirements.txt`

## 🔧 Configuração do PostgreSQL

### 1. Criar Projeto no Supabase

1. Acesse [supabase.com](https://supabase.com)
2. Faça login ou crie uma conta
3. Clique em "New Project"
4. Preencha os dados do projeto:
   - **Name**: `jornada-dados` (ou o nome que preferir)
   - **Database Password**: Crie uma senha forte
   - **Region**: Escolha a região mais próxima
5. Clique em "Create new project"

### 2. Obter Credenciais de Conexão

1. No dashboard do projeto, vá em **Settings > Database**
2. Na seção **Connection Pooling**, copie as informações:
   - **Host**: `aws-1-us-east-2.pooler.supabase.com` (exemplo)
   - **Database name**: `postgres`
   - **Port**: `6543` (para connection pooling)
   - **User**: `postgres.zhyycmjndgewmolilfmx` (exemplo)
   - **Password**: Sua senha do banco

### 3. Criar Tabela no Banco

1. No dashboard do Supabase, vá em **SQL Editor**
2. Copie e cole o conteúdo do arquivo `database/schema.sql`
3. Clique em "Run" para executar o script

### 4. Configurar Credenciais

#### Opção 1: Arquivo .env (Recomendado)

1. Crie um arquivo `.env` na raiz do projeto:
```env
user=postgres.zhyycmjndgewmolilfmx
password=[YOUR-PASSWORD]
host=aws-1-us-east-2.pooler.supabase.com
port=6543
dbname=postgres
```

2. Substitua `[YOUR-PASSWORD]` pela sua senha real do banco

#### Opção 2: st.secrets (Para produção)

1. Crie um arquivo `.streamlit/secrets.toml`:
```toml
[postgresql]
user = "postgres.zhyycmjndgewmolilfmx"
password = "sua-senha-aqui"
host = "aws-1-us-east-2.pooler.supabase.com"
port = "6543"
dbname = "postgres"
```

#### Opção 3: Configuração Manual (Para desenvolvimento)

1. Execute o aplicativo: `streamlit run main.py`
2. No sidebar, expanda "Configurar Credenciais"
3. Preencha todos os campos com as informações do banco
4. Clique em "Salvar Configurações"

## 🧪 Testar a Conexão

Execute o script de teste para verificar se tudo está funcionando:

```bash
python test_connection.py
```

Este script irá:
- ✅ Testar conexão direta com psycopg2
- ✅ Testar PostgreSQLClient
- ✅ Testar QuestionarioRepository
- ✅ Verificar se a tabela existe
- ✅ Contar registros existentes

## 🗄️ Estrutura da Tabela

A tabela `respostas_questionario` possui os seguintes campos:

- `id`: ID único (auto-incremento)
- `timestamp`: Timestamp da resposta (ISO format)
- `respostas`: Respostas do questionário (JSON)
- `trilhas_recomendadas`: IDs das trilhas recomendadas (JSON)
- `trilhas_nomes`: Nomes das trilhas recomendadas (JSON)
- `created_at`: Data de criação do registro
- `updated_at`: Data da última atualização

## 🔍 Verificação da Configuração

1. Execute o aplicativo: `streamlit run main.py`
2. Vá para a página do Questionário
3. Verifique se aparece "✅ Status: Conectado" nas estatísticas
4. Faça um teste respondendo o questionário

## 🛠️ Solução de Problemas

### Erro de Conexão
- Verifique se as credenciais estão corretas no arquivo `.env`
- Confirme se está usando **Connection Pooling** (porta 6543)
- Verifique se o projeto está ativo no Supabase

### Erro de Tabela
- Execute o script SQL em `database/schema.sql`
- Verifique se a tabela foi criada corretamente

### Erro de Importação
- Execute: `pip install -r requirements.txt`
- Verifique se o Python está na versão 3.8+

### Erro de Permissão
- Verifique se o usuário tem permissão para INSERT/SELECT
- No Supabase, vá em **Authentication > Policies**

## 📊 Funcionalidades Disponíveis

- ✅ Salvar respostas do questionário
- ✅ Contar total de respostas
- ✅ Buscar respostas por período
- ✅ Estatísticas em tempo real
- ✅ Interface de configuração integrada
- ✅ Teste de conexão automatizado

## 🔒 Segurança

- Use **Connection Pooling** para melhor performance
- Mantenha as credenciais seguras e não as versionem no Git
- Configure políticas RLS (Row Level Security) se necessário
- Use variáveis de ambiente para produção

## 🚀 Executar a Aplicação

```bash
# Instalar dependências
pip install -r requirements.txt

# Testar conexão
python test_connection.py

# Executar aplicação
streamlit run main.py
```

## 📝 Exemplo de Uso

```python
from database import QuestionarioRepository

# Inicializar repositório
repo = QuestionarioRepository()

# Salvar resposta
respostas = {"goal": "migrar_area", "sql_level": "basico"}
trilhas = ["n8n", "sql", "python"]
nomes = ["Trilha n8n", "Trilha SQL", "Trilha Python"]

success = repo.salvar_resposta(respostas, trilhas, nomes)

# Contar respostas
total = repo.contar_respostas()
print(f"Total de respostas: {total}")
```
