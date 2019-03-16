<template>
  <div>
    <div v-for="(booking, key) in restaurant.bookings" :key="booking.id" class="column">
        <Order :restaurantId="restaurant.id" :bookingId="key" v-bind:booking="booking" />
    </div>
  </div>
</template>

<script>
import db from '@/firestore'

import Order from '@/components/Order'

export default {
    props: ['restaurant'],
    name: 'orders',

    components: {
        Order
    },

    methods: {
      ready (index, newBooking) {
        db.collection('restaurants').doc('')
      }
    }
}
</script>

<style>

</style>
