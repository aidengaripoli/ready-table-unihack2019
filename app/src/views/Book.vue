<template>
  <div>
    <p v-if="bookingDateTime">Booking at {{bookingDateTime}}</p>
    <table class="table">
      <thead>
        <tr>
          <th>Number</th>
          <th>Name</th>
          <th>Cost</th>
          <th>Add/Remove</th>
          <th>Quantity</th>
        </tr>
        <tr v-for="item in restaurant.menuItems" v-bind:key="item.name">
          <th>{{item.number}}</th>
          <th>{{item.name}}</th>
          <th>{{item.cost}}</th>
          <th>
            <button @click="add(item.name, item.cost)" class="button is-success">+</button>
            <button @click="remove(item.name, item.cost)" class="button is-danger">-</button>
          </th>
          <th>{{orderItems[item.name]}}</th>
        </tr>
      </thead>
    </table>
    <p>Total: ${{totalCost}}</p>
    <button @click="book" class="button is-success">Make booking</button>
  </div>
</template>

<script>
export default {
  name: "Book",
  data: function() {
    return {
      orderItems: {},
      totalCost: 0
    };
  },
  props: {
    tableNumber: Number,
    bookingDateTime: String,
    restaurant: {}
  },
  methods: {
    book() {},
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
