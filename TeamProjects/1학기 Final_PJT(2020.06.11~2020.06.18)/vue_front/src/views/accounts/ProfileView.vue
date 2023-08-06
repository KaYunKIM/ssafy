<template>

  <div>
    <div class="greeting d-flex flex-row align-items-center">
      <div class="mx-3">
        <h1 class="mx-4 text-white">Welcome {{ userData.username }}!</h1>
        <p class="mx-4 my-0 text-muted">Member since {{ $moment(userData.date_joined).format('MMM YYYY') }}</p>
        <!-- <p class="mx-4 my-0 text-muted">followers: {}  |  following: {}</p> -->
      </div>
    </div>

    <div class="container my-4">
      <div>
        <h2 class="mx-3">Liked Movies</h2>
      </div>
      <div class="row">
        <div class="col-12 col-md-8">
          <hr>
          <ul v-if="userLikedList.length > 0" class="list-group list-group-flush">
            <router-link :to="`/movies/${movie.id}`" v-for="movie in userLikedList" :key="movie.id" class="list-group-item text-decoration-none text-dark">
              <div class="d-flex flex-row">
                <div class="d-flex flex-column justify-content-center">
                  <img :src="movie.poster_url" alt="movie poster" class="movie-poster">
                </div>
                <div class="mx-3 mt-1">
                  <h4>{{ movie.title }}</h4>
                  <p>{{ movie.genre }} | {{ movie.release_date }}</p>
                </div>
              </div>
            </router-link>
          </ul>
          <div v-else>
            <h5 class="text-muted">Seems like you have no liked movies yet!</h5>
          </div>
        </div>

        <div class="border-left col-12 col-md-4">
          <h4 class="text-center my-3">Movies released on your birthday</h4>
          <div class="row">
            <router-link :to="`/movies/${movie.id}`"  v-for="movie in birthdayList" :key="movie.id" class="text-decoration-none text-dark col-6">
              <div class="card h-100 border-0">
                <img :src="movie.poster_url" class="card-img-top birthday-poster" alt="movie poster">
                <div class="card-body px-2 pt-2">
                  <h6 class="card-title mb-1">{{ movie.title }}</h6>
                  <p class="card-text small">{{ movie.release_date }}</p>
                </div>
              </div>
            </router-link>
          </div>

        </div>

      </div>
    </div>
    <!-- <button@click="follow(username)">follow</button> -->

  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'ProfileView',
  
  computed: {
    ...mapState(['userData', 'userLikedList', 'birthdayList']),
  },
  
  methods: {
    ...mapActions(['fetchUserData', 'fetchLikeList', 'fetchBirthdayList'])
    // ...mapActions(['follow']),
  }, 
  
  created() {
    this.fetchUserData()
      .then(() => {
        this.fetchLikeList()
        this.fetchBirthdayList()
      })
  },
}
</script>

<style scoped>
  .greeting {
    height: 200px;
    background-color: rgba(234, 234, 234, 1);
    background-image: url('../../assets/profile.jpg');
    background-position: center center;
    background-size: cover;
  }

  .movie-poster {
    width: 150px;
  }

</style>