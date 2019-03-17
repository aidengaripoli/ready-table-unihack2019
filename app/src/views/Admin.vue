<template>
  <div>
    <div v-if="restaurant">
      <Orders v-bind:restaurant="restaurant"></Orders>
    </div>
  </div>
</template>

<script>
import db from '@/firestore'

import Orders from "@/components/Orders";

export default {
  name: "admin",

  data() {
    return {
      restaurant: []
    };
  },
  components: {
    Orders
  },
  firestore: {
    restaurant: db.collection("restaurants").doc("03CBqzGzGeSqmCyPgaoP"),
    users: db.collection("users")
  }
};
</script>

<style>
</style>
