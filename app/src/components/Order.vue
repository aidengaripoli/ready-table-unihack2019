<template>
  <div>
    <div class="card">
      <div class="card-header">
        <div class="card-header-title">
          Order for {{ booking.user }}
        </div>
      </div>
      <div class="card-content">
        <div v-for="(item, key) in booking.menuOrderItems" :key="item.name" class="column">
          <div v-show="!item.ready">
            {{item.quantity}} {{item.name}}
            <button
              @click="onItemStatusChange(key)"
              class="button"
            >Ready</button>
          </div>
        </div>
      </div>
      <div class="card-footer"></div>
    </div>
  </div>
</template>

<script>
import db from "@/firestore";
import axios from 'axios'

export default {
  props: ["restaurantId", "bookingId", "booking"],

  methods: {
    onItemStatusChange(itemId) {
      //updates ready and fulfilled
      var update = {
        [`bookings.${this.bookingId}.menuOrderItems.${itemId}.ready`]: true
      };

      db.collection("restaurants")
        .doc(this.restaurantId)
        .update(update)
        .then(() => {
          const readies = Object.keys(this.booking.menuOrderItems).map(key => {
            return this.booking.menuOrderItems[key].ready;
          });

          if (
            readies.every(ready => {
              return ready;
            })
          ) {
            var update = { [`bookings.${this.bookingId}.fulfilled`]: true };
            db.collection("restaurants")
              .doc(this.restaurantId)
              .update(update);

            this.allFoodDelivered()
          } else {
            this.foodReady()
          }
        });
    },
    foodReady() {
      axios.post('https://us-central1-readytable.cloudfunctions.net/bookTable ',
        { message: 'food_ready' }
      )
      .then(res => {
        console.log(res)
        console.log('sent!')
      })
      .catch(err => {
        console.error(err)
      })
    },
    allFoodDelivered() {
      axios.post('https://us-central1-readytable.cloudfunctions.net/bookTable ',
        { message: 'all_food_delivered' }
      )
      .then(res => {
        console.log(res)
        console.log('sent!')
      })
      .catch(err => {
        console.error(err)
      })
    }
  }
};
</script>
