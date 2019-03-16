<template>
  <div>
    <h2>Tables Page</h2>
    <div class="columns" v-if="tables">
      <div v-for="table in tables" :key="table.id" class="column">
        <Table :id="table.id" :available="table.available" />
      </div>
    </div>
    <template v-else>
      <p>No Tables!</p>
    </template>
  </div>
</template>

<script>
import db from '@/firestore'

import Table from '@/components/Table'

export default {
  name: 'tables',

  data() {
    return {
      tables: []
    }
  },

  firestore: {
    tables: db.collection('tables')
  },

  components: {
    Table
  }
}
</script>

<style>

</style>
