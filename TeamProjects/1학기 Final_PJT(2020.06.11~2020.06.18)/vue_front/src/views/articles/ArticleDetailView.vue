<template>
  <div class="container py-4">

    <div v-if="isLoggedIn">
      <!-- article -->
      <div class="card">
        <div class="card-body">

          <h2 class="card-title m-0">{{ article.title }}</h2>
          <small class="text-muted">Written by <span class="font-weight-bolder">{{ article.user.username }}</span></small>
          <hr>

          <p class="card-text">{{ article.content }}</p>

          
          <div class="d-flex justify-content-between">
            <div>
              <small class="text-muted">Created : {{ $moment(article.created_at).format('YYYY-MM-DD HH:MM:SS') }}</small><br>
              <small class="text-muted">Updated : {{ $moment(article.updated_at).format('YYYY-MM-DD HH:MM:SS') }}</small>
            </div>
            <div class="my-auto">
              <router-link v-if="userData.username===article.user.username" :to="{ name: 'ArticleUpdate', params: { articleId: `${article.id}`}}" class="editButton btn text-white mr-1 articleButtons">Edit</router-link>
              <button v-if="userData.username===article.user.username" @click="deleteArticle(article.id)" class="deleteButton btn text-white articleButtons">Delete</button>
            </div>
          </div>

        </div>
      </div>

      <!-- comment -->
      <div class="my-3">
        <div class="row mx-0">
          <input v-model="commentData.content" type="text" class="form-control col-12 col-md-10" id="comment" placeholder="Write a comment">
          <button @click="multiple" class="submitButton btn text-white my-2 my-md-0 mx-md-2">Comment</button>  
        </div>
      </div>

      
      <hr>
      <table class="table">
        <thead class="commentHeader text-white">
          <tr class="row mx-0">
            <td scope="col" class="col-1">Comments</td>
            <td scope="col" class="col-8"></td>
            <td scope="col" class="col-2"></td>
            <td scope="col" class="col-1"></td>
          </tr>
        </thead>
        <tbody>
          <tr v-for="comment in commentList" :key="`comment_${comment.id}`" class="row mx-auto">
            <th scope="row" class="col-2 col-md-2">{{ comment.user.username }}</th>
            <td class="col-7 offset-1 offset-md-0 col-md-7">{{ comment.content }}</td>
            <td class="d-none d-md-block col-md-2">{{ $moment(comment.created_at).format('YYYY-MM-DD HH:MM:SS') }}</td>
            <td class="col-2 col-md-1"><button v-if="userData.username===comment.user.username" @click="deleteComment({ 'articleId': article.id, 'commentId': comment.id })" class="btn btn-secondary">Delete</button></td>
          </tr>
        </tbody>
      </table>  
    </div>

    <div v-else>
      <h3 class="text-muted text-center">To participate in the community, please login :)</h3>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'

export default {
  name: 'ArticleDetailView',

  data() {
    return {
      commentData : {
        article: null,
        content: null,
      },
    }
  },

  computed: {
    ...mapState(['userData', 'article', 'commentList', 'comment']),
    ...mapGetters(['isLoggedIn'])
  },

  methods: {
    ...mapActions([
      'fetchUserData',
      'detailArticle',
      'updateArticle', 
      'deleteArticle',
      'fetchComment',
      'createComment',
      'deleteComment']),

    multiple: function () {
      this.createComment({ 'commentData': this.commentData, 'articleId': this.article.id })
      this.commentData = {}
    },
  },

  created() {
    if (this.isLoggedIn) {
      this.fetchUserData()
        .then(() => {
          this.detailArticle(this.$route.params.articleId)
          this.commentData.article = this.$route.params.articleId
          this.fetchComment(this.$route.params.articleId)
        })
    }
  },
}
</script>

<style scoped>
  .submitButton {
    background-color: rgba(0, 178, 149, 1);
  }

  .deleteButton {
    background-color: rgba(239, 111, 108, 1);
  }

  .editButton {
    background-color: rgba(0, 178, 149, 1);
  }

  .commentHeader {
    background-color: rgb(65, 118, 158);
  }
</style>