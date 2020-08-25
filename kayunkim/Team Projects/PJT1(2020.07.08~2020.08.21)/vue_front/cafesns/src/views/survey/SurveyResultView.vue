<template>
	<div>
    <v-overlay style="background-image:linear-gradient(45deg, #a6c0fe, #f68084);" opacity="0">

      <v-dialog
        v-model="dialog"
        overlay-opacity="0"
        persistent
        width="700px"
        style="background:transparent"
      >
      <v-card class="text-center" style="background:transparent; color:white;" dark>
        <h1 v-if="this.surveyState == 1">"나는야 커피 매니아"</h1>
        <v-card-title v-if="this.surveyState == 1" class="headline justify-center pt-2" ><img class="rounded" src="@/assets/result/coffee.jpg" alt="coffee" width="400"></v-card-title>
        <v-card-text v-if="this.surveyState == 1" class="px-0">
          <h2 class="mt-3">전정한 커피 맛은 까다로운 <br>로스팅 포인트와 완벽한 <br>중력작용, 그리고 로스터의<br>신중한 감각에서 결정된다.</h2>
          <br><h3>카페 본연의 기능에 집중하는 당신,<br>역시 커피 매니아답다. <br>이것저것 따질거 없이 커피 맛이<br>제일 중요하며 본인만의 커피 철학을<br>내세워까다로운 입맛을 소유한 당신은
          <br>원두, 바디감, 추출 방식 등에 깐깐한<br><br>"진정한 커피 매니아!"</h3>
        </v-card-text>
        
        <h1 class="pb-2" v-if="this.surveyState == 2">"나는야 인<span class="material-icons">grade</span> 감성러"</h1>
        <v-card-title v-if="this.surveyState == 2" class="headline justify-center pt-0"><img class="rounded" src="@/assets/result/hot.jpg" alt="hotplace" width="400"></v-card-title>
        <v-card-text v-if="this.surveyState == 2" class="px-0">
          <h4>#핫플 #핵인싸 #인생은웨이팅 #감빼시</h4><br>
          <h2 class="">카페는 역시 맛보단 분위기지 <br> 나는 카페에서 분위기를 마신ㄷr.. <br></h2>
          <br><h3>어차피 커피 맛은 다 거기서 거기라고<br>생각하며 카페는 무조건 핫플 위주로 간다.<br>때문에
          핫플레이스의 기본은 웨이팅이지~를<br>외치며 기다리는 시간이 세상 행복한 당신은<br><br>
          "레알 핵인싸 인스타 감성러!"</h3>
        </v-card-text>

        <h1 v-if="this.surveyState == 3" class="pb-0">"나는야 디저트 덕후"</h1>
        <v-card-title v-if="this.surveyState == 3" class="headline justify-center"><img class="rounded" src="@/assets/result/dessert.jpg" alt="dessert" width="300"></v-card-title>
        <v-card-text v-if="this.surveyState == 3">
          <h2 class="mt-3">커피는 그저 목축임일 뿐<br>카페는 역시 먹으러 가는 곳</h2>
          <br><h3>당신이 카페를 찾는 목적은<br> 베이커리와 케이크 가득 디저트를<br>먹기 위한 것.
          쓰디 쓴 커피보단<br> 달달한 디저트 취향으로<br><br>커피는 디저트를 먹기 위한,<br> 그저 부드러운 목 넘김을 위한 것.<br>그 이상 그 이하도 아니라고 생각하는<br>
          당신은 진정한 빵순이이자,<br><br>"맛있으면 0칼로리 디저트덕후!"</h3>
        </v-card-text>

        <h1 v-if="this.surveyState == 4" class="pt-2">"나는야 유니크 집착러"</h1>
        <v-card-title v-if="this.surveyState == 4" class="headline justify-center"><img class="rounded" src="@/assets/result/theme.jpg" alt="" width="450"></v-card-title>
        <v-card-text v-if="this.surveyState == 4" class="px-0">
          <h2 class="mt-3">세상에서 젤 무서운 호랑이는 평범.<br>커피만 마시는 그냥카페는<br>온 몸의 세포가 거부한다.</h2>
          <br><h3>평소 평범함은 거부하는 당신이 카페를 찾는<br>이유는  한 잔의 커피가 아닌, 누군가와의 만남<br>혹은 재미요소를 위한 것.<br>
          결코 흔하지 않은 이색카페, 테마카페를 <br>기꺼이 찾아다니는 당신은 <br><br>
          "평범함 따위 모르는 유니크 집착러!"</h3>
        </v-card-text>

        <h1 v-if="this.surveyState == 5" class="pt-2">"나는야 프로 귀차니즘"</h1>
        <v-card-title v-if="this.surveyState == 5" class="headline justify-center"><img class="rounded" src="@/assets/result/random.jpg" alt="random" width="450"></v-card-title>
        <v-card-text v-if="this.surveyState == 5">
          <h2 class="mt-3">지나친 고민은 몸에 해로워! <br>나에게 필요한 건<br>당장의 카페인 뿐!</h2>
          <br><h3>어차피 커피는 다 거기서 거기라고<br>생각하는 당신. 저기서 파는 커피<br>여기도 다 판다며
          특정 카페를 찾아<br>멀리 나가기보단 무조건 동네 근처!<br>가가운게 최고! 를 외치는 당신은<br><br>
           "프로 아무거나 귀차니즘" 유형</h3>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
            <v-btn
            color="white"
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
        overlay-opacity="0"
        persistent
        width="700px"
        style="background:transparent"
      >
        <div class="text-right">
          <v-btn
            color="white"
            text
            @click="(dialog=true, dialog2=false)"
          >
          </v-btn>
        </div>
        <h2 class="text-center" style="color:white;">당신만을 기다리고 있는<br> 카페들이에요</h2><br>
        <div class="d-flex justify-space-around">
          <v-card
            v-for="cafe in surveyList"
            :key="cafe.cno"
            class="ma-1"
            @click="onSelectCafe(cafe.cafeno)"
          >
            <v-img
              height="160px"
              width="160px"
              class="grey lighten-2"
              :src="'https://i3a203.p.ssafy.io:5000/api/cafe/get/image/'+cafe.cafeno"
            >
              <v-row align="end" class="lightbox white--text fill-height">
                <v-col style="background:#00000080">
                  <div v-if="cafe.name.length<10" class="subheading text-center">{{ cafe.name }}</div>
                  <div v-else class="subheading text-center">{{ cafe.name.substring(0, 8) + "..." }}</div>
                </v-col>
              </v-row>
            </v-img>
          </v-card>
        </div>
        
        <h4 style="color:white;"><br>KEYWORDS</h4>
        <div class="" style="color:white;">
          <div v-if="surveyState == 1">
            <p>#바리스타 #로스팅 #전문가 #전문성 ..</p>
          </div>

          <div v-else-if="surveyState == 2">
            <p>#감성 #분위기 #포토 #트렌디 ..</p>
          </div>

          <div v-else-if="surveyState == 3">
            <p>#디저트 #베이커리 #와플 #케이크 ..</p>
          </div>

          <div v-else-if="surveyState == 4">
            <p>#테마 #이색 ..</p>
          </div>
          
          <div v-else>
            <p>#핵심키워드가없..</p>
          </div>
        </div>

        <div class="d-flex justify-space-between">
          <div>
            <v-bottom-navigation style="background:transparent; box-shadow:none !important;">
              <v-btn
              @click="(dialog2=false, dialog=true)"
            >
              <span class="white--text">결과보기</span><span class="material-icons white--text">undo</span>
              </v-btn>
            </v-bottom-navigation>
          </div>

          <div>
          <v-bottom-navigation style="background:transparent; box-shadow:none !important;">
            <v-btn
              text
              @click="(dialog2=false, $router.push(`/home`))"
            >
              <span class="white--text">메인으로</span><span class="material-icons white--text">home</span>
            </v-btn>
          </v-bottom-navigation>
          </div>
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