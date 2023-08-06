<template>
  <div class="row my-5">
    <div v-for="movie in movies" :key="movie.id" class="col-6 col-md-3 my-2">
      <MovieListItem :movie="movie" />
    </div>
  </div>
</template>

<script>
import MovieListItem from '../components/MovieListItem.vue'

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  props: {
    movies: {
      type: Array,
    },
  },
}
</script>

<style>

</style>