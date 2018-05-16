<template>
  <div id="app">
    <Forecaster/>
  </div>
</template>

<script>
import Forecaster from './components/forecaster.vue'

export default {
  name: 'forecaster',
  components: {
    Forecaster
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
