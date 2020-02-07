<template>
  <div class="SoundInput">
    <div class="input-group">
      <div class="input-group-prepend">
        <span class="input-group-text" :id="`file${n}-label`"
          >File {{ n }}</span
        >
      </div>
      <div class="custom-file">
        <input
          type="file"
          class="custom-file-input"
          :id="`file${n}-input`"
          :ref="`file-input`"
          aria-describedby="`file${n}-label`"
          v-on:change="changeFile(n)"
        />
        <label
          class="custom-file-label"
          :ref="`file-label`"
          :for="`file${n}-input`"
          >Choose file</label
        >
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";

@Component
export default class SoundInput extends Vue {
  @Prop() private n!: number;

  changeFile(n: number) {
    let input = this.$refs["file-input"];
    let label = this.$refs["file-label"];
    (this.$parent as any).changeFile(n, input, label);
  }
}
</script>
