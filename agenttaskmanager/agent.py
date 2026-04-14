from google.adk.agents.llm_agent import Agent
from trello import TrelloClient
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

API_KEY = os.getenv('TRELLO_API_KEY')
API_SECRET = os.getenv('TRELLO_API_SECRET')
TOKEN = os.getenv('TRELLO_TOKEN')


def get_temporal_context():
    now = datetime.now()
    return now.strftime('%y/%m/%d %H:%M:%S')


def adicionar_tarefa(nome_da_task: str, descricao_da_task: str, due_date: str):
    client = TrelloClient(
        api_key=API_KEY,
        api_secret=API_SECRET,
        token=TOKEN,
    )

    boards = client.list_boards()
    meu_board = [b for b in boards if b.name == "Agente de tarefasDIO"][0]
    listas = meu_board.list_lists()
    minha_lista = [l for l in listas if l.name.upper() == 'TO DO' or l.name.upper() == 'A FAZER'][0]

    minha_lista.add_card(
        name=nome_da_task,
        desc=descricao_da_task,
        due=due_date
    )
    return f"Card '{nome_da_task}' criado com sucesso no Trello!"


root_agent = Agent(
   model='gemini-2.5-flash',
    name='root_agent',
    description='Agente de organização de tarefas',
    instruction="""
        Você é um agente de organização de tarefas integrado ao Trello.
        Você TEM acesso ao Trello e DEVE usar a tool 'adicionar_tarefa' para criar cards.
        
        Fluxo obrigatório:
        1. Use a tool 'get_temporal_context' para obter a data atual e informe ao usuário.
        2. Pergunte quais são as tarefas do dia.
        3. Para CADA tarefa informada, colete:
           - Nome da tarefa
           - Descrição da tarefa
           - Data de vencimento (due_date no formato YYYY-MM-DD)
        4. Chame OBRIGATORIAMENTE a tool 'adicionar_tarefa' com essas informações.
        5. Confirme ao usuário que o card foi criado no Trello.
        6. Pergunte se há mais tarefas.
        7. Repita até o usuário dizer que não tem mais tarefas.
        
        IMPORTANTE: Você NUNCA deve dizer que não tem acesso ao Trello.
        Você TEM acesso via tool 'adicionar_tarefa' e DEVE usá-la sempre que o usuário informar uma tarefa.
    """,
    tools=[get_temporal_context, adicionar_tarefa],
)