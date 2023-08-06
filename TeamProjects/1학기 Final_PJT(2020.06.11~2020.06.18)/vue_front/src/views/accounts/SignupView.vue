<template>
  <div class="container py-4">
    <h1 class="text-center py-2">Signup</h1>
    <div class="mx-auto" :class="windowWidth > 720 ? 'w-50': 'w-100'">
        <form>
            <div class="form-group">
                <label for="username">Username</label>
                <input v-model="signupData.username" type="text" class="form-control" id="username" placeholder="Enter a username"> 
            </div>

            <div class="form-group">
                <label for="password">Password</label>
                <input v-model="signupData.password1" type="password" class="form-control" id="password" placeholder="Enter a password">
            </div>

            <div class="form-group">
                <label for="passwordConfirmation">Password Confirmation</label>
                <input v-model="signupData.password2" type="password" class="form-control" id="passwordConfirmation" placeholder="Confirm your password">
            </div>

            <div class="form-row">
              <div class="form-group col-10 col-md-5">
                <label for="birthDate">Birthday</label>
                <br>
                <b-form-input id="birthDate" type="date" v-model="signupData.date_of_birth" class="mb-2"></b-form-input>
              </div>

              <div class="form-group col-10 col-md-5 mx-md-4">
                <label for="favoriteGenre">Favorite Movie Genre</label>
                <select v-model="signupData.favorite_genre" class="form-control" id="favoriteGenre">
                  <option selected>Action</option>
                  <option>Adventure</option>
                  <option>Animation</option>
                  <option>Comedy</option>
                  <option>Crime</option>
                  <option>Documentary</option>
                  <option>Drama</option>
                  <option>Family</option>
                  <option>Fantasy</option>
                  <option>History</option>
                  <option>Horror</option>
                  <option>Music</option>
                  <option>Mystery</option>
                  <option>Romance</option>
                  <option>Science Fiction</option>
                  <option>TV Movie</option>
                  <option>Thriller</option>
                  <option>War</option>
                  <option>Western</option>
                </select>
                <small id="passwordConfirmationHelp" class="form-text text-muted"> Tell us your favorite movie genre</small>      
              </div>
            </div>
        </form>  

        <button @click="signup(signupData)" class="signupButton btn text-white">Signup</button>    
    </div>

  </div>
</template>

<script>
import { mapActions } from "vuex";
 
export default {
  name: "SignupView",

  data() {
    return {
      signupData: {
        username: null,
        password1: null,
        password2: null,
        date_of_birth: null,
        favorite_genre: null,
      },
      windowWidth: window.innerWidth,
    };
  },


  methods: {
    ...mapActions(["signup"]),
  },
} 
</script>

<style scoped>
  .signupButton {
    background-color: rgba(0, 178, 149, 1);
  }
</style>