<template>
  <div>
    <v-card
      class="mx-auto my-12 pa-3"
    >
      <v-card-title class="pb-0">
        <h1 style="color: #1A1F73">{{ selectedCafe.name }}</h1>
      </v-card-title>
      <v-row>
        <v-col
          cols="12"
          sm="6" 
        >
          <!-- cafe image -->
          <v-img
            height="250"
            class="grey lighten-2 ma-3"
            :src="'https://i3a203.p.ssafy.io:5000/api/cafe/get/image/'+selectedCafe.cafeno"
          >
          </v-img>
          <v-row align="end"> 
            <v-col class="text-start ml-3 pb-0">
              <!-- like -->
              <v-tooltip top>
                <template v-slot:activator="{on}">
                  <v-btn v-if="liked" v-on="on" icon style="color: #8C4F5A" @mouseover="likeExplanation()" @click="thisViewLikeCafe(selectedCafe.cafeno)" class="mr-2">
                    <i class="fas fa-heart fa-2x"></i>
                  </v-btn>
                  <v-btn v-else v-on="on" icon color="grey lighten-1" @click="thisViewLikeCafe(selectedCafe.cafeno)" class="mr-2">
                    <i class="fas fa-heart fa-2x"></i>
                  </v-btn>
                </template>  
                <span>방문하고 싶은 카페</span>
              </v-tooltip>
              <!-- stamp -->
              <v-tooltip top>
                <template v-slot:activator="{on}">
                  <v-btn v-if="stamped" v-on="on" icon style="color: #49538C" @click="thisViewStampCafe(selectedCafe.cafeno)" class="mx-1">
                    <i class="fas fa-shoe-prints fa-rotate-270 fa-2x"></i>
                  </v-btn>
                  <v-btn v-else v-on="on" icon color="grey lighten-1" @click="thisViewStampCafe(selectedCafe.cafeno)" class="mx-1">
                    <i class="fas fa-shoe-prints fa-rotate-270 fa-2x"></i>
                  </v-btn>
                </template>
                <span>방문한 카페</span>
               </v-tooltip>
            </v-col>
          </v-row>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >

            <v-card-title class="pb-0" style="color: #49538C">cafe open - close</v-card-title>
            <v-card-text style="color: #D9A9A9">{{ selectedCafe.business_hours }}</v-card-text>

            <v-card-title class="py-0" style="color: #3F438C">cafe info</v-card-title>
            <v-card-text class="pb-0">
              <div class="d-flex">
                <p class="mb-0" style="color: #D9A9A9">tel)</p>
                <p class="mb-0 px-3" style="color: #49538C">{{ selectedCafe.tel }}</p>
              </div>
              <div class="d-flex">
                <p class="mb-0" style="color: #D9A9A9">address)</p>
                <p class="px-3" style="color: #49538C">{{ selectedCafe.address }}</p>
              </div>
            </v-card-text>

            <v-card-title v-if="cafeKeywords" class="py-0" style="color: #49538C">cafe keywords</v-card-title>
              <div class="ml-3 mt-2">
                <v-chip 
                  v-for="keyword in cafeKeywords"
                  :key="keyword.keyno"
                  class="mx-1"
                  color="#D9A9A9"
                  style="color: white"
                >{{ keyword.keyword }}
                </v-chip>
                <v-chip v-if="!cafeKeywords.length">
                  coffee
                </v-chip>
              </div>
          </v-col>

      </v-row>
        <v-card-title class="pt-4" style="color: #1A1F73">cafe menu</v-card-title>
        <v-card-text v-if="!cafeMenu.length">메뉴 준비 중 입니다.</v-card-text>
        <v-card-text>
          <v-row>
            <v-col
              cols="12"
              sm="6"
               class="py-0"
              v-for="menu in cafeMenu"
              :key="menu.id"
            >
              <v-row>
                <v-col cols="9" class="py-0">
                  <p class="text-justify mb-1" style="color: #D9A9A9">{{ menu.item }}</p>
                </v-col>
                <v-col cols="3" class="py-0">
                  <p style="color: #49538C">{{ menu.price }}</p>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
        </v-card-text>

      <v-card-actions class="pt-0">
        <v-spacer></v-spacer>
        <router-link to="/post/create" class="text-decoration-none">
          <v-bottom-navigation style="background:transparent; box-shadow:none !important;">
            <v-btn
              color="deep-purple lighten-2"
              text
            >
            <span style="color: #49538C">New Post</span>
            <span class="material-icons mx-3" style="color: #1A1F73">add_box</span>
            </v-btn>
          </v-bottom-navigation>
        </router-link>
      </v-card-actions>
    </v-card>
    <PostList/>
  </div>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'
import PostList from '@/components/cafe/PostList.vue'

export default {
  name: 'CafeDetail',
  components: {
    PostList,
  },
  data() {
    return {
      cafeId: this.$route.params.cafe_id,
      active: 1,
      keywords: ['coffee', 'drink', 'dessert'],
      liked: null,
      stamped: null,
    }
  },
  computed: {
    ...mapState([
      'selectedCafe',
      'cafeKeywords',
      'cafeMenu',
    ]),
    ...mapGetters(['isLoggedIn']),
  },
  methods: {
    ...mapActions([
      'cafeDetail',
      'aboutLike',
      'aboutStamp', 
      'likeCafe',
      'stampCafe',
    ]),
    thisViewLikeCafe(data) {
      this.likeCafe(data)
        .then(res => {
          this.liked = !res
        })
    },
    thisViewStampCafe(data) {
      this.stampCafe(data)
        .then(res => {
          this.stamped = !res
        })
    },
  },
  beforeUpdate() {
    this.aboutLike(this.cafeId)
      .then(res => this.liked = res)
    this.aboutStamp(this.cafeId)
      .then(res => this.stamped = res)
  },
  created() {
    this.cafeDetail(this.cafeId)
  },
}
</script>

<style>

</style>