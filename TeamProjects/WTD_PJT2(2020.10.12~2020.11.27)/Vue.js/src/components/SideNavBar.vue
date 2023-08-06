<template>
   <div>
      <v-navigation-drawer
         v-model="drawer"
         :color="color"
         :expand-on-hover="expandOnHover"
         :mini-variant="miniVariant"
         :right="right"
         :permanent="permanent"
         absolute
         dark
      >
         <v-list
         dense
         nav
         class="py-0"
         >
            <v-list-item two-line :class="miniVariant && 'px-0'">
               <v-list-item-avatar>
                  <img src="@/assets/small_logo.png">
               </v-list-item-avatar>
               <v-list-item-content>
                  <v-list-item-title><h3>What To Do ?!</h3></v-list-item-title>
               </v-list-item-content>
            </v-list-item>
            
            <v-divider></v-divider>

            <v-list-item two-line :class="miniVariant && 'px-0'">
               <v-list-item-avatar>
                  <img src="@/assets/boy.png">
               </v-list-item-avatar>
               <v-list-item-content>
                  <v-list-item-title><h6>Hello, {{name}}</h6></v-list-item-title>
               </v-list-item-content>
            </v-list-item>
                                 
            <v-list-item
               v-for="item in items"
               :key="item.title"
               link
               @click="menuAction(item.title)"
            >
               <v-list-item-icon>
                  <v-icon>{{ item.icon }}</v-icon>
               </v-list-item-icon>   
               <v-list-item-content>
                  <v-list-item-title><h6>{{ item.title }}</h6></v-list-item-title>
               </v-list-item-content>
            </v-list-item>
         </v-list>
      </v-navigation-drawer>
   </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
	data () {
		return {
      drawer: true,
      items: [
        { title: 'Schedule', icon: 'far fa-calendar-check' },
        { title: 'My Project', icon: 'fas fa-folder-open' },
        { title: 'Search', icon: 'fas fa-search'},
        { title: 'Profile', icon: 'fas fa-users-cog' },
      // { title: 'meetings', icon: 'fas fa-users-cog' },
         { title: 'Logout', icon: 'fas fa-sign-out-alt' },
         ],
         name: 'James',
         color: '#4c4c65',
      right: false,
      permanent: true,
      miniVariant: true,
      expandOnHover: true,
      background: false,
    }
  },
  computed: {
    ...mapState([
      'userData'
      ])
  },
  methods: {
		...mapActions([
      'userLogout',
    ]),
		menuAction(title) {
			if(title === "Schedule") {
				this.$router.push("/schedule")
			} else if(title === "My Project") {
				this.$router.push("/project")
			} else if(title === "meetings") {
				this.$router.push("/meetinglog")
			} else if(title === "Search") {
				this.$router.push("/search")
			} else if(title === "Profile") {
				this.$router.push("/profile")
			} else if(title === "Logout") {
				this.userLogout()
			}
		},
		// onClose() {
		// 	this.userLogout()
		// },
	},
	// mounted() {
		// window.addEventListener('beforeunload', this.onClose)
	// },
  created() {
		this.name = this.userData.nickname
  }
}
</script>