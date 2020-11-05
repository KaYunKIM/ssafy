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
    profileStatus: null,
    userList: [],
    userNicknameList: [],

    //members
    memberList: [],

    //projects
    projectId: null,
    projectDate: null,
    projectStatus: null,
    addProjectModal: null,
    projectList: [],
    projectDone: [],
    projectInProgress: [],
    
    //meetings
    meetingList: {},
    meetingTempInfo: {},
    addMeetingLogModal: null,
    updateMeetingLogModal: null,
    modalWorkDetail: null,
    meetingInfoStatus: null,
    keywordData: {},
    taskList: [],
    taskInfo: {},
    taskdetail: {},
    taskId:null,
    memberToDoList: {},
    searchStatus: null,

    // schedules
    schedule: {},
    scheduleList: [],
    addScheduleModal: null,
    updateScheduleModal: null,
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
    SET_USERLIST(state, userList){
      state.userList = userList
    },
    SET_USERNICKNAMELIST(state, userNicknameList){
      state.userNicknameList = userNicknameList
    },

    //members
    SET_MEMBERLIST(state, memberList){
      state.memberList = memberList
    },

    //projects
    SET_PROJECTID(state, projectId) {
      state.projectId = projectId
    },
    SET_PROJECTLIST(state, projectList) {
      state.projectList = projectList
    },
    SET_PROJECTINPROGRESS(state, projectInProgress) {
      state.projectInProgress = projectInProgress
    },
    SET_PROJECTDONE(state, projectDone) {
      state.projectDone = projectDone
    },
    SET_PROJECTDATE(state, projectDate) {
      state.projectDate = projectDate
    },
    
    //meetings
    SET_MEETINGLIST(state, meetingList){
      state.meetingList = meetingList
    },
    SET_MEMBERTODOLIST(state, memberToDoList){
      state.memberToDoList = memberToDoList
    },
    SET_KEYWORDATA(state, keywordData){
      state.keywordData = keywordData
    },

    //schedules
    SET_SCHEDULELIST(state, scheduleList){
      state.scheduleList = scheduleList;
    },
    SET_SCHEDULE(state, schedule) {
      state.schedule = schedule
    },

    //tasks
    SET_TASKLIST(state, taskList){
      state.taskList = taskList
    },
    SET_TASKINFO(state, taskInfo){
      state.taskInfo = taskInfo
    },
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
        .catch(err => console.error(err.response.data))
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
        .catch(err => console.error(err.response.data))
    },

    userLogout({ commit }) {
      commit('SET_TOKEN', null)
      commit('SET_USERDATA', {})
      commit('SET_USERSUBDATA', {})
      cookies.remove('auth-token')
      router.push('/')
    },

    fetchUserList({ commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.user)
        .then((res) => {
          commit('SET_USERLIST', res.data["data"])
          commit('SET_USERNICKNAMELIST', res.data["name_list"])
        }) 
        .catch(err => console.error(err))
    },

    updateProfile({ state, commit, getters }, userInfo) {
      axios.put(SERVER.URL + SERVER.ROUTES.mypage, userInfo, getters.config)
      .then((res) => {
          commit('SET_USERDATA', res.data) 
          alert('수정이 완료되었습니다!')
      })
      .catch(err => {
        state.profileStatus = !state.profileStatus
        alert('양식에 맞게 다시 입력해주세요!')
        console.error(err.response.data)
      })
    },

    // projects
    fetchProjectList({ state, getters, commit }, check) {
      axios.get(SERVER.URL + SERVER.ROUTES.projects, getters.config)
        .then((res) => {
          commit('SET_PROJECTLIST', res.data)
          console.log(res.data)
          if (check) {
            state.projectStatus = !state.projectStatus
          }
        })
        .catch(err => console.error(err.response.data))
    },

    addProject({ state, commit, dispatch }, projectInfo) {
      state.addProjectModal = !state.addProjectModal
        if (projectInfo) {
          axios.post(SERVER.URL + SERVER.ROUTES.projects, projectInfo)
            .then((res) => {
              commit('SET_PROJECTID', res.data.id)
              dispatch('fetchProjectList', 1)
            })
            .catch(err => console.error(err.response.data))
        }
      },

    updateProjectStatus({ commit }, statusInfo) {
        commit('SET_PROJECTINPROGRESS', statusInfo.inProgress)
        commit('SET_PROJECTDONE', statusInfo.done)
        // commit('SET_PROJECTINPROGRESS', [])
        // commit('SET_PROJECTDONE', [])
    },

    setProjectId({ commit }, projectId) {
      commit('SET_PROJECTID', projectId)
    },

    //member
    fetchMemberList({ commit }, project_id) {
      return new Promise((resolve) => {
        axios.get(SERVER.URL + SERVER.ROUTES.projects +`${project_id}/members/`)
          .then((res) => {
            commit('SET_MEMBERLIST', res.data)
            resolve()
          })
          .catch(err => console.error(err.response.data))
      })
    },
    
    //meetings
    fetchMeetingList({ state, commit }){
      axios.get(SERVER.URL + SERVER.ROUTES.projects +`${state.projectId}/${state.projectDate}/meeting/`)
      .then((res) => {
        commit('SET_MEETINGLIST', res.data)
        console.log("MeetingList Data")
        console.log(res.data)
      })
      .catch(err => console.error(err.response.data))
    },
    
    addMeetingLog({state, dispatch} , meetingInfo){
      //  project_id = state.project_id
      state.addMeetingLogModal = !state.addMeetingLogModal
    
      // state.project_id = 4
      // const todayDate = new Date().toISOString().slice(0,10);
      // const et = todayDate + " " + meetingInfo.time
      // const meetingData = {
        //   title : meetingInfo.title,
        //   time : new Date(et),
        //   // projectId : this.state.projectId
        // }
      //console.log(meetingInfo.time)
      const curDateTime = state.projectDate + " " + meetingInfo.time
      const meetingData = {
        title : meetingInfo.title,
        time : new Date(curDateTime),
      }

      if(meetingData) {
        //console.log(1, meetingData.time)
        axios.post(SERVER.URL + SERVER.ROUTES.projects +`${state.projectId}/${state.projectDate}/meeting/`, meetingData)
        // axios.post(SERVER.URL + SERVER.ROUTES.meetings, meetingData, project_id)
        .then(() => {
          dispatch('fetchMeetingList')
        })
        .catch(err => console.log(err.response.data))
      }
    },


    // meeting 수정 모달에 값 전달해주는 함수
    updateMeetingTemp({state}, item){
      state.updateMeetingLogModal = !state.updateMeetingLogModal
      state.meetingTempInfo = item
    

      //  2020-10-26,08:24:00Z
      // const temp = state.meetingTempInfo.time.split('T')[1].split('Z')[0].split(':')
      // const tempTime = temp[0] + ":" + temp[1]
      // state.meetingTempInfo.time = tempTime
    },

    // meeting 정보 업데이트하기
    updateMeetingLog({state, dispatch} , meetingInfo){
      state.updateMeetingLogModal = !state.updateMeetingLogModal
      if(meetingInfo == null) return
      const curDateTime = state.projectDate + " " + meetingInfo.time
      const meetingData = {
        title : meetingInfo.title,
        time : new Date(curDateTime),
      }

      if(meetingData) {
        axios.put(SERVER.URL + SERVER.ROUTES.projects +`${meetingInfo.id}/meeting_detail/`, meetingData )
        // axios.post(SERVER.URL + SERVER.ROUTES.meetings, meetingData, project_id)
        .then(() => {
          dispatch('fetchMeetingList')
        })
        .catch(err => console.error(err.response.data))
      }

    },

    deleteMeeting({dispatch}, meeting_id){    
      if(confirm("정말 회의 정보를 삭제하시겠습니까?")){
        axios.delete(SERVER.URL + SERVER.ROUTES.projects +`${meeting_id}/meeting_detail/`)
        .then(() => {
          dispatch('fetchMeetingList')
        })
        .catch(err => console.error(err.response.data))
      }

    },
    
    // 키워드 검색하여 데이터 가져오기
    searchKeyword({getters, commit}, keyword){
      console.log(keyword)
      
      axios.get(SERVER.URL + SERVER.ROUTES.projects + `search/${keyword}/`, getters.config)
      .then((res) => {
        commit('SET_KEYWORDATA', res.data)
        // state.searchStatus = !state.searchStatus
      })
      .catch(err => console.log(err.response.data))
    },

    fetchMemberToDoList({state, commit}, idData){
      axios.get(SERVER.URL + SERVER.ROUTES.projects + `${idData.projectId}/${idData.userId}/${state.projectDate}/member_task_list/`)
      .then((res) => {
        commit('SET_MEMBERTODOLIST', res.data)
      })
      .catch(err => console.log(err.response.data))
    },

    // schedules
    fetchScheduleList({ getters, commit }){
      return new Promise((resolve) => {
        axios.get(SERVER.URL + SERVER.ROUTES.schedules, getters.config)
          .then((res) => {
            commit('SET_SCHEDULELIST', res.data)
            resolve()
          })
          .catch(err => console.error(err.response.data))
      })
    },

    // detailSchedule({ getters, commit }, scheduleId) {
    //   axios.get(SERVER.URL+ SERVER.ROUTES.schedules + `${scheduleId}/`, getters.config)
    //   .then(res => commit('SET_SCHEDULE', res.data))
    //   .catch(err => console.error(err.response.data))
    // },

    detailSchedule({ state, commit }, scheduleInfo) {
      state.updateScheduleModal = !state.updateScheduleModal
      commit('SET_SCHEDULE', scheduleInfo)
    },
    
    addSchedule({ state, getters, dispatch }, scheduleInfo){
      state.addScheduleModal = !state.addScheduleModal
      if (scheduleInfo) {
        const start = scheduleInfo.start_date + " " + scheduleInfo.start_time
        const end = scheduleInfo.end_date + " " + scheduleInfo.end_time
        const scheduleData = {
          title : scheduleInfo.title,
          detail: scheduleInfo.detail,
          start_time: new Date(start),
          end_time: new Date(end)
        }
        axios.post(SERVER.URL + SERVER.ROUTES.schedules, scheduleData, getters.config)
          .then(() => dispatch('fetchScheduleList'))
          .catch(err => console.error(err.response.data))
      }
    },

    updateSchedule({ state, dispatch, getters }, scheduleInfo) {
      state.updateScheduleModal = !state.updateScheduleModal
      if(scheduleInfo==null) return
      const start = scheduleInfo.start_date + " " + scheduleInfo.start_time
      const end = scheduleInfo.end_date + " " + scheduleInfo.end_time
      const scheduleData = {
        title : scheduleInfo.title,
        detail: scheduleInfo.detail,
        start_time: new Date(start),
        end_time: new Date(end)
      }
      axios.put(SERVER.URL + SERVER.ROUTES.schedules+`${scheduleInfo.id}/`, scheduleData, getters.config)
        .then(() => dispatch('fetchScheduleList'))
        .catch(err => console.error(err.response.data))
    },

    deleteSchedule({ commit, getters, dispatch }, scheduleInfo) {
      axios.delete(SERVER.URL + SERVER.ROUTES.schedules+`${scheduleInfo.id}/`, getters.config)
        .then(() => {
          commit('SET_SCHEDULE', {})
          dispatch('fetchScheduleList')
        })
        .catch(err => console.error(err.response.data))
    },

    //task
    showWorkDetail({ state } , {event}){
      state.taskInfo = event
      state.modalWorkDetail = !state.modalWorkDetail
    },
    showTaskDetail({ state } , task){
      state.taskdetail = task
      state.modalWorkDetail = !state.modalWorkDetail
    },

    updateTaskInfo({state , getters, dispatch}, taskinfo){
      state.modalWorkDetail = !state.modalWorkDetail
      if(taskinfo == null) return
      const start = new Date(state.projectDate + " " + taskinfo.start_time)
      const end = new Date(state.projectDate + " " + taskinfo.end_time)
      const taskData = {
        title : taskinfo.title,
        manager: taskinfo.manager,
        start_time: start,
        end_time: end,
        completed: taskinfo.completed,
        detail: taskinfo.detail
      }
      if(taskData) {
        console.log("Task Data")
        console.log(taskData)
        axios.put(SERVER.URL + SERVER.ROUTES.projects +`${taskinfo.id}/task_detail/`, taskData, getters.config)
        .then(() => {dispatch('fetchTaskInfo')})
        .catch(err => console.error(err.response.data))
      }
    },

    deleteWorkInfo({state, getters, dispatch}, task_id){
      state.modalWorkDetail = !state.modalWorkDetail
      axios.delete(SERVER.URL + SERVER.ROUTES.projects +`${task_id}/task_detail/`, getters.config)
      .then(() => {dispatch('fetchTaskList',state.projectId)})
      .catch(err => console.error(err.response.data))
    },
    updateWorkInfo({state , getters, dispatch}, taskinfo){
      state.modalWorkDetail = !state.modalWorkDetail
      if(taskinfo == null) return
      const start = new Date(taskinfo.tmp_date + " " + taskinfo.start_time)
      const end = new Date(taskinfo.tmp_date + " " + taskinfo.end_time)
      const taskData = {
        title : taskinfo.title,
        manager: taskinfo.manager,
        start_time: start,
        end_time: end,
        completed: taskinfo.completed,
        detail: taskinfo.detail
      }
      if(taskData) {
        console.log("Task Data")
        console.log(taskData)
        axios.put(SERVER.URL + SERVER.ROUTES.projects +`${taskinfo.id}/task_detail/`, taskData, getters.config)
        .then(() => {dispatch('fetchTaskList', state.projectId)})
        .catch(err => console.error(err.response.data))
      }
    },

    deleteTaskInfo({state, getters, dispatch}, task_id){
      state.modalWorkDetail = !state.modalWorkDetail
      axios.delete(SERVER.URL + SERVER.ROUTES.projects +`${task_id}/task_detail/`, getters.config)
      .then(() => {dispatch('fetchTaskInfo')})
      .catch(err => console.error(err.response.data))
    },

    fetchTaskList({ commit, getters }, project_id){
      axios.get(SERVER.URL + SERVER.ROUTES.projects +`${project_id}/all_task_list/`, getters.config)
      .then(res => commit('SET_TASKLIST', res.data))
      .catch(err => console.error(err.response.data))
    },  

    uploadAudio({ dispatch, getters } , uploadData){
      const audioName = uploadData.audioName
      const meetingId = uploadData.meetingId
      
      var audioData = {'title' : audioName}
      
      axios.post(SERVER.URL + SERVER.ROUTES.stt, audioData, getters.config)
        .then((res) => {
        // console.log(res.data)
          const Data = {
            data: res.data,
            meetingId: meetingId
          }
          dispatch('updateMeetingInfo', Data)
        })
        .catch(err => console.error(err.response.data))
    },
    
    // realtime stt
    updateSTTInfo({dispatch},originData){
      axios.post(SERVER.URL + SERVER.ROUTES.stt + "real_time/", originData)
      .then((res)=>{
        const Data = {
          data: res.data,
          meetingId: originData.meetingId
        }
        dispatch('updateMeetingInfo', Data)
      })
    },

    updateMeetingInfo({state, dispatch}, Data){
      const meetingId = Data.meetingId
      const meetingInfo = Data.data
      console.log("MeetingInfo Data")
      console.log(meetingInfo)
      axios.post(SERVER.URL + SERVER.ROUTES.projects + `${meetingId}/meeting_info/`, meetingInfo)
        .then(() => {
          dispatch('fetchTaskInfo', state.projectId)
        })
        .catch(err => console.error(err.response.data))
    },
      
    addProjectDate({commit},{date}){
      commit('SET_PROJECTDATE', date)
      router.push({ name: 'MeetingLog', params: { projectDate: date }})
    },
      
    fetchTaskInfo({commit, state}){
      const meetingDate = state.projectDate
      axios.get(SERVER.URL+SERVER.ROUTES.projects + `${state.projectId}/${meetingDate}/task_list`)
      .then((res) => {
        console.log("TaskInfo Data")
        console.log(res.data)
        commit('SET_TASKINFO', res.data)
        state.meetingInfoStatus = !state.meetingInfoStatus
      })
      .catch(err => console.error(err.response.data))
    },

    // fetchKeywordList({commit, state}){

    // }
  },
  modules: {
  },
  plugins: [
    createPersistedState()
  ]
})