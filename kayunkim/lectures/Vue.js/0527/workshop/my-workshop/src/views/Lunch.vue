<template>
  <div>
    <h1>Lunch</h1>
    <input @keypress.enter="addMenu" type="text" v-model="newMenu">
    <p v-if="allMenu.length">{{ allMenu }}</p>
    <button @click="selectMenu">랜덤선택</button>
    <p>{{ menu }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default{
    data: function () {
        return {
            allMenu: [],
            newMenu: '',
            menu: '',
        }
    },
    methods: {
         addMenu: function () {
            if (this.newMenu.trim().length >=1){
                this.allMenu.push(this.newMenu)
                this.newMenu = ''
            }
        },
        selectMenu: function () {
            this.menu = _.sample(this.allMenu)
        },
       
    },
}
</script>

<style>

</style>