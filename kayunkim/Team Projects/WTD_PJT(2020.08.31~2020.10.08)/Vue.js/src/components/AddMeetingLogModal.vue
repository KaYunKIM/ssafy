<template>
<v-app>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600px" >
      <v-card color="#dfdce6" class="mx-lg-auto rounded-lg">
        <v-card-title class="pt-7 d-flex justify-center">
          <span style=" color:black; font-size: x-large;">회의 생성</span>
        </v-card-title>
        <v-card-text>
           <v-container fluid>


    <v-row style="height:70px;">
      <v-col cols="4">
        <v-subheader class="workform">미팅명</v-subheader>
      </v-col>
      <v-col cols="8">
        <v-text-field v-model="meetingInfo.title"
          label="미팅명을 입력해주세요"
          color="#4c4c65"
          solo
        ></v-text-field>
      </v-col>
    </v-row>

    <v-row style="height:70px;">
      <v-col cols="4">
        <v-subheader class="workform">시간</v-subheader>
      </v-col>
      <v-col cols ="8">
        <v-menu
          ref="smenu"
          v-model="menu"
          :close-on-content-click="false"
          :nudge-right="40"
          :return-value.sync="time"
          transition="scale-transition"
          offset-y
          max-width="290px"
          min-width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="meetingInfo.time"
              label="미팅 시간을 선택하세요."
              prepend-icon="mdi-clock-time-four-outline"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-time-picker color="#4C4C65"
            v-if="menu"
            v-model="meetingInfo.time"
            @click:minute="$refs.smenu.save(meetingInfo.time)"
          ></v-time-picker>
        </v-menu>
      </v-col>
    </v-row>

  </v-container>
      
        </v-card-text>
        <v-card-actions class="pb-7 d-flex justify-center">
          <v-spacer></v-spacer>
          <v-spacer></v-spacer>
          <v-btn x-large color="#4c4c65" class="white--text" @click="dialog = false; addMeetingLog(meetingInfo)">확인</v-btn>
          <v-spacer></v-spacer>
          <v-btn x-large color="#FFFFFF" class="black--text" @click="dialog = false; addMeetingLog(null)">취소</v-btn>
          <v-spacer></v-spacer>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</v-app>
</template>

<script>
  import { mapActions } from 'vuex'

  export default {
    name: 'AddMeetingLogModal',
    data: () => ({
      dialog: true,
      time: null,
      menu: false,
      meetingInfo : {
        title: "",
        time: null,
      },
    }),
    methods: {
      ...mapActions([
        'addMeetingLog'
      ]),
    },
  }
</script>
<style scoped>
  .workform {
    font-weight : bold;
    font-size: 1.2em;
   
  }
</style>