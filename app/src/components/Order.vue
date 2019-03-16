<template>
  <div>
    <h1 class="is-size-3">Order for {{booking.user}}</h1>
    <div class="columns">
      <div v-for="(item, key) in booking.menuOrderItems" :key="item.name" class="column">
        <div>
          x{{item.quantity}} {{item.name}} {{item.ready}}
          <button
            @click="onItemStatusChange(key)"
            class="button"
          >Ready</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import db from "@/firestore";

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
          }
        });
    }
  }
};
</script>
