<template>
  <v-simple-table>
    <thead>
      <tr v-if="keywordSearchList.length">
        <th>Cafe Name</th>
        <th>Location</th>
      </tr>
    </thead>
    <tbody>
      <td colspan="2" v-if="!keywordSearchList.length">
        <h3 class="text-center my-3">
          검색 결과가 없습니다.
        </h3>
      </td>
      <tr
        v-for="cafe in keywordSearchList"
        :key="cafe.id"
        class="hover-table"
        @click="onSelectCafe(cafe.cafeno)"
      >
        <td>{{ cafe.name }}</td>
        <td>{{ cafe.address }}</td>
      </tr>
    </tbody>
  </v-simple-table>
</template>

<script>
import { mapState, } from 'vuex'

export default {
  name: 'KeywordSearchList',
  computed: {
    ...mapState([
      'keywordSearchList',
    ])
  },
  methods: {
    onSelectCafe(target) {
      this.$router.push(`/cafe/detail/${target}`)
    },
  },
}
</script>

<style scoped>
.hover-table :hover {
  cursor: pointer;
}
</style>