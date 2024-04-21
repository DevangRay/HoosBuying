import axios from 'axios';


const state = {
    user: null,
    token: null,
};
const getters = {
};
const actions = {
  async getListings() {
    const headers = {
        "Access-Control-Allow-Origin":"*",
        "Content-Type": "application/jsonp"
    }
    const url = "http://127.0.0.1:5000/listings/getAll"
    axios.get(url, {headers})
    .then((res) => {
        console.log("RESULT FOUND ", res);
        console.log("DATA IS", res.data)
        this.result = res.data;
        console.log("RESULT SHOULD BE THE SAME", this.result);
    })
  },
};

const mutations = {
};

export default {
  state,
  getters,
  actions,
  mutations
};