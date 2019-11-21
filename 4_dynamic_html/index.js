function loadItemHandler () {
    // 1. selecionar todos os elementos "li"
    // 2. escutar o evento de click em cada um deles
    // 3. remover ou adicionar a classe done conforme necessário
}

function createTodoItem () {
    // 1. Colocar o conteúdo do texto do formulário e colocar numa variável
    // Dica: ele é o único com a classe "todo-form-text"
    // 2. Criar um elemento li
    // 3. Colocar o texto da variável no elemento
    // 4. Criar o botão de deletar no elemento
    // 5. Colocar o elemento no final da lista
    alert("Altere a função createTodoItem no index.js!!");
}
function loadCreateButtonHandler () {
    // Escutando o evento de click no botão de criar para chamar a função createTodoItem
    document.querySelector('.todo-form-button').addEventListener('click', () => createTodoItem());
}

function deleteItem (itemElement) {
    // Esta função deve ser chamada quando o botão com um "x" for clicado
    // O parâmetro itemElement passado deve ser o elemento todo do item (<li>)
    // Este elemento deve ser removido.
}


loadItemHandler()
loadCreateButtonHandler()
