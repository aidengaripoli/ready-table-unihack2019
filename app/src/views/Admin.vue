<template>
    <div>
        <div v-if="restaurant">
            <Orders v-bind:restaurant="restaurant" ></Orders>
        </div>
        
        <button
            @click="test"
            class="button">Test</button>


        <div v-for="booking in restaurant.booking" :key="booking.id" class="column">
            <!-- <Order v-on:update="doShit" :index="index" v-bind:booking="booking" /> -->
            <p>gefg</p>
        </div>
    </div>
</template>

<script>
import db from '@/firestore'

import Orders from '@/components/Orders'

export default {
    name: 'admin',

    data() {
        return {
            restaurant: []
        }
    },

    components: {
        Orders
    },
    firestore: {
        restaurant: db.collection('restaurants').doc('xBU8ruCxEYoiPsKX2hpR'),
        users: db.collection('users')
    },

  methods: {
    test() {

        var update = {['bookings.1.menuOrderItems.ready']: false};

        db.collection('restaurants').doc('xBU8ruCxEYoiPsKX2hpR').update(update)
        for (var key in this.restaurant.booking) {
            console.log(this.restaurant.booking.key);
            
        }

        Object.keys(this.restaurant.booking).map(key => {
            const booking = this.restaurant.booking[key]
            console.log(booking)
        })
        //console.log(this.restaurant)
        // db.collection('users').add({
        //     username: 'memes'
        // }).then(ref => {
        //     console.log(ref)
        // })

    }
  }

}
</script>

<style>

</style>
