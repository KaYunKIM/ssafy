import Vue from 'vue'
import VueRouter from 'vue-router'
import LoginView from '../views/accounts/LoginView.vue'
import SignupView from '../views/accounts/SignupView.vue'
import ArticleListView from '../views/articles/ArticleListView.vue'
import ArticleCreateView from '../views/articles/ArticleCreateView.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'Signup',
    component: SignupView
  },
  {
    path: '/articles',
    name: 'Articles',
    component: ArticleListView
  },
  {
    path: '/articles/create',
    name: 'Create',
    component: ArticleCreateView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
