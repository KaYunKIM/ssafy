<template>
  <div class="new-releases container my-2">
    <h1 class="pb-2">What's New</h1>
    <div class="d-flex flex-row new-releases-list">
      <router-link :to="`/movies/${movie.id}`" v-for="movie in newReleasesList" :key="movie.id" class="card col-4 col-md-2 text-decoration-none text-dark px-0 border-0">
        <img :src="movie.poster_url" class="card-img-top" alt="movie poster">
        <div class="card-body">
          <p class="card-title">{{ movie.title }}</p>
          <small class="text-muted">{{ movie.release_date }}</small>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'NewReleasesList',

  computed: {
    ...mapState(['newReleasesList']),
  },

  methods: {
    ...mapActions(['fetchNewReleases'])
  },

  created() {
    this.fetchNewReleases()
  },

}
</script>

<style scoped>
  .new-releases-list {
    overflow-x: scroll;
    overflow-y: hidden;
    white-space: nowrap;
  }
  .card {
    white-space: normal;
  }
</style>