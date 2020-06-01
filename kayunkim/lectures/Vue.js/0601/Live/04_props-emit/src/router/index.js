import Vue from 'vue'
import VueRouter from 'vue-router'
import Parent from '..views.Parent.vue'
import About from '..views.About.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/parent',
    name: 'Parent',
    component: Parent
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
