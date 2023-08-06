<template>
  <div>
      <h1>Login</h1>
      username: <input v-model="loginInfo.username" type="text">
      <br>
      password: <input v-model="loginInfo.password" type="password">
      <br>
      <button @click="emitLoginSubmit">login</button>
  </div>
</template>

<script>
export default {
    name: 'LoginView',
    data() {
        return {
            loginInfo: {
                username: '',
                password: '',
            },
        }
    },
    methods: {
        emitLoginSubmit() {
            this.$emit('login-submit', this.loginInfo)
        },

    },
    created() {
        if (this.$cookies.isKey('auth-token')) {
            this.$router.push('/')
        }
    },
}
</script>

<style>

</style>