<template>
  <div v-if="selectedVideo" class="col-lg-8">
    <div class="embed-responsive embed-responsive-16by9 my-3">
      <iframe 
        class="embed-responsive-item" 
        :src= "videoUrl"
        frameborder="0"
        >
        <!-- allowfullscreen -->
      </iframe>
    </div>
    <div class="video-detail">
      <h4>{{ selectedVideo.snippet.title }}</h4>
      <hr>
      {{ selectedVideo.snippet.description }}
      <!-- InnerHTML -->
      <!-- <h4 v-html=""></h4> -->
    </div>
  </div>
  
</template>

<script>
export default {
    name: 'VideoDetail',
    props: {
        selectedVideo: {
            type: Object,
        }
    },
    computed: {
        videoUrl() {
            return `https://youtube.com/embed/${this.selectedVideo.id.videoId}`
        }
    }
}
</script>

<style scoped>
    div.video-detail {
        margin-top: 10px;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 4px;
    }
</style>