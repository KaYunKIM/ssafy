<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link v-if="!isLoggedIn" to="/login">Login</router-link> |
      <router-link v-if="isLoggedIn" @click.native="logout" to="/logout">Logout</router-link> | 
      <router-link v-if="!isLoggedIn" to="/signup">Signup</router-link> |
      <router-link to="/create" >Create</router-link> | 
      <router-link to="/articles">Article List</router-link>
    </div>
    <router-view 
      @login-submit="login"
      @signup-submit="signup"
    />
  </div>
</template>

<script>
import axios from 'axios'
const API_BASE_URL = 'http://localhost:8000'

export default {
  name: 'App',
  data() {
    return {
      isLoggedIn: false,
    }
  },
  methods: {
    setCookie(key) {
      this.$cookies.set('auth-token', key)
      this.isLoggedIn = true
    },
    login(loginInfo) {
      const API_LOGIN_URL = API_BASE_URL + '/rest_auth/login/'
      axios.post(API_LOGIN_URL, loginInfo) // axios.post(URL, data, config)
        .then(res => {
          // expire time: 1day 하루살이(하루동안 살아있음)
          this.setCookie(res.data.key)
          this.$router.push('/')
        })
        .catch(err => {
          console.error(err)
        })
    },
    logout() {
      const API_LOGOUT_URL = API_BASE_URL + '/rest_auth/logout/'
      const config = {
        headers: {
          Authorization: `Token ${this.cookies.get('auth-token')}`
        }
      }
      axios.post(API_LOGOUT_URL, {}, config) // axios.post(URL, data, config)
        .then(() => {
          this.$cookies.remove('auth-token')
          this.isLoggedIn = false
          this.$router.push('/')
        })
        .catch(err => {
          console.log(err)
        })
    },
    signup(signupInfo) {
      const API_SIGNUP_URL = API_BASE_URL + '/rest_auth/registration/'
      axios.post(API_SIGNUP_URL, signupInfo)
        .then(res => {
          this.setCookie(res.data.key)
          this.$router.push('/')
        })
        .catch(err => {
          console.error(err)
        })
    },
    
  },
  created() {
      if (this.$cookies.isKey('auth-token')) {
        this.isLoggedIn = true
      }
    },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
