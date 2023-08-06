<template>
  <div>
    <VideoItemDetail
     v-for="video in videos"
     :key='video.id.videoId'
     :video="video"/>
  </div>
</template>
<script>
import VideoItemDetail from '@/components/VideoItemDetail.vue'

export default {
    name: 'VideoItem',
    components: {
        VideoItemDetail
        
    },
    props: {
        videos: {
            type: Array,
        }
    },
}
</script>

<style>

</style>