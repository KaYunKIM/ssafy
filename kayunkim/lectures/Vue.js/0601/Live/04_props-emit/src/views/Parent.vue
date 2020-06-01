<template>
  <div class="parent">
        <h1>부모 컴포넌트</h1>
        <Child @hungry="parentMsg = 밥먹어라" :propFromParent="parentMsg">
  </div>
</template>

<script>
import Child from '../components/Child.vue'

export default {
    name: 'Parent',
    data () {
        return {
            parentMsg: '부모에서 내리는 메시지',
        }
    },
    components: {
        Child,
    }
}
</script>

<style>

</style>