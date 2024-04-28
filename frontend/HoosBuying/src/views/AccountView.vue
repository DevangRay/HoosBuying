

<template>
    <div class="account">
      <h1>This is an account page</h1>

        <ImgUpload/>
        <ImgListing/>
    </div>
  </template>
  <script>
    import ImgUpload from '../components/ImgUpload.vue'
    import ImgListing from '../components/ImgListing.vue'
  export default {
    name: "AccountView",
    components: {
        ImgUpload,
        ImgListing
    },
  };
  </script>

  <style>
  @media (min-width: 1024px) {
    .search {
      min-height: 100vh;
      display: flex;
      align-items: center;
    }
  }
  </style>
  