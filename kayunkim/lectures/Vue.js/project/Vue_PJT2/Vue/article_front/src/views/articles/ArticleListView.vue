<template>
  <div class="container">
      <!-- <button class="btn btn-warning" @click="$router.push('/articles/create')">글쓰기</button> -->
      <h1>게시판</h1>
      <table class="table">
        <thead>
            <tr>
            <th scope="col">#</th>
            <th scope="col">제목</th>
            <th scope="col">작성자</th>
            </tr>
        </thead>
        <tbody v-for="article in article_list" :key="article.id">
            <tr>
            <th scope="row">{{ article.id }}</th>
            <td>{{ article.title }}</td>
            <td>{{ article.user.username }}</td>
            </tr>
        </tbody>
        </table>
  </div>
</template>

<script>

const API_BASE_URL = 'http://localhost:8000'

export default {
    name: 'ArticleListView',
    data () {
        return {
            article_list: [],
        }
    },
    methods: {
        getArticleList() {
          const API_ARTICLE_LIST_URL = API_BASE_URL+'/articles/'
          
          this.$axios.get(API_ARTICLE_LIST_URL)
            .then(res => {
              this.article_list = res.data
            })
            .catch(err => {
              console.log(err)
            })
           
        }
    },
    created() {
        this.getArticleList()
    },
}
</script>

<style>

</style>