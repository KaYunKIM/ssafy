<template>
  <div class="child">
      <h2>자식 컴포넌트</h2>
      {{ propFromParent }}
      <button @click="hungrySignal">배고파요</button>
      
      
  </div>
</template>

<script>
export default {
    name: 'child',
    props: {
        propFromParent: String, 
    },
    methods: {
        hungrySignal() {
            this.$emit('hungry')
        }
    }
}
</script>

<style>
.child {
    border: 3px solid blue;
    margin: 3px;
    padding: 3px;

}
</style>