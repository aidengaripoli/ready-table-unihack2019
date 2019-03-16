<template>
  <div>
    <div class="columns">
      <div class="column">
        <!-- <p v-if="bookingDateTime">Booking at {{bookingDateTime}}</p>
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
              <th>{{orderItems[item.name] || 0}}</th>
            </tr>
          </thead>
        </table> -->
      
        <div class="card">
          <div class="card-header">
            <div class="card-header-title control">
              <label class="radio">
                <input type="radio" v-model="orderOption" value="later" name="orderOption">
                Order Later
              </label>
            </div>
          </div>
          <div v-show="orderOption === 'later'" class="card-content">
            <p>continue...</p>
          </div>
        </div>

        <div class="card">
          <div class="card-header">
            <div class="card-header-title control">
              <label class="radio">
                <input type="radio" v-model="orderOption" value="now" name="orderOption">
                Order Now!
              </label>
            </div>
          </div>
          <div v-show="orderOption === 'now'" class="card-content">
            <p>menu</p>
          </div>
        </div>
        <!-- <template v-show="totalCost === 0">      
          <button @click="book" class="button is-success" :class="{ 'is-loading': loading }">Make booking</button>
        </template> -->
      </div>

      <div v-show="orderOption === 'now' && totalCost > 0" class="column is-4">
        <div class="field">
          <label class="label">Email</label>
          <div class="control">
            <input class="input" type="email" v-model="stripeEmail" placeholder="Email input">
          </div>
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
      stripeOptions: {},
      orderOption: 0
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
      this.loading = true
      axios.post('https://us-central1-readytable.cloudfunctions.net/bookTable',
        { message: 'reserved' }
      ).then(res => {
          this.loading = false
          console.log(res)
          this.$router.push('/confirmation')
        }).catch(err => {
          console.error(err)
        })
    },

    pay() {
      this.loading = true
      createToken().then(data => {
        console.log(data)
        console.log('token created', data.token)
        axios.post('https://us-central1-readytable.cloudfunctions.net/stripeFunction ', {
          stripeEmail: this.stripeEmail,
          stripeToken: 'tok_visa', //testing token
          stripeAmount: this.totalCost
        }).then(res => {
          console.log(res)
          this.book()
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
