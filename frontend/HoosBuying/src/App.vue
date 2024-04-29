<script setup>
import { RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import NavBar from './components/NavBar.vue'

</script>

<template>
  <v-layout light>
  <v-app-bar :elevation="2">
    <template v-slot:prepend>
      <!-- <v-app-bar-nav-icon></v-app-bar-nav-icon> -->
    </template>

    <v-app-bar-title>HoosBuying</v-app-bar-title>
    <v-spacer></v-spacer>
      <v-app-bar-items class="hidden-xs-only">
        <v-btn
          flat
          v-for="item in menuItems"
          :key="item.title"
          :to="item.path">
          <v-icon left dark>{{ item.icon }}</v-icon>
          {{ item.title }}
        </v-btn>
      </v-app-bar-items>
  </v-app-bar>
  <v-main>
 
  <!-- <h1>HoosBuying</h1> -->
  <!-- <NavBar></NavBar> -->
      
  
  
  
    
  <v-container >
    <RouterView />
  </v-container>
  </v-main>
</v-layout>
</template>
<script>
//import HelloWorld from "./components/HelloWorld";

export default {
  name: "App",
  data(){
    return {
      appTitle: 'Awesome App',
      sidebar: false,
      menuItems: [
          // { title: 'Home', path: '/', icon: 'mdi-home' },
          { title: 'Search', path: '/search', icon: 'mdi-card-search' },
          { title: 'Create Listing', path: '/insertListing', icon: 'mdi-plus-circle-outline' },
          { title: 'My Listings', path: '/myListings', icon: 'mdi-store-search' },
          { title: 'Chats', path: '/chats', icon: 'mdi-forum' },
          { title: 'Account', path: '/account', icon: 'mdi-account-cowboy-hat-outline' },
          { title: 'Logout', path: '/logout', icon: 'mdi-exit-run' },
     ]
    }
  },
  name: "App",
  computed: {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    },
  },
  methods: {
    async logout() {
      await this.$store.dispatch("LogOut");
      // this.$router.push("/login");
    },
  },
};
</script>


<style>
</style>



