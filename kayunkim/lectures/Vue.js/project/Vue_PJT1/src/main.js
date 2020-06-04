import Vue from 'vue'
import App from './App.vue'
import router from './router'
import LazyYoutubeVideo from 'vue-lazy-youtube-video'


Vue.config.productionTip = false
Vue.component('LazyYoutubeVideo', LazyYoutubeVideo)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
