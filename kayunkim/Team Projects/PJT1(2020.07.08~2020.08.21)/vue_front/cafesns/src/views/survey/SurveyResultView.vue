<template>
	<div>
    <v-overlay style="background-image:linear-gradient(45deg, #a6c0fe, #f68084);" opacity="0">

      <v-dialog
        v-model="dialog"
        transition="dialog-bottom-transition"
        overlay-opacity="0"
        persistent
        width="700px"
        style="background:transparent"
      >
      <v-card class="text-center" style="background:transparent; color:white;" dark>
        <h1 v-if="this.surveyState == 1" class="pt-2">나는야 커피 매니아</h1>
        <v-card-title v-if="this.surveyState == 1" class="headline justify-center" ><img class="rounded" src="@/assets/result/coffee.jpg" alt="coffee" width="600"></v-card-title>
        <v-card-text v-if="this.surveyState == 1">
          <h2 class="my-2">전정한 커피 맛은 까다로운 로스팅 포인트와 완벽한 중력작용, <br> 그리고 로스터의 신중한 감각에서 결정된다.</h2>
          <br>카페 본연의 기능에 집중하는 당신, 역시 커피 매니아답다. <br>이것저것 따질거 없이 커피 맛을 제일 중요시하는 유형으로<br>
          본인만의 커피 철학을 내세워 까다로운 입맛을 소유한<br>
          당신은 원두, 바디감, 추출 방식 등에 깐깐한 진정한 커피 매니아!
        </v-card-text>
        
        <h1 v-if="this.surveyState == 2" class="pt-2">나는야 핵인싸 인스타 감성러</h1>
        <v-card-title v-if="this.surveyState == 2" class="headline justify-center"><img class="rounded" src="@/assets/result/hot.jpg" alt="hotplace" width="600"></v-card-title>
        <v-card-text v-if="this.surveyState == 2">
          <h2 class="my-2">#감빼시 #핫플 #핵인싸 #인생은웨이팅 #어커거 <br> 카페는 역시 맛보다 분위기지,나는 카페에서 분위기를 마신ㄷr.. <br></h2>
          <br>당신은 전형적인 감성빼면시체 유형. <br>어차피 커피 맛은 다 거기서 거기라고 생각하기 때문에 카페를 갈 때는 무조건 핫플만 간다.<br>
          핫플레이스의 기본은 웨이팅이지~를 외치며 기다리는 시간이 세상 행복한 <br>
          당신은 레알 핵인싸 인스타 감성러!
        </v-card-text>

        <h1 v-if="this.surveyState == 3" class="pt-2">나는야 빵순이 디저트 덕후</h1>
        <v-card-title v-if="this.surveyState == 3" class="headline justify-center"><img class="rounded" src="@/assets/result/dessert.jpg" alt="dessert" width="600"></v-card-title>
        <v-card-text v-if="this.surveyState == 3">
          <h2 class="my-2">커피는 그저 목축임일 뿐, 카페는 역시 먹으러가는 곳 </h2>
          <br>당신이 카페를 찾는 목적은 베이커리와 케이크들이 가득한 디저트를 먹기 위한 것<br>
          쓰디 쓴 커피보다 달달한 디저트 취향이며,<br> 커피는 그저 디저트를 먹을 때 부드러운 목 넘김을 위한 수단으로 생각하는<br>
          당신은 진정한 빵순이이자, 디저트덕후!
        </v-card-text>

        <h1 v-if="this.surveyState == 4" class="pt-2">나는야 평범거부 유니크 집착러</h1>
        <v-card-title v-if="this.surveyState == 4" class="headline justify-center"><img class="rounded" src="@/assets/result/theme.jpg" alt="" width="600"></v-card-title>
        <v-card-text v-if="this.surveyState == 4">
          <h2 class="my-2">세상에서 제일 무서운 호랑이는 평범. <br>커피만 마시는 그냥카페는 온 몸의 세포가 거부한다.</h2>
          <br>평소 평범함은 거부하는 당신이 카페를 찾는 이유는 <br> 한 잔의 커피가 아닌, 누군가와의 만남 혹은 재미요소를 위한 것<br>
          결코 흔하지 않은 이색카페, 테마카페를 기꺼이 찾아다니는<br>
          당신은 평범함을 모르는 유니크 집착러!
        </v-card-text>

        <h1 v-if="this.surveyState == 5" class="pt-2">나는야 프로 귀차니즘</h1>
        <v-card-title v-if="this.surveyState == 5" class="headline justify-center"><img class="rounded" src="@/assets/result/random.jpg" alt="random" width="600"></v-card-title>
        <v-card-text v-if="this.surveyState == 5">
          <h2 class="my-2">지나친 고민은 몸에 해로워, 나에게 필요한 건 당장의 카페인 뿐</h2>
          <br>어차피 커피는 다 거기서 거기라고 생각하는 당신<br>저기서 파는 커피 여기도 다 판다며 <br> 
          특정 카페를 찾아가기 위해 멀리 나가기보다<br>무조건 동네 근처! 가가운게 최고!를 외치는<br>
          당신은 프로 아무거나 귀차니즘 유형!
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="secondary"
            text
            @click="(dialog=false, dialog2=true)"
          >
            추천 카페 보러가기
          </v-btn>
        </v-card-actions>
        
        </v-card>
      </v-dialog>

      <v-dialog
        v-model="dialog2"
        transition="dialog-bottom-transition"
        overlay-opacity="0"
        persistent
        width="700px"
        style="background:transparent"
      >
        <div class="text-right">
          <v-btn
            color="secondary"
            text
            @click="(dialog=true, dialog2=false)"
          >
            <span class="material-icons">refresh</span>
          </v-btn>
        </div>
        <h2 style="color:white;">추천 카페</h2>
        <div class="d-inline-flex">
          <v-card
            v-for="cafe in surveyList"
            :key="cafe.cno"
            class="ma-1"
            @click="onSelectCafe(cafe.cafeno)"
          >
            <v-img
              height="200px"
              width="200px"
              class="grey lighten-2"
              :src="'https://i3a203.p.ssafy.io:5000/api/cafe/get/image/'+cafe.cafeno"
            >
              <v-row align="end" class="lightbox white--text fill-height">
                <v-col style="background:#00000080">
                  <div v-if="cafe.name.length<10" class="subheading text-center">{{ cafe.name }}</div>
                  <div v-else class="subheading text-center">{{ cafe.name.substring(0, 10) + "..." }}</div>
                </v-col>
              </v-row>
            </v-img>
          </v-card>
        </div>
        
        <h2 style="color:white;">핵심 키워드</h2>
        <div class="text-center" style="color:white;">
          <div v-if="surveyState == 1">
            <p>바리스타 로스팅 전문가 전문성 ..</p>
          </div>

          <div v-else-if="surveyState == 2">
            <p>감성 분위기 포토 트렌디 ..</p>
          </div>

          <div v-else-if="surveyState == 3">
            <p>디저트 베이커리 와플 케이크 ..</p>
          </div>

          <div v-else-if="surveyState == 4">
            <p>테마 이색 ..</p>
          </div>
          
          <div v-else>
            <p>핵심 키워드가 없..</p>
          </div>
        </div>

        <div class="text-right">
          <v-btn
            color="green darken-1"
            text
            @click="(dialog2=false, $router.push(`/home`))"
          >
            <span class="material-icons">home</span>
            <span>메인으로</span>
          </v-btn>
        </div>
      </v-dialog>
    </v-overlay>

  </div>
</template>


<script>
import { mapState } from 'vuex'

export default {
  name: 'SurveyResultView',
  data () {
      return {
        dialog: false,
        dialog2: false,
      }
    },
	computed: {
		...mapState([
      'surveyState',
      'surveyList',
		])
  },
  methods: {
    onSelectCafe(target) {
      this.$router.push(`/cafe/detail/${target}`)
    }
  },
  created() {
    this.dialog = true
  }
}
</script>