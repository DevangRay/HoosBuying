<script setup>
import { RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import NavBar from './components/NavBar.vue'

</script>

<template>
  <v-layout light>
  <v-app-bar :elevation="2">
    <template v-slot:prepend>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>
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
 
  <h1>HoosBuying</h1>
  <NavBar></NavBar>
      
  
  
  
    
  <v-containter >
    <RouterView />
  </v-containter>
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
          { title: 'Home', path: '/home', icon: 'home' },
          { title: 'Sign Up', path: '/signup', icon: 'face' },
          { title: 'Sign In', path: '/signin', icon: 'lock_open' }
     ]
    }
  },
};
</script>
<style>
</style>



