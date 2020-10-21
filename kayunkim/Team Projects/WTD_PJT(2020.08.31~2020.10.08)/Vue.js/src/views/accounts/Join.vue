<template>
  <div>
    <div id="nav">
      <img src = "@/assets/wtdlogo.png" height="70px">
    </div>
    <div class="background">
      <div class="outer"> 
        <div class="subtitle">
          <h5>WELCOME, WTD !</h5>
        </div>
        <div class="container col-6 col-md-4 p-3 mt-3 bg-white login-form">
          <div class="empty"></div>
          <h3 class = "login-title">
            <strong>회원 정보 기입</strong>
          </h3>
          <div class="empty"></div>
          <div class="input-form">
            <i class="fas fa-envelope icon"></i>
            <input v-model="userInfo.email" type = "email" class="input-box">
          </div>
          <div class="input-form mt-2">
            <i class="fas fa-user icon"></i>
            <input v-model="userInfo.nickname" id="nickname" type="text" class="input-box" placeholder="nickname">
          </div>
          <div class="input-form mt-2">
            <i class="fas fa-pen-square icon"></i>
            <input v-model="userInfo.position" id="position" type="text" class="input-box" placeholder="position">
          </div>
          <button @click="userJoin(userInfo)" class = "join-btn mt-2" placeholder="position">회원 가입</button>
          <div class="empty"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Join',

  data: () => ({
    userInfo : {
      email : "",
      platform: "",
      nickname: "",
      position: ""
    }
  }),

  computed: {
    ...mapState([
      'userSubData'
    ])
  },
  
  methods: {
    ...mapActions([
      'userJoin'
    ]),
    // Join() {
    //   let msg = "";
    //   if(!this.nickname){
    //     msg = "닉네임 입력해주세요",
    //     // this.$refs.nickname.focus()
    //     alert(msg);
    //   } else if(!this.position){
    //     msg = "포지션 입력해주세요",
    //     // this.$refs.nickname.focus()
    //     alert(msg);
    //   } else {
    //     this.addUser({userInfo});
    //   }
    // },
  },

  created(){
    this.userInfo.email = this.userSubData.email
    this.userInfo.platform = this.userSubData.platform
    console.log('2',this.userInfo)
  },
}
</script>

<style>

.input-form {
  border: #DFDCE6 1px solid;
  border-radius: 30px;
  width: 70%;
  padding: 5px;
  margin: 0 auto;
}

.icon {
  color:#DFDCE6;
}

.input-box {
  margin-left: 30px;
  outline: none;
  border: none;
  background: transparent;
}

.input-box:focus {
  outline: none;
}

.join-btn {
  border: none;
  background-color: #DFDCE6;
  border-radius: 30px;
  width: 70%;
  padding: 5px;
  margin: 0 auto;
}

.join-btn:focus {
  outline: none;
}

</style>