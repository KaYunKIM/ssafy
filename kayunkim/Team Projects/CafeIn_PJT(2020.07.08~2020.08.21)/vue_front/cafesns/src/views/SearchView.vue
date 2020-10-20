<template>
  <v-flex>
    <v-text-field
      v-model="keyword"
      label="찾으시는 카페가 있으신가요?"
      clearable
      @keypress.enter="searchCafeUser(keyword)"
    >
      <template v-slot:append-outer>
        <v-btn
          small
          dark
          color="secondary"
          @click="searchCafeUser(keyword)"
        >검색</v-btn>
      </template>
    </v-text-field>
    <h3 v-if="searchWord">'{{ searchWord }}'에 대한 검색 결과입니다.</h3>
    <v-tabs>
      <v-tab>Cafe</v-tab>
      <v-tab>User</v-tab>
      <v-tab>Keyword</v-tab>
      <v-spacer></v-spacer>
      <v-tab>카페 전체보기</v-tab>
      <v-tab-item>
        <CafeSearchList/>
      </v-tab-item>
      <v-tab-item>
        <UserSearchList/>
      </v-tab-item>
      <v-tab-item>
        <KeywordSearchList/>
      </v-tab-item>
      <v-tab-item>
        <CafeAllList/>
      </v-tab-item>
    </v-tabs>
  </v-flex>
</template>

<script>
import { mapState, mapActions } from 'vuex'

import CafeAllList from '@/components/search/CafeAllList.vue'
import CafeSearchList from '@/components/search/CafeSearchList.vue'
import UserSearchList from '@/components/search/UserSearchList.vue'
import KeywordSearchList from '@/components/search/KeywordSearchList.vue'

export default {
  name: 'CafeListView',
  data() {
    return {
      keyword: null,
    }
  },
  computed: {
    ...mapState(['searchWord'])
  },
  components: {
    CafeAllList,
    CafeSearchList,
    UserSearchList,
    KeywordSearchList,
  },
  methods: {
    ...mapActions([
      'searchCafeUser',
    ]),
  },
  created() {
    this.searchCafeUser(this.keyword)
  }
}
</script>

<style scoped>
.hover-table :hover {
  cursor: pointer;
}

</style>