<template>
  <div>
      <h1>Signup</h1>
      username: <input v-model="signupInfo.username" type="text">
      <br>
      password1: <input v-model="signupInfo.password1" type="password">
      <br>
      password2: <input v-model="signupInfo.password2" type="password">
      <br>
      <button @click="emitSignupSubmit">login</button>
  </div>
</template>

<script>
export default {
    name: 'SignupView',
    data() {
        return {
            signupInfo: {
                username: '',
                password1: '',
                password2: '',
            },
        }
    },
    methods: {
        emitSignupSubmit() {
            this.$emit('signup-submit', this.signupInfo)
        },
    },
}
</script>

<style>

</style>