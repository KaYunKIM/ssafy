<template>
  <div>

    <div v-if="surveyState">
      <!-- surveyResultRecommend -->
      <h1>'{{ target }}'에게 추천하는 카페</h1>
      <SurveyRecommendList/>
    </div>
    
    <!-- post -->
    <h1>Posts</h1>
    <PostList/>

    <!-- cafe -->
    <h1>Cafes</h1>
    <CafeList/>


    <!-- likeRecommend -->
      <h1><i class="fas fa-heart fa-1x" style="color: #ef9a9a"></i> 많은 카페 </h1>
      <MostLikeRecommendList/>

      <h1>최근 <i class="fas fa-heart fa-1x" style="color: #ef9a9a"></i> 카페</h1>
      <RecentLikeRecommendList/>

    <!-- stampRecommend -->
      <h1>최다 <i class="fas fa-shoe-prints fa-rotate-270 fa-1x" style="color: #90caf9"></i> 카페</h1>
      <MostStampRecommendList/>

      <h1>요즘 <i class="fas fa-shoe-prints fa-rotate-270 fa-1x" style="color: #90caf9"></i> 카페</h1>
      <RecentStampRecommendList/>

    <!-- geo -->
      <h1>내 주위 근처 카페</h1>
      <GeoList/>


  </div>
</template>

<script>
// @ is an alias to /src
import CafeList from '@/components/CafeList.vue'
import PostList from '@/components/PostList.vue'
import GeoList from '@/components/GeoList.vue'

import SurveyRecommendList from '@/components/recommend/SurveyRecommendList.vue'
import MostLikeRecommendList from '@/components/recommend/MostLikeRecommendList.vue'
import RecentLikeRecommendList from '@/components/recommend/RecentLikeRecommendList.vue'
import MostStampRecommendList from '@/components/recommend/MostStampRecommendList.vue'
import RecentStampRecommendList from '@/components/recommend/RecentStampRecommendList.vue'

import { mapState } from 'vuex'

export default {
  name: 'Home',
  components: {
    CafeList,
    PostList,
    GeoList,
    SurveyRecommendList,
    MostLikeRecommendList,
    RecentLikeRecommendList,
    MostStampRecommendList,
    RecentStampRecommendList,
  },
  data() {
    return {
      groups: {
        '1': '커피 매니아',
        '2': '핵인싸 감성러',
        '3': '디저트 덕후',
        '4': '유니크 집착러',
        '5': '프로 귀차니즘',
      },
      target: null,
    }
  },
  computed: {
    ...mapState([
      'surveyState'
    ])
  },
  created() {
    this.target = this.groups[this.surveyState]
  }
}
</script>

<style scoped>
.link-text {
  color: black;
  text-decoration: none;
  text-transform: capitalize;
}

.v-card--reveal {
  align-items: center;
  bottom: 0;
  justify-content: center;
  position: absolute;
  opacity: 0.9;
  width: 100%;
}

.card-list {
  border: none;
}
</style>
