<template>
	<v-app>
		<side-nav-bar></side-nav-bar>
		<div class = "container zpos">
			<div style="text-align: left">
				<v-sheet>
					<h5>{{this.$moment(new Date()).format('YYYY-MM-DD')}} {{name}}'s To Do List</h5>
					<hr>
					<v-container class="white">
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
										shaped
									>
										<v-list-item three-line>
											<v-list-item-content>
												<v-list-item-title class="headline mb-3">{{toDoList[key].projectName}}</v-list-item-title>
												<v-list-item-subtitle class = "mb-2" v-for="(item,idx) in toDoList[key].subTask" :key=idx>
													<h6>{{idx+1}}. {{toDoList[key].subTask[idx]}}</h6>
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

export default {
	name: 'memberToDo',
	components: {SideNavBar},
	data: () => ({
		rowItem: 2,
		name: '김싸피',
		toDoList: [
			{
				projectName: "업무1",
				subTask: ["상세업무1", "상세업무2", "상세업무3"]
			},
			{
				projectName: "업무2",
				subTask: ["상세업무1", "상세업무2", "상세업무3", "상세업무4"]
			},
			{
				projectName: "업무3",
				subTask: ["상세업무1", "상세업무2", "상세업무3", "상세업무4", "상세업무5"]
			},
			{
				projectName: "업무4",
				subTask: ["상세업무1", "상세업무2", "상세업무3"]
			}
		]
	}),
}
</script>

<style>

</style>