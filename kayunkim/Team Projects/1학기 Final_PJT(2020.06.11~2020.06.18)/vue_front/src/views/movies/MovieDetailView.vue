<template>
  <div>
    <div class="movie-info-box">
      <div class="container py-4">
        <div class="movie-body">
          <div class="d-flex flex-column align-items-center flex-md-row">
            <img class="poster mb-4 mb-md-0" :src="movieData.poster_url" :alt="`${movieData.title} poster`">
            <div class="movie-info mx-5">
              <!-- <p>{{ movieData}}</p> -->
              <div class="mb-2">
                <h1 class="movie-title m-0">{{ movieData.title }}</h1>
                <p v-if="!notEnglish" class="h3 text-muted">{{ movieData.original_title }}</p>
              </div>
              <p>{{ genreInfo }} | {{ movieData.runtime }} minutes | {{ $moment(movieData.release_date).format('YYYY.MM.DD') }}</p>
              <h4>Overview</h4>
              <p>{{ movieData.overview }}</p>
              <h4>Rating</h4>
              <p>{{ movieData.rating }} / 10</p>

              <div class="d-flex flex-row justify-content-between">
                <p><i @click="likeMovie" class="fas fa-heart fa-lg mr-2" :class="{liked: likedMovie}"></i>{{ movieData.liked_users.length }} <span class="d-none d-md-inline">people like this movie</span></p>
                <div class="my-auto">
                  <!-- Button trigger modal -->
                  <button type="button" class="text-white btn trailerButton" data-toggle="modal" data-target="#movieTrailer">See Trailer</button>
                </div>
              </div>


              <!-- Modal -->
              <div class="modal fade" id="movieTrailer" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered modal-lg" role="document">
                  <div class="modal-content">
                    <div class="modal-body embed-responsive embed-responsive-16by9">
                      <iframe width="560" height="315" :src="movieData.trailer_url" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                    </div>
                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="credit-info container my-4">
      <div>
        <h4>Director</h4>
        <p>{{ movieData.director }}</p>
      </div>
      <div>
        <h4>Cast</h4>
        <p>{{ movieData.actors }}</p>
      </div>
      <div>
        <h4>Keywords</h4>
        <p>{{ movieData.keywords }}</p>
      </div>
     <hr>
    </div>
    
    <MovieReview />

  </div>
</template>

<script>
import { mapActions, mapState, mapGetters } from 'vuex'
import MovieReview from '../../components/MovieReview.vue'

export default {
  name: 'MovieDetailView',

  components: {
    MovieReview,
  },

  computed: {
    ...mapState(['movieData']),
    ...mapGetters(['genreInfo', 'notEnglish', 'likedMovie', 'isLoggedIn'])
  },

  methods: {
    ...mapActions(['fetchMovieData', 'likeMovie'])
  },

  created() {
    this.fetchMovieData(this.$route.params.movieId)
  },
}
</script>

<style scoped>
.movie-info-box {
  background-color: rgba(234, 234, 234, 1);
}

.poster {
  width: 250px;
}

.trailerButton {
  background-color: rgba(0, 178, 149, 1);
}

.liked {
  color: rgba(239, 111, 108, 1);
}

</style>