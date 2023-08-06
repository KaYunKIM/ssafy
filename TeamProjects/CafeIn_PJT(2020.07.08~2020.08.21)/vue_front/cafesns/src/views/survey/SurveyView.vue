<template>
  <div>
    <v-overlay style="background-image:linear-gradient(45deg, #a6c0fe, #f68084);" opacity="0">
      <v-dialog
        v-model="dialog"
        transition="dialog-bottom-transition"
        overlay-opacity="0"
        persistent
        width="700px"
        class="py-4"
      >
      <v-stepper v-model="survey" class="text-center" style="background:transparent">
        <v-stepper-items style="color:white;">
          <v-row>
            <v-stepper-content
              class="px-0"
              v-for="(item, i) in surveyJSON.elements"
              :key="i"
              :step="i"
            >
              <v-col
                cols="12"
                class="px-2"
              >
                <h2 v-html="item.title" style="line-height:2;"></h2>
              </v-col>
              <v-col
                cols="12"
                v-if="i == 0"
              >
                <v-btn text dark @click="survey = 1" large>next</v-btn>
              </v-col>

              <v-col
                cols="6"
                sm="4"
                v-else-if="item.name === 'question3'"
                v-for="(choice, c) in item.choices"
                :key="c"
                class="d-inline-block survey"
              >
                <v-img
                  outlined
                  :src="choice.text"
                  width="150px"
                  height="230px"
                  contain
                  @click="target=choice.value; onNext(i);"
                ></v-img>

              </v-col>

              <v-col
                cols="6"
                sm="4"
                v-else-if="item.name === 'priority' "
                v-for="(choice, c) in item.choices"
                :key="c"
                class="d-inline-block survey"
              >
                <v-img
                  outlined
                  :src="choice.text"
                  width="300px"
                  height="200px"
                  @click="target=choice.value; onNext(i);"
                ></v-img>

              </v-col>

              <v-col
                cols="12"
                v-else
                v-for="(choice, c) in item.choices"
                :key="c"
              >
                <v-btn text dark @click="target=choice.value; onNext(i);">{{ choice.text }}</v-btn>
              </v-col>

            <div class="text-right" v-if="survey == 0">
              <v-btn rounded text dark color="#ffffff85" @click="$router.push(`/home`)">skip</v-btn>
            </div>
            </v-stepper-content>
          </v-row>
        </v-stepper-items>
      </v-stepper>
      </v-dialog>
    </v-overlay>
  </div>
</template>


<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'SurveyView',
  data() {
    return {
      dialog: true,
      survey: 0,
      target: null,
      answer: [0, 0, 0, 0, 0],
      priority: "priority",
      surveyJSON : {
        "elements":[
          {
            "name":"question",
            "title":"환영합니다!<br>cafe人은 성향 테스트를<br>기반으로 사용자 맞춤형<br>카페를 추천해드립니다.<br>성향 테스트를<br>진행하시겠습니까?",
          },
          {
            "name":"question1",
            "title":"Q1. 당신은 숲 속 길을 걷던 중 집을 한 채 발견했다. <br>이 중 가장 눈에 띄는 것은?",
            "choices":[
              {
                "value": 1,
                "text":"편안한 소파와 푹신한 침대"
              },
              {
                "value": 2,
                "text":"바베큐 파티를 즐기는 모습"
              },
              {
                "value": 3,
                "text":"식탁 위 먹음직스러운 음식들"
              },
              {
                "value": 4,
                "text":"평범한 가정집이 아닌 게스트하우스"
              },
              {
                "value": 5,
                "text":"우와 집이다. 하고 그냥 가던 길 간다"
              },
            ]
          },
          {
            "name":"question2",
            "title":"Q2. 당신의 선물 취향은?",
            "choices":[
              {
                "value": 2,
                "text":"핵인싸템"
              },
              {
                "value": 3,
                "text":"축하 케이크"
              },
              {
                "value": 1,
                "text":"꽃과 손편지"
              },
              {
                "value": 4,
                "text":"직접만든 향수"
              },
              {
                "value": 5,
                "text":"카카오페이 송금"
              },
            ]
          },
          {
            "name":"question3",
            "title":"Q3. 당신의 영화 취향은?",
            "choices":[
              {
                "value": 2,
                "text": require("@/assets/movies/para.jpg")
              },
              {
                "value": 4,
                "text": require("@/assets/movies/avengers.jpg")
              },
              {
                "value": 3,
                "text": require("@/assets/movies/charlie.jpg")
              },
              {
                "value": 1,
                "text": require("@/assets/movies/classic.jpg")
              },
              {
                "value": 5,
                "text": require("@/assets/movies/now.jpg")
              },
            ]
          },
          {
            "name":"question4",
            "title":"Q4. 회사 첫 출근을 위해 <br>출근룩을 준비하는 당신은?",
            "choices":[
              {
                "value": 1,
                "text":"정장을 꺼내 정성스럽게 다려놓는다"
              },
              {
                "value": 2,
                "text":"SNS #출근룩 검색 후 고대로 사러간다"
              },
              {
                "value": 4,
                "text":"미생을 보며 최애 캐릭터룩을 따라입는다"
              },
              {
                "value": 3,
                "text":"출근룩보단 텀블러, 슬리퍼, 쿠션 챙기기"
              },
              {
                "value": 5,
                "text":"옷장을 열어 손에 집히는거 대충 주워 입는다"
              },
            ]
          },
          {
            "name":"question5",
            "title":"Q5. 평소 집에 들어오자마자<br>바로 하는 행동은?",
            "choices":[
              {
                "value": 2,
                "text":"저녁 1깡을 실천한다."
              },
              {
                "value": 4,
                "text":"강아지랑 논다."
              },
              {
                "value": 1,
                "text":"씻고 옷을 갈아입는다."
              },
              {
                "value": 3,
                "text":"출출한데 뭐 먹지? 냉장고부터 연다."
              },
              {
                "value": 5,
                "text":"일단 눕고 생각한다."
              },
            ]
          },
          {
            "name":"priority",
            "title":"Q6. 1초만의 당신의 선택은?",
            "choices": [
              {
                "value": 1,
                "text": require("@/assets/priority/hot.jpg")
              },
              {
                "value": 2,
                "text":require("@/assets/priority/coffee.jpg")
              },
              {
                "value": 3,
                "text":require("@/assets/priority/dessert.jpg")
              },
              {
                "value": 4,
                "text":require("@/assets/priority/theme.jpg")
              },
              {
                "value": 5,
                "text":require("@/assets/priority/random.jpg")
              },
            ]
          },
        ]
      }
    }
  },

  computed: {
    ...mapState([
      'surveyState',
    ])
  },

  methods: {
    ...mapActions(['surveySubmit']),
    toSurveySubmit(questionNo,ans) {
      this.answer[questionNo]= ans
      this.surveySubmit(this.answer)
    },
    onNext(i) {
      function getIndex(array, priority) {
        return new Promise((resolve) => {
          const maxNum = Math.max(...array)
          if (array[priority-1] === maxNum) {
            resolve(priority)
          } else {
            const maxValue = array.indexOf(maxNum) + 1
            resolve(maxValue)
          }
        })
      }

      async function findValue (array, priority) {
        const getValue = await getIndex(array, priority)
        return getValue
      }
      
      if (i === this.surveyJSON.elements.length-1) {
        findValue(this.answer, this.priority)
          .then((res) => {
            this.surveySubmit(res.toString())
          })
      } else {
        this.answer[this.target-1] += 1
        this.survey = i + 1
      }
    },
    
  },
}
</script>

<style scoped>
#surveyContainer ::before {
  background-image: linear-gradient(45deg, #a6c0fe, #f68084);
}

.survey :hover {
  cursor: pointer;
}


</style>