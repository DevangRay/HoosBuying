import axios from 'axios'


const state = {
};
const getters = {
};
const actions = {
  getListing(state, listing_id) {
      const headers = {
        "Access-Control-Allow-Origin":"*",
        "Content-Type": "application/jsonp"
      }
  
      const url = "http://127.0.0.1:5000/listings/get/" + listing_id
      
      return axios.get(url, {headers})
      .then(res=> res.data[0])
      .catch(err => console.error("getListing error", err))
      
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