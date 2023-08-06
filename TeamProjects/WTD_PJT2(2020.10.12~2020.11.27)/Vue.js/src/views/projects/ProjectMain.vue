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
              <!-- <div v-if="!this.projectList"><NoProjectModal/></div> -->
              <div v-if="this.addProjectModal"><AddProjectModal/></div>
            <v-col class="px-5" cols="12" sm="6">
              <h1>진행중</h1>
							<Draggable class="list-group backboard" :list="inProgress" group="projects">
								<div class="list-group-item projects" v-for="project in inProgress" :key="project.id">
									<button v-on:click="onProjectDetail(project.id)">
										<div class="mouse-hover">
											{{ project.title }}
											<br>
											{{ project.leader }}
											<i class="fas fa-user-friends ml-3"></i>
											{{ project.members.length }}
										</div>
									</button>
								</div>
							</Draggable>
            </v-col>

            <v-col class="px-5" cols="12" sm="6">
              <h1>완료</h1>
							<Draggable class="list-group backboard" :list="done" group="projects">
								<div class="list-group-item projects" v-for="project in done" :key="project.id">
									<button v-on:click="onProjectDetail(project.id)">
										<div class="mouse-hover">
											{{ project.title }}
											<br>
											{{ project.leader }}
											<i class="fas fa-user-friends ml-3"></i>
											{{ project.members.length }}
										</div>
									</button>
								</div>
							</Draggable>
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
// import NoProjectModal from '@/components/NoProjectModal'
import AddProjectModal from '@/components/AddProjectModal'
import Draggable from "vuedraggable"

export default {
	name: 'ProjectMain',
	components: {
    SideNavBar,
    // NoProjectModal,
    AddProjectModal,
		Draggable
	},
	data() {
		return {
			addLeader: "",
			addMembers: [],
			inProgress: [
				// {name: "PJT.자동회의서비스", leader: "김기훈", members: "5" },
				// {name: "Style Registration", members: "5"}
			],
			done: [
				// {title: "공통PJT",  leader: "admin2", id: "99", members: ["admin1", "admin2", "gayun1109"]},
				// {title: "Test Dashboard", leader: "admin4", id: "98", members: ["admin1", "admin3", "admin4"]}
			],
		}
  },
  computed: {
    ...mapState([
			'memberList',
			'projectList',
			'projectDone',
			'projectInProgress',
			'projectStatus',
      'addProjectModal',
    ]),
  },
  methods: {
    ...mapActions([
      'addProject',
			'fetchProjectList',
			'fetchMemberList',
			'updateProjectStatus',
    ]),
		addProjectMember(new_pjt) {
			const members = this.memberList
			const addMembers = []
			for (var i in members) {
				if (members[i]["role"] === "leader") {
					this.addLeader = members[i]["user"]["nickname"]
				}
				addMembers.push(members[i]["user"]["nickname"])
			}
			const new_data = {
				id: new_pjt["id"], title: new_pjt["title"], leader : this.addLeader, members: addMembers 
			}
			console.log('final check',new_data)
			this.inProgress.push(new_data)
		},
		onProjectDetail(pjt_id) {
			this.$router.push(`/project/${pjt_id}`)
		},
	},
	watch: {
		projectStatus() {
			this.fetchMemberList(this.projectList.slice(-1)[0]["id"])
				.then(() => {
					this.addProjectMember(this.projectList.slice(-1)[0])
				})
		},
	},
	beforeRouteLeave (to,from,next) {
		next()
		const statusInfo = {
			inProgress : this.inProgress,
			done : this.done
		}
		this.updateProjectStatus(statusInfo)
	},
  created() {
		this.fetchProjectList(0)
		// store에 저장된 projectInProgress의 project 전체를 넣어주기
		// this.projectInProgress.map((project) => {
			// this.inProgress.push(project)
		// })
		console.log("==========",this.projectList)
		console.log('projectInProgress', this.projectInProgress)
		console.log('projectDone', this.projectDone)
		this.inProgress = this.projectInProgress
		this.done = this.projectDone
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