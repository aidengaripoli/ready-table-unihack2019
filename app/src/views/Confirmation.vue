<template>
  <div>
    <div class="container">
      <div class="section">
        <p>Thanks for for booking with us!</p>
        <br>
        <p>Your table number is:</p>
        <h1 class="is-size-1">{{ $route.params.id }}</h1>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'confirmation',

  props: ['tableNumber']
}
</script>

<style>

</style>
