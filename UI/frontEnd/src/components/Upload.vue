<template>
  <div class="wave">
    <h3>Upload Your Bird Calls Here:</h3>
    <form id="file-catcher">
      <input id="sound_files" type="file" multiple />
      <button type="submit">
        Submit
      </button>
    </form>
    <div id="file-list-display"></div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";

@Component
export default class Upload extends Vue {
  // this runs when the component is loaded
  mounted() {
    var fileCatcher = document.getElementById("file-catcher");
    var soundFileInput = document.getElementById(
      "sound_files"
    ) as HTMLInputElement;
    var fileListDisplay = document.getElementById("file-list-display");
    let soundFileList: Array<any>;

    //When submit is pressed, call send function for each selected file
    fileCatcher!.addEventListener("submit", function(evnt) {
      evnt.preventDefault();
      soundFileList.forEach(function(file) {
        sendFile(file);
      });
    });

    //Any time a sound file is uploaded, add it to the list of uploaded sound files and display the name of the file below
    soundFileInput!.addEventListener("change", function(evnt) {
      soundFileList = [];
      for (var i = 0; i < soundFileInput!.files!.length; i++) {
        soundFileList.push(soundFileInput!.files![i]);
      }
      renderFileList();
    });

    //Displays the names of each of the sound files uploaded
    function renderFileList() {
      fileListDisplay!.innerHTML = "";
      soundFileList.forEach(function(file, index) {
        var fileDisplayEl = document.createElement("p");
        fileDisplayEl.innerHTML =
          "Sound File " + (index + 1) + ": " + file.name;
        fileListDisplay!.appendChild(fileDisplayEl);
      });
    }

    //Makes the POST requests for each file
    function sendFile(file: File) {
      var formData = new FormData();
      var request = new XMLHttpRequest();

      formData.append("file", file);
      request.open("POST", "http://localhost:3000/classify/uploadSound");
      request.send(formData);
    }
  }
}
</script>
