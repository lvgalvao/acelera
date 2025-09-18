# 🚀 Acelera - Plataforma de Trilhas de Dados

<div align="center">
  <img src="img/acelerador.jpg" alt="Acelerador - Jornada de Dados" width="600">
</div>

Uma aplicação Streamlit que faz parte da **Jornada de Dados** e oferece trilhas de aprendizado personalizadas na área de dados, com questionário inteligente para recomendar o melhor caminho de estudos.

## 🗺️ Roadmap

Este repositório faz parte da **Jornada de Dados** e tem como objetivo criar um **roadmap de estudo para os próximos 90 dias**, ajudando profissionais a acelerar sua carreira na área de dados através de trilhas personalizadas e um plano de estudos estruturado.

### 🎯 **Seus melhores 90 dias**

**Roadmap adaptado ao seu objetivo profissional:**
- 👨‍💼 **Profissional migrando para a área**
- 📊 **Analista migrando para engenharia**
- 🚀 **Engenheiro se especializando**

**📅 Cronograma do Programa:**
- **12 semanas** de desafios práticos
- **4 Encontros** focados em estratégia de carreira, posicionamento e aumento de renda
- **Início:** 18 de setembro
- **Fim:** 11 de dezembro

## 📋 Funcionalidades

### 🎯 Questionário Inteligente
- **7 perguntas personalizadas** para avaliar seu perfil
- **Recomendação automática** de 3 trilhas baseada nas suas respostas
- **Plano de estudos de 3 meses** (1 trilha por mês)
- **Cálculo baseado em 2 horas de estudo por dia**

### 🗓️ Roadmap de 90 Dias (12 Semanas)
- **Estrutura de 3 meses** com foco em resultados práticos
- **1 trilha por mês** para aprofundamento adequado
- **12 semanas de desafios práticos** para aplicação imediata
- **4 encontros estratégicos** para carreira e posicionamento
- **Cronograma realista** considerando 2 horas diárias de estudo
- **Progressão lógica** das competências em dados

### 📚 Trilhas Disponíveis
- **n8n** - Automação de processos
- **SQL** - Banco de dados e consultas
- **Python** - Programação para dados
- **Engenharia de Dados + IA** - Pipelines e infraestrutura
- **AWS** - Cloud computing

### 📊 Visualização de Conteúdo
- **Descrição detalhada** de cada trilha
- **Lista completa de módulos** com carga horária
- **Métricas de estudo** (horas totais, dias necessários)
- **Download do plano** em formato CSV

### 🎯 Encontros Estratégicos
- **4 encontros focados** em estratégia de carreira
- **Posicionamento profissional** no mercado de dados
- **Estratégias de aumento de renda** na área
- **Networking** com outros profissionais

## 🛠️ Instalação

### Pré-requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Passos para instalação

1. **Clone o repositório:**
```bash
git clone <url-do-repositorio>
cd acelera
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Execute a aplicação:**
```bash
streamlit run main.py
```

4. **Acesse no navegador:**
```
http://localhost:8501
```

## 📁 Estrutura do Projeto

```
acelera/
├── main.py                    # Ponto de entrada da aplicação
├── pages/
│   ├── 1_📚_Trilhas.py       # Página de visualização das trilhas
│   └── 2_🎯_Questionário.py   # Página do questionário
├── data/
│   ├── trilha.csv            # Dados das trilhas (nome e descrição)
│   └── cursos.csv            # Dados dos módulos (conteúdo, carga horária)
├── img/
│   └── logo.svg              # Logo da Jornada de Dados
├── requirements.txt          # Dependências do projeto
└── README.md                 # Este arquivo
```

## 🎮 Como Usar

### 1. Navegação
- **Trilhas**: Visualize todas as trilhas disponíveis e seus módulos
- **Questionário**: Responda às perguntas para receber recomendações personalizadas

### 2. Questionário
1. Responda às 7 perguntas sobre seu perfil e experiência
2. Receba a recomendação de 3 trilhas para os próximos 3 meses
3. Visualize o plano de estudos detalhado
4. Baixe o plano em CSV para acompanhar seu progresso

### 3. Lógica de Recomendação
O sistema considera:
- **Objetivo profissional** (migrar para dados, evoluir como analista, etc.)
- **Experiência com SQL** (avançado, básico, iniciante)
- **Conhecimento em ETL/Pipelines** (avançado, intermediário, básico)
- **Nível de Python** (avançado, intermediário, básico, iniciante)
- **Experiência em Engenharia de Dados**
- **Conhecimento em Cloud** (AWS/Azure/GCP)
- **Experiência com Automação** (n8n/Zapier)

## 📊 Dados

### trilha.csv
Contém informações básicas das trilhas:
- `trilha`: Nome da trilha
- `detalhe`: Descrição detalhada

### cursos.csv
Contém informações dos módulos:
- `Trilha`: Nome da trilha
- `Conteúdo`: Nome do módulo
- `Carga Horária`: Duração em minutos
- `Objetivo`: Objetivo do módulo

## 🔧 Tecnologias Utilizadas

- **Streamlit**: Framework para aplicações web em Python
- **Pandas**: Manipulação e análise de dados
- **Python**: Linguagem de programação principal

## 📝 Dependências

```
streamlit
pandas
```

## 🚀 Executando em Produção

Para executar em um servidor:

```bash
streamlit run main.py --server.port 8501 --server.address 0.0.0.0
```

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Suporte

Para dúvidas ou suporte, entre em contato através dos issues do repositório.

---

**Desenvolvido com ❤️ para acelerar sua jornada em dados!**

*Este projeto faz parte da **Jornada de Dados** - uma iniciativa para democratizar o conhecimento em dados e acelerar a carreira de profissionais na área.*
