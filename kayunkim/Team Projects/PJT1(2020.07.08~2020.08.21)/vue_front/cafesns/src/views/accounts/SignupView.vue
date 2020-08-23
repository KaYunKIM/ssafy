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
            <v-list-item-title class="headline">이제부터 카페 고민은 <br> 저희가 할께요!</v-list-item-title>
          </v-list-item-content>
          <v-list-item-avatar>
            <v-btn icon dark @click="$router.go(-1)">
              <v-icon>mdi-close</v-icon>
            </v-btn>
          </v-list-item-avatar>
        </v-list-item>
        <v-card-text class="pa-3">
          <v-text-field 
            label="E-mail"
            v-model="signupData.id"
            :rules="[rules.emailMatch]"
            id="Username"
            autofocus
            required
            solo
          >
          </v-text-field>
          <v-text-field 
            solo
            label="Password" 
            type="password" 
            v-model="signupData.password"
            :rules="[rules.passwordMatch]"
            hint="* 최소 8자리(영문,숫자,특수문자 모두 포함)"
            persistent-hint
            id="password"
            required 
          >
          </v-text-field>
          <v-text-field 
            solo
            label="Password Confirm"
            type="password" 
            v-model="signupData.password2" 
            :rules="[rules.passwordConfirm]"
            id="password2"
            required
            @keypress.enter="signup(signupData)"
          >
          </v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn :disabled="!checkValidForm()" color="#BCAAA4" @click="signup(signupData)">Sumbit</v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-overlay>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: "SignupView",

  data() {
    return {
      dialog: true,
      signupData: {
        id: null,
        password: null,
        password2: null,
      },
      emailValid : false,
      pwValid: false,
      conPwValid : false,
      rules: {
        emailMatch:  v => {
          const pattern = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})/
          if (pattern.test(v)) {
            this.emailValid = true
          } else {
            this.emailValid = false
            return '유효한 이메일을 입력해주세요'
          }
        },
        passwordMatch:  v => {
          const pattern = /^.*(?=^.{8,15}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=`~;':"-*/?`]).*$/
          if (this.signupData.password2) {
            if (this.signupData.password !== this.signupData.password2) {
              this.conPwValid = false
              this.passwordConfirm(this.signupData.password2)
            }
          }
          if (pattern.test(v)) {
            this.pwValid = true
          } else {
            this.pwValid = false
            return '* 8 - 15자리 이내(영문, 숫자, 특수문자 모두 포함)'
          }
        },
        passwordConfirm: () => {
          if (this.signupData.password2) {
            if (this.signupData.password == this.signupData.password2) {
              this.conPwValid = true
            } else {
              this.conPwValid = false
              return '비밀번호를 확인해주세요.'
            }
          } else {
            this.conPwValid = false
            return '비밀번호를 입력해주세요.'
          }
        },
      },
    }
  },
  methods: {
    ...mapActions(['signup']),
    checkValidForm () {
      if (this.emailValid && this.pwValid && this.conPwValid) {
        return true
      } else {
        return false
      }
    },
  },
}

</script>

<style>

</style>