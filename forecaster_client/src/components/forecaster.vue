<template>
  <div>
    <h1>Forecaster</h1>
    <p>
      Get some forecast data, you dork.
    </p>

    <button @click="getForecast" type="button"/>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Forecaster',

  methods: {
    updateForecast (newForecast) {
      this.forecast = newForecast
    },

    getForecast () {
      let data = JSON.stringify({
        zip_code: this.zipCode,
      })
      let headers = { headers: { "x-api-key": this.forecasterApiKey } }
      axios.post(this.forecasterApiUrl, data, headers)
        .then((resp) => this.updateForecast(resp))
    }
  },

  // these values should really be env vars... hard with client-side only
  data () {
    return {
      forecasterApiUrl: "https://lio6akrrmb.execute-api.us-east-1.amazonaws.com/dev/fetch_forecast",
      forecasterApiKey: "66nhRGa2hc9Anj0oRAbnJ2nkFKnjeYuv95w27Zho",
      forecast: {},
      zipCode: "20230" 
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
