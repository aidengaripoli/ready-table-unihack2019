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
      component: () => import('./views/TableSelection.vue'),
      props: true
    },
    {
      path: '/book/:restaurant/:tableId',
      name: 'book',
      component: () => import('./views/Book.vue'),
      props: true
    }
  ]
})

