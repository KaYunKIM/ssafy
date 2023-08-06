import Vue from 'vue'
import App from './App.vue'
import { VLazyImagePlugin } from 'v-lazy-image'
// import VueScrollMonitor from 'vue-scrollmonitor'

Vue.config.productionTip = false

Vue.use(VLazyImagePlugin)
// Vue.use(VueScrollMonitor)

new Vue({
  render: h => h(App),
}).$mount('#app')
