<template>
  <div class="container my-4">
    <div v-if="isLoggedIn">
      <!-- review form -->
      <div v-if="isLoggedIn">
        <div class="form-row mx-0">
          <input v-model="reviewData.content" type="text" class="form-control col-12 col-md-8" id="review" placeholder="Write a review">
          <select v-model="reviewData.score" class="form-control col-2 col-md-1 my-2 my-md-0 mr-3 mx-md-3" id="scoreSelect">
            <option selected>0</option>
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            <option>5</option>
            <option>6</option>
            <option>7</option>
            <option>8</option>
            <option>9</option>
            <option>10</option>
          </select>
          <button type="submit" class="btn text-white reviewButton my-2 my-md-0" @click="createReview({'reviewData': reviewData, 'movieId': $route.params.movieId})">Submit</button>
        </div>
        <small id="ratingHelp" class="form-text text-muted">Write a review and give a score from 0 to 10.</small>
      </div>

      <!-- review list -->
      <div class="my-4">
        <div v-for="review in reviewList" :key="review.id" class="card my-1">
          <div class="card-body mx-0 row">
            <div class="col-3 col-md-1 px-0">
              <h2 class="mx-auto">{{ review.score }} <i class="far fa-sm" :class="{ 'fa-laugh-beam' : review.score >= 7, 'fa-meh': review.score >= 3 && review.score < 7, 'fa-frown': review.score < 3}"></i></h2>
            </div>
            <div class="col-6 col-md-10 px-0">
              <p class="m-0">{{ review.content }}</p>
              <small class="text-muted">{{ review.user.username }}</small>
            </div>
            <div class="col-3 col-md-1">
              <button v-if="userData.username===review.user.username" @click="deleteReview({ 'reviewId': review.id, 'movieId': $route.params.movieId })" class="deleteButton btn btn-secondary my-auto">Delete</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-if="!isLoggedIn" class="text-center text-muted">
      <h5>To read and write reviews, please login :)</h5>
    </div>

  </div>
</template>

<script>
import { mapActions, mapState, mapGetters } from 'vuex'

export default {
  name: 'MovieReview',

  data() {
    return {
      reviewData: {
        content: null,
        score: null,
      },
    }
  },

  computed: {
    ...mapState(['reviewList', 'userData']),
    ...mapGetters(['isLoggedIn'])
  },

  methods: {
    ...mapActions(['createReview', 'fetchReview', 'fetchUserData', 'deleteReview'])
  },

  created() {
    this.fetchReview(this.$route.params.movieId)
    this.fetchUserData()
  },
}
</script>

<style scoped>
  .reviewButton {
    background-color: rgba(0, 178, 149, 1);
  }

  .fa-frown {
    color: rgba(239, 111, 108, 1);
  }

  .fa-laugh-beam {
    color: rgba(0, 178, 149, 1);
  }
</style>