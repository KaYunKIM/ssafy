<template>
  <div v-cloak>

    <div v-if="errorStr">
      Sorry, but the following error
      occurred: {{errorStr}}
    </div>
    
    <div v-if="gettingLocation">
      <i>Getting your location...</i>
    </div>

    <div v-if="!geoCafeList.length">
      <h2>검색된 카페가 없습니다.</h2>
    </div>
    <v-slide-group
      show-arrows-on-hover
    >
      <v-slide-item
        v-for="cafe in geoCafeList"
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
      
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'GeoList',
  data() {
    return {
      location:null,
      gettingLocation: false,
      errorStr:null ,
    }
  },
  computed: {
    ...mapState(['geoCafeList'])
  },
  methods: {
    ...mapActions(['geo']),
    onSelectCafe(target) {
      this.$router.push(`/cafe/detail/${target}`)
    },
    geoLocation() {
      if(!("geolocation" in navigator)) {
        this.errorStr = 'Geolocation is not available.';
        return;
      } else {
        this.gettingLocation = true;
        // get position
        navigator.geolocation.getCurrentPosition(pos => {
          this.gettingLocation = false;
          this.location = pos;
          this.geo(this.location)
        }, err => {
          this.gettingLocation = false;
          this.errorStr = err.message;
        })
      }
    },
  },
  created() {
    this.geoLocation()
  },
}
</script>

<style scoped>
.hover-table :hover {
  cursor: pointer;
}
</style>