<template>
  <div>
    <h4 v-if="!commentList.length" class="text-center">등록된 댓글이 없습니다.</h4>
    <v-dialog v-model="dialog" persistent max-width="290">
      <template v-slot:activator="{ on }">
        <div
          v-for="comment in commentList"
          :key="comment.key"
          class="px-2"
        >
          <div class="d-flex justify-space-between px-2">
            <div>
              <span class="userPage pl-1" style="font-size:small" @click="onUserPage(comment.uid)">{{ comment.uid }}</span>
              <h3>{{ comment.contents }}</h3>
            </div>
            <div class="d-flex align-center">
              <v-btn
                v-if="comment.uid === currentUser"
                color="error"
                dark
                v-on="on"
                text
                small
                @click="selectComment = comment.cno"
              >
                삭제
              </v-btn>
              <span style="color:grey">{{ comment.date }}</span>
            </div>
          </div>
        </div>
      </template>
      <v-card>
        <v-card-title>
          댓글을 삭제하시겠습니까?
        </v-card-title>
        <v-card-actions>
          <v-btn color="green darken-1" text @click="deleteComment(selectComment), dialog = false">삭제</v-btn>
          <v-spacer></v-spacer>
          <v-btn color="grey darken-1" text @click="dialog = false">취소</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'ReviewList',
  data() {
    return {
      postId: this.$route.params.post_id,
      dialog: false,
      selectComment: null,
    }
  },
  computed: {
    ...mapState([
      'commentList',
      'currentUser'
    ])
  },
  methods: {
    ...mapActions([
      'fetchCommentList',
      'deleteComment',
    ]),
    onUserPage(userid) {
      this.$router.push(`/accounts/${userid}`)
    }
  },
  created() {
    this.fetchCommentList(this.postId)
  },
}
</script>

<style scoped>
.userPage {
  cursor: pointer;
}

</style>