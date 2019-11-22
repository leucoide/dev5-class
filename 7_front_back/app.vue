<template>
  <div>
    <div class="todo-form">
      <!-- v-model reflete o valor de um input numa propriedade do componente -->
      <input
        class="todo-form-text"
        type="text"
        v-model="itemCreationText"
        placeholder="Adicione um item na lista"
      >
      <!-- @click é o mesmo que onclick -->
      <!-- Exercício: como eu faço para pegar o "enter"? -->
      <button
        class="todo-form-button"
        @click="addItem"
      >+</button>
    </div>
    <ul class="todo-list">
      <!-- 
        v-for repete uma tag e tudo dentro substituindo o
        template por cada item da iteração
      -->
      <li
        v-for="(item, index) in items"
        :key="index"
      >
        <span class="content">{{item}}</span>
        <button class="exclude-button">X</button>
      </li>

    </ul>
  </div>
</template>

<script>

import TodoClient from './TodoClient.js';

export default {
  data () {
    return {
      itemCreationText: '',
      items: [
        // dá para transformar em done com esse formato de dado?
        'Fazer uma lista simples em texto plano',
      ]
    }
  },
  created () {
    const url = ''
    this.todoClient = new TodoClient(url)
  },
  methods: {
    addItem () {
      // adicionar texto do formulário à lista
      // limpar form
    },
    deleteItem (item) {
      // remover item da lista
      // este método não está sendo chamado. Olhe onde o addItem é
      // chamado para tentar reproduzir
    }
  }
}

</script>

<style scoped>
/* selecionando todos os elementos <li> que possuam a classe "done" */
li.done {
  /* CSS para deixar item "riscado" */
}
.todo-form-text {
  width: 400px;
  font-size: 14px;
}

.todo-form-button {
  font-size: 16px;
  font-weight: bold;
}

.todo-form-button,
.todo-form-text {
  display: inline-block;
  padding: 10px 15px;
  border-radius: 0;
}
</style>