<template>
  <div>
      <!-- 3, 사용하기 -->
      <TodoList :todos="todos" @checked="updatedTodo"/> 
         <!-- 왼쪽 자식 = 오른쪽 부모 -->
      <TodoInput @create-todo="createTodo"/>
  </div>
</template>

<script>
// 1. 사용할 컴포넌트 불러오기
import TodoList from '@/components/TodoList.vue'
import TodoInput from '@/components/TodoInput.vue'
                    // @: src부터 경로가 시작된다

export default {
    name: 'TodoView',
    // 2. 불러온 컴포넌트 등록하기
    components : {
        TodoList,
        TodoInput,
    },
    data() {
        return {
            todos: [
                {
                    id: 1,
                    content: 'Vue복습',
                    isCompleted: false,

                },
                 {
                    id: 2,
                    content: '저녁먹기',
                    isCompleted: false,
                    
                },
                 {
                    id: 3,
                    content: '커피마시기',
                    isCompleted: false,
                    
                },
            ]
        }
    },
    methods: {
        updatedTodo(todo) {
            todo.isCompleted = !todo.isCompleted
        },
        createTodo(todo) {
            this.todos.push(todo)
        }
    }   

}
</script>

<style>

</style>