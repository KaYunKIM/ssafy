<template>
  <div class="d-flex justify-content-center">  
    <div class="form-inline">
      <input type="text" v-model="keyword" placeholder="Search Trailer Here" class="form-control text-primary" @keydown.enter="searchVideo" v-focus>
      <button class="btn btn-outline-primary" @click="searchVideo">검색</button>
    </div>
  </div>
</template>

<script>
export default {
    name: 'videoSearch',
    data() {
        return {
            keyword: ''
        }    
    },
    methods: {
        searchVideo() {
            if (this.keyword) {
                this.$emit('newsearch', this.keyword)
                this.keyword = ''
            }
        }
    },
    directives: {
        focus: {
            inserted: function(el) {
                el.focus()
            }
        }

    }
}
</script>

<style>

</style>