<template>
  <div class="wave">
    <br/>
    <h3>Wave</h3>
    <div id="waveform"></div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import WaveSurfer from "wavesurfer.js";

@Component
export default class Wave extends Vue {
  @Prop() private msg!: string;
  // this runs when the component is loaded
  mounted() {
    this.loadWave();
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
}
</script>
