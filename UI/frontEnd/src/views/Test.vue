<template>
  <div class="test">
    <h1>This is a test page</h1>
    <ReadBackend />
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";
import ReadBackend from "@/components/ReadBackend.vue";

export default {
  name: "test",
  components: {
    ReadBackend
  }
};
</script>
