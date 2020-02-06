<template>
  <div class="upload2">
    <form>
      <div class="form-group">
        <form>
          <!-- File Input 1 -->
          <div class="input-group">
            <div class="input-group-prepend">
              <span class="input-group-text" id="file1-label">File 1</span>
            </div>
            <div class="custom-file">
              <input
                type="file"
                class="custom-file-input"
                id="file1-input"
                ref="file1-input"
                aria-describedby="file1-label"
                v-on:change="changeFile(1)"
              />
              <label
                class="custom-file-label"
                ref="file1-label"
                for="file1-input"
                >Choose file</label
              >
            </div>
          </div>
          <!-- End File Input 1 -->
          <br />
          <!-- File Input 2 -->
          <div class="input-group">
            <div class="input-group-prepend">
              <span class="input-group-text" id="file2-label">File 2</span>
            </div>
            <div class="custom-file">
              <input
                type="file"
                class="custom-file-input"
                id="file2-input"
                ref="file2-input"
                aria-describedby="file2-label"
                v-on:change="changeFile(2)"
              />
              <label
                class="custom-file-label"
                ref="file2-label"
                for="file2-input"
                >Choose file</label
              >
            </div>
          </div>
          <!-- End File Input 2 -->
          <br />
          <!-- File Input 3 -->
          <div class="input-group">
            <div class="input-group-prepend">
              <span class="input-group-text" id="file3-label">File 3</span>
            </div>
            <div class="custom-file">
              <input
                type="file"
                class="custom-file-input"
                id="file3-input"
                ref="file3-input"
                aria-describedby="file3-label"
                v-on:change="changeFile(3)"
              />
              <label
                class="custom-file-label"
                ref="file3-label"
                for="file3-input"
                >Choose file</label
              >
            </div>
          </div>
          <!-- End File Input 3 -->
        </form>
      </div>
      <button
        v-on:click="submitForm()"
        type="button"
        class="btn btn-outline-primary"
      >
        Submit
      </button>
    </form>
    <br />
    <!-- Sound Upload #1 -->
    <label id="sound_label1" class="hidden">
      Sound File Upload: 1
    </label>

    <div id="soundDisplay1"></div>
    <input
      type="button"
      id="play_button1"
      value="Play"
      disabled="disabled"
      class="hidden"
    />
    <input
      type="button"
      id="pause_button1"
      value="Pause"
      disabled="disabled"
      class="hidden"
    />
    <input
      type="button"
      id="stop_button1"
      value="Stop"
      disabled="disabled"
      class="hidden"
    />
    <br />
    <!-- End Sound Upload #1 -->
    <br />
    <!-- Sound Upload #2 -->
    <label id="sound_label2" class="hidden">
      Sound File Upload: 2
    </label>
    <div id="soundDisplay2"></div>
    <input
      type="button"
      id="play_button2"
      value="Play"
      disabled="disabled"
      class="hidden"
    />
    <input
      type="button"
      id="pause_button2"
      value="Pause"
      disabled="disabled"
      class="hidden"
    />
    <input
      type="button"
      id="stop_button2"
      value="Stop"
      disabled="disabled"
      class="hidden"
    />
    <br />
    <!-- End Sound Upload #2 -->
    <br />
    <!-- Sound Upload #3 -->
    <label id="sound_label3" class="hidden">
      Sound File Upload: 3
    </label>
    <div id="soundDisplay3"></div>
    <input
      type="button"
      id="play_button3"
      value="Play"
      disabled="disabled"
      class="hidden"
    />
    <input
      type="button"
      id="pause_button3"
      value="Pause"
      disabled="disabled"
      class="hidden"
    />
    <input
      type="button"
      id="stop_button3"
      value="Stop"
      disabled="disabled"
      class="hidden"
    />
    <!-- End Sound Upload #3 -->
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import WaveSurfer from "wavesurfer.js";

@Component
export default class Upload extends Vue {
  private files: Array<File | undefined> = [undefined, undefined, undefined];
  // this runs when the component is loaded
  mounted() {}

  changeFile(n: number) {
    console.log(`File changed (${n})`);
    //@ts-ignore
    let uploadFile = this.$refs[`file${n}-input`].files[0];
    this.updateInputLabel(`file${n}-label`, uploadFile.name);
    this.files[n - 1] = uploadFile;
    const url = URL.createObjectURL(uploadFile);
    this.generateSoundWaves(url, n);
  }

  generateSoundWaves(url: string, n: any) {
    var soundDisplay = document.getElementById("soundDisplay" + n);
    // If a new sound file is uploaded, clear the previous
    soundDisplay!.innerHTML = "";
    // Create the Sound Wave
    var wavesurfer = WaveSurfer.create({
      container: "#soundDisplay" + n,
      waveColor: "red",
      progressColor: "black"
    });
    // Display the Sound File Upload Label
    document.getElementById("sound_label" + n)!.className = "";
    // Load the file for the Sound Wave
    wavesurfer.load(url);
    // Initialize the buttons used to control the sound wave audio
    var buttons = {
      play: document.getElementById("play_button" + n) as HTMLInputElement,
      pause: document.getElementById("pause_button" + n) as HTMLInputElement,
      stop: document.getElementById("stop_button" + n) as HTMLInputElement
    };
    // Make the Sound Wave Audio Buttons Visible
    buttons.stop.className = "";
    buttons.pause.className = "";
    buttons.play.className = "";

    // If play is pressed, play audio
    buttons.play.addEventListener(
      "click",
      function() {
        wavesurfer.play();

        buttons.stop.disabled = false;
        buttons.pause.disabled = false;
        buttons.play.disabled = true;
      },
      false
    );

    // If pause is pressed, pause audio
    buttons.pause.addEventListener(
      "click",
      function() {
        wavesurfer.pause();

        buttons.pause.disabled = true;
        buttons.play.disabled = false;
      },
      false
    );

    // If stop is pressed, reset sound file to play from beginning
    buttons.stop.addEventListener(
      "click",
      function() {
        wavesurfer.stop();

        buttons.pause.disabled = true;
        buttons.stop.disabled = true;
        buttons.play.disabled = false;
      },
      false
    );

    // Once a sound file is successfully displayed, enable the "play" audio button
    wavesurfer.on("ready", function() {
      buttons.play.disabled = false;
    });
  }

  submitForm() {
    let formData = new FormData();
    // upload files to form data
    this.files.forEach((file, n) => {
      if (file) formData.append(`file${n + 1}`, file);
    });
    // send post request to back end
    Vue.axios
      .post("http://localhost:3000/classify/uploadForm", formData, {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      })
      // This will get called after response is returned
      .then(response => {
        console.log(response);
      })
      // This will run if there is a server error
      .catch(error => {
        console.log(error);
      })
      // This will always run
      .then(() => {});
  }
  updateInputLabel(id: string, label: string) {
    //@ts-ignore
    this.$refs[id].innerHTML = label;
  }
}
</script>

<style lang="scss">
form {
  text-align: left;
}

/* Makes the element invisible */
.hidden {
  display: none !important;
  visibility: hidden !important;
}
</style>
