<template>
  <div>
    <v-dialog v-model="dialog" scrollable max-width="300px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="#BCAAA4"
          v-bind="attrs"
          v-on="on"
          text
        >
          POSTS {{ userPostList.length }}
        </v-btn>
      </template>
      <v-card class="d-inline-block">
        <v-row class="d-inline-block px-2">
          <v-card-title>Posts</v-card-title>
        </v-row>
        <v-divider></v-divider>
        <v-card-text style="height: 300px;">
          <div v-if="!userPostList.length" class="text-center">
            <span>아직 등록된 글이 없습니다.</span>
          </div>
          <v-radio-group v-model="dialogm1" column>
            <v-row v-for="post in userPostList" :key="post.pno">
              <v-list rounded>
                <v-list-item-group color="primary">
                  <v-list-item
                    @click="onSelectPost(post.pno)"
                  >
                    <v-list-item-avatar>
                      <v-img
                        :src="'https://i3a203.p.ssafy.io:5000/api/post/get/image/'+post.pno+'/'+new Date()"
                        @click="onSelectPost(post.pno)"
                      >
                      </v-img>
                    </v-list-item-avatar>
                  <v-list-item-content>
                    <v-list-item-title v-if="post.cafename.length<10">{{ post.cafename }}</v-list-item-title>
                    <v-list-item-title v-else>{{ post.cafename.substring(0, 10) + "..." }}</v-list-item-title>
                  </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-row>
          </v-radio-group>
        </v-card-text>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: "UserPostList",
  data () {
    return {
      dialogm1: '',
      dialog: false,
      currentUserId : null,
    }
  },

  computed: {
    ...mapState([ 
      'userPostList', 
    ])
  },
  
  methods: {
    ...mapActions([
      'fetchUserPostList',
    ]),
    onSelectPost(postno) {
      this.dialog = false  
      this.$router.push(`/post/detail/${postno}`)
    },
  },
  
  created() {
    this.currentUserId = this.$route.params.user_id,
    this.fetchUserPostList(this.currentUserId)
  },
}
</script>