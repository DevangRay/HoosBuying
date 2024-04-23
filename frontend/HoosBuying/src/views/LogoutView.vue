<template>
</template>
    
<script>
    export default {
      name: "Logout",
      computed: {
        isLoggedIn: function() {
          return this.$store.getters.isAuthenticated;
        },
      },
      methods: {
        async logout() {
          this.$store.commit('clearTags')
          await this.$store.dispatch("LogOut");
          this.$router.push("/login");
        },
      },
      beforeMount() {
        this.logout()
      }
    };
</script>