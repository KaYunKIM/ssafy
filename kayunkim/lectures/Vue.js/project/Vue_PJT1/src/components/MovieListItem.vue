<template>
  <div class="card h-100">
    <img :src="movie.poster_url" class="card-img-top" alt="movie poster">
    <div class="card-body">
      <h5 class="card-title">{{ movie.title }}</h5>
      <button class="btn btn-warning" type="button" data-toggle="modal" :data-target="`#movie${movie.id}`">영화 정보 상세보기</button>
    </div>
    <MovieListItemModal :movie="movie" />
  </div>
</template>

<script>
import MovieListItemModal from '../components/MovieListItemModal.vue'

export default {
  name: 'MovieListItem',
  components: {
    MovieListItemModal,
  },
  props: {
    movie: {
      type: Object,
    },
  },
  methods: {
    showInfo() {
      console.log('info!')
    },
  },
}
</script>

<style>

</style>