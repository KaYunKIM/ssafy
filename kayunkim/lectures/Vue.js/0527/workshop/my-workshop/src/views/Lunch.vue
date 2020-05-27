<template>
  <div>
    <h1>Lunch</h1>
    <p>{{ menus }}</p>
    <button @click="getLunchMenu">메뉴추천!</button>
    <p>{{ todayLunch }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
    data: function () {
        return {
            menus: ['짜장면', '짬뽕', '김밥', '라면'],
            select : '',
        }
    },
    methods: {
        getLunchMenu () {
            this.todayLunch = _.sample(this.menus)
        }
    }
}
</script>

<style>

</style>