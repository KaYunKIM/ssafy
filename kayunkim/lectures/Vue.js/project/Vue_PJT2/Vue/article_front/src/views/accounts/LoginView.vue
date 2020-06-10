<template>
  <div> 
    <h1>Login</h1>
      <div class="container form-group text-left">
        <label for="userId">아이디</label>
        <input v-model="loginInfo.username" type="text" class="form-control" id="userId" aria-describedby="userIdMessage">
        <small id="userIdMessage" class="form-text text-muted">아이디를 작성해주세요</small>
        <br>
        <label for="userPassword">비밀번호</label>
        <input v-model="loginInfo.password" type="password" class="form-control" id="userPassword" aria-describedby="userPwMessage">
        <small id="userPwMessage" class="form-text text-muted">비밀번호를 작성해주세요</small>
        <br>
        <button @click="emitLoginSubmit" class="btn btn-primary">확인</button>
      </div>
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
  }, //data
  methods: {
    emitLoginSubmit() {
      this.$emit('login-submit', this.loginInfo)
    },    
  }, //methods
}
</script>

<style>

</style>