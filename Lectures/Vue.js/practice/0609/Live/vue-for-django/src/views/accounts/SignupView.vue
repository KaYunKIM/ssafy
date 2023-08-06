<template>
  <div>
      <h1>Signup</h1>
      <div>
          <label for="username">username: </label>
          <input v-model="signupData.username" id="username" type="text">
      </div>
      <div>
          <label for="password1">password1: </label>
          <input v-model="signupData.password1" id="password1" type="password">
      </div>
      <div>
          <label for="password2">password2: </label>
          <input v-model="signupData.password2" id="password2" type="password">
      </div>
      <div>
          <button @click="signup">Signup</button>
      </div>
  </div>
</template>

<script>
export default {
    name: 'SignupView',
    data () {
        return {
            signupData: {
                username: null,
                password1: null,
                password2: null,
            }
        }
    },
    methods: {
        signup() {
            this.$emit('submit-signup-data', this.signupData)
        }
    },

}
</script>

<style>

</style>