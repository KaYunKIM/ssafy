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

              <v-card-text class="text-center pt-0 px-0">
                <v-card-title class="pa-0">
                  <v-btn @click="onMypage(selectedPost.uid)" class="ma-0 pa-0" text style="color: #D9A9A9"><h2 style="color: #1A1F73">{{ selectedPost.uid.split('@')[0] }}</h2></v-btn>
                  <v-spacer></v-spacer>
                  <v-btn @click="onCafeDetail(selectedPost.cafeno)" class="ma-0 pa-0" text small>{{ selectedPost.cafename }}</v-btn>
                </v-card-title>
                
                <v-divider class="my-2"></v-divider>

                <v-row class="d-flex align-center justify-center mt-5 pt-2">
                  <span style="color: #49538C">맛</span>
                  <v-rating
                    v-model="selectedPost.taste"
                    color="#8C4F5A"
                    background-color="grey darken-1"
                    empty-icon="$ratingFull"
                    readonly
                  ></v-rating>
                  <span style="color: #49538C">({{ selectedPost.taste }})</span>
                </v-row>

                <v-row class="d-flex align-center justify-center">
                  <span style="color: #49538C">분위기</span>
                  <v-rating
                    v-model="selectedPost.mood"
                    color="#8C4F5A"
                    background-color="grey darken-1"
                    empty-icon="$ratingFull"
                    readonly
                  ></v-rating>
                  <span style="color: #49538C">({{ selectedPost.mood }})</span>
                </v-row>

                <v-row class="d-flex align-center justify-center">
                  <span style="color: #49538C">위생</span>
                  <v-rating
                    v-model="selectedPost.clean"
                    color="#8C4F5A"
                    background-color="grey darken-1"
                    empty-icon="$ratingFull"
                    readonly
                  ></v-rating>
                  <span style="color: #49538C">({{ selectedPost.clean }})</span>
                </v-row>
              

              <p class="my-5 py-4 text-center" style="color: #49538C">{{ selectedPost.contents }}</p>
              </v-card-text>

              <CommentCreate/>
              <CommentList/>

            </v-col>
          </v-row>


          <v-card-actions>
            <v-bottom-navigation
              v-if="selectedPost.uid === currentUser"
              style="background:transparent; box-shadow:none !important;"
              class="d-flex justify-end"
            >
              <v-btn
                color="deep-purple lighten-2"
                text
                @click="onUpdatePost(selectedPost.pno)"
              >
              <span style="color: #49538C">Edit</span>
              <span class="material-icons mx-3" style="color: #1A1F73">edit</span>
              </v-btn>

              <v-dialog v-model="dialog" persistent max-width="320">
                <template v-slot:activator="{ on }">
                  <v-btn
                    v-on="on"
                    color="deep-purple lighten-2"
                    text
                    @click="dialog = true"
                  >
                  <span style="color: #49538C">Delete</span>
                  <span class="material-icons mx-3" style="color: #D9A9A9">delete</span>
                  </v-btn>
                </template>
                  <v-card>
                    <v-card-title>
                      포스트를 삭제하시겠습니까?
                    </v-card-title>
                    <v-card-actions>
                      <v-btn color="green darken-1" text @click="deletePost(selectedPost.pno), dialog = false">삭제</v-btn>
                      <v-spacer></v-spacer>
                      <v-btn color="grey darken-1" text @click="dialog = false">취소</v-btn>
                    </v-card-actions>
                  </v-card>
              </v-dialog>
            </v-bottom-navigation>
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
      dialog: false,
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
  },
  mounted() {
    this.postDetail(this.postId)
  }
}
</script>

<style scoped>
.disabled-button {
  pointer-events: none;
}

</style>