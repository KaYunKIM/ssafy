<template>
  <v-app>
    <v-row justify="center">
      <v-dialog v-model="dialog" max-width="900px" >
        <v-card color="#dfdce6" class="mx-lg-auto rounded-lg">
          <v-card-title class="pa-7 d-flex justify-center">
          <span style="font-weight:bold; color:#4c4c65;font-size: x-large;">Create Your Awesome Project</span>
          </v-card-title>

          <v-container>
            <div align="center">

            <v-col class="p-0" cols="12" sm="7">
            <v-text-field
              v-model="projectInfo.name"
              class="addProjectFont"
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
                v-model="projectInfo.date"
                label="Deadline"
                placeholder="이 날짜에는 반드시 끝내자"
                readonly
                v-bind="attrs"
                v-on="on"
                outlined
              ></v-text-field>
            </template>
            <v-date-picker v-model="projectInfo.date" color="#4C4C65" @input="menu = false"></v-date-picker>
            </v-menu>
            </v-col>
            <v-spacer></v-spacer>

            <v-col class="p-0" cols="12" sm="7">
              <v-select
                v-model="projectInfo.leader"
                class="addProjectFont"
                :items="items"
                chips
                label="Team Leader"
                placeholder="우리팀을 이끌 능력자 팀장님은?"
                outlined
              ></v-select>
            </v-col>
    
            <v-col class="p-0" cols="12" sm="7">
              <v-select
                v-model="projectInfo.recording"
                class="addProjectFont"
                :items="items"
                chips
                label="Recording Manager"
                placeholder="팀 회의 녹음 담당자님은?"
                outlined
              ></v-select>
            </v-col>

            <v-col class="p-0" cols="12" sm="7">
              <v-select
                class="addProjectFont"
                v-model="projectInfo.member"
                :items="items"
                chips
                label="Team Member"
                placeholder="함께 세상을 바꿀 어벤져스 멤버들은 누군가요?"
                multiple
                outlined
                clearable
              >
              <!-- <template v-slot:selection="data">
                <v-chip 
                  :selected="data.selected"
                  close
                  :color="getColor(data.item)"
                  @input="remove(data.item)">
                  <strong>{{ data.item }}</strong>&nbsp;
                </v-chip>
              </template> -->
              </v-select>
            </v-col>
            </div>

            <div>
              <v-btn large color="#4c4c65" class="white--text m-2" @click="dialog = false; addProject(ProjectInfo)">확인</v-btn>
              <v-btn large color="#FFFFFF" class="black--text m-2" @click="dialog = false; addProject('0')">취소</v-btn>
            </div>
            <div class="empty"></div>
          </v-container>
        </v-card>
      </v-dialog>
    </v-row>
  </v-app>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'AddProjectModal',
  data: () => ({
    dialog: true,
    menu: false,
    items: ['member1', 'member2', 'member3', 'member4'],
    projectInfo : {
      name: null,
      date: new Date().toISOString().substr(0, 10),
      leader: null,
      recording: null,
      member: [],
    },
  }),
  methods: {
    ...mapActions([
      'addProject' 
    ]),
  },
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
}
</style>
