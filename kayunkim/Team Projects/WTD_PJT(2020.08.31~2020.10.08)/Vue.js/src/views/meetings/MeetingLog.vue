<template>
<v-app>
<side-nav-bar></side-nav-bar>
<div class="meetinglog_background">

  <div class="maintitle">
      <h4>PJT. 자동 회의록 서비스 </h4>
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
            >5명</v-btn>  
          </template>
          <span>팀원</span>
        </v-tooltip>
      </template>
      <v-list class="team_member" >
        
        <v-list-tiem >
          Team Members
        </v-list-tiem>
        <v-list-item
          v-for="(item, index) in items"
          :key="index"
          style="background-color:#4c4c65"
        >
          <v-list-item-title style="color:white">{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </div>


<div class="project_list">
    <v-row justify="center">
    <v-expansion-panels accordion>
      <v-expansion-panel
        v-for="(item,i) in 1"
        :key="i"
      >
        <v-expansion-panel-header>2020-09-21</v-expansion-panel-header>
        <v-expansion-panel-content>
          
          <div class="project_detail">
             <v-card
              class="mx-auto"
            
            >
              <v-list>
               

                <v-list-group
                  value="false"
                >
                  <template v-slot:activator>
                     <v-icon large color="#4c4c65">mdi-message-text</v-icon>
                  <v-list-item-title>[SSAFY PJT3 오전 미팅] 09:00</v-list-item-title>
                  </template>
                  <v-chip class="ma-2" label>키워드1</v-chip>
                  <v-chip class="ma-2" label>키워드2</v-chip>
                  <v-chip class="ma-2" label>키워드3</v-chip>
                  <v-chip class="ma-2" label>키워드4</v-chip>
                  <div class="empty"></div>
                  <div class="meeting">
                    <div class="record">
                      <input type="file" ref="audio" id="audio" accept=".mp3,audio/*" @change="record()">
                      <button @click="upload_record()" class = "join-btn mt-2" placeholder="position">업로드</button>
                      <hr>
                    </div>
                    <div class="summary">
                      <h5>회의 개략 :)</h5>
                      <p>오늘 업무는 ~~위주로 할 예정입니다.</p>
                      <p> 000님은 꼭 오늘까지 xx업무 마감 부탁드립니다.</p>
                      <hr>
                    </div>
                    <div class="work row">
                      <div class="team">
                         <span>00팀 업무정보</span>
                         <div class="box">
                          <div class="team_work"><span>할 일1</span><br><span>담당: 김기훈</span></div>
                          <div class="team_work"><span>할 일2</span><br><span>담당: 김가윤</span></div>
                          <div class="team_work"><span>할 일3</span><br><span>담당: 김우희</span></div>
                          <div class="team_work"><span>할 일4</span><br><span>담당: 오우승</span></div>
                          <div class="team_work"><span>할 일5</span><br><span>담당: 임효진</span></div>
                         </div>
                      </div> 
                      <div class="personal">
                         <span>팀원별 업무 정보</span>
                         <progress class="col" value="30" max="100"></progress>
                         <progress class="col" value="77" max="100"></progress>
                         <progress class="col" value="50" max="100"></progress>
                         <progress class="col" value="60" max="100"></progress>
                         <progress class="col" value="90" max="100"></progress>
                      </div>
                    </div>
                      
           
                  </div>
                </v-list-group>

                 <v-list-group
                  value="false"
                >
                  <template v-slot:activator>
                     <v-icon large color="#4c4c65">mdi-message-text</v-icon>
                  <v-list-item-title>[SSAFY PJT3 오후 미팅] 13:00</v-list-item-title>
                  </template>
                  <v-chip class="ma-2" label>키워드1</v-chip>
                  <v-chip class="ma-2" label>키워드2</v-chip>
                  <v-chip class="ma-2" label>키워드3</v-chip>
                  <v-chip class="ma-2" label>키워드4</v-chip>
                </v-list-group>
                 <v-list-group
                  value="false"
                >
                  <template v-slot:activator>
                     <v-icon large color="#4c4c65">mdi-message-text</v-icon>
                  <v-list-item-title>[SSAFY PJT3 종례 미팅] 17:00</v-list-item-title>
                  </template>
                  <v-chip class="ma-2" label>키워드1</v-chip>
                  <v-chip class="ma-2" label>키워드2</v-chip>
                  <v-chip class="ma-2" label>키워드3</v-chip>
                  <v-chip class="ma-2" label>키워드4</v-chip>
                </v-list-group>

              </v-list>
            </v-card>
          </div>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </v-row>
  </div>

</div>
</v-app>
</template>

<script>
import SideNavBar from '@/components/SideNavBar'
import {mapActions} from 'vuex'
import axios from 'axios'

  export default {
    components: {SideNavBar},
    data: () => ({
      audio: '',
      projectname: [0, 1],
      disabled: false,
      readonly: false,
      items: [
        
        { title: '김가윤' },
        { title: '김기훈' },
        { title: '김우희' },
        { title: '오우승' },
        { title: '임효진' },
      ],
    }),
    methods: {
      record(){
        this.audio = this.$refs.audio[0].files[0]
        console.log(this.audio)
        console.log(this.audio['name'])
        console.log(this.audio['size'])
      },
      upload_record(){
        const fd = new FormData()
        fd.append('name', this.audio['name'])
        fd.append('audio', this.audio)
        //http://localhost:8000
        axios.post('http://j3a511.p.ssafy.io:8000' + '/projects/audio/', fd, {headers: { "content-type": "multipart/form-data" }})
        .then((res) => {
          if(res.data === '0'){
            console.log("No Valid")
          }
          else{
            console.log("Success")
            var audioName = this.audio['name']
            this.uploadAudio(audioName)
          }
        })
        .catch(function(){
          console.log('Error');
        });

      },
      ...mapActions([
        'uploadAudio'
      ]),
    },
  }
</script>

<style>
.meetinglog_background{
  background-color : white;
 
}
.project_detail{
  width: 100%;
}
.project_list{
  margin : 0 auto;
  padding : 0 auto;
  width: 50%;

}
.team_member{
  width: 150px;
  text-align: center;
  color:white;
}
.member_list{
  position : relative;
  margin-right:15px;
  float : right;
}
.maintitle{
  margin-top:30px;
  margin-left:20px;
}
.record{
  text-align: left;
  margin-left: 15px;
}
.start_record, .upload_record{
  margin-left: 50px;
}

.record_img{
  height: 26px;
  width: 26px;
}
.start_record, .upload_record{
  height: 32px;
  font-size: 13px;
  background-color: #4C4C65;
  color: white;
  border-radius: 5px;
}
.start_record{
  width: 13%;
}
.upload_record{
  width: 18%;
}
.summary{
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
.summary > p{
   text-align: left;
   white-space: pre-line;
   margin-left: 15px;
   font-size: 14px;
}
.team, .personal{
  margin-left: 43px;
  font-size : 19px;
  font-weight: bold;
}
.team > span {
  margin-left: -113px;
}
.team > .box {
  width: 245px;
  height: 500px;
  background-color: #DFDCE6;
}
.personal > span{
  margin-left: -10%;
}
.personal > progress {
  margin-left: 18%;
  margin-top: 73px;
} 
.team_work{
  width: 200px;
  height: 90px;
  background-color: white;
  color: black;
  font-size: 15px;
  margin-left: 20px;
  margin-top: 10px;
}
</style>