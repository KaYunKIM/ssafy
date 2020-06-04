<template>
  <div class="card center mx-auto" style="width: 35rem; height:450px;">
    <!-- <LazyYoutubeVideo
    class="embed-responsive-item"
    style="height:350px"
    :src= "videoUrl"
    frameborder="0"
    allowfullscreen
    /> -->
    <iframe
    class="embed-responsive-item"
    style="height:350px"
    :src= "videoUrl"
    frameborder="0"
    allowfullscreen
    >
    </iframe>
    <div class="card-body">
      <h4 class="card-text">{{ originalTitle }}</h4>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
    name: 'VideoDetail',
    props: {
        video: {
            type: Object,
        }
    },
    computed: {
        videoUrl() {
            return `https://youtube.com/embed/${this.video.id.videoId}`
        },
        originalTitle() {
            return _.unescape(this.video.snippet.title)
        },
    },
}
</script>

<style scoped>
.v-lazy-image.embed-responsive-item {
    border-radius: 4px;
}

.v-lazy-imgae {
    width: 100%;
    height: 100%;
    filter: blur(3px);
    transition: filter 0.5s;
}

.v-lazy-image-loaded {
    filter: blur(0);
}
</style>