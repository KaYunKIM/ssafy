<template>
  <v-slide-group
    show-arrows-on-hover
  >
    <v-slide-item
      v-for="post in postList"
      :key="post.pno"
      v-slot:default="{ toggle }"
      class="current-image"
    >
        <v-card
          class="ma-1"
          @click="toggle"
        >
          <v-img
            class="grey lighten-2"
            height="200"
            width="200"
            :src="'https://i3a203.p.ssafy.io:5000/api/post/get/image/'+ post.pno + '/' + new Date()"
            @click="onSelectPost(post.pno)"
          >
            <v-row align="end" class="lightbox white--text fill-height">
              <v-col style="background:#00000080">
                <div v-if="post.contents.length<10" class="subheading text-center">{{ post.contents }}</div>
                <div v-else class="subheading text-center">{{ post.contents.substring(0, 10) + "..." }}</div>
              </v-col>
            </v-row>
          </v-img>
        </v-card>
    </v-slide-item>
  </v-slide-group>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'PostList',
  computed: {
    ...mapState([
      'postList'
    ])
  },
  methods: {
    ...mapActions([
      'fetchPostList',
    ]),
    onSelectPost(pno) {
      this.$router.push(`/post/detail/${pno}`)
    },
  },
  created() {
    this.fetchPostList(1)
  }
}
</script>

<style scoped>
/* .current-image :hover {
  transform: scale(1.1);
} */
.current-image ::-webkit-scrollbar {
  display: none;
}
</style>