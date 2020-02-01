<template>
  <div class="read-backend">
    <button v-on:click="testMethod">TEST!</button>
    <p id="response-list-display"></p>
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
      .get("http://localhost:3000/classify/responseExample", {})
      .then(function(response) {
        var responseListDisplay = document.getElementById(
          "response-list-display"
        );
        console.log(response.data);
        // Resets the Response Displayed on Screen
        responseListDisplay!.innerHTML = "";
        //Grabs the file name from the response
        var fileName = response.data.fileName;
        var uploadResultsArray = [];
        // For each "result" inside of results, add it to results array
        for (var i = 0; i < Object.keys(response.data.results).length; i++) {
          uploadResultsArray.push(
            '<p class="borderexample"><u>Result ' +
              (i + 1) +
              ":</u> " +
              "<br>Classification: " +
              response.data.results[i].classification +
              " " +
              "<br>Time Start: " +
              response.data.results[i].timeStart +
              " " +
              "<br>Time End: " +
              response.data.results[i].timeEnd +
              "</p> "
          );
        }
        // Display Respose on Screen
        responseListDisplay!.innerHTML =
          '<br><font size="5">File Name: </font>' +
          '<p class="borderexample">' +
          fileName +
          '</p><br><br><font size="5">Final Results: </font><br>' +
          uploadResultsArray.join("");
      })
      .catch(function(error) {
        console.log(error);
      });
  }
}
</script>

<style>
.borderexample {
  border-style: solid;
  border-color: #287ec7;
  display: inline-block;
  border-width: thick;
  padding: 1%;
  background-color: lightblue;
}
</style>
