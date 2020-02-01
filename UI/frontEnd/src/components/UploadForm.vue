<template>
  <div class="upload2">
    <form id="sound-upload">
      <h3>Sound Upload Form</h3>
      <input id="file1-input" type="file" />
      <br />
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
  mounted() {}
}
</script>
