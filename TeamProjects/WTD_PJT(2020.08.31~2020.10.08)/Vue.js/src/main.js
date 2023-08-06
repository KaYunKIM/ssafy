import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'

// vuetify
import vuetify from './plugins/vuetify';


//Google
import GAuth from 'vue-google-oauth2'

// momentjs
import moment from "moment"
import VueMomentJS from "vue-momentjs"
Vue.use(VueMomentJS, moment)


Vue.config.productionTip = false


new Vue({
  store,
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')


window.Kakao.init("8c7ceac2c50b6110539dd4cb4b29a483");

const gauthOption = {
  clientId: '338122686257-abqr6lp6po1qaegicnocqmcl65odnahq.apps.googleusercontent.com',
  scope: 'email profile',
  prompt: 'consent',
  fetch_basic_profile: true
}

Vue.use(GAuth, gauthOption)