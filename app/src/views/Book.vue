<template>
  <div>
    <table class="table">
      <thead>
        <tr>
          <th>Number</th>
          <th>Name</th>
          <th>Cost</th>
          <th>Add/Remove</th>
          <th>Quantity</th>
        </tr>
        <tr v-for="item in menu" v-bind:key="item.id">
          <th v-if="item.restaurantId === $route.params.restaurant">{{item.number}}</th>
          <th v-if="item.restaurantId === $route.params.restaurant">{{item.name}}</th>
          <th v-if="item.restaurantId === $route.params.restaurant">{{item.cost}}</th>
          <th v-if="item.restaurantId === $route.params.restaurant">
            <button @click="add(item.id, item.cost)" class="button is-success">+</button>
            <button @click="remove(item.id, item.cost)" class="button is-danger">-</button>
          </th>
          <th>{{orderItems[item.id]}}</th>
        </tr>
      </thead>
    </table>
    <p>Total: ${{totalCost}}</p>
  </div>
</template>

<script>
import db from "@/firestore";

export default {
  name: "Book",
  data: function() {
    return {
      menu: [],
      orderItems: {},
      totalCost: 0
    };
  },
  firestore: {
    menu: db.collection("menuItems")
  },
  methods: {
    add(itemId, cost) {
      if (this.orderItems[itemId]) {
        this.$set(this.orderItems, itemId, this.orderItems[itemId] + 1);
      } else {
        this.$set(this.orderItems, itemId, 1);
      }

      this.totalCost += parseInt(cost);
    },
    remove(itemId, cost) {
      if (this.orderItems[itemId]) {
        this.orderItems[itemId]--;
        this.totalCost -= parseInt(cost);
      }
    }
  }
};
</script>

<style>
</style>
