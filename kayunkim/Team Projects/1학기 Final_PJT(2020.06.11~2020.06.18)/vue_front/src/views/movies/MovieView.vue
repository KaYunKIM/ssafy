<template>
  <div>
    <div class="search d-flex justify-content-center align-items-center">
        <input v-model="searchKeyword" @keypress.enter="getSearchResult(searchKeyword)" class="searchInput mx-2 form-control d-inline-block" :class="windowWidth > 720 ? 'w-50': 'w-100'" type="text" placeholder="Search for a movie title"> 
        <button class="mx-2 searchButton btn text-white" @click="getSearchResult(searchKeyword)"><i class="fas fa-search fa-lg"></i></button>
    </div>
    
    <div v-if="searchResult.length > 0" class="container my-4">
      <h6 class="mx-3">{{ searchResult.length }} results</h6>
      <ul class="list-group list-group-flush">
        <router-link :to="`/movies/${result.id}`" v-for="result in searchResult" :key="result.id" class="list-group-item text-decoration-none text-dark">
          <div class="d-flex flex-column flex-md-row">
            <div class="d-flex flex-md-column justify-content-center">
              <img :src="result.poster_url" alt="movie poster" class="result-poster">
            </div>
            <div class="mx-5 py-3 text-center text-md-left">
              <h3>{{ result.title }}</h3>
              <p>{{ result.genre }} | {{ result.release_date }}</p>
              <p class="d-none d-md-block">{{ result.overview }}</p>
            </div>
          </div>
        </router-link>
      </ul>
      <hr>
    </div>

    <PopularList />
  </div>
</template>

<script>
import { mapActions, mapState, mapGetters } from 'vuex'
import PopularList from '../../components/PopularList.vue'

export default {
  name: 'MovieView',

  components: {
    PopularList,
  },

  data() {
    return {
      searchKeyword: null,
      windowWidth: window.innerWidth,
    }
  },

  computed: {
    ...mapState(['searchResult']),
    ...mapGetters(['genreInfo'])
  },

  methods: {
    ...mapActions(['getSearchResult', 'clearSearchResult'])
  },

  created() {
    this.clearSearchResult()
  }
}
</script>

<style scoped>
  .search {
    height: 300px;
    background-image: url('../../assets/search_banner.jpg');
    background-position: center center;
    background-size: cover;
    background-color: rgba(234, 234, 234, 1);
  }

  .searchInput {
    height: 50px;
  }

  .searchButton {
    height: 52px;
    width: 70px;
    background-color: rgba(0, 178, 149, 1);
    border-radius: .7rem;
  }

  .result-poster {
    width: 200px;
  }
</style>