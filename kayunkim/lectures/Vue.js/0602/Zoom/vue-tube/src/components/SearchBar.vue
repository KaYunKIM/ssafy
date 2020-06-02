<template>
  <div>
      <!-- <input type="text" @keydown.enter="onEnter" autofocus> -->
      <input type="text" placeholder="Search Anything Here" class="col-md-8 bg-success text-warning" @keydown.enter="onEnter" v-focus>
  </div>
</template>

<script>
export default {
    name: 'searchBar',
    methods: {
        onEnter(event) {
            this.$emit('input-change', event.target.value)
        }
    },
    directives: {
        focus: {
            inserted: function (el) {
                el.focus()
            }
        }
    },
}
</script>

<style>

</style>