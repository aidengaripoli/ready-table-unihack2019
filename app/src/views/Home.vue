<template>
  <div class="columns">
    <div class="column" v-for="(item, index) in restaurants" v-bind:key="item.name">
      <Restaurant :index="index" :restaurant="item"/>
    </div>
  </div>
</template>

<script>
import db from "@/firestore";

import Restaurant from "@/components/Restaurant";

export default {
  name: 'home',
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
