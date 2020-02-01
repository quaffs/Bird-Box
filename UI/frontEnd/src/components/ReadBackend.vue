<template>
  <div class="read-backend">
    <button v-on:click="testMethod">TEST!</button>
    <div id="response-list-display"></div>
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
            " <br><br>Result " +
              (i + 1) +
              ": " +
              "<br>Classification: " +
              response.data.results[i].classification +
              " " +
              "<br>Time Start: " +
              response.data.results[i].timeStart +
              " " +
              "<br>Time End: " +
              response.data.results[i].timeEnd
          );
        }
        // Display Respose on Screen
        responseListDisplay!.innerHTML =
          "<br>File Name: " +
          fileName +
          "<br><br>Final Results: " +
          uploadResultsArray.join("");
      })
      .catch(function(error) {
        console.log(error);
      });
  }
}
</script>
