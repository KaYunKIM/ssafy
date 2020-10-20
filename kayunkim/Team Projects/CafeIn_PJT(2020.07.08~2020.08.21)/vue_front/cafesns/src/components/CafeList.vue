<template>
  <v-slide-group
    show-arrows-on-hover
  >
    <v-slide-item
      v-for="cafe in cafeList"
      :key="cafe.id"
      v-slot:default="{ toggle }"
    >
      <v-card
        class="ma-1"
        @click="toggle"
      >
        <v-img
          height="170px"
          width="170px"
          class="grey lighten-2"
          :src="'https://i3a203.p.ssafy.io:5000/api/cafe/get/image/'+cafe.cafeno"
          @click="onSelectCafe(cafe.cafeno)"
        >
          <v-row align="end" class="lightbox white--text fill-height">
            <v-col style="background:#00000080">
              <div v-if="cafe.name.length<10" class="subheading text-center">{{ cafe.name }}</div>
              <div v-else class="subheading text-center">{{ cafe.name.substring(0, 10) + "..." }}</div>
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
  name: 'CafeList',
  computed: {
    ...mapState([
      'cafeList'
    ])
  },
  methods: {
    ...mapActions([
      'fetchCafeList',
    ]),
    onSelectCafe(target) {
      this.$router.push(`/cafe/detail/${target}`)
    },
  },
  created() {
    this.fetchCafeList(1)
  }
}
</script>

<style scoped>
  .cafeList {
    overflow-x: hidden;
    overflow-y: hidden;
    white-space: nowrap;
  }
  .card {
    white-space: normal;
  }
</style>
