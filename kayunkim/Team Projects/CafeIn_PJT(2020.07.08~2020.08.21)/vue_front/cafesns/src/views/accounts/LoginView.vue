<template>
  <v-overlay style="background-image:linear-gradient(45deg, #a6c0fe, #f68084);" opacity="0">
    <v-dialog
      v-model="dialog"
      transition="dialog-bottom-transition"
      overlay-opacity="0"
      persistent
      width="700px"
      class="py-4"
    >
      <v-card ref="form" color="#2c001e" dark class="pb-3" style="background:transparent">
        <v-list-item color="#2c001e" dark>
          <v-list-item-content>
            <v-list-item-title class="headline">오늘은 <br> 무슨 카페를 갈까?</v-list-item-title>
          </v-list-item-content>
          <v-list-item-avatar>
            <v-btn icon dark @click="$router.go(-1)">
              <v-icon>mdi-close</v-icon>
            </v-btn>
          </v-list-item-avatar>
        </v-list-item>
        <v-card-text class="px-3 pt-5">
          <v-text-field 
            label="Username"
            v-model="loginData.id"
            :rules="[rules.emailMatch]"
            persistent-hint
            id="username"
            autofocus
            solo
          >
          </v-text-field>
          <v-text-field 
            solo
            label="Password" 
            type="password"
            v-model="loginData.pw"
            id="password" 
            @keypress.enter="login(loginData)"
          >
          </v-text-field>
        <div class="text-center">
          <v-btn style="background:transparent" @click="login(loginData)">Login</v-btn>
        </div>
        </v-card-text>
        <v-card-actions>
          <v-btn class="my-0" @click="onSingup" text small><span style="font-size:small;">회원가입은 어떠세요?</span></v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-overlay>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    name: 'LoginView',
    data() {
      return {
        dialog: true,
        loginData: {
          id:null,
          pw:null,
        },
        rules: {
          emailMatch:  v => {
            const pattern = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})/
            if (pattern.test(v)) {
              this.emailValid = true
            } else {
              this.emailValid = false
              return '* 이메일 형식으로 입력해주세요.'
            }
          },
        },
      }
    },
    methods: {
      ...mapActions(['login']),
      onSingup() {
        this.$router.replace({ name: 'Signup'})
      }
    }

}
</script>

<style>
.v-input__slot{
  background: #ffffff40 !important;
  box-shadow: none !important;
}
</style>