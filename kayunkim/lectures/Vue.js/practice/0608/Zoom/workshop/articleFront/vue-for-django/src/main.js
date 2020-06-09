import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueCookies from 'vue-cookies'
import axios from 'axios'

Vue.use(VueCookies)
Vue.config.productionTip = false

// Axios 글로벌 설정: 어떤 컴포넌트에서도 바로 불러올 수 있음
Vue.prototype.$axios = axios

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
