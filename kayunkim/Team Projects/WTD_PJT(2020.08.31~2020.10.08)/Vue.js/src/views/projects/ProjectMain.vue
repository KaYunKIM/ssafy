<template>
	<v-app>
		<side-nav-bar></side-nav-bar>
		<div class = "container zpos">
      <div style="text-align: left">
        <v-sheet>
          <h1>{{ projectName }}</h1>
          <hr>
          <div class="btn" @click="addMeetingLog()">
            <i class="fas fa-folder-plus plus"></i>
            <span class="ml-3"><strong>미팅 생성</strong></span>
          </div>
        </v-sheet>
      </div>
      <v-sheet
        tile
        height="54"
        color="white lighten-3"
        class="d-flex"
      >
        <div v-if="this.addMeetingLogModal"><AddMeetingLogModal/></div>
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
// Components
import SideNavBar from '@/components/SideNavBar'
import AddMeetingLogModal from '@/components/AddMeetingLogModal'
import { mapActions, mapState } from 'vuex'

export default {
	name: 'projectPlan',
	components: {
    SideNavBar,
    AddMeetingLogModal
  },
	data: () => ({
    projectName: '특화 프로젝트',
    type: 'week',
    mode: 'column',
    weekday: [1, 2, 3, 4, 5, 6, 0],
    value: '',
    events: [],
    colors: ['blue', 'indigo', 'deep-purple', 'cyan', 'green', 'orange', 'grey darken-1'],
    names: ['Meeting', 'Holiday', 'PTO', 'Travel', 'Event', 'Birthday', 'Conference', 'Party'],
  }),
  computed:{
    ...mapState([
      'addMeetingLogModal',
    ])
  },
  methods: {
    ...mapActions([
      'addMeetingLog'
    ]),
    getEvents ({ start, end }) {
      const events = []

      const min = new Date(`${start.date}T00:00:00`)
      const max = new Date(`${end.date}T23:59:59`)
      const days = (max.getTime() - min.getTime()) / 86400000
      const eventCount = this.rnd(days, days + 20)

      for (let i = 0; i < eventCount; i++) {
        const allDay = this.rnd(0, 3) === 0
        const firstTimestamp = this.rnd(min.getTime(), max.getTime())
        const first = new Date(firstTimestamp - (firstTimestamp % 900000))
        const secondTimestamp = this.rnd(2, allDay ? 288 : 8) * 900000
        const second = new Date(first.getTime() + secondTimestamp)

        events.push({
          name: this.names[this.rnd(0, this.names.length - 1)],
          start: first,
          end: second,
          color: this.colors[this.rnd(0, this.colors.length - 1)],
          timed: !allDay,
        })
      }

      this.events = events
    },
    getEventColor (event) {
      return event.color
    },
    rnd (a, b) {
      return Math.floor((b - a + 1) * Math.random()) + a
    },
    addMeeting (){
      alert("모달창 띄우기")
    },
  },
}
</script>

<style>

</style>
