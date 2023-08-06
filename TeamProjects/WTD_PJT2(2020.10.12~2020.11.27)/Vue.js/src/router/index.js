import Vue from 'vue'
import VueRouter from 'vue-router'
import cookies from 'vue-cookies'

// accounts
import Login from '@/views/accounts/Login.vue'
import Join from '@/views/accounts/Join.vue'
import Profile from '@/views/accounts/Profile.vue'

// projects
import ProjectMain from '@/views/projects/ProjectMain.vue'
import ProjectDetail from '@/views/projects/ProjectDetail.vue'

// meetings
import MeetingLog from '@/views/meetings/MeetingLog.vue'
import MemberToDo from '@/views/meetings/MemberToDo.vue'
import SearchKeyword from '@/views/meetings/SearchKeyword.vue'

// Schedules
import Schedule from '@/views/schedules/Schedule.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/join',
    name: 'Join',
    component: Join,
    props: true
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/project',
    name: 'ProjectMain',
    component: ProjectMain
  },
  {
    path: '/project/:projectId',
    name: 'ProjecDetail',
    component: ProjectDetail
  },
  {
    path: '/search',
    name: 'SearchKeyword',
    component: SearchKeyword
  },
  {
    path: '/schedule',
    name: 'Schedule',
    component: Schedule
  },
  {
    path:'/project/:projectId/meetinglog/:projectDate',
    name: 'MeetingLog',
    component : MeetingLog
  },
  {
    path:'/:userId/project/:projectId/ToDoList',
    name:'MemberToDo',
    component: MemberToDo
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to,from, next) => {
  const publicPages = ['Login', 'Join']   //login 안 한 상태에서 접근 가능 페이지
  const authRequired = !publicPages.includes(to.name)  //login이 필요한 페이지
  const isLoggedIn = !!cookies.isKey('auth-token')

  if (!authRequired && isLoggedIn) {
    next('/schedule')
  }

  if (authRequired && !isLoggedIn) {
    next('/')
  }
  else {
    next()
  }
})

export default router