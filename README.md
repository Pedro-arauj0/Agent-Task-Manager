# Agent Task Manager 🤖

Agente inteligente em Python capaz de automatizar o gerenciamento de tarefas no Trello, desenvolvido como desafio do curso da DIO.

## 📋 Sobre o Projeto

Este projeto foi desenvolvido como parte do desafio **"Criando um Agente para Automatizar um Fluxo de Trabalho em Python"** da plataforma DIO.

O agente utiliza Inteligência Artificial (Google Gemini) para interagir com o usuário via chat, coletar informações sobre as atividades do dia e criar cards automaticamente no Trello, aumentando a produtividade e eficiência no fluxo de trabalho.

## 🚀 Tecnologias Utilizadas

- **Python 3.13**
- **Google ADK** (Agent Development Kit)
- **Google Gemini 2.5 Flash** (modelo de IA)
- **Trello API**
- **py-trello** (biblioteca Python para integração com Trello)
- **python-dotenv** (gerenciamento de variáveis de ambiente)

## 💡 Funcionalidades

- ✅ Inicia a conversa perguntando as tarefas do dia
- ✅ Informa a data e hora atual automaticamente
- ✅ Coleta nome, descrição e data de vencimento de cada tarefa
- ✅ Cria cards automaticamente no board do Trello
- ✅ Confirma a criação de cada card
- ✅ Continua perguntando até o usuário não ter mais tarefas

## 🗂️ Estrutura do Projeto
Agent-Task-Manager/
│
├── agenttaskmanager/
│   ├── __init__.py
│   └── agent.py
│
├── .gitignore
├── requeriments.txt
└── README.md
## ⚙️ Como Configurar

### Pré-requisitos

- Python 3.13+
- Conta no Google AI Studio (https://aistudio.google.com)
- Conta no Trello com um board criado

### 1. Clone o repositório

```bash
git clone https://github.com/Pedro-arauj0/Agent-Task-Manager.git
cd Agent-Task-Manager
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

```bash
pip install -r requeriments.txt
```

### 4. Configure as credenciais

Crie um arquivo `.env` dentro da pasta `agenttaskmanager/` com o seguinte conteúdo:

```env
GOOGLE_GENAI_USE_VERTEXAI=0
GOOGLE_API_KEY=sua_chave_google_aqui
TRELLO_API_KEY=sua_chave_trello_aqui
TRELLO_API_SECRET=seu_secret_trello_aqui
TRELLO_TOKEN=seu_token_trello_aqui
```

#### Como obter as credenciais do Google

1. Acesse https://aistudio.google.com
2. Clique em **"Get API Key"**
3. Copie a chave gerada

#### Como obter as credenciais do Trello

1. Acesse https://trello.com/power-ups/admin
2. Crie um novo Power-Up
3. Vá em **"Chave de API"** e gere uma nova chave
4. Para o Token, acesse a URL abaixo substituindo pela sua chave: `https://trello.com/1/authorize?expiration=never&scope=read,write&response_type=token&key=SUA_API_KEY`

### 5. Configure o nome do board no código

No arquivo `agenttaskmanager/agent.py`, certifique-se que o nome do board está correto:

```python
meu_board = [b for b in boards if b.name == "NOME_DO_SEU_BOARD"][0]
```

## ▶️ Como Rodar

### Via interface web (recomendado)

```bash
adk web
```

Acesse no navegador: **http://127.0.0.1:8000**

### Via terminal

```bash
python agenttaskmanager/agent.py
```

## 🖥️ Como Usar

1. Inicie o agente com `adk web`
2. Acesse http://127.0.0.1:8000
3. Digite uma mensagem para iniciar
4. O agente irá perguntar as tarefas do dia
5. Informe o nome da tarefa, descrição e data de vencimento
6. O card será criado automaticamente no seu Trello!

## 📸 Demonstração

O agente coleta as informações e cria os cards automaticamente no Trello:

1. Usuário informa a tarefa
2. Agente coleta descrição e data
3. Card criado no Trello ✅

## 👨‍💻 Autor

**Pedro Arthur**
- GitHub: [@Pedro-arauj0](https://github.com/Pedro-arauj0)

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais como parte do curso da [DIO](https://www.dio.me).
