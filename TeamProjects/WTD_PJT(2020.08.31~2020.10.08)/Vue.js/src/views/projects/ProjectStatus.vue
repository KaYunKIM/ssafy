<template>
	<v-app>
		<SideNavBar/>
		<div class = "container zpos">
      <div style="text-align: left">
        <v-sheet>
          <div class="btn" @click="addProject()">
            <i class="fas fa-folder-plus plus"></i>
            <span class="ml-3"><strong>프로젝트 생성</strong></span>
          </div>
          <hr>
          <div align="center">
            <v-row>
              <div v-if="!this.projectList"><NoProjectModal/></div>
              <div v-if="this.addProjectModal"><AddProjectModal/></div>
            <v-col class="px-5" cols="12" sm="6">
              <h1>진행중</h1>
							<Draggable class="list-group backboard" :list="inProgress" group="tasks">
								<div class="list-group-item projects" v-for="task in inProgress" :key="task.name">
									<div class="mouse-hover">
										{{ task.name }}
										<br>
										{{ task.leader }}
										<i class="fas fa-user-friends ml-3"></i>
										{{ task.members }}
									</div>
								</div>
							</Draggable>
            </v-col>

            <v-col class="px-5" cols="12" sm="6">
              <h1>완료</h1>
							<draggable class="list-group backboard" :list="done" group="tasks">
								<div class="list-group-item projects" v-for="task in done" :key="task.name">
									<div class="mouse-hover">
										{{ task.name }}
										<br>
											{{ task.leader }}
											<i class="fas fa-user-friends ml-3"></i>
											{{ task.members }}
										
									</div>
								</div>
							</draggable>
            </v-col>
            </v-row>
          </div>
        </v-sheet>
      </div>
		</div>
	</v-app>
</template>


<script>
import { mapState, mapActions } from 'vuex'

// Components
import SideNavBar from '@/components/SideNavBar'
import NoProjectModal from '@/components/NoProjectModal'
import AddProjectModal from '@/components/AddProjectModal'
import Draggable from "vuedraggable"

export default {
	name: 'ProjectStatus',
	components: {
    SideNavBar,
    NoProjectModal,
    AddProjectModal,
		Draggable,
	},
	data() {
		return {
			newTask: "",
			backLog: [
				
			],
			inProgress: [
				{name: "PJT.자동회의서비스", leader: "김기훈", members: "5" },
				{name: "Style Registration", members: "5"}
			],
			done: [
				{name: "공통PJT",  leader: "김기훈", members: "5"},
				{name: "Test Dashboard", members: "5"}
			],
		}
  },
  computed: {
    ...mapState([
      'projectList',
      'addProjectModal',
    ]),
  },
  methods: {
    ...mapActions([
      'addProject',
      'fetchProjecList',
    ]),
		add() {
			if(this.newTask) {
				this.Backlog.push({name: this.newTask})
				this.newTask = ""
			}
		}
  },
  created() {
    this.fetchProjectList()
  }
}

</script>

<style>
.backboard{
	border: none;
	background-color: #dfdce6;
	/* border-radius: 10px; */
	width: 350px; 
	height: 500px;
	margin: 10px;
}
.projects{
	margin: 10px;
}
.mouse-hover:hover {
  cursor: pointer;
}
</style>