<template>
  <div class="popular container my-4">
    <h1 class="pb-3">What's Popular</h1>
    <div class="row popular-list px-3">
      <router-link :to="`/movies/${movie.id}`" v-for="movie in popularList" :key="movie.id" class="card col-4 col-md-2 text-decoration-none text-dark px-0 border-0">
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
import { mapState, mapActions } from 'vuex'

export default {
  name: 'PopularList',

  computed: {
    ...mapState(['popularList']),
  },

  methods: {
    ...mapActions(['fetchPopular'])
  },

  created() {
    this.fetchPopular()
  },
}
</script>

<style>

</style>