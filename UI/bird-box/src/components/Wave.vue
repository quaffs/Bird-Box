<template>
  <div class="wave">
    <h3>Wave</h3>
    <div id="waveform"></div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import WaveSurfer from "wavesurfer.js";
Vue.nextTick(() => {
  console.log("next tick");
  var wavesurfer = WaveSurfer.create({
    container: "#waveform",
    waveColor: "red",
    progressColor: "black"
  });
  wavesurfer.load("northern-cardinal-dvg1.wav");
});

@Component
export default class Wave extends Vue {
  @Prop() private msg!: string;
  onClick(): void {
    window.alert("Hello World");
  }
}
</script>
