<template>
  
  <div>
      <h1>CreateView</h1>
      title: <input v-model="articleInfo.title" type="text">
      <br>
      content: <input v-model="articleInfo.content" type="text">
      <br>
      <button @click="createArticle">create</button>
  </div>
</template>

<script>
import axios from 'axios'
const API_BASE_URL = 'http://localhost:8000'

export default {
    name: 'CreateView',
    data() {
        return {
            articleInfo: {
                title: '',
                content: '',
            }
        }
    },
    methods: {
        createArticle() {
            const API_CREATE_URL = API_BASE_URL + '/articles/'
            const config = {
                headers: {
                    Authorization: `Token ${this.$cookies.get('auth-token')}`
                }
            }
            axios.post(API_CREATE_URL, this.articleInfo, config)
              .then(() => {
                  this.$router.push('/articles')
              })
              .catch(err => {
                  console.log(err)
              })

        },
    },

}
</script>

<style>

</style>