import Vue from 'vue'
import Vuex from 'vuex'
import cookies from 'vue-cookies'
import router from '@/router/index'

import axios from 'axios'

import SERVER from '@/API/url'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    //accounts
    authToken: cookies.get('auth-token'),
    userData: {},
    userSubData: {},

    //members
    memberList: {},

    //projects
    projectList: {},
    addProjectModal: null,
    
    meetingList: {},
    addMeetingLogModal: null,
    
    // schedules
    scheduleList: {},
    addScheduleModal: null,
  },

  getters: {
    config: state => ({
      headers: {
        Authorization: `${state.authToken}` 
      }
    }),
  },

  mutations: {
    //accounts
    SET_TOKEN(state, token) {
      state.authToken = token
      cookies.set('auth-token', token)
    },
    SET_USERDATA(state, userData){
      state.userData = userData
    },
    SET_USERSUBDATA(state, userSubData){
      state.userSubData = userSubData
    },

    //members
    SET_MEMBERLIST(state, memberList){
      state.memberList = memberList
    },

    //meetings
    SET_MEETINGLIST(state, meetingList){
      state.meetingList = meetingList
    },

    //projects
    SET_PROJECTLIST(state, projectList) {
      state.projectList = projectList
    },
    //schedules
    SET_SCHEDULELIST(state, scheduleList){
      state.scheduleList = scheduleList;
    }
  },

  actions: {
    //accounts
    userLogin({ state, commit }, userSubData) {
      console.log('userLogin pass')
      axios.post(SERVER.URL + SERVER.ROUTES.login, userSubData)
        .then((res) => {
          console.log('userLogin success')
          if(res.data === '0') {
            commit('SET_USERSUBDATA', userSubData)
            console.log('email',state.userSubData.email)
            router.push(`/join`)
          } else {
            // 정상로그인
            console.log('userData', res.data.userInfo)
            commit('SET_USERDATA', res.data.userInfo) 
            console.log(state.userData)
            // 토큰저장
            commit('SET_TOKEN', res.data.token) 
            router.push(`/schedule`)
          }
        })
        .catch(err => console.log(err))
    },
      
    userJoin({ commit }, userInfo) {
      console.log('userJoin pass')
      axios.post(SERVER.URL + SERVER.ROUTES.join, userInfo)
        .then((res) => {
          console.log('userJoin success')
          if(res.data === '0') {
            alert('양식에 맞게 다시 입력해주세요!')
          } else {
            console.log('userdata',res.data) 
            // commit('SET_USERDATA', res.data) 
            // 정상로그인
            commit('userData', userInfo)
            commit('SET_USERDATA', userInfo)
            // 토큰저장
            commit('SET_TOKEN', res.data.token) 
            router.push(`/schedule`)
          }
        })
        .catch(err => console.log(err))
    },

    updateProfile({ commit, getters }, userInfo) {
      axios.put(SERVER.URL + SERVER.ROUTES.mypage, userInfo, getters.config)
      .then((res) => {
        if(res.data === '0') {
          alert('양식에 맞게 다시 입력해주세요!')
        } else {
          console.log(res.data)
          commit('SET_USERDATA', res.data) 
          router.push(`/schedule`)
        }
      })
      .catch(err => console.log(err))
    },

    // projects
    fetchProjectList({ state, commit }) {
      const userid = state.userData.id
      axios.get(SERVER.URL + SERVER.ROUTES.projects + `/projects/${userid}`)
        .then(res => commit('SET_PROJECTLIST', res.data))
        .catch(err => console.error(err))
    },

    addProject({ state, dispatch }, projectInfo) {
      state.addProjectModal = !state.addProjectModal
      if (projectInfo) {
        axios.post(SERVER.URL + SERVER.ROUTES.projects, projectInfo)
        .then(() => dispatch('fetchProjectList'))
        .catch(err => console.log(err.response.data) )
      }
    },

    //member
    fetchMemberList({ commit, getters }, project_id) {
      axios.get(SERVER.URL + SERVER.ROUTES.projects +`${project_id}/members/`, getters.config)
        .then(res => commit('SET_MEMBERLIST', res.data))
        .catch(err => console.error(err))
    },
    
    addMember({ dispatch, getters }, memberInfo, project_id) {
      if (memberInfo) {
        axios.post(SERVER.URL + SERVER.ROUTES.projects +`${project_id}/members/`, memberInfo.member, getters.config)
        .then(() => dispatch('fetchMemberList'))
        .catch(err => console.log(err.response.data) )
      }
    },

    //meetings
    fetchMeetingList({ commit }, project_id){
      axios.get(SERVER.URL + SERVER.ROUTES.projects + `${project_id}/meetings/`, project_id)
      .then(res => commit('SET_MEETINGLIST', res.data))
      .catch(err => console.err(err))
    },

    addMeetingLog({state, dispatch} , meetingInfo, project_id){
      state.addMeetingLogModal = !state.addMeetingLogModal
      const todayDate = new Date().toISOString().slice(0,10);
      const et = todayDate + " " + meetingInfo.time
      const meetingData = {
        title : meetingInfo.title,
        end_time : new Date(et)
      }
      if(meetingData) {
        axios.post(SERVER.ROUTES.projects + `${project_id}/meetings/`, meetingData)
        // axios.post(SERVER.URL + SERVER.ROUTES.meetings, meetingData, project_id)
        .then(() => dispatch('fetchMeetingList'))
        .catch(err => console.log(err.response.data))
      }
    },
    
    // schedules
    fetchScheduleList({ getters, commit }){
      axios.get(SERVER.URL + SERVER.ROUTES.schedules, getters.config)
      .then(res => commit('SET_SCHEDULELIST', res.data))
      .catch(err => console.err(err))
    },
    
     
    addSchedule({ state, getters, dispatch }, scheduleInfo){
      state.addScheduleModal = !state.addScheduleModal
      const start = scheduleInfo.start_date + " " + scheduleInfo.start_time
      const end = scheduleInfo.end_date + " " + scheduleInfo.end_time
      const scheduleData = {
        title : scheduleInfo.title,
        detail: scheduleInfo.detail,
        start_time: new Date(start),
        end_time: new Date(end)
      }
      if(scheduleData) {
        axios.post(SERVER.URL + SERVER.ROUTES.schedules, scheduleData, getters.config)
          .then(() => dispatch('fetchScheduleList'))
          .catch(err => console.log(err.response.data))
      }
    },
    uploadAudio({ getters } , audioName){
      var audioData = {'title' : audioName}
      axios.post(SERVER.URL + SERVER.ROUTES.stt, audioData, getters.config)
          .then((res) => console.log(res.data))
          .catch(err => console.log(err.response.data))
    },
  },
  modules: {
  },
  plugins: [
    createPersistedState()
  ]
})