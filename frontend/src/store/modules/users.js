import axios from 'axios';

const state = {
  user: null,
};

const getters = {
  isAuthenticated: state => !!state.user,
  stateUser: state => state.user,
};

const headers = {'Access-Control-Allow-Origin': '*'}

const actions = {
  async register({dispatch}, form) {
    await axios.post('register', form, headers);
    let UserForm = new FormData();
    UserForm.append('username', form.username);
    UserForm.append('password', form.password);
    await dispatch('logIn', UserForm);
  },
  async logIn({dispatch, commit}, user) {
    let userLogin = await axios.post('api/users/login/', user, headers);
    await commit('setUser', userLogin.data.user);
    // await dispatch('viewMe', userLogin);
  },
  async viewMe({commit}, userLogin) {

    await commit('setUser', userLogin.data.user);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteUser({}, id) {
    await axios.delete(`user/${id}`);
  },
  async logOut({commit}) {
    let user = null;
    commit('logout', user);
  }
};

const mutations = {
  setUser(state, username) {
    console.log(username)
    state.user = username;
  },
  logout(state, user){
    state.user = user;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
