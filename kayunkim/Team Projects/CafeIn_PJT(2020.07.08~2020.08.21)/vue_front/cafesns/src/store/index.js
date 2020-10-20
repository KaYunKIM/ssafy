import Vue from 'vue'
import Vuex from 'vuex'

import cookies from 'vue-cookies'
import router from '@/router/index'
import axios from 'axios'

import SERVER from '@/API/url'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)
// test

export default new Vuex.Store({
  state: {
    authToken: cookies.get('auth-token'),
    currentUser: null,
    userData: {},
    
    postList: {},
    userPostList: {},
    cafePostList: {},
    selectedPost: null,

    updatePostData: {},
    uploadImageURL: null,
    
    commentData: {},
    commentList: {},
    selectedComment: null,
    
    likeState: null,
    likeList: {},
    stampState: null,
    stampList: {},
    
    followState: null,
    followingList: {},
    followerList: {},
    
    cafeList: {},
    geoCafeList: {},
    selectedCafe: null,
    cafeKeywords: {},
    cafeMenu: {},

    searchWord: null,
    cafeSearchList: {},
    userSearchList: {},
    keywordSearchList: {},

    surveyState: null,
    surveyList: {},

    surveyRecommendList: {},
    mostLikeRecommendList: {},
    recentLikeRecommendList: {},
    mostStampRecommendList: {},
    recentStampRecommendList: {},
    
  },
  
  getters: {
    //accounts
    isLoggedIn(state) {
      return !!state.authToken
    },
    config: state => ({
      headers: {
        ACCESS_TOKEN: `${state.authToken}`
      }
    }),
  },

  // state변경
  mutations: {
    SET_TOKEN(state, token) {
      state.authToken = token
      cookies.set('auth-token', token)
    },
    SET_USERDATA(state, userData) {
      state.userData = userData
    },
    
    SET_POSTLIST(state, postList) {
      state.postList = postList
    },
    SET_USERPOSTLIST(state, POSTLIST) {
      state.userPostList = POSTLIST
    },
    SET_CAFEPOSTLIST(state, postList) {
      state.cafePostList = postList
    },
    SET_SELECTPOST(state, selectedPost) {
      state.selectedPost = selectedPost
    },

    SET_COMMENTLIST(state, commentList) {
      state.commentList = commentList
    },

    SET_LIKELIST(state, likeList) {
      state.likeList = likeList
    },
    SET_STAMPLIST(state, stampList) {
      state.stampList = stampList
    },

    SET_FOLLOWINGLIST(state, followingList) {
      state.followingList = followingList
    },
    SET_FOLLOWERLIST(state, followerList) {
      state.followerList = followerList
    },

    SET_ADDCAFELIST(state, cafeList) {
      state.cafeList = state.cafeList.concat(cafeList)
    },
    SET_CAFELIST(state, cafeList) {
      state.cafeList = cafeList
    },
    SET_GEOCAFELIST(state, cafeList) {
      state.geoCafeList = cafeList
    },
    SET_SELECTCAFE(state, selectedCafe) {
      state.selectedCafe = selectedCafe
    },
    SET_CAFEKEYWORD(state, keywords) {
      state.cafeKeywords = keywords
    },
    SET_CAFEMENU(state, menuList) {
      state.cafeMenu = menuList
    },
    SET_IMAGEURL(state, imageURL) {
      state.uploadImageURL = imageURL
    },
    SET_SEARCHWORD(state, word) {
      state.searchWord = word
    },
    SET_CAFESEARCHLIST(state, cafeList) {
      state.cafeSearchList = cafeList
    },
    SET_USERSEARCHLIST(state, userList) {
      state.userSearchList = userList
    },
    SET_KEYWORDSEARCHLIST(state, cafeList) {
      state.keywordSearchList = cafeList
    },
    SET_SURVEYRECOMMENDLIST(state, surveyRecommendList) {
      state.surveyRecommendList = surveyRecommendList
    },
    SET_MOSTLIKERECOMMENDLIST(state, mostLikeRecommendList) {
      state.mostLikeRecommendList = mostLikeRecommendList
    },
    SET_RECENTLIKERECOMMENDLIST(state, recentLikeRecommendList) {
      state.recentLikeRecommendList = recentLikeRecommendList
    },
    SET_MOSTSTAMPRECOMMENDLIST(state, mostStampRecommendList) {
      state.mostStampRecommendList = mostStampRecommendList
    },
    SET_RECENTSTAMPRECOMMENDLIST(state, recentStampRecommendList) {
      state.recentStampRecommendList = recentStampRecommendList
    },
    SET_SURVEY(state, survey) {
      state.surveyState = survey
    },
    SET_SURVEYLIST(state, cafeList) {
      state.surveyList = cafeList
    }
  },

  actions: {
    // accounts
    authData({ state, commit }, info) {
      axios.post(SERVER.URL + info.location, info.data)
        .then(res => {
          commit('SET_TOKEN', res.data.data.accessToken)
          state.currentUser = info.data.id
          router.go(-1)
        })
        .catch(error => {
          const msg = error.response.data
          if ( msg === 'NO_ID') {
            alert('존재하지 않는 계정입니다.')
          } else if (msg === 'WRONG_PW') {
            alert('비밀번호를 확인해주세요.')
          } else if (msg === 'EXISTING_ID') {
            alert('이미 존재하는 계정입니다.')
          } else {
            alert("잘못된 접근입니다.")
          }
        })
    },

    signup({ dispatch }, signupData) {
      const info = {
        location: SERVER.ROUTES.signup,
        data: signupData
      }
      dispatch('authData', info)
    },

    login({ state, dispatch }, loginData) {
      if (state.surveyState) {
        dispatch('fetchUserSurvey', loginData.id)
      }
      const info = {
        location: SERVER.ROUTES.login,
        data: loginData
      }
      dispatch('authData', info)
    },

    logout({ state, commit }) {
      commit('SET_TOKEN', null)
      commit('SET_SURVEY', null)
      state.currentUser = null
      cookies.remove('auth-token')
      router.push('/home')
    },

    // user
    fetchUserData({ getters, commit }, userid) {
      return new Promise((resolve, reject) => {
        axios.get(SERVER.URL + SERVER.ROUTES.mypage + `/${userid}`, getters.config)
          .then(res => {
            commit('SET_USERDATA', res.data)
            resolve(res)
          })
          .catch(err => {
            console.error(err.response.data)
            reject(err)
          })
      })
    },

    // post
    createPost({ state, getters }, postList) {
      postList.cafeno = state.selectedCafe.cafeno
      postList.cafename = state.selectedCafe.cafename
      postList.uid = state.currentUser
      postList.image = state.uploadImageURL
      axios.post(SERVER.URL + SERVER.ROUTES.postDetail, postList, getters.config)
        .then((res) => {
          router.push(`/post/detail/${res.data}`)
        })
        .catch(err => console.log('error', err))
      },
    fetchPostList({ commit }, page) {
      axios.get(SERVER.URL + SERVER.ROUTES.postList + page)
      .then(res => {
          commit('SET_POSTLIST', res.data)
        })
        .catch(err => console.error(err))
    },
    fetchCafePostList({ commit }, cafeno) {
      axios.get(SERVER.URL + SERVER.ROUTES.cafePostList + cafeno)
        .then(res => commit('SET_CAFEPOSTLIST', res.data))
        .catch(err => console.error(err))
    },
    fetchUserPostList({ commit }, userId) {
      axios.get(SERVER.URL + SERVER.ROUTES.userPostList + `${userId}`)
        .then(res => commit('SET_USERPOSTLIST', res.data))
        .catch(err => console.error(err))
    },
    postDetail({ commit }, id) {
      axios.get(SERVER.URL + SERVER.ROUTES.postDetail + `/${id}`)
        .then(res => {
          commit('SET_SELECTPOST', res.data)
        })
        .catch(err => console.error(err))
      },
    updatePost({ state, commit, dispatch, getters }, postData) {
      postData.image = state.uploadImageURL
      axios.put(SERVER.URL + SERVER.ROUTES.postDetail, postData, getters.config)
        .then(() => {
          commit('SET_SELECTPOST', postData)
          dispatch('fetchPostList', postData.cafeno)
          dispatch('postDetail', postData.pno)
          router.push(`/post/detail/${postData.pno}`)
        })
        .catch(err => console.error(err))
    },
    deletePost({ state, getters, dispatch }, postId) {
      axios.delete(SERVER.URL + SERVER.ROUTES.postDelete + `${postId}`, getters.config)
        .then(() => {
          dispatch('fetchPostList', state.selectedPost.pno)
          router.push(`/cafe/detail/${state.selectedCafe.cafeno}`)
        })
        .catch(err => console.log(err))
    },
    uploadImage({ dispatch, commit }, postData) {
      return new Promise((resolve, reject) => {
        if (!postData.formData.get("image")) {
          dispatch('updatePost', postData.selectedPost)
        } else {
          axios.post(SERVER.URL + SERVER.ROUTES.uploadImage, postData.formData)
            .then((res) => {
              const msg = res.data
              if (msg === 'NOT_IMAGE_FILE') {
                alert('이미지 파일(jpg, jpeg, png)만 업로드 가능합니다.')
              } else if (postData.selectedPost) {
                commit('SET_IMAGEURL', res.data)
                dispatch('updatePost', postData.selectedPost)
              } else {
                commit('SET_IMAGEURL', res.data)
                dispatch('createPost', postData.postList)
              }
              resolve(res)
            })
            .catch(err => {
              console.log(err)
              reject(err)
            })
        }
      })
    },
    
    // comment
    createComment({ state, getters, dispatch }, commentData) {
      commentData.uid = state.currentUser
      axios.post(SERVER.URL + SERVER.ROUTES.createComment, commentData, getters.config)
        .then(() => {
          dispatch('fetchCommentList', state.selectedPost.pno)
          return null
        })
        .catch(err => console.log(err))
    },
    fetchCommentList({ commit }, postno) {
      axios.get(SERVER.URL + SERVER.ROUTES.commentList + postno)
        .then(res => {
          commit('SET_COMMENTLIST', res.data)
        })
        .catch(err => console.error(err))
    },
    deleteComment({ state, getters, dispatch }, commentId) {
      axios.delete(SERVER.URL + SERVER.ROUTES.deleteComment + `${commentId}`, getters.config)
        .then(() => {
          dispatch('fetchCommentList', state.selectedPost.pno)
        })
        .catch(err => console.log(err))
    },

    // like
    fetchLikeList({ state, getters, commit }) {
      const userid = state.userData.id
      axios.get(SERVER.URL + SERVER.ROUTES.like + `/list/${userid}`, getters.config)
        .then(res => commit('SET_LIKELIST', res.data))
        .catch(err => console.log(err))
    },

    aboutLike({ state, getters }, cafeno) {
      return new Promise((resolve, reject) => {
        if (!getters.isLoggedIn) {
          return null
        } else {
          axios.get(SERVER.URL + SERVER.ROUTES.like + `/check/${cafeno}/${state.userData.id}`, getters.config)
            .then(res => resolve(res.data)) // -> resolve == retrun 역할
            .catch(err => {
              console.error(err.response.data)
              reject(err)
            })
        }
      })
    },

    likeCafe({ state, getters, dispatch }, cafeno) {
      if (!getters.isLoggedIn) {
        alert('로그인이 필요합니다!')
        router.replace(`/accounts/login`)
      }
      return new Promise((resolve, reject) => {
        const userid = state.userData.id
        axios.get(SERVER.URL + SERVER.ROUTES.like + `/check/${cafeno}/${userid}`, getters.config)
          .then(res => {
            if (res.data === 0) {
              const likeData = {
                cafeno: cafeno,
                uid: userid
              }
              axios.post(SERVER.URL + SERVER.ROUTES.like, likeData, getters.config)
                .then(() => {
                  dispatch('fetchLikeList')
                })
                .catch(err => console.log(err))
            } else {
              axios.delete(SERVER.URL + SERVER.ROUTES.like + `/delete/${cafeno}/${userid}`, getters.config)
                .then(() => {
                  dispatch('fetchLikeList')
                })
                .catch(err => console.log(err))
            }
            resolve(res.data)
          })
          .catch(err => {
            console.error(err.response.data)
            reject(err)
          })
      })
    },

    //stamp
    fetchStampList({ state, commit }) {
      const userid = state.userData.id
      axios.get(SERVER.URL + SERVER.ROUTES.stamp + `/list/${userid}`)
        .then(res => commit('SET_STAMPLIST', res.data))
        .catch(err => console.log(err))
    },

    aboutStamp({ state, getters }, cafeno) {
      return new Promise((resolve, reject) => {
        if (!getters.isLoggedIn) {
          return null
        } else {
          axios.get(SERVER.URL + SERVER.ROUTES.stamp + `/check/${cafeno}/${state.userData.id}`, getters.config)
            .then(res => resolve(res.data))
            .catch(err => {
              console.error(err.response.data)
              reject(err)
            })
        }
      })
    }, 

    stampCafe({ state, getters, dispatch }, cafeno) {
      if (!getters.isLoggedIn) {
        alert('로그인이 필요합니다!')
        router.replace(`/accounts/login`)
      }
      return new Promise((resolve, reject) => {
        const userid = state.userData.id
        axios.get(SERVER.URL + SERVER.ROUTES.stamp + `/check/${cafeno}/${userid}`, getters.config)
          .then(res => {
            if (res.data === 0) {
              const stampData = {
                cafeno: cafeno,
                uid: userid
              }
              axios.post(SERVER.URL + SERVER.ROUTES.stamp, stampData, getters.config)
                .then(() => {
                  dispatch('fetchStampList')
                })
                .catch(err => console.log(err))
            } else {
              axios.delete(SERVER.URL + SERVER.ROUTES.stamp + `/delete/${cafeno}/${userid}`, getters.config)
                .then(() => {
                  dispatch('fetchStampList')
                })
                .catch(err => console.log(err))
            }
            resolve(res.data)
          })
          .catch(err => {
            console.error(err.response.data)
            reject(err)
          })
      })
    },

    // follow
    fetchFollowingList({ state, commit }) {
      const userid = state.userData.id
      axios.get(SERVER.URL + SERVER.ROUTES.follow + `/list/following/${userid}`)
        .then(res => commit('SET_FOLLOWINGLIST', res.data))
        .catch(err => console.log(err))
    },
    fetchFollowerList({ state, commit }) {
      const userid = state.userData.id
      axios.get(SERVER.URL + SERVER.ROUTES.follow + `/list/follower/${userid}`)
      .then(res => commit('SET_FOLLOWERLIST', res.data))
      .catch(err => console.log(err))
    },

    aboutFollow({ state, getters }, followingid) {
      axios.get(SERVER.URL + SERVER.ROUTES.follow + `/check/${state.currentUser}/${followingid}`, getters.config)
        .then(res => {
          state.followState = res.data
        })
        .catch(err => console.error(err.response.data))
    },

    followUser({ state, getters, dispatch, }, followingid) {
      if (!getters.isLoggedIn) {
        alert('로그인이 필요합니다!')
        router.push(`/accounts/login`)
      }
      return new Promise((resolve, reject) => {
        const currentUserId = state.currentUser
        axios.get(SERVER.URL + SERVER.ROUTES.follow + `/check/${currentUserId}/${followingid}`, getters.config)
          .then(res => {
            if (res.data === 0) {
              const followData = {
                followingid: followingid,
                uid: currentUserId
              }
              axios.post(SERVER.URL + SERVER.ROUTES.follow, followData, getters.config)
                .then(() => {
                  state.followState = 1 
                  dispatch('fetchFollowerList')
                })
                .catch(err => console.log(err))
              } else {
                axios.delete(SERVER.URL + SERVER.ROUTES.follow + `/delete/${currentUserId}/${followingid}`, {followingid, currentUserId,}, getters.config)
                .then(() => {
                  state.followState = 0
                  dispatch('fetchFollowerList')
                })
                .catch(err => console.log(err))
            }
            resolve(res)
          })
          .catch(err => {
            console.error(err.response.data)
            reject(err)
          })
      })
    },
   
    //cafe
    fetchCafeList({ state, commit }, page) {
      const cafeLen = Object.keys(state.cafeList).length
      axios.get(SERVER.URL + SERVER.ROUTES.cafeList + page)
      .then(res => {
        if (!cafeLen) {
          commit('SET_CAFELIST', res.data)
        } else if (page === 1) {
            return
          } else {
            commit('SET_ADDCAFELIST', res.data)
          }
        })
        .catch(err => console.error(err))
    },
    cafeDetail({ commit, dispatch }, id) {
      axios.get(SERVER.URL + SERVER.ROUTES.cafeDetail + id)
      .then(res => {
        commit('SET_SELECTCAFE', res.data)
        dispatch('cafeKeyword', id)
        dispatch('cafeMenu', id)
      })
      .catch(err => console.error(err))
    },
    cafeKeyword({ commit }, cafeno) {
      axios.get(SERVER.URL + SERVER.ROUTES.cafeKeyword + cafeno)
        .then( res => {
          commit('SET_CAFEKEYWORD', res.data)
        })
        .catch(err => console.error(err))
    },
    cafeMenu({ commit }, cafeno) {
      axios.get(SERVER.URL + SERVER.ROUTES.cafeMenu+ cafeno)
        .then( res => {
          commit('SET_CAFEMENU', res.data)
        })
        .catch(err => console.error(err))
    },
    
    // search
    // - cafeSearch, userSearch, keywordSearch
    searchCafeUser({ commit }, word) {
      if (!word) {
        commit('SET_CAFESEARCHLIST', {})
        commit('SET_USERSEARCHLIST', {})
        commit('SET_KEYWORDSEARCHLIST', {})
        commit('SET_SEARCHWORD', null)
      } else {
        commit('SET_SEARCHWORD', word)
        axios.get(SERVER.URL + SERVER.ROUTES.cafeSearch + word)
          .then((res) => {
            commit('SET_CAFESEARCHLIST', res.data)
          })
          .catch(err => console.error(err))
  
        axios.get(SERVER.URL + SERVER.ROUTES.userSearch + word)
          .then((res) => {
            commit('SET_USERSEARCHLIST', res.data)
          })
          .catch(err => console.error(err))

        axios.get(SERVER.URL + SERVER.ROUTES.keywordSearch + word)
          .then((res) => {
            commit('SET_KEYWORDSEARCHLIST', res.data)
          })
          .catch(err => console.error(err))
      }
    },
    
    // geo
    geo({ commit }, location) {
      if (!location) {
        commit('SET_GEOCAFELIST', {})
      } else {
        const userLoc = {
          lat: location.coords.latitude, //위도
          lng: location.coords.longitude, //경도
        }
        axios.post(SERVER.URL + SERVER.ROUTES.geolocation, userLoc)
          .then(res => {
            commit('SET_GEOCAFELIST', res.data)
          })
          .catch(err => {
            console.error(err)
          })
      }
    },

    surveySubmit({ state, commit, dispatch, getters }, result ) {
      if (getters.isLoggedIn) {
        dispatch('fetchUserSurvey', state.currentUser)
      }
      axios.get(SERVER.URL + SERVER.ROUTES.surveyResult + result)
        .then(res => {
          commit('SET_SURVEY', result)
          commit('SET_SURVEYLIST', res.data)
          router.push('/survey/result')
        })
        .catch(err => console.error(err))
    },

    fetchUserSurvey({ state }, userid) {
      const survey = state.surveyState
      axios.put(SERVER.URL + SERVER.ROUTES.surveyResult + survey + '/' + userid)
        .then(res => console.log(res))
        .catch(err => console.error(err))
    },

    //recommend
    fetchSurveyRecommendList({ state, commit }) {
      const type = state.surveyState
      axios.get(SERVER.URL + SERVER.ROUTES.surveyResult + `list/${type}/1`)
        .then(res => commit('SET_SURVEYRECOMMENDLIST', res.data))
        .catch(err => console.error(err))
    },

    fetchMostLikeRecommendList({ state, getters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.recommend + "like/count/")
        .then(res => commit('SET_MOSTLIKERECOMMENDLIST', res.data))
        .catch(err => console.error(err))
      if (getters.isLoggedIn) {
        const userid = state.userData.id
        axios.get(SERVER.URL + SERVER.ROUTES.recommend + `like/count/${userid}`, getters.config)
          .then(res => {
            if (res.data) {
              commit('SET_MOSTLIKERECOMMENDLIST', res.data)
            }
          })
          .catch(err => console.error(err))
      }
    },

    fetchRecentLikeRecommendList({ state, getters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.recommend + "like/recent/")
        .then(res => commit('SET_RECENTLIKERECOMMENDLIST', res.data))
        .catch(err => console.error(err))
      if (getters.isLoggedIn) {
        const userid = state.userData.id
        axios.get(SERVER.URL + SERVER.ROUTES.recommend + `like/recent/${userid}`, getters.config)
          .then(res => {
            if (res.data) {
              commit('SET_RECENTLIKERECOMMENDLIST', res.data)
            }
          })
          .catch(err => console.error(err))
      }
    },

    fetchMostStampRecommendList({ state, getters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.recommend + "stamp/count")
        .then(res => commit('SET_MOSTSTAMPRECOMMENDLIST', res.data))
        .catch(err => console.error(err))
      if (getters.isLoggedIn) {
        const userid = state.userData.id
        axios.get(SERVER.URL + SERVER.ROUTES.recommend + `stamp/count/${userid}`, getters.config)
          .then(res => {
            if (res.data) {
              commit('SET_MOSTSTAMPRECOMMENDLIST', res.data)
            }
          })
          .catch(err => console.error(err))
      }
    },

    fetchRecentStampRecommendList({ state, getters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.recommend + "stamp/recent/")
        .then(res => commit('SET_RECENTSTAMPRECOMMENDLIST', res.data))
        .catch(err => console.error(err))
      if (getters.isLoggedIn) {
        const userid = state.userData.id
        axios.get(SERVER.URL + SERVER.ROUTES.recommend + `stamp/recent/${userid}`, getters.config)
          .then(res => {
            if (res.data) {
              commit('SET_RECENTSTAMPRECOMMENDLIST', res.data)
            }
          })
          .catch(err => console.error(err))
      }
    },

  },

  modules: {
  },
  plugins: [
    createPersistedState()
  ]
})