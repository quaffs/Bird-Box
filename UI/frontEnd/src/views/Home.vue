<template>
  <div class="home">
    <h1>Bird Box</h1>
    <img id="logo" alt="Vue logo" src="../assets/logo/logo.png" />
    <!-- <HelloWorld msg="Welcome to Your Vue.js App!" /> -->
    <Wave />
    <Upload />
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";
import Wave from "@/components/Wave.vue";
import Upload from "@/components/Upload.vue";

export default {
  // name: "home"
  name: "home",
  components: {
    Wave,
    Upload
  }
};
</script>

<style scoped lang="scss">
#logo {
  height: 275px;
}
</style>
