import createPersistedState from "vuex-persistedstate";
import Vue from 'vue';
import Vuex from 'vuex';

import notes from './modules/notes';
import users from './modules/users';
import clients from './modules/clients';



Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    notes,
    users,
    clients,
  },
  plugins: [createPersistedState()]
});
