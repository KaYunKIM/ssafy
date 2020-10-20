<template>
  <v-simple-table>
    <thead>
      <tr v-if="userSearchList.length">
        <th>E-mail</th>
      </tr>
    </thead>
    <tbody>
      <td v-if="!userSearchList.length">
        <h3 class="text-center my-3">
          검색 결과가 없습니다.
        </h3>
      </td>
      <tr
        v-for="user in userSearchList"
        :key="user.id"
        class="hover-table"
        @click="onSelectUser(user)"
      >
        <td>{{ user }}</td>
      </tr>
    </tbody>
  </v-simple-table>
</template>

<script>
import { mapState, } from 'vuex'

export default {
  name: 'UserSearchList',
  computed: {
    ...mapState([
      'userSearchList',
    ])
  },
  methods: {
    onSelectUser(target) {
      this.$router.push(`/accounts/${target}`)
    },
  },
}
</script>

<style scoped>
.hover-table :hover {
  cursor: pointer;
}
</style>