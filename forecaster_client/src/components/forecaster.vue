<template>
  <div>
    <div class="head-material">
      <h1>Forecaster</h1>
      <p>
        Zipcode: <input v-model="zipCode"/>
      </p>
      <button @click="getForecast" type="button">Get forecast</button> 
    </div>

    <div v-if="showLoader" class="spinner">
      <img src="../assets/spinner.gif" />
    </div>

    <div v-if="errorStatus">
      Error fetching forecast - 
      Please confirm that {{ zipCode }} is a valid Zipcode
    </div>

    <div v-if="!showLoader" class="forecast">
      <Day v-for="day in forecastDays"
        :key="day.date.weekday_short"
        :conditions="day.conditions"
        :date="day.date"
        :high="day.high"
        :low="day.low"
        :iconUrl="day.icon_url" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Day from './day.vue'
import utils from '../utils.js'

export default {
  name: 'Forecaster',

  components: { Day },

  methods: {
    updateForecast (newForecast) {
      if (newForecast.data.forecast === undefined) {
        this.errorStatus = true
        return
      }
      this.forecast = this.parseForecast(newForecast)
      this.showLoader = false
    },

    parseForecast (rawResponse) {
      let jsonBlob = rawResponse.data.forecast.S
      return JSON.parse(jsonBlob)
    },

    getForecast () {
      this.showLoader = true
      let data = JSON.stringify({
        zip_code: this.zipCode,
      })
      let headers = { headers: { "x-api-key": utils.apiKey() } }
      axios.post(utils.apiUrl(), data, headers)
        .then((resp) => this.updateForecast(resp))
    },
    
    // I know lodash is a thing, just don't want to deal with more deps
    isEmpty (obj) {
      return Object.keys(obj).length === 0 && obj.constructor === Object
    },

    limitDays (allForecastDays) {
      return allForecastDays.slice(0, 3)
    }
  },

  created () {
    this.getForecast
  },

  computed: {
    forecastDays () {
      if (this.forecast.forecast === undefined) {
        return {}
      } else {
        return this.limitDays(this.forecast.forecast.simpleforecast.forecastday)
      }
    },

    errorStatus () {
      return (this.isEmpty(this.forecastDays)) && !this.showLoader
    }
  },

  data () {
    return {
      forecast: {
        forecast: {
          simpleforecast: {
            forecastday: []
          }
        }
      },
      zipCode: "20230",
      showLoader: false
    }
  }
}
</script>

<style scoped>
.head-material {
  padding-bottom: 40px;
}
.spinner {
  text-align: center;
}
</style>
