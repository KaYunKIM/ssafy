import Vue from 'vue'
import VueRouter from 'vue-router'

// Home
import HomeView from '../views/HomeView.vue'

// accounts
import SignupView from '../views/accounts/SignupView.vue'
import LoginView from '../views/accounts/LoginView.vue'
import ProfileView from '../views/accounts/ProfileView.vue'

// articles
import ArticleListView from '../views/articles/ArticleListView.vue'
import ArticleDetailView from '../views/articles/ArticleDetailView.vue'
import ArticleCreateView from '../views/articles/ArticleCreateView.vue'
import ArticleUpdateView from '../views/articles/ArticleUpdateView.vue'


// movies
import MovieView from '../views/movies/MovieView.vue'
import MovieDetailView from '../views/movies/MovieDetailView.vue'


Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView,
    meta: {
      title: 'Movie Home'
    },
  },

  // accounts
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
    path: '/accounts/:username',
    name: 'Profile',
    component: ProfileView,
    meta: {
      title: 'My Page'
    },
  },

  // articles
  {
    path: '/articles',
    name: 'Articles',
    component: ArticleListView,
    meta: {
      title: 'Community'
    },
  },
  {
    path: '/articles/:articleId',
    name: 'ArticleDetail',
    component: ArticleDetailView,
    meta: {
      title: 'Article'
    },
  },
  {
    path: '/new_article',
    name: 'ArticleNew',
    component: ArticleCreateView,
    meta: {
      title: 'Create Article'
    },
  },
  {
    path: '/update_article/:articleId',
    name: 'ArticleUpdate',
    component: ArticleUpdateView,
    meta: {
      title: 'Edit Article'
    },
  },

  // movies
  {
    path: '/movies',
    name: 'Movie',
    component: MovieView,
    meta: {
      title: 'Search Movies'
    },
  },
  {
    path: '/movies/:movieId',
    name: 'MovieDetail',
    component: MovieDetailView,
    meta: {
      title: 'Movie Details'
    },
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const publicPages = ['Home', 'Signup', 'Login', 'Movie' ]  //login 안해도 됨
  const privatePages = ['Login', 'Signup', ]  //login 되어 있으면 안됨

  const authRequired = !publicPages.includes(to.name)
  const unauthRequired = privatePages.includes(to.name)  //로그인 안한 상태가 필요함
  
  const isLoggedIn = !!Vue.$cookies.isKey('auth-token')

  document.title = to.meta.title

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
