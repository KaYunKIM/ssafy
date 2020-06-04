<template>
  <ul class="list-group col-lg-4 pr-0">
      <VideoListItem 
        @video-select="onVideoSelect"
        v-for="video in videos" 
        :key="video.etag"
        :video="video"/>
  </ul>
</template>

<script>
import VideoListItem from '@/components/VideoListItem.vue'

export default {
    name: 'VideoList',
    components: {
        VideoListItem
    },
    props: {
        videos: {
            type: Array,
        }
    },
    methods: {
        onVideoSelect(video) {
            this.$emit('video-select', video)
        }
    }
}
</script>

<style>

</style>