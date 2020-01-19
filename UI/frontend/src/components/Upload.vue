<template>
  <div class="wave">
    <form id="file-catcher">
      <h3>Upload Your Bird Calls Here:</h3>
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

    var soundFileInput = document.getElementById("sound_files");
    var fileListDisplay = document.getElementById("file-list-display");
    var soundFileList = [];
    var renderFileList, sendFile;

    fileCatcher.addEventListener("submit", function(evnt) {
      evnt.preventDefault();
      soundFileList.forEach(function(file) {
        sendFile(file);
      });
    });

    soundFileInput.addEventListener("change", function(evnt) {
      soundFileList = [];
      for (var i = 0; i < soundFileInput.files.length; i++) {
        soundFileList.push(soundFileInput.files[i]);
      }
      renderFileList();
    });

    renderFileList = function() {
      fileListDisplay.innerHTML = "";
      soundFileList.forEach(function(file, index) {
        var fileDisplayEl = document.createElement("p");
        fileDisplayEl.innerHTML = "Sound File " + (index + 1) + ": " + file.name;
        fileListDisplay.appendChild(fileDisplayEl);
      });
    };

    sendFile = function(file) {
      var formData = new FormData();
      var request = new XMLHttpRequest();

      formData.set("file", file);
      request.open("POST", "localhost:3000");
      request.send(formData);
    };
  }
}
</script>
