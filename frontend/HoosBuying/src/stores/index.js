import {createStore} from "vuex";
import createPersistedState from "vuex-persistedstate";
import auth from "./modules/auth";
import search from "./modules/search";

// Load Vuex

// Create store
const store = createStore({
  modules: {
    auth,
    search,
  },
  plugins: [createPersistedState()],
});

export default store;