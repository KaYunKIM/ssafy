<template>
  <div>
    <v-row justify="center">
      <v-col
        cols="12"
      >
        <v-card ref="form" class="px-3">
          
          <v-row>
            <v-col
              cols="12"
              sm="6"
            >
              <v-img :src="postImage" style="background:#f7f7f7" contain height="100%" width="100%"></v-img>
            </v-col>
            <v-col
              cols="12"
              sm="6"
            >

              <v-card-text class="text-center">
                <v-card-title>
                  <v-btn @click="onCafeDetail(selectedPost.cafeno)" class="ma-0 pa-0" text><h2>{{ selectedPost.cafename }}</h2></v-btn>
                  <v-spacer></v-spacer>
                  <v-btn @click="onMypage(selectedPost.uid)" class="ma-0 pa-0" text small>{{ selectedPost.uid }}</v-btn>
                </v-card-title>
                
                <v-divider class="mb-3"></v-divider>

                <p class="my-3 text-start">{{ selectedPost.contents }}</p>
                <v-row class="d-flex align-center justify-center">
                  <span>맛</span>
                  <v-rating
                    v-model="selectedPost.taste"
                    color="yellow darken-3"
                    background-color="grey darken-1"
                    empty-icon="$ratingFull"
                    readonly
                  ></v-rating>
                  <span>({{ selectedPost.taste }})</span>
                </v-row>

                <v-row class="d-flex align-center justify-center">
                  <span>분위기</span>
                  <v-rating
                    v-model="selectedPost.mood"
                    color="yellow darken-3"
                    background-color="grey darken-1"
                    empty-icon="$ratingFull"
                    readonly
                  ></v-rating>
                  <span>({{ selectedPost.mood }})</span>
                </v-row>

                <v-row class="d-flex align-center justify-center">
                  <span>위생</span>
                  <v-rating
                    v-model="selectedPost.clean"
                    color="yellow darken-3"
                    background-color="grey darken-1"
                    empty-icon="$ratingFull"
                    readonly
                  ></v-rating>
                  <span>({{ selectedPost.clean }})</span>
                </v-row>

              </v-card-text>

              <CommentCreate/>
              <CommentList/>

            </v-col>
          </v-row>


          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn v-if="selectedPost.uid === currentUser" @click="onUpdatePost(selectedPost.pno)" text color="primary">수정</v-btn>
            <v-btn v-if="selectedPost.uid === currentUser" @click="deletePost(selectedPost.pno)" text color="secondary">삭제</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'

import CommentCreate from '@/components/comment/CommentCreate.vue'
import CommentList from '@/components/comment/CommentList.vue'

export default {
  name: 'PostDetailView',
  components: {
    CommentCreate,
    CommentList,
  },
  data() {
    return {
      postId: this.$route.params.post_id,
      postImage: null,
    }
  },
  computed: {
    ...mapState([
      'selectedPost',
      'currentUser',
    ]),
    ...mapGetters([
      'isLoggedIn'
    ]),
  },
  methods: {
    ...mapActions([
      'postDetail',
      'deletePost',
    ]),
    onMypage(userid) {
      this.$router.push(`/accounts/${userid}`)
    },
    onUpdatePost(postid) {
      if (!this.isLoggedIn) {
        this.$router.push({ name: 'Login'})
      } else {
        this.$router.push(`/post/update/${postid}`)
      }
    },
    onCafeDetail(cafeid) {
      this.$router.push(`/cafe/detail/${cafeid}`)
    },
  },
  created() {
    this.postDetail(this.postId)
    this.postImage = "https://i3a203.p.ssafy.io:5000/api/post/get/image/"+this.postId+'/'+ new Date()
  }
}
</script>

<style scoped>
.disabled-button {
  pointer-events: none;
}

</style>