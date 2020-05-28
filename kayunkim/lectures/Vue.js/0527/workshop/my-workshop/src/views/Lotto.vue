<template>
  <div>
    <h1>Lotto</h1>
    <button @click="select">숫자생성</button>
    <p v-if="numbers.length">{{ numbers }}</p>
    
    <button @click="visible = !visible">Add One</button>
    <p v-if="visible">{{ addOne() }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
    data: function () {
        return {
            randomNumbers: _.range(1,46),
                   numbers: [],
            count:0,
            visible: true,
        }
    },
    methods: {
        select: function () {
            this.numbers = _.sampleSize(this.randomNumbers, 6)
        },
        addOne: function () {
            this.count +=1
            return this.count
        },
    },
}
</script>

<style>

</style>
