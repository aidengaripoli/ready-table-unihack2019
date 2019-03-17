<template>
  <div>
    <div class="columns">
      <div class="column">
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
            <p>You will be able to order when you arrive.</p>
          </div>
        </div>

        <div class="card is-paddingless">
          <div class="card-header">
            <div class="card-header-title control">
              <label class="radio">
                <input type="radio" v-model="orderOption" value="now" name="orderOption">
                Order Now!
              </label>
            </div>
          </div>

          <div v-show="orderOption === 'now'" class="card-content">
            <br>
            <h2 class="is-size-3">Menu</h2>
            <br>
            
            <div v-for="item in restaurant.menuItems" v-bind:key="item.name" class="card is-shadowless">
              <div class="card-content">
                <div class="level is-mobile">
                  <div class="level-left">
                    <div class="level-item">
                      {{ item.name }}
                    </div>
                  </div>
                  <div class="level-right">
                    <div class="level-item">
                      ${{ item.cost }}
                    </div>
                    <div class="level-item">
                      <div class="field has-addons">
                        <p class="control">
                          <button @click="remove(item.name, item.cost)" class="button">
                            -
                          </button>
                        </p>
                        <p class="control">
                          <button @click="add(item.name, item.cost)" class="button">
                            +
                          </button>
                        </p>
                      </div>
                    </div>
                    <div class="level-item">
                      {{ orderItems[item.name] || 0 }}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div v-show="orderOption === 'now' && totalCost > 0" class="column">
        <div class="card">
          <div class="card-content">
            <div class="field">
              <div class="control">
                <input class="input" type="email" v-model="stripeEmail" placeholder="Email">
              </div>
            </div>

            <div class="card">
              <card class='card-content'
                :class='{ complete }'
                stripe='pk_test_0ysGpufB2SoUGt85fEZ72rbG'
                :options='stripeOptions'
                @change='complete = $event.complete'
              />
            </div>

            <br>

            <button
              class='button is-primary pay-with-stripe'
              @click='pay'
              :disabled='!complete'
              :class="{ 'is-loading': loading }"
            >
              Pay ${{ totalCost }}
            </button>
          </div>
        </div>
      </div>

      <div v-show="orderOption === 'later'" class="column is-pulled-right">
        <button @click="book" class="button is-info" :class="{ 'is-loading': loading }">Continue</button>
      </div>
    </div>
  </div>
</template>

<script>
import db from '@/firestore'
import uuid from 'uuid'
import axios from 'axios'
import { Card, createToken } from 'vue-stripe-elements-plus'

export default {
  name: "Book",
  data () {
    return {
      orderItems: {},
      totalCost: 0,
      complete: false,
      isPaid: false,
      loading: false,
      stripeEmail: '',
      stripeOptions: {},
      orderOption: 'later',
      paid: false
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

      const tableUpdate = { [`tables.${this.tableNumber}.available`]: false }
      db.collection('restaurants').doc(this.restaurant.id).update(tableUpdate);

      const menuItems = Object.keys(this.orderItems).map(key => {
        return { name: key, paid: true, quantity: this.orderItems[key], ready: false }
      })
      const menuOrderItems = {...menuItems}

      let update = {[`bookings.${uuid()}`]: {
          dateTime: this.bookingDateTime,
          fulfilled: false,
          menuOrderItems,
          user: 'dosatross'
      }};

      db.collection('restaurants').doc(this.restaurant.id).update(update);

      axios.post('https://us-central1-readytable.cloudfunctions.net/bookTable',
        { message: 'reserved' }
      ).then(res => {
          this.loading = false
          console.log(res)
          this.$router.push(`/confirmation/${this.tableNumber}`)
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
          this.paid = true
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
