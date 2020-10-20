import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'

// accounts
import SignupView from '@/views/accounts/SignupView.vue'
import LoginView from '@/views/accounts/LoginView.vue'
import MypageView from '@/views/accounts/MypageView.vue'

// post
import PostCreateView from '@/views/post/PostCreateView.vue'
import PostUpdateView from '@/views/post/PostUpdateView.vue'
import PostDetailView from '@/views/post/PostDetailView.vue'

// cafe
import CafeDetailView from '@/views/cafe/CafeDetailView.vue'

import SearchView from '@/views/SearchView.vue'
import NotFound from '@/components/404.vue'

//survey
import SurveyView from '@/views/survey/SurveyView.vue'
import SurveyResultView from '@/views/survey/SurveyResultView.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: SignupView,
    meta: {
      title: 'Signup'
    },
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: LoginView,
    meta: {
      title: 'Login'
    },
  },
  {
    path: '/accounts/:user_id',
    name: 'Mypage',
    component: MypageView
  },
  {
    path: '/post/create',
    name: 'PostCreate',
    component: PostCreateView
  },
  {
    path: '/post/update/:post_id',
    name: 'PostUpdate',
    component: PostUpdateView
  },
  {
    path: '/post/detail/:post_id',
    name: 'PostDetail',
    component: PostDetailView,
  },
  {
    path: '/cafe/detail/:cafe_id',
    name: 'CafeDetail',
    component: CafeDetailView,
  },
  {
    path: '/search',
    name: 'Search',
    component: SearchView,
  },
  {
    path: '*',
    name: '404Page',
    component: NotFound,
  },
  {
    path: '/',
    name: 'Survey',
    component: SurveyView,
  },
  {
    path: '/survey/result',
    name: 'SurveyResult',
    component: SurveyResultView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const publicPages = ['Home', 'Signup', 'Login', 'PostDetail', 'CafeList', 'CafeDetail', 'Survey' ]  //login 안해도 됨
  const privatePages = ['Login', 'Signup', ]  //login 되어 있으면 안됨

  const authRequired = !publicPages.includes(to.name)
  const unauthRequired = privatePages.includes(to.name)  //로그인 안한 상태가 필요함
  
  const isLoggedIn = !!Vue.$cookies.isKey('auth-token')
  

  if (unauthRequired && isLoggedIn) {
    next('/')
  }

  if (authRequired && !isLoggedIn) {
    next({ next: 'Login' })
  } else {
    next()
  }
})

export default router
