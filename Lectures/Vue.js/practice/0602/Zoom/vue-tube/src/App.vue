<template>
  <div class="container" id="app">
    <SearchBar @input-change="getYoutubeVideos"/>
    <div class="row">
      <VideoDetail :selectedVideo="selectedVideo"/>
      <VideoList id="video" @video-select="onVideoSelect" :videos="videos"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import SearchBar from '@/components/SearchBar.vue'
import VideoList from '@/components/VideoList.vue'
import VideoDetail from '@/components/VideoDetail.vue'

const YOUTUBE_API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data() {
    return {
      inputValue: '',
      videos: [],
      selectedVideo: null,  //개발자가 명시적으로 빈 값을 주고 싶을 때 사용.
    }
  },
  methods: {
    getYoutubeVideos(userInput) {
      const config = {
        params: {
          key: YOUTUBE_API_KEY,
          part: 'snippet',
          type: 'video',
          q: userInput,
          maxResults: 50,

        }
      }
      axios.get(YOUTUBE_API_URL, config)
        .then(res => {
          this.videos = res.data.items
        })
        .catch(err => {
          console.error(err)
        })
    },
    onVideoSelect(video) {
      this.selectedVideo = video
    },
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
