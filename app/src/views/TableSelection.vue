<template>
  <div class="booking">
    <h1>{{ restaurant.name }}</h1>
    <p>{{ restaurant.description }}</p>
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
      <div class="field has-addons">
        <p class="control">
          <input
            v-model.number="day"
            class="input"
            type="number"
            min="1"
            max="31"
            placeholder="Day"
          >
        </p>
        <p class="control">
          <input
            v-model.number="month"
            class="input"
            type="number"
            min="1"
            max="12"
            placeholder="Month"
            required
          >
        </p>
        <p class="control">
          <input
            v-model.number="year"
            class="input"
            type="number"
            min="2019"
            max="2100"
            placeholder="Year"
          >
        </p>
      </div>

      <div class="field has-addons">
        <p class="control">
          <input
            v-model.number="hour"
            class="input"
            type="number"
            min="1"
            max="12"
            placeholder="Hour"
          >
        </p>
        <p class="control">
          <input
            v-model.number="minute"
            class="input"
            type="number"
            min="0"
            max="60"
            placeholder="Minute"
          >
        </p>
        <p class="control">
          <span class="select">
            <select v-model="period">
              <option>AM</option>
              <option>PM</option>
            </select>
          </span>
        </p>
      </div>
    </div>

    <p>Lets see where you can sit.</p>
    <table class="table">
      <thead>
        <tr>
          <th>Table No</th>
          <th>Num Seats</th>
          <th>Availability</th>
          <th>Book</th>
        </tr>
        <tr v-for="item in restaurant.tables" v-bind:key="item.number">
          <th>{{item.number}}</th>
          <th>{{item.numSeats}}</th>
          <th>
            <p v-if="item.available">Available</p>
            <p v-else>Unavailable</p>
          </th>
          <th>
            <div class="field has-addons" v-if="item.available">
              <div class="control">
                <label class="radio">
                  <input :value="item.number" v-model="tableNumber" type="radio" name="question">
                  Pick
                </label>
              </div>
            </div>
          </th>
        </tr>
      </thead>
    </table>

    <button @click="book(tableNumber, restaurant)" class="button is-success">book</button>
  </div>
</template>

<script>
export default {
  name: "Booking",
  data: function() {
    return {
      bookingNow: true,
      seatNumber: 0,
      day: Number,
      month: Number,
      year: Number,
      hour: Number,
      minute: Number,
      period: "AM",
      dateTime: "1/1/1000 12:00 AM",
      tableNumber: Number
    };
  },
  props: {
    restaurant: {}
  },
  methods: {
    toggleBookingNow: function(isBookingNow) {
      this.bookingNow = isBookingNow;
    },

    book(tableNumber, restaurant) {
      let bookingDateTime = "";
      if (!this.bookingNow) {
        bookingDateTime =
          this.day + "/" + this.month + "/" + this.year + " " + this.hour + ":";
        if (this.minute < 10) {
          bookingDateTime += "0";
        }
        bookingDateTime += this.minute + this.period;
      }

      this.$router.push({
        name: "book",
        params: { tableNumber, bookingDateTime, restaurant }
      });
    }
  }
};
</script>