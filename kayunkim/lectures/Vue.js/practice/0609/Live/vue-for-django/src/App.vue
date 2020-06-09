<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link v-if="!isLoggedIn" :to="{ name: 'Login' }">Login</router-link> |
      <router-link v-if="isLoggedIn" to="/accounts/signup">Signup</router-link> |
      <router-link v-if="isLoggedIn" :to="{ name: 'Create' }">New Article</router-link> |
      <router-link v-if="isLoggedIn" to="/accounts/logout" @click.native="logout">Logout</router-link>
     
    </div>
    <router-view @submit-login-data="login" @sumbit-signup-data="signup" />
  </div>
</template>

<script>
import axios from 'axios'

//axios.post(URS, BODY, HEADER 순서)
const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'App',
  data() {
    return {
      isLoggedIn: false,
      
    }
  },
  methods: {
    setCookie(token) {
      this.$cookies.set('auth-token', token)
      this.isLoggedIn = true
    },
    signup(signupData) {
      axios.post(SERVER_RUL + '/rest-auth/signup/', signupData)
        .then(res => {
          this.setCookie(res.data.key)
          this.$route.push({ name: 'Home' })
        })
        .catch(err => console.log(err.response.data))
    },
    login(loginData) {
      axios.post(SERVER_RUL + '/rest-auth/login/', loginData)
        .then(res => {
          this.setCookie(res.data.key)
          this.$route.push({ name: 'Home' })
          // this.$cookies.set('auth-token', res.data.key)
          // this.token = res.data.key // { key: key값 }
        })
        .catch(err => console.log(err.response.data))
    },
    logout() {
      const requestHeaders = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`
        }
      }

      axios.post(SERVER_URL + '/rest-auth/logout/', null, requestHeaders)
        .then(() => {
          this.$cookies.remove('auth-token')
          this.isLoggedIn = false
          this.$router.push({ name: 'Home' })
        })
        .catch(err => console.log(err.response.data))
    }

  },
  mounted() {
    this.isLoggedIn = this.$cookies.isKey('auth-token')
  }
  
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
