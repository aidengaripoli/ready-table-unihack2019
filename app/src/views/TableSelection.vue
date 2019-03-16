<template>
  <div class="booking">
    <div class="field has-addons is-fullwidth">
      <p class="control">
        <button
          class="button"
          :class="{ 'button is-info': this.bookingNow }"
          @click="toggleBookingNow(true)"
        >
          Now!
        </button>
      </p>
      <p class="control">
        <button
          class="button"
          :class="{ 'button is-info': !this.bookingNow }"
          @click="toggleBookingNow(false)"
        >
          Later
        </button>
      </p>
    </div>

    <div v-if="!this.bookingNow">
      <p>When do you want to make a reservation for?</p>
      <br>
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

    <div class="columns">
      <div v-for="(item, index) in restaurant.tables" v-bind:key="item.number" class="column">
        <div class="box">
          <div @click="selectBooking(index)">
            <div class="level is-mobile">
              <div class="level-item">
                Table: {{ item.number }}
              </div>
              <div class="level-item">
                Seats: {{ item.numSeats }}
              </div>
              <div class="level-item">
                <span class="tag is-primary" :class="{ 'is-info': selectedBooking == index }">
                  {{ selectedBooking == index ? 'Selected' : 'Available!' }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <button
      @click="book(selectedBooking, restaurant)"
      class="button is-info is-pulled-right"
    >
      Continue
    </button>
  </div>
</template>

<script>
export default {
  name: "Booking",
  data () {
    return {
      selectedBooking: 1,
      bookingNow: true,
      seatNumber: 0,
      day: 0,
      month: 0,
      year: 0,
      hour: 0,
      minute: 0,
      period: "AM",
      dateTime: "1/1/1000 12:00 AM"
    };
  },
  props: {
    restaurant: {}
  },
  methods: {
    selectBooking (index) {
      this.selectedBooking = parseInt(index)
    },

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
