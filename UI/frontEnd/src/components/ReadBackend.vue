<template>
  <div class="read-backend">
    <button v-on:click="testMethod">TEST!</button>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";

@Component
export default class Wave extends Vue {
  // this runs when the component is loaded
  mounted() {
    console.log("This is loaded");
  }

  testMethod() {
    Vue.axios
      .post("http://localhost:3000/classify/responseExample", {
        name: "Brady",
        message: "Hello World"
      })
      .then(function(res) {
        console.log(res);
      });
  }
}
</script>
