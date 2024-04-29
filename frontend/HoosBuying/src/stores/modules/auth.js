import Login from '@/views/Login.vue';
import axios from 'axios';
import bcrypt from 'bcryptjs'
import router from '@/router';


const state = {
    user: null,
    token: null,
    uid:null,
};
const getters = {
    isAuthenticated: state => !!state.token,    
    StateUser: state => state.user,
    StateUid: state =>state.uid,
    StateToken:state => state.token,
    get_user(state) {
      return state.user
    },
    get_uid(state) {
      return state.uid
    },
    get_token(state) {
      return state.token
    }
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

  getPassword(state, username) {
    let passwordForm = new FormData();
    passwordForm.append("username", username)

    const url = "http://127.0.0.1:5000/auth/getPassword"
    return axios.post(url, passwordForm)
      .then(res=> res.data.password)
  },

  async LogIn({commit}, user) {
    await axios.post("auth/login", user)
      .then((response) => {
        console.log("response is", response.data)
        let token = response.data.token;
        let user_id = response.data.u_id;
        console.log("user is", user_id, "token is", token);
        commit("setUser",response.data.username)
        commit("setUid", user_id);
        commit("setToken",token);


        console.log("state   " + state.user + state.uid + state.token)
      })
  },
  async LogOut({ commit }) {
    let user = null;
    let uid = null
    let token = null;
    commit("logout", user,token,uid);
    router.push("/login")
  },
  async callGetUser({getters}) {
    console.log("returning", getters.get_user)
    let user_name = null
    user_name = await getters.get_user;
    return getters.get_user
  },
  async checkToken({getters}) {
    let token = await getters.get_token;
    let tokenForm = new FormData()
    tokenForm.append("token", token)
    let response = await axios.post('auth/checkToken', tokenForm);
    console.log("GOT RESPONSE HERE", response)
    console.log("returning", response.data == "Success, Token Found")
    return response.data == "Success, Token Found"
  }
};

const mutations = {
  setUser(state, username) {
    state.user = username;
  },
  setUid(state, uid) {
    state.uid = uid;
  },
  setToken(state, token) {
    state.token = token;
    console.log("set token", state.token, "to", token)
  },

  logout(state, user, token, uid) {
    state.user = user;
    state.token = token;
    state.uid = uid;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};