<!-- <script setup>
defineProps({
  id: Number
})
</script> -->

<template>
  <div class="listing">
    <h1>This is a listing page</h1>
    {{ $route.params.id }} | {{ id }} | {{ this.singleListing }}
  </div>
</template>

<script>
  // defineProps({
  //   id: Number
  // })
  import axios from 'axios'
  import store from '@/stores';
  import router from '@/router';

  export default{
      name: 'SingleListing',
    //   components: {
    //     SearchBar
    // },
      data() {
          return {
              singleListing : {}
          };
      },
      props: {
          msg: String
      },
      mounted() {
          this.getSingleListing(this.$route.params.id);
      },
      methods: {
        getSingleListing(listing_id) {
          store.dispatch('getListing', listing_id)
          .then((result) => {
            console.log("ListingVue result is", result)
            this.singleListing = result;
          })
      }
    }
  }
</script>

<style>
@media (min-width: 1024px) {
  .listing {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
