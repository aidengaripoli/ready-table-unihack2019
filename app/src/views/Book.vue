<template>
  <div>
    <p v-if="bookingDateTime">Booking at {{bookingDateTime}}</p>
    <table class="table">
      <thead>
        <tr>
          <th>Number</th>
          <th>Name</th>
          <th>Cost</th>
          <th>Add/Remove</th>
          <th>Quantity</th>
        </tr>
        <tr v-for="item in restaurant.menuItems" v-bind:key="item.name">
          <th>{{item.number}}</th>
          <th>{{item.name}}</th>
          <th>{{item.cost}}</th>
          <th>
            <button @click="add(item.name, item.cost)" class="button is-success">+</button>
            <button @click="remove(item.name, item.cost)" class="button is-danger">-</button>
          </th>
          <th>{{orderItems[item.name]}}</th>
        </tr>
      </thead>
    </table>
    <p>Total: ${{totalCost}}</p>
    <button @click="book" class="button is-success">Make booking</button>

    <div class="container">
      <div class="section">
        <div class="columns">
          <div class="column is-4">
            <div class="field">
              <label class="label">Email</label>
              <div class="control">
                <input class="input" type="email" v-model="stripeEmail" placeholder="Email input">
                <!-- <span class="icon is-small is-left">
                  <i class="fas fa-envelope"></i>
                </span> -->
                <!-- <span class="icon is-small is-right">
                  <i class="fas fa-exclamation-triangle"></i>
                </span> -->
              </div>
              <!-- <p class="help is-danger">This email is invalid</p> -->
            </div>

            <card class='box'
              :class='{ complete }'
              stripe='pk_test_0ysGpufB2SoUGt85fEZ72rbG'
              :options='stripeOptions'
              @change='complete = $event.complete'
            />
            <button
              class='button is-primary pay-with-stripe'
              @click='pay'
              :disabled='!complete'
              :class="{ 'is-loading': loading }"
            >
              Pay with credit card
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { Card, createToken } from 'vue-stripe-elements-plus'

export default {
  name: "Book",
  data () {
    return {
      orderItems: {},
      totalCost: 0,
      complete: false,
      loading: false,
      stripeEmail: '',
      stripeOptions: {
        // see https://stripe.com/docs/stripe.js#element-options for details
      }
    };
  },
  props: {
    tableNumber: Number,
    bookingDateTime: String,
    restaurant: {}
  },

  components: {
    Card
  },

  methods: {
    book() {
      if (Object.keys(this.menuItems).length === 0) {
        // book without paying.
      } else {
        // need to pay for items.

      }
    },

    pay() {
      // createToken returns a Promise which resolves in a result object with
      // either a token or an error key.
      // See https://stripe.com/docs/api#tokens for the token object.
      // See https://stripe.com/docs/api#errors for the error object.
      // More general https://stripe.com/docs/stripe.js#stripe-create-token.
      this.loading = true
      createToken().then(data => {
        console.log(data)
        console.log('token created', data.token)
        axios.post('https://us-central1-readytable.cloudfunctions.net/stripeFunction ', {
          stripeEmail: this.stripeEmail,
          stripeToken: 'tok_visa', //testing token
          stripeAmount: this.totalCost
        }).then(res => {
          this.loading = false
          console.log(res)
          // this.$router.push('/confirmation')
        }).catch(err => {
          this.loading = false
          console.error(err)
        })
      })
    },

    add(itemId, cost) {
      if (this.orderItems[itemId]) {
        this.$set(this.orderItems, itemId, this.orderItems[itemId] + 1);
      } else {
        this.$set(this.orderItems, itemId, 1);
      }

      this.totalCost += parseInt(cost);
    },
    remove(itemId, cost) {
      if (this.orderItems[itemId]) {
        this.orderItems[itemId]--;
        this.totalCost -= parseInt(cost);
      }
    }
  }
};
</script>

<style>
/* .stripe-card {
  border: 1px solid #ccc;
} */
</style>
