<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">

      <a class="navbar-brand" @click="resetPage"><router-link to="/" class="text-white text-decoration-none">Movie App</router-link></a>
      
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item mx-2">
            <router-link class="text-white" to="/">Movie</router-link>
          </li>    
          <li class="nav-item mx-2">
            <router-link class="text-white" to="/video">Video</router-link>
          </li>   
        </ul>
      </div>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  methods: {
    resetPage() {
      location.reload()
    },
  },
}
</script>

<style>

</style>
