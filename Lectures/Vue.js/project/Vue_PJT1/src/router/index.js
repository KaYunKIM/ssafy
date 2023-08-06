import Vue from 'vue'
import VueRouter from 'vue-router'

import video from '../views/VideoView.vue'
import MovieView from '../views/MovieView.vue'


Vue.use(VueRouter)

  const routes = [
  {
    path: '/video',
    name: 'Video',
    component: video
  },
  {
    path: '/',
    name: 'MovieView',
    component: MovieView

  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
