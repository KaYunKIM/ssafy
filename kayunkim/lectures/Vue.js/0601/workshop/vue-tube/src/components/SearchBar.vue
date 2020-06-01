<template>
    <div>
        <input type="text" @keypress.enter="onInput">
    </div>
</template>


<script>
export default {
    name: 'SearchBar',
    methods: {
        onInput(e) {
            this.$emit('input-change', e.target.value)
        },
    },
    
}
</script>

<style>

</style>