<template>
    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-6" role="tab">
        <h3 class="my-2">{{ name }}</h3>
        <b-button v-b-toggle="'accordion-'+(index+1)" variant="primary" class="my-2">Show Info</b-button>
      </b-card-header>
      <b-collapse :id="'accordion-'+(index+1)" accordion="my-accordion" role="tabpanel">
        <b-card-body>
          <b-card-title>School: {{ institution }}</b-card-title>
          <b-card-sub-title class="m-2">Results:</b-card-sub-title>
          <b-list-group>
            <b-list-group-item v-for="sub in subject" :key="sub.id">{{ sub.tittle }} : {{ sub. marks}}</b-list-group-item>
          </b-list-group>
        </b-card-body>
      </b-collapse>
    </b-card>
</template>

<script>
import axios from "axios";
export default {
  name: 'Card',
  props: {
    data: Object,
    index: Number
  },
  computed: {
    name(){
      var output = this.data.firstName + " "+ this.data.lastName;
      return output;
    },
    institution(){
      this.findInstitution(this.data.institution);
      return this.instiName
    },
    id(){
      var output = "accordian-" + this.index;
      return output;
    }
  },
  data() {
    return {
      instiName: "",
      subject: []
    }
  },
  methods: {
    findInstitution(id) {
    axios
      .get('http://localhost:5000/institution/' + id)
      .then(response => {
        var item = response.data.data;
        this.instiName = item.tittle;
      })
    }
  },
  mounted () {
    axios
      .get('http://localhost:5000/subject')
      .then(response => {
        var item = response.data.data;
        this.subject = item;
      })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  display: inline-block;
}
.card-header {
  text-align: left
}
.card-header button {
  float: right;
}
</style>
