<template>
  <div>
    <h1 class="is-size-3">Orders:</h1>
    <br>
    <div class="columns is-multiline">
      <div v-for="(booking, key) in restaurant.bookings" :key="booking.id" class="column is-4 is-offset-4">
        <Order v-show="!booking.fulfilled" :restaurantId="restaurant.id" :bookingId="key" v-bind:booking="booking"/>
      </div>
    </div>
  </div>
</template>

<script>
import Order from "@/components/Order";

export default {
  props: ["restaurant"],
  name: "orders",

  components: {
    Order
  }
};
</script>

<style>
</style>
