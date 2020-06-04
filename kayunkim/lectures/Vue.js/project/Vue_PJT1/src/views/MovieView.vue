<template>
  <div class="container text-center my-4">
    <h1>나만의 무비 컬렉션</h1>
    <button v-if="!buttonClicked" @click="getMovies" class="btn btn-primary my-3" ref="getMoviesButton">영화 가져오기</button>
    <MovieList v-if="movies" :movies="movies" />
  </div>
</template>

<script>
import axios from 'axios'

import MovieList from '../components/MovieList.vue'

export default {
  name: 'MovieView',
  components: {
    MovieList,
  },
  data() {
    return {
      movies: null,
      buttonClicked: false,
    }
  },
  methods: {
    getMovies() {
      this.buttonClicked = !this.buttonClicked
      axios.get('https://www.json-generator.com/api/json/get/ceNyuXZmwi?indent=2')
        .then(res => {
          this.movies = res.data
          console.log(res.data)
          })
        .catch(err => console.log(err))
    },
  },
}
</script>

<style>
  .visible {
    display: block;
  }
</style>