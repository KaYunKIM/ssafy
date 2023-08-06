<template>
  <div class="home">
    <div class="banner d-flex flex-column justify-content-center">
      <h1 class="ml-5 display-3 text-center text-md-left">Welcome.</h1>
      <h3 class="ml-5 text-center text-md-left">Search movies and get recommedations just for you.</h3>
    </div>
    <RecommendationsList v-if="isLoggedIn"/>
    <NewReleasesList />
  </div>
</template>

<script>
// @ is an alias to /src
import { mapGetters } from 'vuex'
import NewReleasesList from '../components/NewReleasesList.vue'
import RecommendationsList from '../components/RecommendationsList.vue'

export default {
  name: 'HomeView',

  components: {
    NewReleasesList,
    RecommendationsList,
  },

  computed: {
    ...mapGetters(['isLoggedIn']),
  },
}
</script>

<style scoped>
  .banner {
    height: 350px;
    background-image: url('../assets/main_page_banner.jpg');
    background-position: center center;
    background-size: cover;
    background-color: rgba(234, 234, 234, 1);
    color: rgba(234, 234, 234, 1);
  }
</style>
