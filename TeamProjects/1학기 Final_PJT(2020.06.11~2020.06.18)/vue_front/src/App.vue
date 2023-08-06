<template>
  <div id="app">
    <!-- navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark">
      <a class="navbar-brand p-0"><router-link class="nav-link text-white" to="/">Movies</router-link></a>

      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <router-link v-if="!isLoggedIn" class="nav-link" to="/accounts/login">Login</router-link>
          </li>
          <li class="nav-item">
            <router-link v-if="!isLoggedIn" class="nav-link" to="/accounts/signup">Signup</router-link>
          </li>
          <li class="nav-item">
            <router-link v-if="isLoggedIn" class="nav-link" :to="`/accounts/${userData.username}`">My Page</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/movies">Movies</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/articles">Community</router-link>
          </li>
          <li class="nav-item">
            <router-link v-if="isLoggedIn" class="nav-link" to="#" @click.native="logout">Logout</router-link>
          </li>
        </ul>
      </div>
    </nav>

    <!-- router-view -->
    <router-view/>

    <!-- footer -->
    <div class="position-static footer">
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'

export default {
  name: 'App',
  
  computed: {
    ...mapState(['userData']),
    ...mapGetters(['isLoggedIn'])
  },

  methods: {
    ...mapActions(['logout',])
  },

}
</script>

<style>
  @import url(https://fonts.googleapis.com/css?family=Oswald);
  @import url(https://fonts.googleapis.com/css?family=Lato);

  #app {
   font-family: 'Lato', sans-serif;
  }

  .navbar {
    background-color: rgba(51, 101, 138, 1);
  }

  .footer {
    height: 100px;
    width: 100%;
    bottom: 0;
  }
</style>

