<template>
  <div class="home">
    <h1>Bird Box</h1>
    <img id="logo" alt="Vue logo" src="../assets/logo/logo.png" />
    <!-- <HelloWorld msg="Welcome to Your Vue.js App!" /> -->
    <Wave />
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";
import Wave from "@/components/Wave.vue";
import SoundMedia from "@/components/formComponents/SoundMedia.vue";

export default {
  mounted() {},
  // name: "home"
  name: "home",
  components: {
    Wave
  }
};
</script>

<style scoped lang="scss">
#logo {
  height: 275px;
}
</style>
