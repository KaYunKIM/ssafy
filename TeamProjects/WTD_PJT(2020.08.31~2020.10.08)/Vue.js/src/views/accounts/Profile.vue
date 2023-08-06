<template>
<v-app>
<side-nav-bar></side-nav-bar>
    <div class="profile_background">
        <div class="profile_modify">
          <strong class="profileM_page">프로필 수정</strong>
        </div>
        <!-- <div class="row">
            
        </div> -->
        <div class="col-6 col-md-9 p-3 mt-3 bg-white profile-form">
            <img src="@/assets/boy.png" style="">
          <div class="empty"></div>
          <div class="input-form">
            <i class="fas fa-envelope icon"></i>
            <input v-model="userInfo.email" type = "email" class = "input-box">
          </div>
          <div class="input-form mt-2">
            <i class="fas fa-user icon"></i>
            <input v-model="userInfo.nickname" type = "text" class = "input-box">
          </div>
          <div class="input-form mt-2">
            <i class="fas fa-pen-square icon"></i>
            <input type = "text" v-model="userInfo.position" class = "input-box">
          </div>
        </div>
        <button @click="updateProfile(userInfo)" class = "modify-btn mt-1" placeholder="position">수정하기</button>
        <div class="empty"></div>
    </div>
</v-app>
</template>

<script>
import SideNavBar from '@/components/SideNavBar'

import { mapState, mapActions } from 'vuex'

export default {
  components: {SideNavBar},

  data: () => ({
    userInfo : {
      email : "",
      nickname: "",
      position: ""
    }
  }),

  computed: {
    ...mapState([
      'userData'
    ])
  },

  methods: {
    ...mapActions([
      'updateProfile'
    ]),
  },

  created() {
    console.log(this.userData)
    this.userInfo.email = this.userData.email
    this.userInfo.nickname = this.userData.nickname
    this.userInfo.position = this.userData.position
  },
}
</script>

<style>
.input-form{
  margin-bottom: 20px;
  width: 70%;
  height: 40px;
}
.profile-form{
  /* margin-left: 100px; */
  margin: 0 auto
}
.ProfileM_page {
  text-shadow: 4px 4px 4px  rgb(114, 114, 114);
}
.profile-form > img {
  border-radius: 100px;
  width:30%; 
  height:30%;
  margin-bottom: 20px;
}
.profile_modify{
  background-color: #DFDCE6;
  height: 8%;
  color: white;
  font-size: 25px;
  text-shadow: 2px;
  margin-bottom: 20px;
}
.profile_background {
  /* border:black 1px solid;  */
  width:60%; 
  height:80%; 
  margin: 5% 0 0 23%; 
  box-shadow: 5px 7px 5px 7px lightgray;
}
.modify-btn {
  border: none;
  background-color: #DFDCE6;
  border-radius: 30px;
  width: 50%;
  padding: 5px;
  margin: 0 auto;
  /* margin-right: 23px; */
}

</style>