<template>
  <div>
      <ul>
          VideoList
          {{ videos }}
      </ul>
  </div>
</template>

<script>
export default {
    name: 'VideoList',
    props: {
        videos: {
            type: Array,
        },
    },
}
</script>

<style>

</style>