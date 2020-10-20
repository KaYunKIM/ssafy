<template>
  <div>
    <v-dialog v-model="dialog" scrollable max-width="300px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="#BCAAA4"
          v-bind="attrs"
          v-on="on"
          text
        >
          Followers {{ followerList.length }}
        </v-btn>
      </template>
      <v-card class="d-inline-block">
        <v-row class="d-inline-block px-2">
          <v-card-title style="color: #1A1F73">Followers</v-card-title>
        </v-row>
        <v-divider class="mb-2"></v-divider>
        <v-card-text style="height: 300px;">
          <div v-if="!followerList.length" class="text-center">
            <span style="color: #D9A9A9">현재 팔로워하는 유저가 없습니다.</span>
          </div>
          <v-radio-group v-model="dialogm1" column>
            <v-row v-for="user in followerList" :key="user.id">
              <v-list rounded>
                <v-list-item-group>
                  <v-list-item
                    @click="onMypage(user)"
                  >
                  <v-list-item-icon>
                    <v-icon v-text="'mdi-account'"></v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title >{{ user }}</v-list-item-title>
                  </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-row>
          </v-radio-group>
        </v-card-text>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: "FollowerList",
  data () {
    return {
      dialogm1: '',
      dialog: false,
      currentUserId : this.$route.params.user_id,
    }
  },

  computed: {
    ...mapState([
      'userData',  
      'followerList', 
    ])
  },
  
  methods: {
    ...mapActions([
      'fetchUserData',
      'fetchFollowerList',
      'followUser',
    ]),
    onMypage(userid) {
      this.dialog = false
      this.$router.push(`/accounts/${userid}`)
    }
  },
  
  created() {
    this.fetchUserData(this.currentUserId)
      this.fetchFollowerList()
  },
}
</script>