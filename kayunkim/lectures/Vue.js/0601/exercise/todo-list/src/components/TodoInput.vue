<template>
  <div>
      <input type="text" v-model="userInput" @keypress.enter="createTodo">
      <button @click="createTodo">할 일 등록</button>
  </div>
</template>

<script>
export default {
    name: 'TodoInput',
    data() {
        return {
            userInput: '',
        }
    },
    methods: {
        createTodo() {
            const newTodo = {
                id: Date.now(),
                content: this.userInput,
                isCompleted: false,
            }
            this.$emit('create-todo', newTodo)
            // methods 안에서는 $emit 앞에 this.를 꼭 붙인다
            this.userInput = ''
        },
    }
}
</script>

<style>

</style>