import axios from 'axios'


const state = {
  // selected_listing : null,
  listing_info : {},
};
const getters = {
  get_listing_info(state) {
      return state.listing_info
  }
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
      // .then((result) => {
      //   console.log("SINGULAR LISTING DATA IS", result.data[0])
      //   // state.commit('changeSelectedListing', result.data[0])
      //   state.listing_info = result.data[0]
      // })
      
  },
  callListingGetter({getters}) {
    return getters.get_listing_info
  }
};

const mutations = {
  changeSelectedListing(state, new_info) {
    state.listing_info = new_info
  }
};

export default {
state,
getters,
actions,
mutations
};