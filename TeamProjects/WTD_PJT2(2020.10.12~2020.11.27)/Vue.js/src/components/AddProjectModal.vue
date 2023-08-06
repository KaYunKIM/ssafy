<template>
  <v-app>
    <v-row justify="center">
      <v-dialog v-model="dialog" persistent max-width="900px" >
        <v-card color="#dfdce6" class="mx-lg-auto rounded-lg">
          <v-card-title class="pa-7 d-flex justify-center">
          <span style="font-weight:bold; color:#4c4c65;font-size: x-large;">Create Your Awesome Project</span>
          </v-card-title>

          <v-container>
            <div align="center">
              <v-col class="p-0" cols="12" sm="7">
                <v-text-field
                  v-model="projectInfo.title"
                  label="Project Name"
                  placeholder="세상을 바꿀 위대한 프로젝트"
                  outlined
                ></v-text-field>
              </v-col>
            
              <v-col class="p-0" cols="12" sm="7">
                <v-menu
                  v-model="menu"
                  :close-on-content-click="false"
                  :nudge-right="40"
                  transition="scale-transition"
                  offset-y
                  min-width="290px"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="projectInfo.deadline"
                      label="Deadline"
                      placeholder="이 날짜에는 반드시 끝내자"
                      readonly
                      v-bind="attrs"
                      v-on="on"
                      outlined
                    ></v-text-field>
                  </template>
                  <v-date-picker 
                  v-model="projectInfo.deadline" 
                  color="#4C4C65"
                  :min="checktoday()" 
                  @input="menu = false"
                  ></v-date-picker>
                </v-menu>
              </v-col>
              <v-spacer></v-spacer>

              <v-col class="p-0" cols="12" sm="7">
                <!-- <v-select
                  v-model="projectInfo.leader"
                  class="addProjectFont"
                  :items="userList"
                  chips
                  label="Team Leader"
                  placeholder="우리팀을 이끌 능력자 팀장님은?"
                  outlined
                ></v-select> -->
                
                <v-autocomplete
                  v-model="leader"
                  :disabled="isUpdating"
                  :items="userList"
                  filled
                  chips
                  label="Team Leader"
                  outlined
                >
                  <template v-slot:selection="data">
                    <v-chip
                      v-bind="data.attrs"
                      :input-value="data.selected"
                      close
                      @click="data.select; addMember(data.select, leader);"
                      @click:close="remove(data.item)"
                    >

                      <!-- profile img 삽입 -->
                      <!-- <v-avatar left>
                        <v-img :src="data.item.avatar"></v-img>
                      </v-avatar> -->

                      {{ data.item }}
                    </v-chip>
                  </template>
                  <template v-slot:item="data">
                    <template v-if="typeof data.item !== 'object'">
                      <v-list-item-content v-text="data.item"></v-list-item-content>
                    </template>
                    <template v-else>

                    <!-- profile img 삽입 -->
                    <!-- <v-list-item-avatar>
                      <img :src="data.item.avatar">
                    </v-list-item-avatar> -->

                    <v-list-item-content>
                      <v-list-item-title v-html="data.item"></v-list-item-title>
                    </v-list-item-content>
                    </template>
                  </template>
                </v-autocomplete>
              </v-col>
    
              <v-col class="p-0" cols="12" sm="7">
                <!-- <v-select
                  v-model="projectInfo.recording"
                  class="addProjectFont"
                  :items="userList"
                  chips
                  label="Recording Manager"
                  placeholder="팀 회의 녹음 담당자님은?"
                  outlined
                >
                </v-select> -->

                <v-autocomplete
                  v-model="recorder"
                  :disabled="isUpdating"
                  :items="userList"
                  filled
                  chips
                  label="Recording Manager"
                  outlined
                >
                  <template v-slot:selection="data">
                    <v-chip
                      v-bind="data.attrs"
                      :input-value="data.selected"
                      close
                      @click="data.select; addMember(data.select, recorder);"
                      @click:close="remove(data.item)"
                    >
                      <!-- profile img 삽입 -->
                      <!-- <v-avatar left>
                        <v-img :src="data.item.avatar"></v-img>
                      </v-avatar> -->

                      {{ data.item }}
                    </v-chip>
                  </template>
                  <template v-slot:item="data">
                    <template v-if="typeof data.item !== 'object'">
                      <v-list-item-content v-text="data.item"></v-list-item-content>
                    </template>
                    <template v-else>

                    <!-- profile img 삽입 -->
                    <!-- <v-list-item-avatar>
                      <img :src="data.item.avatar">
                    </v-list-item-avatar> -->

                    <v-list-item-content>
                      <v-list-item-title v-html="data.item"></v-list-item-title>
                    </v-list-item-content>
                    </template>
                  </template>
                </v-autocomplete>
              </v-col>

              <v-col class="p-0" cols="12" sm="7">
                <v-autocomplete
                  v-model="memberList"
                  :disabled="isUpdating"
                  :items="userList"
                  filled
                  chips
                  multiple
                  label="Team Member"
                  outlined
                >
                  <template v-slot:selection="data">
                    <v-chip
                      v-bind="data.attrs"
                      :input-value="data.selected"
                      close
                      @click="data.select"
                      @click:close="remove(data.item)"
                    >
                      <!-- profile img 삽입 -->
                      <!-- <v-avatar left>
                        <v-img :src="data.item.avatar"></v-img>
                      </v-avatar> -->

                      {{ data.item }}
                    </v-chip>
                  </template>
                  <template v-slot:item="data">
                    <template v-if="typeof data.item !== 'object'">
                      <v-list-item-content v-text="data.item"></v-list-item-content>
                    </template>
                    <template v-else>

                    <!-- profile img 삽입 -->
                    <!-- <v-list-item-avatar>
                      <img :src="data.item.avatar">
                    </v-list-item-avatar> -->

                    <v-list-item-content>
                      <v-list-item-title v-html="data.item"></v-list-item-title>
                    </v-list-item-content>
                    </template>
                  </template>
                </v-autocomplete>
              </v-col>

            </div>
              <div>
                <v-btn large color="#4c4c65" class="white--text m-2" @click="dialog = false; addMember(memberList)">확인</v-btn>
                <v-btn large color="#FFFFFF" class="black--text m-2" @click="dialog = false; addProject()">취소</v-btn>
              </div>
            <v-spacer></v-spacer>
          </v-container>
        </v-card>
      </v-dialog>
    </v-row>
  </v-app>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'AddProjectModal',
  data: () => ({
    dialog: true,
    menu: false,
    userList: [],
    leader: null,
    recorder: null,
    memberList: [],
    projectInfo: {
      title: null,
      deadline: '',
      // deadline: new Date().toISOString().substr(0, 10),   #오늘날짜설정
      members: [],
    },
    autoUpdate: true,
    isUpdating: false,
    
  }),
  computed: {
    ...mapState([
      'addProjectModal',
      'userNicknameList',
      'userData'
    ]),
  },
  methods: {
    ...mapActions([
      'fetchUserList',
      'addProject'
    ]),
     checktoday(){
      let today = new Date();   
      let year = today.getFullYear(); // 년도
      let month = today.getMonth() + 1;  // 월
      let date = today.getDate();  // 날짜
      if (date < 10){ // 날짜가 한자리면 0 붙여주기
        date = ('0' + date)
      }
      let todaydate = (year + '-' + month + '-' + date)
      return todaydate
    },

    remove(item) {
      const index = this.userList.indexOf(item)
      if (index >= 0) this.userList.splice(index, 1)
    },
    addMember(memberList) {
      this.projectInfo.members.push({ "nickname" : this.leader, "role": "leader" })
      this.projectInfo.members.push({ "nickname" : this.recorder, "role": "recorder" })
      memberList.map((member) => {
        this.projectInfo.members.push({ "nickname" : member })
      })
      
      for(var i=0; i<this.projectInfo.members.length;i++){
        if(this.projectInfo.members[i].nickname == this.userData.nickname){
          this.addProject(this.projectInfo)
          return
        }
      }
      alert('본인의 역할을 포함시켜 주세요')
      return
    },
  },
  watch: {
    isUpdating(val) {
      if (val) {
        setTimeout(() => (this.isUpdating = false), 3000)
      }
    },
  },
  created() {
    this.fetchUserList()
    this.userList = this.userNicknameList
  }
}
</script>

<style>
.submit-btn{
  border: none;
  background-color: #4C4C65;
  color: white;
  border-radius: 30px;
  width:10%;
  padding: 5px;
  margin: 5px;
}
.cancel-btn{
  border: none;
  background-color: #DFDCE6;
  color: #4C4C65; 
  border-radius: 30px;
  width: 10%;
  padding: 5px;
  margin: 5px;
}
.addProjectFont{
  font-weight: bold;
  color: white;
}
.addProjectTextField{
  font-weight: bold;
  background-color: #DFDCE6;
}
</style>