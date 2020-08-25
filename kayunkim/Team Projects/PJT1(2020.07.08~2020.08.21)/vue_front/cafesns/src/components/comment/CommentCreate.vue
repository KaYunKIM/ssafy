<template>
  <v-layout>
    <v-text-field
      v-if="isLoggedIn"
      label="Content" 
      v-model="commentData.contents"
      id="content"
      clearable
      @keypress.enter="checkBeforeCreateComment(commentData)"
    >
    <template v-slot:append-outer>
      <v-btn
        small
        dark
        color="#D9A9A9"
        @click="checkBeforeCreateComment(commentData)"
      >등록</v-btn>
    </template>
    </v-text-field>
    <v-text-field v-else label="Content" @click="toLoginPage()"></v-text-field>
  </v-layout>
</template>



<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentCreate',
  data() {
    return {
      commentData: {
        pno: this.$route.params.post_id,
        contents: null,
        uid: null,
      }
    }
  },

  computed: {
    ...mapGetters(['isLoggedIn']),
  },

  methods: {
    ...mapActions(['createComment']),
    checkBeforeCreateComment(commentData) {
      if (!this.isLoggedIn) {
        this.$router.replace({ name: 'Login'})
      } else if (!this.commentData.contents) {
        alert('내용을 입력해주세요.')
      } else {
        this.createComment(commentData)
          .then(res => this.commentData.contents = res)
      }
    },
    toLoginPage() {
      this.$router.replace({ name: 'Login'})
    },
  },
}
</script>

<style>

</style>