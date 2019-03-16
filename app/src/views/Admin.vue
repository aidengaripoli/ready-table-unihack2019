<template>
  <div>
    <div v-if="restaurant">
      <Orders v-bind:restaurant="restaurant"></Orders>
    </div>

    <button @click="test" class="button">Test</button>

    <div v-for="booking in restaurant.booking" :key="booking.id" class="column">
      <!-- <Order v-on:update="doShit" :index="index" v-bind:booking="booking" /> -->
      <p>gefg</p>
    </div>
  </div>
</template>

<script>
import db from '@/firestore'
import uuid from 'uuid/v4'

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
    restaurant: db.collection("restaurants").doc("xBU8ruCxEYoiPsKX2hpR"),
    users: db.collection("users")
  },

  methods: {
    test() {
        let update = {[`bookings.${uuid()}`]: {
            dateTime: '11/5/2019 4:00 PM',
            fulfilled: false,
            menuOrderItems: {
                1: {
                    name: 'Coco Loco',
                    number: 1,
                    paid: true,
                    quantity: 1,
                    ready: false
                }
            },
            user: 'dosatross'
        }};

        db.collection('restaurants').doc('xBU8ruCxEYoiPsKX2hpR').update(update);
        

        // Object.keys(this.restaurant.booking).map(key => {
        //     const booking = this.restaurant.booking[key]
        // })
        //console.log(this.restaurant)
        // db.collection('users').add({
        //     username: 'memes'
        // }).then(ref => {
        //     console.log(ref)
        // })

      Object.keys(this.restaurant.booking).map(key => {
        const booking = this.restaurant.booking[key];
        console.log(booking);
      });
      //console.log(this.restaurant)
      // db.collection('users').add({
      //     username: 'memes'
      // }).then(ref => {
      //     console.log(ref)
      // })
    }
  }
};
</script>

<style>
</style>
