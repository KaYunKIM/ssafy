<template>
	<v-app>
		<side-nav-bar></side-nav-bar>
		<div class = "container zpos">
      <div class="back_btn">
        <v-btn @click="back()">back</v-btn>
      </div>
      <div style="text-align: left">
        <v-sheet>
          <h1>{{ projectName }}</h1>
          <hr>
        </v-sheet>
      </div>
      <v-sheet
        tile
        height="54"
        color="white lighten-3"
        class="d-flex"
      >
        <v-btn
          icon
          class="ma-2"
          @click="$refs.calendar.prev()"
        >
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
        <v-spacer></v-spacer>
        <v-toolbar-title v-if="$refs.calendar">
              {{ $refs.calendar.title }}
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn
          icon
          class="ma-2"
          @click="$refs.calendar.next()"
        >
          <v-icon>mdi-chevron-right</v-icon>
        </v-btn>
      </v-sheet>
      <v-sheet height="600">
        <v-calendar
          ref="calendar"
          v-model="value"
          :weekdays="weekday"
          :type="type"
          :events="events"
          :event-overlap-mode="mode"
          :event-overlap-threshold="30"
          :event-color="getEventColor"
          @click:date="addProjectDate"
          @change="getEvents"
          @click:event="showWorkDetail"
        ></v-calendar>
     <div v-if="this.modalWorkDetail"><WorkDetailModal/></div>
      </v-sheet>
		</div>
	</v-app>
</template>

<script>
// Components
import SideNavBar from '@/components/SideNavBar'
import WorkDetailModal from '@/components/WorkDetailModal'
import { mapActions, mapState } from 'vuex'

export default {
	name: 'projectDetail',
	components: {
    SideNavBar,
    WorkDetailModal,
  },
	data: () => ({
    projectName: '특화 프로젝트',
    type: 'week',
    mode: 'column',
    weekday: [1, 2, 3, 4, 5, 6, 0],
    value: '',
    tasks : [],
    // tasks2 : [ {title : "title1",
    //   start_time : "2020-10-22T07:10",
    //   end_time : "2020-10-22T12:10",
    //   manager : "김기훈이",
    //   meeting : 1,
    //   detail : "이것은 디테일입니다.",
    //   completed : true},
    //   {title : "title2",
    //   start_time : "2020-10-23T16:10",
    //   end_time : "2020-10-23T19:10",
    //   manager : "지린이",
    //   meeting : 1,
    //   detail : null,
    //   completed : false}],
    events: [],
    colors: ['blue', 'indigo', 'deep-purple', 'cyan', 'green', 'orange', 'grey darken-1'],
    // names: ['Meeting', 'Holiday', 'PTO', 'Travel', 'Event', 'Birthday', 'Conference', 'Party'],
  }),
  computed:{
    ...mapState([
      'modalWorkDetail',
      'taskList',
      'projectId',
    ])
  },
  methods: {
    getDate(date) {
      return this.$moment(date).format('YYYY-MM-DD HH:mm')
    },
    ...mapActions([
      'setProjectId',
      'addProjectDate',
      'fetchTaskList',
      'showWorkDetail',
      'fetchTaskList'
    ]),
    getEvents () {
      const events = []

      for(var i=0;i<this.tasks.length; i++){
        events.push({
          name: this.tasks[i].title,
          start: this.getDate(this.tasks[i].start_time),
          end: this.getDate(this.tasks[i].end_time),
          meeting : this.tasks[i].meeting,
          detail : this.tasks[i].detail,
          completed : this.tasks[i].completed,
          manager : this.tasks[i].manager,
          color: '#8d93ab',
          id : this.tasks[i].id
        })
      }
      this.events = events
    },
    getEventColor (event) {
      return event.color
    },
    back(){
      this.$router.go(-1);
    },
  },
  watch: {
    taskList() {
      this.tasks = this.taskList
      this.getEvents()
      console.log(this.tasks)
    },
  },
  mounted() {
    this.fetchTaskList(this.$route.params.projectId)
    this.tasks = this.taskList
    this.getEvents()
  },
  created() {
    this.setProjectId((this.$route.params.projectId))
  }
}
</script>

<style>
.back_btn{
  position : relative;
  margin-right:30px;
  float : right;
}
</style>