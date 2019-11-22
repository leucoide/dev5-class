from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


def create_app():
    # O objeto que representa a aplicação
    app = FastAPI()
    
    # Nossa lista de tarefas
    TODOS = []
    # Variável de controle do ID
    LAST_ID = 0
    
    # Funções de manipulação de dados
    def get_id() -> int:
        """Generate a new id value."""
        nonlocal LAST_ID
        LAST_ID += 1
        return LAST_ID

    def find_todo(todo_id):
        """Find a todo item in the list given it's id."""
        nonlocal TODOS
        todos = [todo for todo in TODOS if todo['id'] == todo_id]
        return todos[0]

    def add_todo(todo):
        """Add a todo item to the todo list."""
        nonlocal TODOS
        TODOS.append(todo)

    def remove_todo(todo_id):
        """Remove a todo item in the list given it's id."""
        nonlocal TODOS
        TODOS = [item for item in TODOS if item['id'] != todo_id]

    @app.get('/todos')
    def get_todos():
        # Listar todos os itens
        return TODOS

    # Rotas
    

    class TodoCreateModel(BaseModel):
        """Todo item data model."""
        text: str
        done: bool 

    @app.post('/todos')
    def create_todo(todo_data: TodoCreateModel):
        """Handler that creates a todo item and persists it."""
        # 1. Criar um dicionario a partir de "todo_data" e colocar em uma variável
        # 2. Gerar um novo id e adicionar ao dicionário
        # 3. adicionar item a lista de todos
        # 4. Retornar item
        return

    class TodoUpdateModel(BaseModel):
        text: Optional[str]
        done: Optional[bool] 

    @app.put('/todos/{todo_id}')
    def update_todo(todo_id: int, data: TodoUpdateModel):
        """Handler that updates a todo item data given it's id."""
        # 1. Achar item com id 'todo_id'
        # 2. Mesclar propriedades de 'data' com o item encontrado
        # Dica: Para transformar um modelo pydantic em dicionário,
        # basta chamar o método 'dict'
        # Dica2: Para ignorar os campos nulos, basta passar o
        #  parâmetro 'skip_defaults' como True
        return
    
    @app.delete('/todos/{todo_id}')
    def delete_todo(todo_id: int):
        """Handler that deletes a todo item given it's id."""
        # 1. Encontrar item
        # 2. Remover item da lista
        return 

    return app
