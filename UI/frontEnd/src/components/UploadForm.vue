<template>
  <div class="uploadForm">
    <div id="alert-panel"></div>
    <form>
      <div class="form-group">
        <form>
          <SoundInput n="1" fileDirection="Microphone 1" />
          <br />
          <SoundInput n="2" fileDirection="Microphone 2" />
          <br />
          <SoundInput n="3" fileDirection="Microphone 3" />
          <br />
          <SoundInput n="4" fileDirection="Microphone 4" />
          <br />
          <SoundInput n="5" fileDirection="Microphone 5" />
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
    <SoundMedia n="1" fileDirection="Microphone 1" />
    <br />
    <SoundMedia n="2" fileDirection="Microphone 2" />
    <br />
    <SoundMedia n="3" fileDirection="Microphone 3" />
    <br />
    <SoundMedia n="4" fileDirection="Microphone 4" />
    <br />
    <SoundMedia n="5" fileDirection="Microphone 5" />
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import WaveSurfer from "wavesurfer.js";
import SoundInput from "@/components/formComponents/SoundInput.vue";
import SoundMedia from "@/components/formComponents/SoundMedia.vue";

@Component({
  components: {
    SoundInput,
    SoundMedia
  }
})
export default class Upload extends Vue {
  private files: Array<File | undefined> = [undefined, undefined, undefined];
  // this runs when the component is loaded
  mounted() {}

  changeFile(n: number, input: HTMLElement, label: HTMLElement) {
    let uploadFile = (input as any).files[0];
    label.innerHTML = uploadFile.name;
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
        let error = response.data.error;
        let errorMsg = response.data.errorMsg;
        let alert = "";
        if (error) {
          alert = `<div class="alert alert-warning" role="alert">There was an errorL ${errorMsg}</div>`;
        } else {
          alert = `<div class="alert alert-success" role="alert">File was successfully processed!</div>`;
        }

        (document.getElementById(
          "alert-panel"
        ) as HTMLElement).innerHTML = alert;
      })
      // This will run if there is a server error
      .catch(error => {
        let alert = `<div class="alert alert-danger" role="alert">There was an interal server error. Unable to process files.</div>`;
        (document.getElementById(
          "alert-panel"
        ) as HTMLElement).innerHTML = alert;
      })
      // This will always run
      .then(() => {});
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
