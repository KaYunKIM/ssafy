<template>
  <div class="container text-center my-4">
    <h1>영화 예고편 검색</h1>
    <br>
    <VideoSearch @newsearch="getVideos"/>
    <hr>
    <VideoItem :videos="videos"/>
  </div>
</template>

<script>
import axios from 'axios'

import VideoSearch from '@/components/VideoSearch.vue'
import VideoItem from '@/components/VideoItem.vue'

const YOUTUBE_API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'Video',
  components: {
    VideoSearch,
    VideoItem,
  },
  data() {
    return {
      inputValue: '',
      videos: [],
    }
  },
  methods: {
    getVideos(keyword) {
      const config = {
        params: {
          key: YOUTUBE_API_KEY,
          part: 'snippet',
          type: 'video',
          q: keyword+' trailer',
        }
      }
      axios.get(YOUTUBE_API_URL, config)
        .then(res => {
          this.videos = res.data.items
        })
        .catch(err =>{
          console.log(err)
        })
    },
  }
}
</script>
