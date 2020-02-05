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
    <label id="sound_label1">
      Sound File Upload: 1
    </label>
    <div id="soundDisplay1"></div>
    <input type="button" id="play_button1" value="Play" disabled="disabled" />
    <input type="button" id="pause_button1" value="Pause" disabled="disabled" />
    <input type="button" id="stop_button1" value="Stop" disabled="disabled" />
    <br />

    <br />
    <label id="sound_label2">
      Sound File Upload: 2
    </label>
    <div id="soundDisplay2"></div>
    <input type="button" id="play_button2" value="Play" disabled="disabled" />
    <input type="button" id="pause_button2" value="Pause" disabled="disabled" />
    <input type="button" id="stop_button2" value="Stop" disabled="disabled" />
    <br />

    <br />
    <label id="sound_label3">
      Sound File Upload: 3
    </label>
    <div id="soundDisplay3"></div>
    <input type="button" id="play_button3" value="Play" disabled="disabled" />
    <input type="button" id="pause_button3" value="Pause" disabled="disabled" />
    <input type="button" id="stop_button3" value="Stop" disabled="disabled" />
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

  renderFileList() {
    /// Clears previous uploads
    var soundDisplay = document.getElementById("soundDisplay" + n);
    soundDisplay!.innerHTML = "";
    this.files.forEach((file, n) => {
      const url = URL.createObjectURL(file);
      this.generateSoundWaves(url, n);
    });
  }

  generateSoundWaves(url: string, n: any) {
    var soundDisplay = document.getElementById("soundDisplay" + n);
    soundDisplay!.innerHTML = "";

    var wavesurfer = WaveSurfer.create({
      container: "#soundDisplay" + n,
      waveColor: "red",
      progressColor: "black"
    });
    wavesurfer.load(url);

    var buttons = {
      play: document.getElementById("play_button" + n) as HTMLInputElement,
      pause: document.getElementById("pause_button" + n) as HTMLInputElement,
      stop: document.getElementById("stop_button" + n) as HTMLInputElement
    };

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

    buttons.pause.addEventListener(
      "click",
      function() {
        wavesurfer.pause();

        buttons.pause.disabled = true;
        buttons.play.disabled = false;
      },
      false
    );

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
    Vue.axios.post("http://localhost:3000/classify/uploadForm", formData, {
      headers: {
        "Content-Type": "multipart/form-data"
      }
    });
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
</style>
