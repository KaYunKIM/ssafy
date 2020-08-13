<template>
  <div>
    <div class="create-header d-flex justify-content-center align-items-center">
      <h1 class="text-white">New Article</h1>
    </div>
    <div class="w-50 mx-auto container py-4">
      <form>
        <div class="form-group">
          <label for="title">Title</label>
          <input v-model="articleData.title" type="text" class="form-control" id="title">
        </div>
        <div class="form-group">
          <label for="content">Content</label>
          <textarea  v-model="articleData.content" class="form-control" rows="10"></textarea>
        </div>
      </form>
      <button @click="createArticle(articleData)" class="submitButton btn text-white">Create</button>    
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'ArticleCreateView',
  data() {
    return {
      articleData: {}
    }
  },

  beforeCreate () {
    this._routeRoot = null
  },

  computed: {
    ...mapState(['article']),
  },

  methods: {
    ...mapActions(['detailArticle','createArticle', 'updateArticle'])
  },

  created() {
    if (this.$route.params.articleId) {
      this.detailArticle(this.$route.params.articleId)
      this.articleData = {
        title: this.article.title,
        content: this.article.content
      } 
    } else {
      this.articleData = {}
    }
  }
}
</script>

<style scoped>
  .create-header {
    height: 150px;
    background-image: url('../../assets/community2.jpg');
    background-position: center center;
    background-size: cover;
    background-color: rgba(234, 234, 234, 1);
  }

  .submitButton {
    background-color: rgba(0, 178, 149, 1);
  }
</style>