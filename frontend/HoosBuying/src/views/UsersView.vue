<script>
import UserTable from '../components/UserTable.vue'
import { mapActions } from "vuex";

export default {
    name: 'UsersView',
    components: {
        UserTable
    },
    data(){
      return{
        showError:false
      };
    },
    methods:{
      ...mapActions(["LogIn"]),
      async login(){
        const User = new FormData()
        User.append("username","devang")

        try {
          await this.LogIn(User);
          this.$router.push("/");
          this.showError = false
        } catch (error) {
          this.showError = true
        }
      },
    },
}
</script>

<template>
    <div class="about">
      <h1>This is a user page</h1>
      <button @click="login">buttton</button>
      <p v-if="showError" id="error">Username or Password is incorrect</p>
      <UserTable/>
    </div>
  </template>
  
  <style>
  @media (min-width: 1024px) {
    .about {
      min-height: 100vh;
      display: flex;
      align-items: center;
    }
  }
  </style>
  