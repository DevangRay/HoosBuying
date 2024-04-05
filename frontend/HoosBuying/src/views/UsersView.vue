<script>
import UserTable from '../components/UserTable.vue'

export default {
    name: 'UsersView',
    components: {
        UserTable
    }
}
</script>

<template>
    <div class="about">
      <h1>This is a user page</h1>
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
  