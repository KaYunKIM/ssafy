<template>
  <v-app>
    <side-nav-bar></side-nav-bar>
        <v-form >
          <v-container class="d-flex justify-center">
            <!-- <v-row> -->
              <v-col cols="12" sm="8">
                <v-form  v-on:submit.prevent>
                  <v-text-field v-model="keyword" label="키워드 검색" filled shaped @keypress.enter="searchKeyword(keyword)">

                  </v-text-field>
                </v-form>
                <v-container class="keywordContent">
                    <v-list-item v-for="(item, idx) in data" :key="idx">
                        <v-card class="ml-10 mt-5 content" @click="goMeetingLog(item.project.id, item.time)">
                            {{item}}
                        </v-card>
                    </v-list-item>
                </v-container>
              </v-col>
            <!-- </v-row> -->
          </v-container>
        </v-form>
  </v-app>
</template>

<script>
import SideNavBar from "@/components/SideNavBar";
import {  mapState, mapActions } from "vuex";
// import SERVER from '@/API/url'

export default {
  name: "SearchKeyword",
  components: {
    SideNavBar,
  },
  data: () => ({
    keyword: null,
    data:[

    ]
  }),
  computed: {
    ...mapState([
        'keywordData',
        'searchStatus',
    ]),
  },
  methods: {
    ...mapActions([
        'searchKeyword',
        'searchMain'
    ]),
    goMeetingLog(project_id, time){
        const date = time.substr(0, 10)
        this.$router.push(`/project/${project_id}/meetinglog/${date}`)
    }
  },
  watch: {
    keywordData(){
      this.data = this.keywordData
    }
  },
};
</script>
<style>
.keywordContent{
    background-color: #dfdce6;
    height: 680px;
    border-radius: 0px;
}
.content{
    color:white; 
    /* width: 40%;  */
    height: 200px;
}
</style>
