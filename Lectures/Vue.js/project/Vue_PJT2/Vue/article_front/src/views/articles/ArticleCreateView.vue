<template>
  <div> 
    <h1>커뮤니티</h1>
    <form class="container">
      <div class="form-group text-left">
        <label for="articleNewTitle">Title</label>
        <input v-model="articleInfo.title" type="text" class="form-control" id="articleNewTitle" aria-describedby="articleTitle">
        <small id="articleTitle" class="form-text text-muted">영화와 관련된 자유로운 의견을 남겨주세요</small>
        <br>
        <label for="articleNewContent">Content</label>
        <textarea v-model="articleInfo.content" type="text" class="form-control" id="articleNewContent"></textarea>
        <br>
        <button @click="createArticle" class="btn btn-primary">작성하기</button>
      </div>
    </form>
  </div>
</template>

<script>
const API_BASE_URL = 'http://localhost:8000'

export default {
    name: "ArticleCreateView",
    data () {
        return {
            articleInfo: {
                title: '',
                content: '',
            }
        }
    },
    methods: {
        createArticle() {
            const API_ARTICLE_CREATE_URL = API_BASE_URL+ '/articles/create/'
            const config = {
                headers: {
                    Authorization: `Token ${this.$cookies.get('auth-token')}`
                }
            }
            this.$axios.post(API_ARTICLE_CREATE_URL, this.articleInfo, config)
              .then(() => {
                  this.$router.push('/articles/create')
              })
              .catch(err => {
                  console.log(err)
              })
        }
    }
}
</script>

<style>

</style>