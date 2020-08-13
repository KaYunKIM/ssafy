<template>
  <div class="recommendations container mt-4 mb-1">
    <h1 class="pb-2">For You</h1>
    <div class="d-flex flex-row recommendations-list">
      <router-link :to="`/movies/${movie.id}`" v-for="movie in recommendationsList" :key="movie.id" class="card col-4 col-md-2 text-decoration-none text-dark px-0 border-0">
        <img :src="movie.poster_url" class="card-img-top" alt="movie poster">
        <!-- <span class="badge recommendation-reason text-white position-absolute">Because you like Comedy</span> -->
        <div class="card-body">
          <p class="card-title">{{ movie.title }}</p>
          <small class="text-muted">{{ movie.release_date }}</small>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState, mapGetters } from 'vuex'

export default {
  name: 'RecommendationsList',

  computed: {
    ...mapState(['recommendationsList', 'userData']),
    ...mapGetters(['isLoggedIn'])
  },

  methods: {
    ...mapActions(['fetchRecommendations', 'fetchUserData'])
  },

  created() {
    this.fetchUserData()
    .then(() => {
      this.fetchRecommendations()
    })
  }
}
</script>

<style scoped>
  .recommendations-list {
    overflow-x: scroll;
    overflow-y: hidden;
    white-space: nowrap;
  }

  .recommendation-reason {
    background-color: rgba(239, 111, 108, 1);
    top: 10px;
  }

  .card {
    white-space: normal;
  }
</style>