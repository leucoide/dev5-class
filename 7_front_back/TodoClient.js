import axios from "axios";

export default class TodoClient {

    constructor(baseURL) {
        this.client = axios.create({
            baseURL: baseURL
        });
    }

    listTodos () {
        // 1. Enviar get para listar os todos
        // 2. Retornar a lista
    }

    createTodo (text, done = false) {
        // 1. Enviar post para criar o todo
        // 2. Retornar id
    }

    setDone (todoId, done) {
        // 1. Enviar post para atualizar o todo
        // 2. Retornar item alterado
    }

    setText (todoId, text) {
        // 1. Enviar post para atualizar o todo
        // 2. Retornar item alterado
    }

    deleteTodo (todoId) {
        // 1. Enviar delete para apagar o todo
    }

}