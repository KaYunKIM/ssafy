<template>
  <div id="app">
    <div id="nav">
      <router-link to="/articles">목록으로 | </router-link> 
      <router-link v-if="!isLoggedIn" to="/login">Login | </router-link> 
      <router-link v-if="!isLoggedIn" to="/signup">Signup | </router-link>
      <router-link v-if="isLoggedIn" @click.native="logout" to="/logout">Logout</router-link>
      <br>
      <router-link class="btn btn-warning" v-if="isLoggedIn" to="/articles/create" tag="button">글쓰기</router-link>
    </div>
    <router-view
      @login-submit="login"
      @signup-submit="signup"
    />
  </div>
</template>

<script>
const API_BASE_URL = 'http://localhost:8000'
export default {
  namd: 'App',
  data() {
    return {
      isLoggedIn: false,
    } 
  }, // data
  methods: {
    setCookie(key) {
        this.$cookies.set('auth-token', key)
        this.isLoggedIn = true
    },
    login(loginInfo) {
      const API_LOGIN_URL = API_BASE_URL + '/rest-auth/login/'
      this.$axios.post(API_LOGIN_URL, loginInfo)
      .then(res => {
        this.setCookie(res.data.key)
        this.$router.push('/')
      })
      .catch(err => {
        console.log(err)
      })
    },
    signup(signupInfo) {
      const API_SIGNUP_URL = API_BASE_URL + '/rest-auth/signup/'
      this.$axios.post(API_SIGNUP_URL, signupInfo)
        .then(res => {
          this.setCookie(res.data.key)
          this.$router.push('/')
        })
        .catch(err => {
          console.log(err)
        })
    },
    logout() {
      const API_LOGOUT_URL = API_BASE_URL + '/rest-auth/logout/'
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }        
      }
      this.$axios.post(API_LOGOUT_URL, {}, config)
        .then(() => {
          this.$cookies.remove('auth-token')
          this.isLoggedIn = false
          this.$router.push('/')
        })
        .catch(err => {
          console.log(err)
        })
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
