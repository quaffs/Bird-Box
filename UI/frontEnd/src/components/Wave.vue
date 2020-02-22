<template>
  <div class="wave">
    <br />
    <div id="waveform"></div>
    <SoundMedia n="1" fileDirection="hello" />
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import WaveSurfer from "wavesurfer.js";
import SoundMedia from "@/components/formComponents/SoundMedia.vue";

@Component({
  components: {
    SoundMedia
  }
})
export default class Wave extends Vue {
  @Prop() private msg!: string;
  // this runs when the component is loaded
  mounted() {
    //this.loadWave();
    this.generateSoundWaves(1);
  }

  // this loads the wave form
  loadWave() {
    var wavesurfer = WaveSurfer.create({
      container: "#waveform",
      waveColor: "red",
      progressColor: "black"
    });
    wavesurfer.load("northern-cardinal-dvg1.wav");
  }

  //Generate the SoundWave and Allow user to play/pause audio
  generateSoundWaves(n: any) {
    var soundDisplay = document.getElementById(
      "sound_label" + n
    ) as HTMLElement;
    soundDisplay.innerHTML = "";
    // If a new sound file is uploaded, clear the previous
    //soundDisplay!.innerHTML = "DOPE";
    // Create the Sound Wave
    var wavesurfer = WaveSurfer.create({
      container: "#soundDisplay" + n,
      waveColor: "red",
      progressColor: "black"
    });
    // Load the file for the Sound Wave
    wavesurfer.load("northern-cardinal-dvg1.wav");
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
}
</script>
