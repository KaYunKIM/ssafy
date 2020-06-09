<template>
  <div>
      <h1>New Article</h1>
      <div>
        <label for="title">title: </label>
        <input v-model="articleData.title" id="title" type="text">
      </div>
      <div>
        <label for="content">content: </label>
        <input v-model="articleData.content" id="content" type="text">
      </div>
      <div>
          <button @click="createArticle">submit</button>
      </div>
  </div>
    

</template>

<script>
import axios from 'axios'
const SERVER_URL = ""

export default {
    name: 'CreateView',
    data() {
        return {
            articleData: {
                title: null,
                content: null,
            }
        }
    },
    methods: {  
        createArticle() {
            const config - {
                headers: {
                    Authorization: `Token ${this.$cookies.get('auth-token')}`
                }
            }
            // article 생성은 Header: Token/ Body: { title:, content: }
            axios.post(SERVER_URL + '/articles/create/', this.articleData, config)
              .then()
              .catch()
        }

    }
}
</script>

<style>

</style>