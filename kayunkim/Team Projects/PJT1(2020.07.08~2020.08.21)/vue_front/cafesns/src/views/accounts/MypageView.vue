<template>
    <div>
        <v-row>
          <div class="d-flex justify-end align-center mx-2">
            <h1 class="px-3" style="color: #1A1F73">{{ userData.id.split('@')[0] }}</h1>
            <v-btn v-if="profileUserId !== currentUser" color="#D9A9A9" @click="followUser(profileUserId)" small>
              <span v-if="!followState" style="color: white">Follow</span>
              <span v-else style="color: white">Following</span>
            </v-btn>
          </div>
          <v-row align="center" justify="end" class="mr-1">
            <FollowingList/>
            <FollowerList/>
            <UserPostList/>
          </v-row>
        </v-row>
      <v-divider class="my-2"></v-divider>
      <div>
        <i class="fas fa-heart fa-3x ma-3" style="color: #8C4F5A"></i>
        <div class="home text-center">
          <LikeList/>
        </div>
      </div>
      <div class="mt-4">
        <i class="fas fa-shoe-prints fa-rotate-270 fa-3x ma-3" style="color: #49538C"></i>
          <div class="home text-center">
            <StampList/>
          </div>
      </div>
  </div>
</template>

<script>
import LikeList from '@/components/user_profile/LikeList.vue'
import StampList from '@/components/user_profile/StampList.vue'
import FollowingList from '@/components/user_profile/FollowingList.vue'
import FollowerList from '@/components/user_profile/FollowerList.vue'
import UserPostList from '@/components/user_profile/UserPostList.vue'

import { mapState, mapActions } from 'vuex'

export default {
  name: "MyPageView",
  data() {
    return {
      profileUserId : null,
      check: 1,
    }
  },

  components: {
    LikeList,
    StampList,
    FollowingList,
    FollowerList,
    UserPostList,
  },
  
  computed: {
    ...mapState([
      'userData',
      'currentUser',
      'likeList',
      'stampList', 
      'followState',
      'followingList', 
      'followerList',
      'postList',
    ])
  },
  
  methods: {
    ...mapActions([
      'fetchUserData', 
      'fetchLikeList', 
      'fetchStampList', 
      'aboutFollow',
      'fetchFollowingList',
      'fetchFollowerList',
      'followUser',
    ]),
    showUserProfile() {
      this.profileUserId = this.$route.params.user_id
      this.fetchUserData(this.profileUserId)
        .then(() => {
          this.fetchLikeList()
          this.fetchStampList()
          this.fetchFollowingList()
          this.fetchFollowerList()
        })
    },
    
  },

  created() {
    this.showUserProfile()
    this.aboutFollow(this.$route.params.user_id)
  },
  mounted() {
    this.showUserProfile()
    this.aboutFollow(this.$route.params.user_id)
  },

  watch: {
    '$route' (to, from) {
      if (to !== from ) {
        this.showUserProfile()
      }
    }
  },
}
</script>

<style>

</style>