<template>

<nav>
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/about">About</RouterLink>
    <RouterLink to="/getAllUsers">See Users</RouterLink>
    <span v-if="isLoggedIn">
      <a @click="logout">Logout</a>
    </span>
    <span v-else>
      <router-link to="/register">Register</router-link> |
      <router-link to="/login">Login</router-link>
    </span>
</nav>
  
</template>

<script>
export default {
  name: "NavBar",
  computed: {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    },
  },
  methods: {
    async logout() {
      await this.$store.dispatch("LogOut");
      this.$router.push("/login");
    },
  },
};



</script>