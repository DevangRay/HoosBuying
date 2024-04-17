import axios from 'axios';
import bcrypt from 'bcryptjs'


const state = {
    user: null,
    token: null,
};
const getters = {
    isAuthenticated: state => !!state.user,    
    StateUser: state => state.user,
};
const actions = {
  async Register({dispatch}, form) {
    
    let UserForm = new FormData()

    UserForm.append('username', form.username)
    const saltRounds = 10;
    const hashedPassword = await bcrypt.hash(form.password,saltRounds)
    UserForm.append('password', hashedPassword)
    console.log("--" + hashedPassword+"--")
    await axios.post('register', UserForm)

    UserForm.set('password', form.password)
    await dispatch('LogIn', UserForm)
  },

  async LogIn({commit}, user) {
    await axios.post("login", user);
    await commit("setUser", user.get("username"));
  },
  async LogOut({ commit }) {
    let user = null;
    commit("logout", user);
  },
};
const mutations = {
  setUser(state, username) {
    state.user = username;
  },

  logout(state, user) {
    state.user = user;
  },
};
export default {
  state,
  getters,
  actions,
  mutations
};