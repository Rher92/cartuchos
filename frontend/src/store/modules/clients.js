import axios from 'axios';

// const state = {
//   clients: null,
// };

// const getters = {
//   clients = state => state.clients
// };

const headers = {'Access-Control-Allow-Origin': '*'}

const actions = {
  getClients(cifrc) {
    axios
    .get(`/api/clients/short/?cifrc=${cifrc}`, headers)
    .then(
      response => {
        return response.data.results
      } 
    ).catch(
      error => {
        console.log(error)
        return []
      })
  },

  // async viewMe({commit}, userLogin) {
  //   // await commit('setUser', userLogin.data.user);
  // },

  // eslint-disable-next-line no-empty-pattern
  // async deleteUser({}, id) {
  //   await axios.delete(`user/${id}`);
  // },

  // async logOut({commit}) {
  //   let user = null;
  //   commit('logout', user);
  // }
};

// const mutations = {
//   chargeClients(state, clients) {
//     state.clients = clients;
//   },
// };

export default {
  // state,
  // getters,
  actions,
  // mutations
};
