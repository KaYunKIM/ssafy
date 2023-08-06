<template>
	<v-app>
		<side-nav-bar></side-nav-bar>
		<div class = "container zpos">
      <div style="text-align: left">
        <v-sheet>
          <h1>할 일을 꼭 마칩시다!</h1>
          <hr>
          <div class="btn" @click="addSchedule(0)">
            <i class="far fa-calendar-plus plus"></i>
            <span class="ml-3"><strong>할 일 생성</strong></span>
          </div>
        </v-sheet>
      </div>
      <div>
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
      <v-sheet height="750">
        <v-calendar
          ref="calendar"
          v-model="value"
          :weekdays="weekday"
          :type="type"
          :events="events"
          :event-overlap-mode="mode"
          :event-overlap-threshold="10"
          :event-color="getEventColor"
          :event-height="22"
          :event-margin-bottom="2"
          @change="getEvents"
          @mouseenter:event="showEvent"
          @click:date="viewDay"
        ></v-calendar>
        <v-menu
          v-model="selectedOpen"
          max-width="400px"
          :close-on-content-click="false"
          :activator="selectedElement"
          offset-x
        >
          <v-card
            color="grey lighten-4"
            min-width="350px"
            flat
          >
            <v-toolbar
              :color="selectedEvent.color"
              dark
            >
              <v-icon large class="mr-3">mdi-calendar-check</v-icon>
              <v-toolbar-title v-html="selectedEvent.name"></v-toolbar-title>
              <!-- <v-spacer></v-spacer>
              <v-btn icon>
                <v-icon>mdi-pencil</v-icon>
              </v-btn>
              <v-btn icon>
                <v-icon>mdi-trash-can</v-icon>
              </v-btn> -->
            </v-toolbar>
            <v-card-subtitle>
              {{ this.selectedEvent.detail }}
            </v-card-subtitle>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn icon 
                :color="selectedEvent.color"
                @click="detailSchedule(selectedEvent); selectedOpen=false"
              >
                <v-icon>mdi-pencil</v-icon>
              </v-btn>
              <v-btn icon
               :color="selectedEvent.color"
               @click="deleteSchedule(selectedEvent); selectedOpen=false"
              >
                <v-icon>mdi-trash-can</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-menu>
        <div v-if="this.updateScheduleModal"><UpdateScheduleModal/></div>
      </v-sheet>
		</div>
	</v-app>
</template>

<script>
import { mapActions, mapState } from 'vuex'

// Components
import SideNavBar from '@/components/SideNavBar'
import AddScheduleModal from '@/components/AddScheduleModal'
import UpdateScheduleModal from '@/components/UpdateScheduleModal'


export default {
	name: 'schedule',
	components: {
    SideNavBar,
    AddScheduleModal,
    UpdateScheduleModal,
  },
	data: () => ({
    schedules: {},
    type: 'month',
    mode: 'stack',
    weekday: [0, 1, 2, 3, 4, 5, 6],
    value: new Date(),
    events: [],
    selectedEvent: {},
    selectedElement: null,
    selectedOpen: false,
    prev_idx : 0,
    now_idx : 0,
    check: false,
    colors: ['#FFBC42', '#D81159', '#8F2D56', '#218380', 'blue', 'indigo', 'deep-purple', 'cyan', 'green', 'orange', 'grey darken-1'],
    modal: ''
  }),
  computed: {
    ...mapState([
      'schedule',
      'addScheduleModal',
      'updateScheduleModal',
      'scheduleList',
      'ScheduleModalDetail',
    ])
  },
  methods: {
    ...mapActions([
      'fetchScheduleList',
      'detailSchedule',
      'addSchedule',
      'deleteSchedule',
    ]),
    getDate(date) {
      return this.$moment(date).format('YYYY-MM-DD HH:mm')
    },
    getEvents () {
      return new Promise(() => {
        const events = []
        for (var i = 0; i < this.schedules.length; i++) {
          events.push({
            name: this.schedules[i].title,
            detail : this.schedules[i].detail,
            start: this.getDate(this.schedules[i].start_time),
            end: this.getDate(this.schedules[i].end_time),
            id : this.schedules[i].id,
            color: this.colors[this.schedules[i].id%this.colors.length],
          })
        }
        this.events = events
      })
    },
    getName () {
      return ""
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
    },
    showEvent ({ nativeEvent, event }) {
        const open = () => {
          this.selectedEvent = event
          this.selectedElement = nativeEvent.target
          setTimeout(() => {
            this.selectedOpen = true
          }, 20)
        }

        if (this.selectedOpen) {
          this.selectedOpen = false
          setTimeout(open, 20)
        } else {
          open()
        }
        nativeEvent.stopPropagation()
    },
    viewDay ({ date }) {
      this.focus = date
      if(this.type == 'month') 
        this.type = 'week'
      else 
        this.type = 'month'
    },
    randomIdx(){
      this.now_idx = Math.floor(this.colors.length * Math.random())
      if(this.prev_idx == this.now_idx) this.randomIdx()
      else this.prev_idx = this.now_idx
    }
  },
  watch: {
    scheduleList() {
      this.schedules = this.scheduleList
      console.log('scheduleList', this.schedules)
      this.getEvents()
    }
  },
  mounted() {
    this.fetchScheduleList()
      .then(() => {
        this.schedules = this.scheduleList
        this.getEvents()
      })
  },
}
</script>

<style>
.zpos {
  z-index: 0;
  width: 80%;
}
.plus {
  padding: 0 auto;
}
</style>