<template>
  <div>
    <div class="edit-header d-flex justify-content-center align-items-center">
      <h1 class="text-white">Edit Article</h1>
    </div>
    <div class="w-50 mx-auto container py-4">
      <form>
        <div class="form-group">
          <label for="title">Title</label>
          <input name="title" v-model="articleData.title" type="text" class="form-control" id="title">
        </div>
        <div class="form-group">
          <label for="content">Content</label>
          <textarea name="content" v-model="articleData.content" class="form-control" rows="10"></textarea>
        </div>
      </form>
      <button @click="updateArticle({'articleData': articleData, 'articleId': article.id})" class="submitButton btn text-white">Edit</button>    
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'ArticleUpdateView',

  data() {
    return {
      articleData: {},
    }
  },

  methods: {
    ...mapActions(['detailArticle','updateArticle'])
  },

  computed: {
    ...mapState(['article'])
  },
  
  created() {
    this.detailArticle(this.$route.params.articleId)
    this.articleData = {
      title: this.$store.state.article.title,
      content: this.$store.state.article.content
    }
  }
}
</script>

<style scoped>
  .edit-header {
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