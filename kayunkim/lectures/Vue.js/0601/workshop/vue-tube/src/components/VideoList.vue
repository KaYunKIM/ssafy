<template>
  <div>
      <ul>
          <VideoListItem : video="video" v-for="video in videos" :key="video.etag"/>
          {{ videos }}
      </ul>
  </div>
</template>

<script>
import VideoList from './VideoList.vue'

export default {
    name: 'VideoList',
    props: {
        videos: {
            type: Array,
        },
    },
}
</script>

<style>

</style>