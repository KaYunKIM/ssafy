<template>
  <v-app>
    <side-nav-bar></side-nav-bar>
    <div class="meetinglog_background">
      <div class="maintitle">
        <h4>PJT. 자동 회의록 서비스</h4>
      </div>
      <div class="btn" @click="addMeetingLog()">
        <i class="fas fa-folder-plus plus"></i>
        <span class="ml-3"><strong>미팅 생성</strong></span>
      </div>
      <div class="member_list">
        <v-btn @click="back()">back</v-btn>
      </div>
      <div class="member_list">
        <v-menu>
          <template v-slot:activator="{ on: menu, attrs }">
            <v-tooltip bottom>
              <template v-slot:activator="{ on: tooltip }">
                <v-btn
                  color="#4c4c65"
                  dark
                  v-bind="attrs"
                  v-on="{ ...tooltip, ...menu }"
                  >{{ items.length }}명</v-btn
                >
              </template>
              <span>팀원</span>
            </v-tooltip>
          </template>
          <v-list class="team_member">
            <v-list-item> Team Members </v-list-item>
            <v-list-item
              v-for="(item, index) in items"
              :key="index"
              style="background-color: #4c4c65"
            >
              <v-list-item-title style="color: white"
                ><button
                  v-on:click="onToDoDetail($route.params.projectId, item.title)"
                >
                  {{ item.title }}
                </button></v-list-item-title
              >
            </v-list-item>
          </v-list>
        </v-menu>
      </div>

      <div class="project_list">
        <v-row justify="center">
          <h4>{{ $store.state.projectDate }}</h4>
          <v-expansion-panels popout>
            <v-expansion-panel v-for="(item2, idx) in meetingDetail.meetingList" :key="idx">
              <v-expansion-panel-header style="background-color: #dfdce6">
                <v-container style="text-align: left">
                  <v-layout column>
                    <v-flex class="ml-3 mb-3" style="display: inline-flex">
                      <v-icon class="mr-2" medium color="#4c4c65"
                        >mdi-message-text</v-icon
                      >
                      <v-flex style="display: inline-flex">
                        <v-list-item-title
                          style="font-size: 18px; color: #4c4c65"
                          >{{ item2.title }}</v-list-item-title
                        >
                      </v-flex>
                      <v-flex xs12 offset-xs1 align-end>
                        <!-- <v-btn @click="updateMeetingTemp(item)" small class="mr-3" color="#DFDCE6" style="outline:none"> -->
                        <v-icon
                          @click="updateMeetingTemp(item2)"
                          small
                          class="mr-3"
                          color="black"
                          dark
                          >mdi-pencil</v-icon
                        >
                        <!-- </v-btn> -->
                        <!-- <v-btn @click="deleteMeeting(item.id)" small color="#DFDCE6"> -->
                        <v-icon
                          @click="deleteMeeting(item2.id)"
                          small
                          color="black"
                          dark
                          >mdi-trash-can</v-icon
                        >
                        <!-- </v-btn> -->
                      </v-flex>
                    </v-flex>
                    <v-flex>
                      <v-sheet style="background-color: #dfdce6">
                        <li
                          style="display: inline-block"
                          v-for="(keyword, idx2) in meetingDetail.meetingList[idx].keyword"
                          :key="idx2"
                        >
                          <v-chip
                            class="ma-2"
                            filter
                            color="#4C4C65"
                            text-color="#ffffff"
                            >{{ keyword }}</v-chip
                          >
                        </li>
                      </v-sheet>
                    </v-flex>
                  </v-layout>
                </v-container>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <div class="empty"></div>
                <div class="meeting">
                  <div class="record" v-show="item2.summary == null">
                    <Speech :meetingId="item2.id" />
                    <!-- <input
                      type="file"
                      ref="audio"
                      id="audio"
                      accept=".mp3,audio/*"
                      @change="record(idx)"
                    />
                    <button
                      @click="upload_record(item2.id)"
                      class="join-btn mt-2"
                      placeholder="position"
                    >
                      업로드
                    </button>
                    <hr />
                  </div>
                  <div v-show="item2.summary != null">
                    <div class="summary">
                      <h5>회의 개략 :)</h5>
                      <p>{{ item2.summary }}</p>
                      <hr />
                    </div>
                     <div class="work row"> -->
                    
                    <div>
                      <v-responsive max-width="400" class="mx-auto mb-4">
                      </v-responsive>

                      <h4>업무 리스트</h4>
                      <div v-show="taskDetail[idx] == null">없습니다.</div>
                      <div v-show="taskDetail[idx] != null">
                      <v-card elevation="16" max-width="400" class="mx-auto">
                        <v-virtual-scroll
                          :items="taskDetail[idx]"
                          height="300"
                          item-height="110"
                        >
                          <template v-slot:default="{ item }">
                            <v-list-item >
                              <v-list-item-content>
                                <v-list-item-title                                 
                                  @click="showTaskDetail(item)"
                                >
                                  <strong>{{ item.title }}</strong
                                  ><br />
                                  <br>
                                  <strong>담당자 : {{ item.manager }}</strong>
                                </v-list-item-title>
                              </v-list-item-content>
                            </v-list-item>

                            <v-divider></v-divider>
                          </template>
                        </v-virtual-scroll>
                      </v-card>
                      <br>

                      <div class="personal">
                         <!-- <span>팀원 업무 진행도</span><br> -->
                         <li
                          v-for="(managerTask, idx3) in managerDetail[idx]"
                          :key="idx3"
                          >
                          <div>
                            <span>{{managerTask.nickname}}</span>
                            <v-progress-linear
                              :value="Math.ceil(managerTask.acheivement)"
                              color="#4c4c65"
                              height="25"
                              
                            >
                              <template v-slot:default="{ value }">
                                <strong>{{ value }}%</strong>
                              </template>
                            </v-progress-linear>
                            <br>
                          </div>
                          </li>
                      </div>
                      </div>
                    </div>
                    <!-- <div class="team">
                  <span>업무 리스트</span>
                  <div class="box">
                    <div v-for="(task, index) in taskDetail" :key=index>
                      <div class="team_work pt-1 pb-1" v-show="item.id == task.meeting.id" @click="showTaskDetail(task)">
                        <center>[업무내용]</center>
                        <br>{{task.title}}
                      </div>
                    </div>
                  </div>
                </div>  -->
                    <!-- </div> -->
                  </div>
                </div>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-row>
      </div>
      <div v-if="this.updateMeetingLogModal"><UpdateMeetingLogModal /></div>
      <div v-if="this.addMeetingLogModal"><AddMeetingLogModal /></div>
      <div v-if="this.modalWorkDetail"><TaskDetailModal /></div>
    </div>
  </v-app>
</template>

<script>
import SideNavBar from "@/components/SideNavBar";
import { mapActions, mapState } from "vuex";
import AddMeetingLogModal from "@/components/AddMeetingLogModal";
import UpdateMeetingLogModal from "@/components/UpdateMeetingLogModal";
import TaskDetailModal from "@/components/TaskDetailModal";
import Speech from '@/components/Speech';
import axios from "axios";

export default {
  name: "MeetingLog",
  components: {
    SideNavBar,
    AddMeetingLogModal,
    UpdateMeetingLogModal,
    TaskDetailModal,
    Speech,
  },
  data: () => ({
    audio: "",
    audio2: "",
    title: "",
    disabled: false,
    readonly: false,
    items: [],
    meetingDetail: {},
    taskDetail: [],
    managerDetail: [],
    // meetingDetail : [
    //   title: '',
    //   time: '',
    //   origin_text: null,
    //   summary: null,
    //   keywords : [

    //   ]
    // ]
    taskList: {},
  }),
  computed: {
    ...mapState([
      "memberList",
      "meetingInfoStatus",
      "addMeetingLogModal",
      "meetingList",
      "taskInfo",
      "updateMeetingLogModal",
      "modalWorkDetail",
    ]),
  },
  methods: {
    record(idx) {
      this.audio = this.$refs.audio[idx].files[0];
      // console.log(this.audio);
      // console.log(this.audio["name"]);
      // console.log(this.audio["size"]);
    },
    upload_record(meeting_id) {
      //console.log(meeting_id);
      const fd = new FormData();
      fd.append("name", this.audio["name"]);
      fd.append("audio", this.audio);
      //http://j3a511.p.ssafy.io:8000
      axios
        .post("http://localhost:8000" + "/projects/audio/", fd, {
          headers: { "content-type": "multipart/form-data" },
        })
        .then((res) => {
          if (res.data === "0") {
            console.log("No Valid");
          } else {
            console.log("Success");
            var audioName = res.data;
            const uploadData = {
              audioName: audioName,
              meetingId: meeting_id,
            };
            this.uploadAudio(uploadData);
          }
        })
        .catch(function () {
          console.log("Error");
        });
    },
    onToDoDetail(projectId, userId) {
      this.$router.push({name: 'MemberToDo', params: {userId: userId, projectId: projectId}});
    },
    back() {
      this.$router.go(-1);
    },
    ...mapActions([
      "uploadAudio",
      "addMeetingLog",
      "fetchMemberList",
      "fetchMeetingList",
      "fetchTaskInfo",
      "updateMeetingTemp",
      "deleteMeeting",
      "showTaskDetail",
    ]),
  },
  watch: {
    // 미팅리스트가 변화하면 meetingDetail에 다시 재저장
    meetingList() {
      //console.log("watch order1");
      this.meetingDetail = this.meetingList;
      // console.log(2,meetingDetail)
    },
    meetingInfoStatus() {
      this.fetchMeetingList(this.$store.state.projectDate).then(() => {
        //console.log("watch order2");
        this.meetingDetail = this.meetingList;
        // console.log(1,meetingDetail)
      });
    },
    taskInfo() {
      //console.log("watch order3");
      this.taskList = this.taskInfo;
      // let taskMap = new Map()
      // var counter = 0;
      this.taskDetail = []
      for(var i = 0; i < this.meetingList.length; i++){
        const id = this.meetingList[i].id
        const tmp_list = []
        for(var j = 0; j < this.taskList.length; j++){
          if(this.taskList[j].meeting.id == id){
            tmp_list.push(this.taskList[j])
          } 
        }
        this.taskDetail.push(tmp_list)
      }
      console.log("TaskDetail Data")
      console.log(this.taskDetail)

      this.managerDetail = []
      for(var meet=0; meet<this.meetingList.length; meet++){
        const tmp_list2 = []
        for(var i1 = 0; i1 < this.memberList.length; i1++){
          const nickname = this.memberList[i1].user.nickname
          var cnt_total = 0;
          var cnt_progress = 0;
          var cnt_complete = 0;
          for(var j1 = 0; j1 < this.taskDetail[meet].length; j1++){
            if(this.taskDetail[meet][j1].manager == nickname){
              if(this.taskDetail[meet][j1].completed) cnt_complete++;
              else cnt_progress++;
              cnt_total++
            } 
          }
          var acheivement = (cnt_complete / cnt_total) * 100
          if(isNaN(acheivement)) acheivement = 0
          tmp_list2.push({nickname : nickname , cnt_total : cnt_total , cnt_progress : cnt_progress , cnt_complete : cnt_complete,
          acheivement: acheivement})
        }
        this.managerDetail.push(tmp_list2)
      }
      console.log("ManagerDetail Data")
      console.log(this.managerDetail)
    },
  },
  created() {
    // for(var i=0; i < this.meetingList.size(); i++){
    // 	this.meetingDetail.push(this.meetingList[i])
    // }
    this.meetingDetail = this.meetingList;
    // Team Members
    this.fetchMemberList(this.$route.params.projectId).then(() => {
      console.log("MemberList Data")
      console.log(this.memberList);
      const members = this.memberList;
      for (var i in members) {
        this.items.push({ title: members[i]["user"]["nickname"] });
      }
    });

    this.fetchTaskInfo()
      .then(() => {})
      .catch(() => {});
    // for (i in this.projectList) {
    //   if this.projectList[i][]
    // }

    // console.log(this.taskInfo)
    // console.log(this.meetingDetail)
  },
};
</script>

<style>
.meetinglog_background {
  background-color: white;
}
.project_detail {
  width: 100%;
}
.project_list {
  margin: 0 auto;
  padding: 0 auto;
  width: 50%;
}
.team_member {
  width: 150px;
  text-align: center;
  color: white;
}
.member_list {
  position: relative;
  margin-right: 15px;
  float: right;
}
.maintitle {
  margin-top: 30px;
  margin-left: 20px;
}
.record {
  text-align: left;
  margin-left: 15px;
}
.start_record,
.upload_record {
  margin-left: 50px;
}

.record_img {
  height: 26px;
  width: 26px;
}
.start_record,
.upload_record {
  height: 32px;
  font-size: 13px;
  background-color: #4c4c65;
  color: white;
  border-radius: 5px;
}
.start_record {
  width: 13%;
}
.upload_record {
  width: 18%;
}
.summary {
  color: black;
}
.summary > h5 {
  font-weight: bold;
  text-align: left;
  margin-left: 15px;
}

.work {
  font-size: 14px;
  color: black;
}
.summary > p {
  text-align: left;
  white-space: pre-line;
  margin-left: 15px;
  font-size: 14px;
}
.team,
.personal {
  margin-left: 43px;
  font-size: 19px;
  font-weight: bold;
}
.team > span {
  margin-left: -113px;
}
.team > .box {
  width: 245px;
  height: 500px;
  background-color: #dfdce6;
}
.personal > span {
  margin-left: -10%;
}
.personal > progress {
  margin-left: 18%;
  margin-top: 73px;
}
.team_work {
  width: 200px;
  height: 90px;
  background-color: white;
  color: black;
  font-size: 15px;
  margin-left: 20px;
  margin-top: 10px;
}
</style>
