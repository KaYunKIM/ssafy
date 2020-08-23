<template>
  <v-slide-group
    class="pa-4"
    active-class="secondary"
    show-arrows
  >
    <div v-if="!likeList.length" class="mx-auto">
      현재 좋아하는 카페가 없습니다.
    </div>
    <v-slide-item
      v-for="cafe in likeList"
      :key="cafe.id"
      v-slot:default="{ toggle }"
    >
      <v-card
        class="ma-4"
        @click="toggle"
      >
        <v-img
          :src="'https://i3a203.p.ssafy.io:5000/api/cafe/get/image/'+cafe.cafeno"
          height="200px"
          width="200px"
          @click="onSelectCafe(cafe.cafeno)"
        >
          <v-row align="end" class="lightbox white--text fill-height">
            <v-col style="background:#00000080">
              <div v-if="cafe.name.length<10" class="subheading">{{ cafe.name }}</div>
              <div v-else class="subheading">{{ cafe.name.substring(0, 10) + "..." }}</div>
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
  name: 'LikeList',
  data() {
    return {
      randomImg : "https://cdn.vuetifyjs.com/images/cards/cooking.png",
    }
  },
  computed: {
    ...mapState([
      'likeList'
    ])
  },
  methods: {
    ...mapActions([
      'fetchLikeList',
    ]),
    onSelectCafe(target) {
      this.$router.push(`/cafe/detail/${target}`)
    },
  },
  created() {
    this.fetchLikeList()
  }
}
</script>
