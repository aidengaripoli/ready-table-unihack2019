<template>
  <div class="home">
    <ul>
      <li v-for="item in restaurants" v-bind:key="item.name">
        <Restaurant :resName="item.name" :resId="item.id" :resDesc="item.description"/>
      </li>
    </ul>
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
