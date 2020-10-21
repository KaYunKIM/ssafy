<template>
	<v-app>
		<side-nav-bar></side-nav-bar>
		<div class = "container zpos">
      <div style="text-align: left">
        <v-sheet>
          <h1>할 일을 꼭 마칩시다!</h1>
          <hr>
          <div class="btn" @click="addSchedule()">
            <i class="far fa-calendar-plus plus"></i>
            <span class="ml-3"><strong>할 일 생성</strong></span>
          </div>
        </v-sheet>
      </div>
      <v-sheet
        tile
        height="54"
        color="white lighten-3"
        class="d-flex"
      >
        <div v-if="this.addScheduleModal"><AddScheduleModal/></div>
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
          @change="getEvents"
        ></v-calendar>
      </v-sheet>
		</div>
	</v-app>
</template>

<script>
import { mapActions, mapState } from 'vuex'

// Components
import SideNavBar from '@/components/SideNavBar'
import AddScheduleModal from '@/components/AddScheduleModal'


export default {
	name: 'schedule',
	components: {
    SideNavBar,
    AddScheduleModal
  },
	data: () => ({
    schedules: {},
    type: 'month',
    mode: 'stack',
    weekday: [0, 1, 2, 3, 4, 5, 6],
    value: '',
    events: [],
    colors: ['#393b44', '#8d93ab', '#d6e0f0', '#f1f3f8'],
    // names: ['Meeting', 'Holiday', 'PTO', 'Travel', 'Event', 'Birthday', 'Conference', 'Party'],
    modal: ''
  }),
  computed: {
    ...mapState([
      'addScheduleModal',
      'scheduleList'
    ])
  },
  methods: {
    ...mapActions([
      'addSchedule',
      'fetchScheduleList'
    ]),
    getDate(date) {
      return this.$moment(date).format('YYYY-MM-DD hh:mm')
    },
    getEvents () {
      const events = []

      for (var i = 0; i < this.schedules.length; i++) {
        events.push({
          name: this.schedules[i].title,
          start: this.getDate(this.schedules[i].start_time),
          end: this.getDate(this.schedules[i].end_time),
          color: '#8d93ab'
        })
      } 
      console.log(events)
      this.events = events
    },
    getEventColor (event) {
      return event.color
    },
    rnd (a, b) {
      return Math.floor((b - a + 1) * Math.random()) + a
    },
    getData(){
      for(var i = 0; i<this.scheduleList.length; i++){
        console.log(this.scheduleList[i])
      }
    }
  },
  created() {
    this.fetchScheduleList()
    this.schedules = this.scheduleList
  },
  mounted() {
    this.fetchScheduleList()
    this.schedules = this.scheduleList
    this.getEvents()
  }
}
</script>

<style>
.zpos {
  z-index: 0;
  width: 30%;
}
.plus {
  padding: 0 auto;
}
</style>
