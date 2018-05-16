<template>
  <div>
    <div class="day">
      <h3>{{ date.weekday_short }} {{ date.monthname }} {{ date.day }}</h3>
      <div>
        <ul class="conditions-group">
          <li><img class="condition-icon" :src="iconUrl" /></li>
          <li>{{ conditions }}</li>
        </ul>
      </div>
      <div>
        <ul>
          <li>High: {{ high.fahrenheit }}{{ this.degreeSymbol() }} F</li>
          <li>Low: {{ low.fahrenheit }}{{ this.degreeSymbol() }} F</li>
        </ul>
      </div>
      <hr />
    </div>
  </div>
</template>

<script>
export default {
  name: 'Day',

  methods: {
    degreeSymbol () { return '\u00B0' }
  },

  props: [
    'conditions',
    'date',
    'high',
    'low',
    'iconUrl'
  ]
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin-top: 0px;
  margin-bottom: 5px;
  padding-top: 0px;
}

.condition-icon {
  margin-bottom: -10px;
  width: 40px;
  height: 40px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

.day {
  text-align: center;
  padding-bottom: 20px;
}

.conditions-group {
  height: 40px;
  line-height: 40px;
  white-space: nowrap;
}
hr {
  width: 12%;
  margin-top: 30px;
}
</style>
