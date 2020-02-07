<template>
  <div class="SoundMedia">
    <label :id="`sound_label${n}`" class="hidden">
      Sound File Upload: {{ n }}
    </label>

    <div :id="`soundDisplay${n}`"></div>
    <input
      type="button"
      :id="`play_button${n}`"
      value="Play"
      disabled="disabled"
      class="hidden"
    />
    <input
      type="button"
      :id="`pause_button${n}`"
      value="Pause"
      disabled="disabled"
      class="hidden"
    />
    <input
      type="button"
      :id="`stop_button${n}`"
      value="Stop"
      disabled="disabled"
      class="hidden"
    />
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";

@Component
export default class SoundMedia extends Vue {
  @Prop() private n!: number;
}
</script>
