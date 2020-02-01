import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";
import VueAxios from "vue-axios";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import "./custom.scss";

Vue.use(VueAxios, axios); // axios for requests
Vue.use(BootstrapVue); // bootstrap for style
Vue.use(IconsPlugin); // bootstrap icons

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
