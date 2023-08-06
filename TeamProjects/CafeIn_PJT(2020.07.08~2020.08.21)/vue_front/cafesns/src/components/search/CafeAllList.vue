<template>
  <v-simple-table>
    <thead>
      <tr>
        <th>Cafe Name</th>
        <th>Location</th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="cafe in cafeList"
        :key="cafe.id"
        class="hover-table"
        @click="onSelectCafe(cafe.cafeno)"
      >
        <td>{{ cafe.name }}</td>
        <td>{{ cafe.address }}</td>
      </tr>
    </tbody>
  <infinite-loading @infinite="infiniteHandler" spinner="waveDots"></infinite-loading>
  </v-simple-table>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import InfiniteLoading from 'vue-infinite-loading'

export default {
  name: 'CafeAllList',
  data() {
    return {
      page: 1,
    }
  },
  components: {
    InfiniteLoading,
  },
  computed: {
    ...mapState([
      'cafeList',
    ])
  },
  methods: {
    ...mapActions([
      'fetchCafeList',
    ]),
    onSelectCafe(target) {
      this.$router.push(`/cafe/detail/${target}`)
    },
    infiniteHandler($state) {
      this.fetchCafeList(this.page)
        .then(() => {
          setTimeout(() => {
            if (Object.keys(this.cafeList).length) {
              $state.loaded()
              this.page += 1
              if (Object.keys(this.cafeList).length / 10 == 0) {
                $state.complete()
              }
            } else {
              $state.complete()
            }
          }, 1000)
        })
        .catch(err => console.log(err))
    },
  },
  created() {
    this.fetchCafeList(this.page)
    this.page += 1
  },
}
</script>

<style scoped>
.hover-table :hover {
  cursor: pointer;
}
</style>