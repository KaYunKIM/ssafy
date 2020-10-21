<template>
  <v-app>
    <v-row justify="center">
      <v-dialog v-model="dialog" persistent max-width="600px" >
        <v-card color="#dfdce6" class="mx-lg-auto rounded-lg">
          <v-card-title class="pa-7 d-flex justify-center">
            <span style="font-weight:bold; color:#4c4c65;font-size: x-large;">일정 추가</span>
          </v-card-title>

          <v-card-text>
            <v-container fluid>
              <v-row style="height:70px;">
                <v-col cols="4">
                  <v-subheader class="workform">일정명</v-subheader>
                </v-col>
                <v-col cols="8">
                  <v-text-field
                    label="일정명을 입력해주세요"
                    color="#4c4c65"
                    solo
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>

          <v-card-actions class="pa-7 d-flex justify-center">
            <v-spacer></v-spacer>
            <v-spacer></v-spacer>
            <v-btn large color="#4c4c65" class="white--text m-2" @click="dialog = false; addProject();">확인</v-btn>
            <v-spacer></v-spacer>
            <v-btn large color="#FFFFFF" class="black--text m-2" @click="dialog = false">취소</v-btn>
            <v-spacer></v-spacer>
            <v-spacer></v-spacer>
          </v-card-actions>
          <div v-if="this.addProjectModal"><AddProjectModal/></div>
        </v-card>
      </v-dialog>
    </v-row>
  </v-app>
</template>

<script>
import { mapState, mapActions } from 'vuex'

import AddProjectModal from '@/components/AddProjectModal'

export default {
	name: 'NoProjectModal',
	
  components: {
    AddProjectModal,
	},

  data: () => ({
    dialog: true,
	}),

	computed: {
	...mapState([
		'addProjectModal',
		]),
	},

  methods: {
    ...mapActions([
      'addProject',
    ]),
  },
}
</script>

<style scoped>
.workform {
  font-weight : bold;
  font-size: 1.2em; 
}
</style>