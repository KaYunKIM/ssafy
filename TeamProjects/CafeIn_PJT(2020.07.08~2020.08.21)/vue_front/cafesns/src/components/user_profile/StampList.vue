<template>
  <v-slide-group
    show-arrows-on-hover
  >
    <div v-if="!stampList.length" class="mx-auto">
      현재 방문한 카페가 없습니다.
    </div>
    <v-slide-item
      v-for="cafe in stampList"
      :key="cafe.id"
      v-slot:default="{ toggle }"
    >
      <v-card
        class="ma-1"
        @click="toggle"
      >
        <v-img
          :src="'https://i3a203.p.ssafy.io:5000/api/cafe/get/image/'+cafe.cafeno"
          height="170px"
          width="170px"
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
  name: 'StampList',
  data() {
    return {
      randomImg : "https://cdn.vuetifyjs.com/images/cards/cooking.png"
    }
  },
  computed: {
    ...mapState([
      'stampList'
    ])
  },
  methods: {
    ...mapActions([
      'fetchStampList',
    ]),
    onSelectCafe(target) {
      this.$router.push(`/cafe/detail/${target}`)
    },
  },
  created() {
    this.fetchStampList()
  }
}
</script>
