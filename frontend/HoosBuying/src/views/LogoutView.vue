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
          await this.$store.dispatch("LogOut");
          this.$router.push("/login");
        },
      },
      beforeMount() {
        this.logout()
      }
    };
</script>