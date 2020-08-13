import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router'
import axios from 'axios'
import cookies from 'vue-cookies'
import SERVER from '../api/django_rest_framework'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // user, accounts 
    authToken: cookies.get('auth-token'),
    userData: {},
    userLikedList: [],
    birthdayList: [],
    movieData: {},

    // movies
    newReleasesList: [],
    recommendationsList: [],
    popularList: [],
    reviewList: [],
    searchResult: [],

    // articles
    articleList: [],
    article: {},
    commentList: [],
    comment: {},
    articles: [],
  },

  getters: {
    // accounts, user
    isLoggedIn: state => !!state.authToken,
    config: state => ({
      headers: {
        Authorization: `Token ${state.authToken}`
      }
    }),

    // movies
    genreInfo: state => {
      const genres = state.movieData.genre.split(',')
      let result = ''
      for (const g of genres) {
        result += g + ' ' 
      }
      return result
    },
    notEnglish: state => {
      return state.movieData.language === 'en'
    },
    likedMovie: state => {
      return !!state.movieData.liked_users.includes(state.userData.id)
    },
  },

  mutations: {
    // user, accounts
    SET_TOKEN(state, token) {
      state.authToken = token
      cookies.set('auth-token',token)
    },
    SET_USERDATA(state, userData) {
      state.userData = userData
    },
    SET_LIKE_LIST(state, userLikedList) {
      state.userLikedList = userLikedList
    },
    SET_BIRTHDAY_LIST(state, birthdayList) {
      state.birthdayList = birthdayList
    },

    // movies
    SET_MOVIE_DATA(state, movieData) {
      state.movieData = movieData
    },
    SET_NEW_RELEASES(state, newReleasesList) {
      state.newReleasesList = newReleasesList
    },
    SET_RECOMMENDATIONS(state, recommendationsList) {
      state.recommendationsList = recommendationsList
    },
    SET_POPULAR(state, popularList) {
      state.popularList = popularList
    },
    SET_REVIEW_LIST(state, reviewList) {
      state.reviewList = reviewList
    },
    SET_SEARCH_RESULT(state, searchResult) {
      state.searchResult = searchResult
    },

    // articles
    SET_ARTICLE_LIST(state, articles) {
      state.articleList = articles
    },
    SET_ARTICLE(state, article) {
      state.article = article
    },
    SET_COMMENT_LIST(state, comments) {
      state.commentList = comments
    },
    SET_COMMENT(state, comment) {
      state.comment = comment
    },
  },

  actions: {
    // user_auth, accounts
    authData({ commit, dispatch }, info) {
      axios.post(SERVER.URL + info.location, info.data)
      .then(res => {
        commit('SET_TOKEN', res.data.key)
        dispatch('fetchUserData')
        router.push('/')
      })
      .catch(err => console.error(err.response.data))
    },

    signup({ dispatch }, signupData) {
      const info = {
        location: SERVER.ROUTES.signup,
        data: signupData
      }
      dispatch('authData', info)
    },

    login({ dispatch }, loginData) {
      const info = {
        location: SERVER.ROUTES.login,
        data: loginData,
      }
      dispatch('authData', info)
    },
    
    logout({ getters, commit }) {
      axios.post(SERVER.URL + SERVER.ROUTES.logout, null, getters.config)
       .then(() => {
        commit('SET_TOKEN', null)
        commit('SET_USERDATA', {})
        cookies.remove('auth-token')
        router.push('/')
       })
       .catch(err => console.error(err.response.data))
    },

    fetchUserData({ getters, commit }) {
      return new Promise((resolve, reject) => {
        axios.get(SERVER.URL + SERVER.ROUTES.profile, getters.config)
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

    fetchLikeList({state, getters, commit}) {
      axios.get(SERVER.URL + SERVER.ROUTES.likeList + `${state.userData.id}/`, getters.config)
      .then(res => commit('SET_LIKE_LIST', res.data))
      .catch(err => console.error(err.response.data))
    },

    fetchBirthdayList({ state, getters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.birthdayList + `${state.userData.id}/`, getters.config)
        .then(res => commit('SET_BIRTHDAY_LIST', res.data))
        .catch(err => console.error(err.response.data))
    },

    // follow({ getters }, username) {
    //   axios.post(SERVER.URL + SERVER.ROUTES.profile + username + '/follow/', username, getters.config)
    //     .then(res => {
    //       console.log(res)
    //     })
    //     .catch(err => console.error(err.response.data))
    // },


    // movies
    fetchNewReleases({ commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.new)
        .then(res => commit('SET_NEW_RELEASES', res.data))
        .catch(err => console.error(err.response.data))
    },

    fetchRecommendations({ commit, getters, state }) {
      axios.get(SERVER.URL + SERVER.ROUTES.recommendations + `${state.userData.id}/`, getters.config)
        .then(res => commit('SET_RECOMMENDATIONS', res.data))
        .catch(err => console.error(err.response.data))
    },

    fetchPopular({ commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.popular)
        .then(res => commit('SET_POPULAR', res.data))
        .catch(err => console.error(err.response.data))
    },

    fetchMovieData({ commit }, movieId) {
      axios.get(SERVER.URL + `/movies/${movieId}/`)
        .then(res => commit('SET_MOVIE_DATA', res.data))
        .catch(err => console.error(err.response.data))
    },

    likeMovie({ state, getters, commit }) {
      axios.post(SERVER.URL + SERVER.ROUTES.like + `${state.movieData.id}/`, null, getters.config)
        .then(res => commit('SET_MOVIE_DATA', res.data))
        .catch(err => console.error(err.response.data))
    },

    createReview({ getters, dispatch }, { reviewData, movieId }) {
      axios.post(SERVER.URL + `/movies/${movieId}/review/`, reviewData, getters.config)
        .then(() => dispatch('fetchReview', movieId))
        .catch(err => console.error(err.response.data))
    },

    fetchReview({ getters, commit }, movieId) {
      axios.get(SERVER.URL + `/movies/${movieId}/review/`, getters.config)
        .then(res => commit('SET_REVIEW_LIST', res.data))
        .catch(err => console.log(err.response.data))
    },

    deleteReview({ getters, commit, dispatch }, { reviewId, movieId }) {
      axios.delete(SERVER.URL + `/movies/${movieId}/review/${reviewId}/`, getters.config)
      .then(res => {
        commit('SET_REVIEW_LIST', res.data)
        dispatch('fetchReview', movieId)
      })
      .catch(err => console.error(err.response.data))
    },

    getSearchResult({ commit }, searchKeyword) {
      const strippedKeyword = searchKeyword.replace(/\s+/g, '')
      axios.get(SERVER.URL + `/movies/${strippedKeyword}/`)
        .then(res => commit('SET_SEARCH_RESULT', res.data))
        .catch(err => console.log(err.response.data))
    },
    clearSearchResult({ commit }) {
      commit('SET_SEARCH_RESULT', [])
    },


    // articles
    fetchArticles({ commit }) {
      axios.get(SERVER.URL+ SERVER.ROUTES.articles)
      .then(res => commit('SET_ARTICLE_LIST', res.data))
      .catch(err => console.error(err.response.data))
    },
    
    detailArticle({ getters, commit }, articleId) {
      axios.get(SERVER.URL+ SERVER.ROUTES.articles + `${articleId}/`, getters.config)
      .then(res => commit('SET_ARTICLE', res.data))
      .catch(err => console.error(err.response.data))
    },

    createArticle({ getters }, articleData) {
      axios.post(SERVER.URL + SERVER.ROUTES.articles, articleData , getters.config)
       .then(() => router.push('/articles/'))
       .catch(err => console.error(err.response.data))
    },

    updateArticle({ getters }, { articleData, articleId }) {
      axios.put(SERVER.URL + SERVER.ROUTES.articles + `${articleId}/`, articleData , getters.config)
       .then(() => router.push(`/articles/${articleId}/`))
       .catch(err => console.error(err.response.data))
    },

    deleteArticle({ getters, commit }, articleId) {
      axios.delete(SERVER.URL+ SERVER.ROUTES.articles + `${articleId}/`, getters.config)
      .then(() => {
        commit('SET_ARTICLE', {})
        router.push('/articles/')
      })
      .catch(err => console.error(err.response.data))
    },

    fetchComment({ getters, commit }, articleId) {
      axios.get(SERVER.URL+ SERVER.ROUTES.articles+ `${articleId}/comments/`, getters.config)
      .then(res => commit('SET_COMMENT_LIST', res.data))
      .catch(err => console.error(err.response.data))
    },

    createComment({ getters, dispatch },{ commentData, articleId }) {
      axios.post(SERVER.URL + SERVER.ROUTES.articles+ `${articleId}/comments/`, commentData , getters.config)
       .then(() => dispatch('fetchComment', articleId))
       .catch(err => console.error(err.response))
    },

    deleteComment({ getters, commit, dispatch }, { articleId, commentId }) {
      axios.delete(SERVER.URL+ SERVER.ROUTES.articles + `${articleId}/comments/${commentId}/`, getters.config)
      .then(() => {
        commit('SET_COMMENT', {})
        dispatch('fetchComment', articleId)
      })
      .catch(err => console.error(err.response.data))
    },

  },

  modules: {
  }

})