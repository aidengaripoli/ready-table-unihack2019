import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/booking',
      name: 'tableSelection',
      component: () => import(/*  webpackChunkName: "tableSelection" */ './views/TableSelection.vue'),
      props: true
    },
    {
      path: '/book',
      name: 'book',
      component: () => import(/*  webpackChunkName: "book" */ './views/Book.vue'),
      props: true
    },
    {
      path: '/confirmation/:id',
      name: 'confirmation',
      component: () => import(/* webpackChunkName: "confirmation" */ './views/Confirmation.vue')
    }
  ]
})

