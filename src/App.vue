<template>
<b-container fluid id="app" class="wrapper">
  <b-row class="overlay">
    <b-col></b-col>
    <b-col>
      <img alt="Vue logo" src="./assets/logo.png">
      <h1 style="color: white"> Student Results </h1>
      <div class="accordion" role="tablist">
        <Card v-for="(item, index) in data" :key="index" :data="item" :index="index" />
      </div>
    </b-col>
    <b-col></b-col>
  </b-row>
</b-container>
</template>

<script>
import Card from './components/Card.vue'
import axios from "axios";

export default {
  name: 'App',
  components: {
    Card
  },
  data() {
    return {
      data: [],
    }
  },
  mounted () {
    axios
      .get('http://localhost:5000/student')
      .then(response => {
        this.data = response.data.data;
      })
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
.wrapper {
  animation: scroll 70s linear infinite;
  background: url("https://img.freepik.com/free-vector/sea-waves-seamless-pattern-ocean-water-wave-lines-raging-curve-sea-waves-summer-beach-waves-storm-background-illustration_229548-699.jpg"), rgb(0, 162, 255);
  height: 100vh;
  min-width: 360px;
  perspective: 500px;
  perspective-origin: 30% 30%;
}
.overlay {
  background-color: rgba(2, 13, 34, 0.637);
  height: inherit;
}
@keyframes scroll {
   100%{
    background-position:0px -1000px;
  }
}

@media (prefers-reduced-motion) {
  .wrapper {
    animation: scroll 200s linear infinite;
  }
}
</style>
