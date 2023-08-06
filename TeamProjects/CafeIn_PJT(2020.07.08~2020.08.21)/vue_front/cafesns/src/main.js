import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import store from './store'
import vueCookies from 'vue-cookies'
import infiniteScroll from 'vue-infinite-scroll'

Vue.config.productionTip = false

Vue.use(vueCookies, infiniteScroll)

new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')
