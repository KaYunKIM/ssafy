<template>
  <div> 
    <h1>Signup</h1>
      <div class="container form-group text-left">
        <label for="userId">아이디</label>
        <input v-model="signupInfo.username" type="text" class="form-control" id="userId" aria-describedby="userIdMessage">
        <small id="userIdMessage" class="form-text text-muted">아이디를 작성해주세요</small>
        <br>
        <label for="userPassword1">비밀번호</label>
        <input v-model="signupInfo.password1" type="password" class="form-control" id="userPassword1" aria-describedby="userPwMessage1">
        <small id="userPwMessage1" class="form-text text-muted">비밀번호를 작성해주세요</small>
        <br>
        <label for="userPassword2">비밀번호 확인</label>
        <input v-model="signupInfo.password2" type="password" class="form-control" id="userPassword2" aria-describedby="userPwMessage2">
        <small id="userPwMessage2" class="form-text text-muted">비밀번호를 다시 한번 입력해주세요</small>
        <br>
        <button @click="emitSignupSubmit" class="btn btn-primary">확인</button>
      </div>
  </div>
</template>

<script>
export default {
  name: 'signup',
  data() {
    return {
      signupInfo: {
        username: '',
        password1: '',
        password2: '',
      }
    }
  }, // data
  methods: {
    emitSignupSubmit() {
        this.$emit('signup-submit', this.signupInfo)
    }
  }, 
}


</script>

<style>

</style>