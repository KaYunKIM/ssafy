<template>
	<v-app>
		<side-nav-bar></side-nav-bar>
		<div class = "container zpos">
			<div style="text-align: left">
				<v-sheet>
					<h5>{{this.projectDate}} {{this.$route.params.userId}}'s To Do List</h5>
					<hr>
					<v-container class="white">
						<template v-if="toDoList.length==0">
							업무 리스트가 없습니다. :)
						</template>
						<v-row
							class="mb-4"
							justify="center"
							no-gutters
							v-for="(rowItem, key) in toDoList"
							:key="key"
						>
							<v-col class =".col-md-3 .col-sm-4">
								<template>
									<v-card
										class="mx-auto"
										max-width="344"
										display="flex"
										outlined
										elevation="5"
									>
										<v-list-item three-line>
											<v-list-item-content>
												<v-list-item-title class="headline mb-3"><h6>{{toDoList[key].title}}</h6></v-list-item-title>
												<v-list-item-subtitle class = "mb-2">
													<h6>{{toDoList[key].detail}}</h6>
												</v-list-item-subtitle>
											</v-list-item-content>
										</v-list-item>
									</v-card>
								</template>
							</v-col>
						</v-row>
					</v-container>
				</v-sheet>				
			</div>	
		</div>
	</v-app>
</template>

<script>
// Components
import SideNavBar from '@/components/SideNavBar'
import { mapActions, mapState } from 'vuex'

export default {
	name: 'MemberToDo',
	components: {
		SideNavBar
	},
	data: () => ({
		rowItem: 2,
		requestData:{
			userId: '',
			projectId: '',
		},
		toDoList: [],
	}),
	computed: {
		...mapState([
			'memberToDoList',
			'projectDate'
		])
	},
	methods: {
		...mapActions([
			'fetchMemberToDoList'
		]),
	},
	watch: {
		memberToDoList(){
			console.log("watch order")
			this.toDoList = this.memberToDoList
		}
	},
	created() {
		this.requestData.userId = this.$route.params.userId
		this.requestData.projectId = this.$route.params.projectId
		this.fetchMemberToDoList(this.requestData)
		.then(() => {
			this.toDoList = this.memberToDoList
		})
		console.log(this.toDoList)
	}
}
</script>

<style>

</style>