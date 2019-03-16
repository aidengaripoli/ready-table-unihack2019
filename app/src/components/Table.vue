<template>
  <div>
    <button
      @click="book"
      class="button"
      :disabled="!available"
      :class="{ 'is-loading': loading }"
    >Book Table</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  props: ['id', 'available'],

  data() {
    return {
      loading: false
    }
  },

  methods: {
    book() {
      this.loading = true

      axios
        .post(
          'https://us-central1-midyear-reactor-233903.cloudfunctions.net/send-command',
          {
            tableId: this.id,
            message: 'on'
          }
        )
        .then(data => {
          this.loading = false
          console.log(data)
        })
        .catch(err => {
          this.loading = false
          console.error(err)
        })
    }
  }
}
</script>
