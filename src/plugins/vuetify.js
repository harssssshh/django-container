import '@mdi/font/css/materialdesignicons.css'
import '@fortawesome/fontawesome-free/css/all.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import Vue from 'vue';
import Vuetify from 'vuetify/lib';
 import { mdbIcon } from 'mdbvue';
var SocialSharing = require('vue-social-sharing');

Vue.use(SocialSharing);

Vue.use(Vuetify);

export default new Vuetify({
  icons: {
   iconfont: 'mdiSvg' // 'mdi' //|| 'mdiSvg' || 'md' || 'fa' || 'fa4' || 'faSvg'
 },
 name: 'ButtonsSocial',
    components: {
      mdbIcon
    },
});
