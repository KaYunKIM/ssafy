<template>
  <div style="color: #1A1F73">
    <div v-if="surveyState">
      <!-- surveyResultRecommend -->
      <h1><br>'{{ target }}' 취향저격 카페</h1>
      <SurveyRecommendList/>
    </div>
    <!-- <div v-else>
      <h1>아직 유형 추천 카페가 없어요. 설문을 진행하시겠어요?</h1>
    </div> -->
    
    <h1><br><i class="fas fa-heart fa-1x" style="color: #8C4F5A"></i> 많은 카페</h1>
    <MostLikeRecommendList/>

    <h1><br>최다 <i class="fas fa-shoe-prints fa-rotate-270 fa-1x" style="color: #49538C"></i> 카페</h1>
    <MostStampRecommendList/>
    
    <h1><br>최근 <i class="fas fa-heart fa-1x" style="color: #8C4F5A"></i> 카페</h1>
    <RecentLikeRecommendList/>
    
    <h1><br>실시간 <i class="fas fa-shoe-prints fa-rotate-270 fa-1x" style="color: #49538C"></i> 카페</h1>
    <RecentStampRecommendList/>

    <!-- geo -->
      <h1><br>내 주위 <i class="material-icons md-48" style="color: #49538C">gps_fixed</i> 카페</h1>
      <GeoList/>


  </div>
</template>

<script>
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
  color: "#1A1F73";
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
