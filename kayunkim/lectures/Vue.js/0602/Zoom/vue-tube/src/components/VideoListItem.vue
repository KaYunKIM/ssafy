<template>
<div>
  <li @click="onVideoSelect" class="video-list-item list-group-item my-3 row">
    <!-- <img :src="thumbnailUrl" alt="youtube thumbnail image"> -->
    <v-lazy-image :src="thumbnailUrl" alt="youtube thumbnail image"/>
    <p class="font-weight-bold">{{ safeTitle }}</p>
  </li>
</div>
  
</template>
<script>
import _ from 'lodash'

export default {
    name: 'VideoListItem', 
    props: {
        video: {
            type:Object,
        }
    },
    methods : {
        onVideoSelect() {
            this.$emit('video-select', this.video)
            scroll(0,0)
        },
    },
    computed: {
        // 함수지만 명사 => 결국 리턴되는 값으로 사용되기 때문
        thumbnailUrl() {
            return this.video.snippet.thumbnails.high.url
        },
        safeTitle() {
            return _.unescape(this.video.snippet.title)
        }
    }
}
</script>

<style scoped>
li.video-list-item {
    display: flex;
    cursor: pointer;
    border-radius: 4px;
}

li.video-list-item:hover {
    background-color: #eee;
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