<template>

<nav>
  <span v-if="isLoggedIn">
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/getAllUsers">See Users</RouterLink>
    
    <a @click="logout">Logout</a>
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