<template>
  <div>
      <h1>Login</h1>
      <div>
          <label for="username">username: </label>
          <input v-model="loginData.username" id="username" type="text">
      </div>
      <div>
          <label for="password">password: </label>
          <input v-model="loginData.password" id="password" type="password">
      </div>
      <div>
          <button @click="login">Login</button>
      </div>
  </div>
</template>

<script>
export default {
    name: 'LoginView',
    data () {
        return {
            loginData: {
                username: null,
                password: null,
            }
        }
    },
    methods: {
        login() {
            this.$emit('submit-login-data', this.loginData)
        }
    },

}
</script>

<style>

</style>