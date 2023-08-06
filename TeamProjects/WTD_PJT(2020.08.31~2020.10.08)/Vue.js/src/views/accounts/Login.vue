<template>
  <div>
    <div id="nav">
      <img src = "@/assets/wtdlogo.png" height="70px">
    </div>
    <div class="background">
      <div class="outer"> 
        <div class="subtitle">
          <h5>HELLO WTD !</h5>
        </div>
        <!-- <div class="container box">
        <h6 class="mt-0 mb-0 ml-2 mr-0">로그인</h6>
        </div>
        <div class ="triangle">
        </div> -->
        <div class="container col-6 col-md-4 p-3 mt-4 bg-white login-form">
          <div class="empty"></div>
          <h3 class = "login-title">
            <strong>소셜 로그인</strong>
          </h3>
          <div class="empty"></div>
     
          <!-- 네이버 -->
          <template>
            <div id="app" class="naver_login">
              <NaverLogin
                client-id="UgFs4DYW2gEvCXivJnTV"
                callback-url="http://localhost:8080/join"
                is-popup="false"
                :callbackFunction="callbackFunction"
                />
            </div>
          </template>
          <div class="blank"></div>
          <!-- 카카오 -->
          <button class="login_btn" @click="KakaoLogin()"><img class="kakao_login" src="@/assets/kakao.png"></button>
          <!-- 구글 -->
          <button class="login_btn" @click="GoogleLogin()"><img class="google_login" src="@/assets/google.png"></button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NaverLogin from 'vue-naver-login'
import {mapActions} from 'vuex'

// let onSuccess = (data) => {
//   console.log(data)
//   console.log("success")
// }
// let onFailure = (data) => {
//   console.log(data)
//   console.log("failure")
// }

let callbackFunction = (status) => {
  if (status) {
    /* (5) 필수적으로 받아야하는 프로필 정보가 있다면 callback처리 시점에 체크 */
    var email = NaverLogin.user.getEmail();
    if( email === undefined || email === null) {
      alert("이메일은 필수정보입니다. 정보제공을 동의해주세요.");
      /* (5-1) 사용자 정보 재동의를 위하여 다시 네아로 동의페이지로 이동함 */
      NaverLogin.reprompt();
      return;
    } else {
      this.userSubData.email = email
      this.userSubData.platform = 'naver'
      this.userLogin(this.userSubData)
    }
    // this.$router.push({name: 'Join', params: {email:  NaverLogin.user.getEmail()}});
    window.location.replace("http://" + window.location.hostname + ( (location.port==""||location.port==undefined)?"":":" + location.port) + "/sample/main.html");
  } else {
    console.log("callback 처리에 실패하였습니다.");
  }
}

export default {
  name: 'Login',

  components: {
    NaverLogin,
  },

  data: () => ({
    userSubData : {
      email : "",
      platform: "",
    }
  }),
  // created() {
  //   let uri = window.location.href.split("#");
    
  //   if (uri.length == 2) {
  //     let vars = uri[1].split("&");
  //     let vars2 = vars[0].split("=");
  //     //axios.get('http://localhost:8399/api/user/naver', {
  //     axios.get("http://localhost:8080/join", {params: {email: vars2[1]}})
  //       .then(({ data }) => {

  //         this.$session.set("user_auth", data.response.id);
  //         localStorage.setItem("user_auth", data.response.id);
  //         this.$session.set("user_type", "naver");
  //         localStorage.setItem("user_type", "naver");
  //         this.$session.set("user_token", localStorage.getItem("token"));
          
  //         alert("환영합니다. " + this.$session.get("user_auth") + "님");
  //       });
  //   }
  // },
  methods: {
    ...mapActions([
      'userLogin'
    ]),
    KakaoLogin() {
        window.Kakao.Auth.login({
        scope: "profile, account_email",
        success: this.GetInfo,
        fail: this.GetNotInfo,
      });
    },
    GetInfo() {
      window.Kakao.API.request({
        url: "/v2/user/me",
        success: (res) => {
          const kakao_account = res.kakao_account;
          // const userInfo = {
            // nickName: kakao_account.profile.nickname,
            // email: kakao_account.email,
          // };
          this.userSubData.email = kakao_account.email
          this.userSubData.platform = 'kakao'
          this.userLogin(this.userSubData)
          // social_login(userInfo);
          // this.$router.push({name: 'Join', params: {email: userInfo.email}});
        },
      });
    },
    async GoogleLogin() {
      const googleUser = await this.$gAuth.signIn();
      const profile = googleUser.getBasicProfile();
      // const userInfo = {
      //   nickName: profile.getName(),
      //   email: profile.getEmail(),
      // };
      // axios하는 코드는 따로 추가필요
      // this.$router.push({name: 'Join', params: {email: userInfo.email}});
      this.userSubData.email = profile.getEmail()
      this.userSubData.platform = 'google'
      this.userLogin(this.userSubData)
    },
    callbackFunction,
  }
}
</script>

<style>
.login_btn{
  margin-top: 2px;
}
.kakao_login{
  width: 310px;
  height: 65px;
  margin-top: 4px;
}
.google_login {
    width: 311px;
    height: 65px;
}
.outer {
   margin-top: 20vh !important;
}

.login-form {
  opacity: 0.9;
  
}
.login-title{
  margin-bottom: 12px;
}
.container {
  width: 40%;
  border-radius: 25px;
}

.naver{
  background-color: #1EC800;
  border-radius: 30px;
  width: 60%;
}

.kakao {
  background-color: #ffe812;
  border-radius: 30px;
  width: 60%;
}

.google {
  background-color: #ffffff;
  border-radius: 30px;
  width: 60% !important;
  border-color: #D5D5D5;
  border-width: 2px;
}

.empty {
  padding: 10px;  
}

.background {
    background-color: #4C4C65; 
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    background-repeat: repeat;
    z-index: -1;
}

.subtitle {
  color: #ffffff;
}

.box {
   text-align: left;
   margin-top: 10vh !important;
   color: #ffffff;
}

/* .triangle {
  position: relative;
  width: 0;
  height: 0;
  top: 16px;
  left: 500px;
  border-left: 10px solid transparent;
  border-right: 10px solid transparent;
  border-bottom: 10px solid #ffffff;
} */
</style>