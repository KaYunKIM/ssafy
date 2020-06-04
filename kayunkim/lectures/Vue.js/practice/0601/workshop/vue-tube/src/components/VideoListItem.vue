<template>
  <div>
      {{ video.snippet.title }}
      <h1></h1>
      <ul>

      </ul>
      <videoListItem/>
  </div>
</template>
import VideoListItem from './VideoListItem.vue'

<script>
export default {
    name: 'VideoListItem',
    components : {
        VideoListItem,
    },
    props: {
        videos: Object,
    },
}
</script>

<style>

</style>