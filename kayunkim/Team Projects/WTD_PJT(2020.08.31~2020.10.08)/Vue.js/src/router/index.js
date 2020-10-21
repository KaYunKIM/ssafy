import Vue from 'vue'
import VueRouter from 'vue-router'
// accounts
import Login from '@/views/accounts/Login.vue'
import Join from '@/views/accounts/Join.vue'
import Profile from '@/views/accounts/Profile.vue'
// projects
import ProjectStatus from '@/views/projects/ProjectStatus.vue'
// import NewProject from '@/views/projects/NewProject.vue'
import MainProject from '@/views/projects/ProjectMain.vue'
import MemberToDo from '@/views/projects/MemberToDo.vue'

// Schedules
import Schedule from '@/views/schedules/Schedule.vue'
import MeetingLog from '@/views/meetings/MeetingLog.vue'


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
    name: 'Project',
    component: ProjectStatus
  },
  // {
  //   path: '/project/new',
  //   name: 'NewProject',
  //   component: NewProject
  // },
  {
    path: '/project/main',
    name: 'ProjectMain',
    component: MainProject
  },
  {
    path: '/schedule',
    name: Schedule,
    component: Schedule
  },
  {
    path:'/meetinglog',
    name: 'MeetingLog',
    component : MeetingLog
  },
  {
    path:'/project/todo',
    name:'MemberToDo',
    component: MemberToDo
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router