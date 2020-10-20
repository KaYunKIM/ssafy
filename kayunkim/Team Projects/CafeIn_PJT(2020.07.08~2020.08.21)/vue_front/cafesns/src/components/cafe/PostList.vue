<template>
  <div>
    <h3 style="color: #1A1F73">Posts</h3>
    <v-list flat>
      <v-list-item-group>
        <v-list-item
          v-for="post in cafePostList"
          :key="post.pno"
          @click="onSelectPost(post.pno)"
        >
          <v-list-item-avatar>
            <!-- <v-icon class="grey lighten-1 white--text" v-text="folder"></v-icon> -->
            <v-img
              :src="'https://i3a203.p.ssafy.io:5000/api/post/get/image/'+post.pno+'/'+new Date()"
              @click="onSelectPost(post.pno)"
            >
            </v-img>
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title style="color: #49538C">{{ post.contents }}</v-list-item-title>
            <v-list-item-subtitle style="color: #D9A9A9">{{ post.uid }}</v-list-item-subtitle>
          </v-list-item-content>
          <v-list-item-action style="color: #1A1F73">{{ post.date }}</v-list-item-action>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'PostList',
  computed: {
    ...mapState(['cafePostList'])
  },
  methods: {
    ...mapActions(['fetchCafePostList']),
    onSelectPost(postno) {
      this.$router.push(`/post/detail/${postno}`)
    }
  },
  created() {
    this.fetchCafePostList(this.$route.params.cafe_id)
  },

}
</script>

<style>

</style>