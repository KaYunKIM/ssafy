<template>
  <div>
      <h1>Article List</h1>
      <p v-for="article in article_list" :key="article.id">
          {{ article.title }}: {{ article.content }}
      </p>
      <hr>
  </div>
</template>

<script>
const API_BASE_URL = 'http://localhost:8000'

export default {
    name: 'ArticleListView',
    data() {
        return {
            article_list: [],
        }
    },
    methods: {
        fetchArticleList() {
          const API_ARTICLE_LIST_URL = API_BASE_URL + '/articles/'
          const config = {
            headers: {
                Authorization:  `Token ${this.$cookies.get('auth-token')}`
            }
          }
          this.$axios.get(API_ARTICLE_LIST_URL, config)  //axios.get(URL, config)
            .then(res => {
              this.article_list = res.data
            })
            .catch(err => {
              console.error(err)
            })

          },
    },
    created() {
       this.fetchArticleList()
    },
}
</script>

<style>

</style>