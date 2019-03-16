<template>
  <div>
    <div v-for="(booking, key) in restaurant.bookings" :key="booking.id" class="column">
      <Order :restaurantId="restaurant.id" :bookingId="key" v-bind:booking="booking"/>
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
