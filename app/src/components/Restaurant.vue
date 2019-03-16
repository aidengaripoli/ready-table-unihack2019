<template>
  <div class="card">
    <div class="card-image">
      <img alt="Vue logo" src="../assets/logo.png">
    </div>
    <div class="card-content">
      <h1>{{ restaurant.name }}</h1>
      <div class="content">
        <p>{{ restaurant.description }}</p>
      </div>
      <router-link
        class="button is-large button-primary"
        :to="{ name: 'tableSelection', params: { restaurant } }"
      >Book a table</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    restaurant: {}
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a {
  color: #42b983;
}
</style>
