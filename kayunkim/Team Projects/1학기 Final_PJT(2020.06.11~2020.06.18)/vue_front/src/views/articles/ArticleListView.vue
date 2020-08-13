<template>
  <div>
    <div class="community-header"> </div>

    <div class="container py-4">
      <table class="table">
        <thead class="tableHeader">
          <tr>
            <td scope="col">No.</td>
            <td scope="col">Username</td>
            <td scope="col">Title</td>
            <td scope="col">Created</td>
          </tr>
        </thead>
        <tbody>          
          <tr v-for="article in articleList" :key="`article_${article.id}`">
            <th scope="row">{{ `${article.id}` }}</th>
            <td>{{ article.user.username }}</td>
            <td><router-link :to="{ name: 'ArticleDetail', params: { articleId: `${article.id}`}}">{{ article.title }}</router-link></td>
            <td>{{ $moment(article.created_at).format('YYYY-MM-DD') }}</td>
          </tr>
        </tbody>
      </table>
      <div v-if="isLoggedIn" class="d-flex flex-row-reverse">
        <router-link to="/new_article" class="submitButton btn text-white">New</router-link>
      </div>  
    </div>
  </div>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'

export default {
  name: 'ArticleListView',
  computed: {
    ...mapState(['articleList']),
    ...mapGetters(['isLoggedIn'])
  },
  methods: {
    ...mapActions([
      'fetchArticles',
      'articleCreate',])
  },
  created() {
    this.fetchArticles()
  }
}
</script>

<style scoped>
  .community-header {
    height: 250px;
    background-image: url('../../assets/community.jpg');
    background-position: center center;
    background-size: cover;
    background-color: rgba(234, 234, 234, 1);
  }

  .submitButton {
    background-color: rgba(0, 178, 149, 1);
  }
  .tableHeader {
    background-color: rgba(234, 234, 234, 1);
  }
  .textColor {
    color: rgba(51, 101, 138, 1);
  }
</style>