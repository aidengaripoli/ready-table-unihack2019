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

    <div v-if="this.bookingNow">
      <p>Lets see where you can sit.</p>
      <table class="table">
        <thead>
          <tr>
            <th>Table No</th>
            <th>Num Seats</th>
            <th>Availability</th>
            <th>Book</th>
          </tr>
          <tr v-for="item in resTables" v-bind:key="item.number">
            <th>{{item.number}}</th>
            <th>{{item.numSeats}}</th>
            <th>
              <p v-if="item.available">Available</p>
              <p v-else>Unavailable</p>
            </th>
            <th>
              <button
                @click="book(resId, item.id)"
                v-if="item.available"
                class="button is-success"
              >book</button>
              <button v-if="!item.available" class="button is-danger" disabled>book</button>
            </th>
          </tr>
        </thead>
      </table>
    </div>
    <div v-else>
      <p>When do you want to make a reservation for?</p>
      <input type="datetime-local" name="bday" max="1979-12-31" value>
    </div>
  </div>
</template>

<script>
export default {
  name: "Booking",
  data: function() {
    return {
      bookingNow: true,
      seatNumber: 0
    };
  },
  props: {
    resName: String,
    resId: String,
    resDesc: String,
    resTables: {}
  },
  methods: {
    toggleBookingNow: function(isBookingNow) {
      this.bookingNow = isBookingNow;
    },

    book(restaurant, tableId) {
      this.$router.push({ name: "book", params: { restaurant, tableId } });
    }
  }
};
</script>