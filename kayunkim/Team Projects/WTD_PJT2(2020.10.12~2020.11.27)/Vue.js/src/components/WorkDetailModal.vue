<template>
<v-app>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600px" >
      <v-card color="#dfdce6" class="mx-lg-auto rounded-lg">
        <v-card-title class="pt-7 d-flex justify-center">
          <span style="font-weight:bold; color:#4c4c65;font-size: x-large;">업무 정보</span>
        </v-card-title>
        <v-card-text>
           <v-container fluid>


    <v-row style="height:70px;">
      <v-col cols="4" >
        <v-subheader class="workform">업무명</v-subheader>
      </v-col>
      <v-col cols="8">
        <v-text-field
          color="#4c4c65"
          v-model="task.title"
          solo
          label="업무명"
          clearable
        >
        </v-text-field>
      </v-col>
    </v-row>

    <v-row style="height:70px;">
      <v-col cols="4">
        <v-subheader class="workform">담당자</v-subheader>
      </v-col>
      <v-col cols="8">
        <v-select
          v-model="task.manager"
          :items="items"
        ></v-select>
      </v-col>
    </v-row>
  
  <v-row style="height:70px;">
      <v-col cols="4">
        <v-subheader class="workform">시작 시간</v-subheader>
      </v-col>
      <!-- <v-col cols="8">
        <v-text-field
          v-model="task.start_time"
          solo
          type="time"
          color="#4c4c65"
          clearable
        ></v-text-field>
      </v-col> -->
      <v-col cols ="8">
        <v-menu
          ref="smenu"
          v-model="start_menu"
          :close-on-content-click="false"
          :nudge-right="40"
          :return-value.sync="stime"
          transition="scale-transition"
          offset-y
          max-width="290px"
          min-width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="task.start_time"
              label="업무 시작 시간을 선택하세요."
              prepend-icon="mdi-clock-time-four-outline"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-time-picker color="#4C4C65"
            v-if="start_menu"
            :max="task.end_time"
            v-model="task.start_time"
            @click:minute="$refs.smenu.save(task.start_time)"
          ></v-time-picker>
        </v-menu>
      </v-col>
    </v-row>
    <v-row style="height:70px;">
      <v-col cols="4">
        <v-subheader class="workform">마감 시간</v-subheader>
      </v-col>
       <v-col cols ="8">
        <v-menu
          ref="emenu"
          v-model="end_menu"
          :close-on-content-click="false"
          :nudge-right="40"
          :return-value.sync="etime"
          transition="scale-transition"
          offset-y
          max-width="290px"
          min-width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="task.end_time"
              label="업무 마감 시간을 선택하세요."
              prepend-icon="mdi-clock-time-four-outline"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-time-picker color="#4C4C65"
            v-if="end_menu"
            v-model="task.end_time"
             :min="task.start_time"
            @click:minute="$refs.emenu.save(task.end_time)"
          ></v-time-picker>
        </v-menu>
      </v-col>
      <!-- <v-col cols="8">
        <v-text-field
          v-model="task.end_time"
          solo
          type="time"
          color="#4c4c65"
          clearable
        ></v-text-field>
      </v-col> -->
    </v-row>
    
     <v-row style="height:160px;">
      <v-col cols="4">
        <v-subheader class="workform">상세 업무</v-subheader>
      </v-col>
      <v-col cols="8">
        <v-text-field
          color="#4c4c65"
          v-model="task.detail"
          solo
          label="상세 업무"
          clearable
          height="150"
          
        >
        </v-text-field>
      </v-col>

    </v-row>
    <v-row style="height:20px;">
      <v-col cols="4">
      
        <v-subheader class="workform">완료 여부</v-subheader>
      </v-col>
      <v-col cols="5">
      </v-col>
      <v-col cols="3">
      <v-checkbox
        v-model="task.completed"
      ></v-checkbox>
      </v-col>
    </v-row>

  </v-container>
      
        </v-card-text>
        <v-card-actions class="pa-7 d-flex justify-center">
          <v-spacer></v-spacer>
          <v-spacer></v-spacer>
           <v-btn x-large color="#4c4c65" class="white--text" @click="updateWorkInfo(task)">수정</v-btn>
          <v-btn x-large color="#4c4c65" class="white--text" @click="deleteWorkInfo(task.id)">삭제</v-btn>
          <v-btn x-large color="#4c4c65" class="white--text" @click="updateWorkInfo(null)">취소</v-btn>
          <!-- <v-btn x-large color="#4c4c65" class="white--text" @click="dialog = false; $store.state.modalWorkDetail = !$store.state.modalWorkDetail">확인</v-btn> -->
          <!-- <v-spacer></v-spacer>
          <v-btn x-large color="#FFFFFF" class="black--text" @click="dialog = false">취소</v-btn> -->
          <v-spacer></v-spacer>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</v-app>
</template>

<script>
import {  mapActions, mapState } from 'vuex'

export default {
  name: 'WorkDetailModal',
    data: () => ({
      dialog: true,
      stime: null,       
      etime : null,       
      start_menu : false,       
      end_menu : false,
      task: {
        id :  "",
        title : "",
        manager : "",
        start_time : "",
        end_time : "",
        completed : "",
        detail : "",
        tmp_date: "",
      },
      items: [],
    }),
    computed:{
    ...mapState([
      'taskInfo',
      'memberList',
      'projectDate',
    ]),
  },
   methods:{
    ...mapActions([
      'updateWorkInfo',
      'deleteWorkInfo',
    ]),
  },
  created() {
    this.task.tmp_date = this.taskInfo.start.substr(0,10)
    
    this.task.id = this.taskInfo.id
    this.task.title = this.taskInfo.name
    this.task.detail = this.taskInfo.detail
    this.task.completed = this.taskInfo.completed
    this.task.manager = this.taskInfo.manager
    this.task.start_time = this.taskInfo.start.substr(11,5)
    this.task.end_time = this.taskInfo.end.substr(11,5)
    
    const members = this.memberList
    for (var i in members) {
      this.items.push(members[i]["user"]["nickname"])
    }
  }
}
</script>

<style scoped>
.workform {
  font-weight : bold;
  font-size: 1.2em;
}
</style>