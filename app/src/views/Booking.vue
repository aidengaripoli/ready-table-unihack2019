<template>
  <div class="booking">
    <h1>{{ resName }}</h1>
    <p>{{ resDesc }}</p>
    <p>I want to book for:</p>
    <button
      :class="{ 'button is-success': this.bookingNow, 'button is-danger': !this.bookingNow }"
      @click="toggleBookingNow(true)"
    >Right now!</button>
    <button
      :class="{ 'button is-success': !this.bookingNow, 'button is-danger': this.bookingNow }"
      @click="toggleBookingNow(false)"
    >Later</button>

    <div v-if="!this.bookingNow">
      <p>When do you want to make a reservation for?</p>

      <input type="datetime-local" name="bday" max="1979-12-31" value>
    </div>
    <div v-else>
      <p>Lets see where you can sit.</p>
      <table class="table">
        <thead>
          <tr>
            <th>Table No</th>
            <th>Num Seats</th>
            <th>Availability</th>
            <th>Book</th>
          </tr>
          <tr v-for="item in tables" v-bind:key="item.name">
            <th v-if="resName === item.restaurantName">{{item.tableNumber}}</th>
            <th v-if="resName === item.restaurantName">{{item.numSeats}}</th>
            <th v-if="resName === item.restaurantName">
              <p v-if="item.available">Available</p>
              <p v-else>Unavailable</p>
            </th>
            <th v-if="resName === item.restaurantName">
              <button v-if="item.available" class="button is-success">book</button>
              <button v-if="!item.available" class="button is-danger" disabled>book</button>
            </th>
          </tr>
        </thead>
      </table>
    </div>
  </div>
</template>

<script>
import db from "@/firestore";

export default {
  name: "Booking",
  data: function() {
    return {
      bookingNow: true,
      seatNumber: 0,
      tables: []
    };
  },
  firestore: {
    tables: db.collection("tables")
  },
  props: {
    resName: String,
    resDesc: String
  },
  methods: {
    toggleBookingNow: function(isBookingNow) {
      this.bookingNow = isBookingNow;
    }
  }
};
</script>