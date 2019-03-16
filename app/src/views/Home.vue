<template>
  <div class="home">
    <div v-for="item in restaurants" v-bind:key="item.name">
      <Restaurant :restaurant="item"/>
    </div>
  </div>
</template>

<script>
import db from "@/firestore";

import Restaurant from "@/components/Restaurant";

export default {
  name: "home",
  data: function() {
    return {
      restaurants: []
    };
  },
  components: {
    Restaurant
  },
  firestore: {
    restaurants: db.collection("restaurants")
  }
};
</script>
