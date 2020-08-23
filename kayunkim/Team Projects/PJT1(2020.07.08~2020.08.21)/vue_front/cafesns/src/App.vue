<template>
  <v-app>
    <AppBar/>
    <v-main>
      <v-container>
        <router-view/>
         <!-- :key="$route.fullPath" -->
      </v-container>
    </v-main>

    <v-footer
      class="font-weight-medium mt-10 white"
      style="background-image: linear-gradient(45deg, #a6c0fe, #f68084);"
    >
      <v-col
        class="text-center"
        cols="12"
      >
        &copy; 2020  <strong>Cafe人: 나를 위한 카페 추천</strong>
      </v-col>
    </v-footer>
  </v-app>
</template>

<script>
import AppBar from '@/components/AppBar.vue'

export default {
  name: 'App',
  components: {
    AppBar,
  },
};
</script>

<style>
.v-dialog {
  box-shadow: none !important;
}

</style>