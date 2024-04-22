import axios from 'axios';
import bcrypt from 'bcryptjs'


const state = {
    user: null,
    token: null,
};
const getters = {
    isAuthenticated: state => !!state.token,    
    StateUser: state => state.user,
    StateToken:state => state.token,
};
const actions = {
  async Register({dispatch}, form) {
    
    let UserForm = new FormData()

    UserForm.append('username', form.username)
    const saltRounds = 10;
    const hashedPassword = await bcrypt.hash(form.password,saltRounds)
    UserForm.append('password', hashedPassword)
    UserForm.append('fname', form.fname)
    UserForm.append('lname', form.lname)
    UserForm.append('computing_id', form.computing_id)
    UserForm.append('address', form.address)
    UserForm.append('phone_number', form.phone_number)
  
    await axios.post('auth/register', UserForm)

    
    let LoginForm = new FormData()
    LoginForm.append('username', form.username)
    LoginForm.append('password', form.password)
    await dispatch('LogIn', LoginForm)
  },

  async LogIn({commit}, user) {
    await axios.post("auth/login", user)
      .then((response) => {
        let token = response.data.token;
        let user_name = response.data.username;
        console.log("user is", user_name, "token is", token);
        commit("setUser", user_name);
        commit("setToken",token);
      })
  },
  async LogOut({ commit }) {
    let user = null;
    let token = null;
    commit("logout", user,token);
  },
};

const mutations = {
  setUser(state, username) {
    state.user = username;
  },
  setToken(state, token) {
    state.token = token;
  },

  logout(state, user, token) {
    state.user = user;
    state.token = token;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};