import {createStore} from "vuex";
import createPersistedState from "vuex-persistedstate";
import auth from "./modules/auth";
import search from "./modules/search";
import listing from "./modules/listing";

// Load Vuex

// Create store
const store = createStore({
  modules: {
    auth,
    search,
    listing,
  },
  plugins: [createPersistedState()],
});

export default store;