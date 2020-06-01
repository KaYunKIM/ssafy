import Vue from 'vue'
import VueRouter from 'vue-router'
import TodoView from '@/views/TodoView.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'TodoView',
    component: TodoView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
