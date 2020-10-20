<template>
<v-bottom-navigation>
  <v-app-bar
    fixed
    style="background-image: linear-gradient(45deg, #a6c0fe, #f68084);"
    hide-on-scroll
    >
      <v-toolbar-title class="align-center">
        <router-link to="/home" class="link-text">
          <v-img src="@/assets/cafeIn_logo.png" alt="logoImage" width="100px"></v-img>
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <router-link v-if="!isLoggedIn" to="/accounts/login" class="link-text">
        <v-btn><span class="white--text">Login</span><span class="material-icons mx-3 white--text">login</span></v-btn>
      </router-link>
      <router-link v-if="!isLoggedIn" to="/accounts/signup" class="link-text">
        <v-btn><span class="white--text">Signup</span><span class="material-icons mx-3 white--text">group_add</span></v-btn>
      </router-link>
      <router-link v-if="isLoggedIn" :to="`/accounts/${currentUser}`" class="link-text">
        <v-btn><span class="white--text">Mypage</span><span class="material-icons mx-3 white--text">assignment_ind</span></v-btn>
      </router-link>
      <router-link to="/" class="link-text">
        <v-btn><span class="white--text">Survey</span><span class="material-icons mx-3 white--text">fact_check</span></v-btn>
      </router-link>
      <router-link to="/search" class="link-text">
        <v-btn><span class="white--text">Search</span><span class="material-icons mx-3 white--text">search</span></v-btn>
      </router-link>
      <router-link v-if="isLoggedIn" to="#" @click.native="logout" class="link-text">
        <v-btn><span class="white--text">Logout</span><span class="material-icons mx-3 white--text">logout</span></v-btn>
      </router-link>
    </v-app-bar>
  </v-bottom-navigation>
</template>

<script>
import { mapGetters, mapActions, mapState } from 'vuex';

export default {
  name: 'AppBar',

  computed: {
    ...mapState(['currentUser']),
    ...mapGetters(['isLoggedIn']),
  },

  methods: {
    ...mapActions(['logout']),
    onMypage(userid) {
      this.$router.push(`/accounts/${userid}`)
    }
  },
}
</script>

<style scoped>
.link-text {
  text-decoration: none;
  color: white;
}
</style>