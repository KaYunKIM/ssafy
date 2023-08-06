<template>
<v-app>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="40%">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="#4c4c65"
          dark
          v-bind="attrs"
          v-on="on"
        >
          Project 생성
        </v-btn>
      </template>
      <v-card color="#dfdce6" min-height="300" class="pa-md-15 mx-lg-auto rounded-lg">
          <v-card-title class="pa-5 d-flex justify-center">
          <span>생성된 프로젝트가 없습니다:)</span>
          <span>프로젝트를 생성하시겠습니까?</span>
        </v-card-title>
          
        <v-card-actions justify="center">
        <v-spacer></v-spacer>
          <v-btn x-large color="#4c4c65" class="white--text" @click="dialog = false">Yes</v-btn>
          <v-spacer></v-spacer>
          <v-btn x-large color="#FFFFFF" class="black--text" @click="dialog = false">No</v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>

      </v-card>
    </v-dialog>
  </v-row>
</v-app>
</template>

<script>
  export default {
    data () {
      return {
        dialog: false,
      }
    },
  }
</script>