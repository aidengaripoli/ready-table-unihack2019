<template>
  <div class="card">
    <div class="card-image">
      <img alt="Vue logo" src="../assets/logo.png">
    </div>
    <div class="card-content">
      <h1>{{ resName }}</h1>
      <div class="content">
        <p>{{ resDesc }}</p>
      </div>
      <router-link
        class="button is-large button-primary"
        :to="{ name: 'booking', params: { resName, resId, resDesc } }"
      >Book a table</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    resName: String,
    resId: String,

    resDesc: String
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a {
  color: #42b983;
}
</style>
