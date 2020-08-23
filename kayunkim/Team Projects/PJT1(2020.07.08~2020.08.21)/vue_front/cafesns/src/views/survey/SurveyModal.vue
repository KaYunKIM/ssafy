<template>
  <v-overlay :value="overlay" style="background:#2c001e;">
    <v-carousel hide-delimiters>
      <v-carousel-item
        v-for="(item,i) in items"
        :key="i"
        :src="item.question"
      >
      <h2 v-html="item.question"></h2>
      </v-carousel-item>
    </v-carousel>
      <v-btn @click="surveySubmit('Y')">예</v-btn>
      <v-btn @click="surveySubmit('N')">아니오</v-btn>
      <v-btn absolute right rounded text @click="$router.push(`/`)">skip</v-btn>
      <v-btn
        class="ma-2"
        :loading="loading"
        :disabled="loading"
        color="success"
        @click="loader = 'loading'"

      >
      추천 카페 보기
      <template v-slot:loader>
        <span>카페 찾는 중...</span>
      </template>
      </v-btn>  
  </v-overlay>
</template>


<script>
import { mapActions } from 'vuex'

export default {
  name: 'SurveyResult',
  data () {
    return {
      activeColor: "#2c001e",
      overlay: true,
      items: [
        { 
          question:
            '환영합니다. <br> cafe人 서비스는 <br>  성향테스트 결과에 따른 <br> 맞춤형 카페를 추천해드립니다. <br> 설문을 진행하시겠습니까?'
        },
        {
          question: '맛 vs 위치   dfasdfdfdafadfdfasdsdffffffff'
        },
        {
          question: '음료 vs 디저트   asdfasdfsdfasdfasdfsddsff'
        },
        // {
        //   question: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg',
        // },
        // {
        //   question: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg',
        // },
        // {
        //   question: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg',
        // },
      ],
      loader: null,
      loading: false,
    }
  },

  methods : {
    ...mapActions([
      'surveySubmit',
    ]),
  },

  watch: {
    loader () {
      const l = this.loader
      this[l] = !this[l]
      setTimeout(() => (this[l] = false), 3000)
      this.loader = null
    },
  },
}
</script>



<style scoped>
.backgroundcolor{
  background: #2c001e
}
.custom-loader {
    animation: loader 1s infinite;
    display: flex;
  }
  @-moz-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @-webkit-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @-o-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
</style>


<template>
  <div id="surveyContainer">
    <v-dialog
    v-model="dialog"
    transition="dialog-bottom-transition"
    persistent
    max-width="600px"
    overlay-color="#2c001e"
    overlay-opacity="0"
    >
    <v-row justify="space-around">
      <v-icon v-if="questionNo===0" @click="questionNo++">YES1</v-icon>
      <v-icon v-if="questionNo!==0 && questionNo!==2" @click="questionNo++, answer[questionNo-1]= 1;">YES2</v-icon>
      <v-icon v-if="questionNo>=2" @click="toSurveySubmit(questionNo,1)">YES3</v-icon>
        <!-- <h2 v-for="(item,i) in items" :key="i" > -->  
        <h2>{{ items[questionNo].title }}</h2> 
        <!-- </h2> -->
      <h1 v-html="item"></h1>
      <v-icon v-if="questionNo===0" @click="questionNo++">NO1</v-icon>
      <v-icon v-if="questionNo!==0 && questionNo!==2" @click="questionNo++, answer[questionNo-1]= 0;">NO2</v-icon>
      <v-icon v-if="questionNo>=2" @click="toSurveySubmit(questionNo,0)">NO3</v-icon>
      <h2>{{ answer }}</h2>
      <v-btn v-if="questionNo!==3" absoute right rounded text dark color="red" @click="$router.push(`/`)">skip</v-btn>
    </v-row>
    </v-dialog>
  </div>
</template>
  
  <!-- <input
      background-color="white"
      color="black"
      label="username"
  > -->

<script>
import { mapState, mapActions } from 'vuex'

// Survey.StylesManager.applyTheme("bootstrap");

export default {
  name: 'LoginView',
  data() {
    return {
      dialog: true,
      questionNo:0,
      answer: {
        1: null,
        2: null,
        3: null,
        4: null,
        5: null,
      },
      items: [
        { 
          title:
            "환영합니다. <br> cafe人 서비스는 <br> 성향테스트 결과에 따른 <br> 맞춤형 카페를 추천해드립니다. <br> 설문을 진행하시겠습니까?"
        },
        {
          title: '맛 vs 위치'
        },
        {
          title: '음료 vs 디저트'
        },
      ],
      // survey : new Survey.Model(surveyJSON),
      // $("#surveyContainer").Survey({
      //   model: survey,
      //   onComplete: sendDataToServer
      // }),
      surveyJSON : {
        "elements":[
          {
            "type":"radiogroup",
            "name":"question1",
            "title":"맛 vs 분위기",
            "choices":[
              {
                "value":"item1",
                "text":"맛"
              },
              {
                "value":"item2",
                "text":"분위기"
              }
            ]
          },
          {
            "type":"radiogroup",
            "name":"question2",
            "title":"커피  vs 디저트",
            "choices":[
              {
                "value":"item1",
                "text":"커피"
              },
              {
                "value":"item2",
                "text":"디저트"
              }
            ]
          }
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
    sendDataToServer(survey) {
  //send Ajax request to your web server.
    alert("The results are:" + JSON.stringify(survey.data))
    },
  },
  
}
</script>


<style scoped>
.background_color {
  color: white;
}
</style>