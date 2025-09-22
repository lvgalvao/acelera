# 🚀 Configuração do Supabase

Este guia explica como configurar o Supabase para o projeto Jornada de Dados.

## 📋 Pré-requisitos

1. Conta no [Supabase](https://supabase.com)
2. Python 3.8+ instalado
3. Dependências instaladas: `pip install -r requirements.txt`

## 🔧 Configuração do Supabase

### 1. Criar Projeto no Supabase

1. Acesse [supabase.com](https://supabase.com)
2. Faça login ou crie uma conta
3. Clique em "New Project"
4. Preencha os dados do projeto:
   - **Name**: `jornada-dados` (ou o nome que preferir)
   - **Database Password**: Crie uma senha forte
   - **Region**: Escolha a região mais próxima
5. Clique em "Create new project"

### 2. Obter Credenciais

1. No dashboard do projeto, vá em **Settings > API**
2. Copie as seguintes informações:
   - **Project URL**: `https://seu-projeto.supabase.co`
   - **anon public key**: `sua-chave-anonima-aqui`

### 3. Criar Tabela no Banco

1. No dashboard do Supabase, vá em **SQL Editor**
2. Copie e cole o conteúdo do arquivo `database/schema.sql`
3. Clique em "Run" para executar o script

### 4. Configurar Credenciais no Streamlit

#### Opção 1: Usando st.secrets (Recomendado para produção)

1. Crie um arquivo `.streamlit/secrets.toml` na raiz do projeto:
```toml
[supabase]
url = "https://seu-projeto.supabase.co"
key = "sua-chave-anonima-aqui"
```

#### Opção 2: Variáveis de Ambiente

1. Crie um arquivo `.env` na raiz do projeto:
```env
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_KEY=sua-chave-anonima-aqui
```

#### Opção 3: Configuração Manual (Para desenvolvimento)

1. Execute o aplicativo: `streamlit run main.py`
2. No sidebar, expanda "Configurar Credenciais"
3. Cole a URL e a chave do Supabase
4. Clique em "Salvar Configurações"

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
- Verifique se as credenciais estão corretas
- Confirme se a tabela foi criada no banco
- Verifique se o projeto está ativo no Supabase

### Erro de Permissão
- Verifique se a chave anônima tem permissão para INSERT
- No Supabase, vá em **Authentication > Policies**
- Certifique-se de que há políticas adequadas para a tabela

### Erro de Importação
- Execute: `pip install -r requirements.txt`
- Verifique se o Python está na versão 3.8+

## 📊 Funcionalidades Disponíveis

- ✅ Salvar respostas do questionário
- ✅ Contar total de respostas
- ✅ Buscar respostas por período
- ✅ Estatísticas em tempo real
- ✅ Interface de configuração integrada

## 🔒 Segurança

- Use sempre a chave anônima (anon key) para o frontend
- Configure políticas RLS (Row Level Security) se necessário
- Mantenha as credenciais seguras e não as versionem no Git
