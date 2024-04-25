
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
  async getListing(state, listing_id) {
      const headers = {
        "Access-Control-Allow-Origin":"*",
        "Content-Type": "application/jsonp"
      }
  
      const url = "http://127.0.0.1:5000/listings/get/" + listing_id
      
      axios.get(url, {headers})
      .then((result) => {
        console.log("SINGULAR LISTING DATA IS", result.data)
        state.commit('changeSelectedListing', result.data)
      })
  },
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