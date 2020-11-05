<template>
  <v-app>
    <v-row justify="center">
      <v-dialog v-model="dialog" persistent max-width="600px" >
        <v-card color="#dfdce6" class="mx-lg-auto rounded-lg">
          <v-card-title class="pa-7 d-flex justify-center">
            <span style="font-weight:bold; color:#4c4c65;font-size: x-large;">일정 추가</span>
          </v-card-title>
          <v-card-text>
            <v-container fluid>
              <v-row style="height:70px;">
                <v-col cols="4">
                  <v-subheader class="workform">일정명</v-subheader>
                </v-col>
                <v-col cols="8">
                  <v-text-field v-model="scheduleInfo.title"
                    label="일정명을 입력해주세요"
                    color="#4c4c65"
                    solo
                    clearable
                  ></v-text-field>
                </v-col>
              </v-row>

              <v-row style="height:70px;">
                <v-col cols="4">
                  <v-subheader class="workform" >내용</v-subheader>
                </v-col>
                <v-col cols="8">
                  <v-text-field v-model="scheduleInfo.detail"
                    label="내용을 입력해주세요"
                    color="#4c4c65"
                    solo
                    clearable
                  ></v-text-field>
                </v-col>
              </v-row>
      
              <v-row style="height:70px;">
                <v-col cols="4" >
                  <v-subheader class="workform" >시작일자</v-subheader>
                </v-col>
                <v-col cols ="8">
                  <v-menu
                    ref="sdmenu"
                    v-model="start_date_menu"
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
                        v-model="scheduleInfo.start_date"
                        prepend-icon="mdi-clock-time-four-outline"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-date-picker color="#4C4C65"
                      v-if="start_date_menu"
                      v-model="scheduleInfo.start_date"
                      :show-current="false"
                      @click:date="$refs.sdmenu.save(scheduleInfo.end_date)"
                    ></v-date-picker>
                  </v-menu>
                </v-col>
              </v-row>

              <v-row style="height:70px;">
                <v-col cols="4" >
                  <v-subheader class="workform" >시작시간</v-subheader>
                </v-col>
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
                        v-model="scheduleInfo.start_time"
                        placeholder="일정 시작 시간을 선택하세요."
                        prepend-icon="mdi-clock-time-four-outline"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-time-picker color="#4C4C65"
                      v-if="start_menu"
                      v-model="scheduleInfo.start_time"
                       :max="checkMax(scheduleInfo.start_date, scheduleInfo.end_date, scheduleInfo.end_time)"
                      @click:minute="$refs.smenu.save(scheduleInfo.start_time)"
                    ></v-time-picker>
                  </v-menu>
                </v-col>
              </v-row>

              <v-row style="height:70px;">
                <v-col cols="4" >
                  <v-subheader class="workform">마감일자</v-subheader>
                </v-col>
                <v-col cols ="8">
                  <v-menu
                    ref="edmenu"
                    v-model="end_date_menu"
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
                        v-model="scheduleInfo.end_date"
                        prepend-icon="mdi-clock-time-four-outline"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-date-picker color="#4C4C65"
                      v-if="end_date_menu"
                      v-model="scheduleInfo.end_date"
                      :show-current="false"
                      @click:date="$refs.edmenu.save(scheduleInfo.end_date)"
                      :min="scheduleInfo.start_date + 1"
                    ></v-date-picker>
                  </v-menu>
                </v-col>
              </v-row>

              <v-row style="height:70px;">
                <v-col cols="4" >
                  <v-subheader class="workform">마감시간</v-subheader>
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
                        v-model="scheduleInfo.end_time"
                        placeholder="일정 마감 시간을 선택하세요."
                        prepend-icon="mdi-clock-time-four-outline"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-time-picker color="#4C4C65"
                      v-if="end_menu"
                      v-model="scheduleInfo.end_time"
                      :min="checkMin(scheduleInfo.start_date,scheduleInfo.end_date,scheduleInfo.start_time)"
                      @click:minute="$refs.emenu.save(scheduleInfo.end_time)"
                    ></v-time-picker>
                  </v-menu>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
          <v-card-actions class="pa-7 d-flex justify-center">
            <v-spacer></v-spacer>
            <v-spacer></v-spacer>
            <v-btn x-large color="#4c4c65" class="white--text" @click="dialog = false; updateSchedule(scheduleInfo);">확인</v-btn>
            <v-spacer></v-spacer>
            <v-btn x-large color="#FFFFFF" class="black--text" @click="dialog = false; updateSchedule(null);">취소</v-btn>
            <v-spacer></v-spacer>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </v-app>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'UpdateScheduleModal',
  data: () => ({
    stime: null,
    etime: null,
    start_menu: false,
    start_date_menu: false,
    end_date_menu: false,
    end_menu: false,
    dialog: true,
    scheduleInfo : {
    },
  }),
  computed: {
    ...mapState([
      'schedule',
    ])
  },
  methods: {
    ...mapActions([
      'detailSchedule',
      'updateSchedule'
    ]),
    checkMin(sdate, edate, stime){
      if(sdate == edate){
        return stime
      }
    },
    checkMax(sdate, edate, etime){
      if(sdate == edate){
          return etime;
      }
    }

  },
  created() {
    this.scheduleInfo = {
      id: this.schedule.id,
      title: this.schedule.name,
      detail: this.schedule.detail,
      start_date: this.schedule.start.split(' ')[0],
      start_time: this.schedule.start.split(' ')[1],
      end_date: this.schedule.end.split(' ')[0],
      end_time: this.schedule.end.split(' ')[1],
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