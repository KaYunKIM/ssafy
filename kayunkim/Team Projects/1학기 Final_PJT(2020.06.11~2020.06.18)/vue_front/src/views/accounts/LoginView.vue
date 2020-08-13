<template>
  <div class="container py-4">
    <h1 class="text-center py-2">Login</h1>
    <div class="mx-auto" :class="windowWidth > 720 ? 'w-50': 'w-100'">
      <form>
          <div class="form-group">
              <label for="username">Username</label>
              <input v-model="loginData.username" type="text" class="form-control" id="username">
              <small id="usernameHelp" class="form-text text-muted">Please enter your username</small>
          </div>
          <div class="form-group">
              <label for="password">Password</label>
              <input @keypress.enter="login(loginData)" v-model="loginData.password" type="password" class="form-control" id="password">
              <small id="passwordHelp" class="form-text text-muted">Please enter your password</small>
          </div>
      </form>
      <button @click="login(loginData)" class="loginButton btn text-white">Login</button>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
    name: 'LoginView',
    data() {
        return {
            loginData: {
                username: null,
                password: null,
            },
            windowWidth: window.innerWidth,
        }
    },
    // store로 보내기
    methods: {
        ...mapActions(['login'])
    }

}
</script>

<style scoped>
  .loginButton {
    background-color: rgba(0, 178, 149, 1);
  }
</style>