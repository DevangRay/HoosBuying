<template>
  <div class="listing">
    <!-- <h1>This is a listing page</h1> -->
    <!-- {{ $route.params.id }} | {{ id }} | {{ this.singleListing }} -->
    <!-- {{this.singleListing}} -->
    <v-sheet :elevation="24" :width="700" :height="600" :rounded="'xl'" color="green-lighten-3">
      <v-container>
      <v-row class="mx-auto px-16 pt-16">
        <v-col>
          <v-row>
            <h1>{{ this.singleListing.title }}</h1>
          </v-row>
          <v-row class="mx-auto  mb-16 pb-16">
            <h3>${{ this.singleListing.price }}</h3>
          </v-row>

          <v-row class="mx-auto pt-5">
              IMAGE INFO GOES HERE
          </v-row>
        </v-col>

        <v-col>
          <v-row class="mx-auto py-16">
              {{ this.singleListing.description }}
          </v-row>
          <v-row class="mx-auto">
              Status: {{ this.singleListing.status_name }}
              <v-icon v-if="singleListing.status_id==1" size="x-large" color="success" icon="mdi-cart"></v-icon>
              <v-icon v-else-if="singleListing.status_id==2" size="x-large" color="warning" icon="mdi-cart"></v-icon>
              <v-icon v-else-if="singleListing.status_id==3" size="x-large" color="error" icon="mdi-cart"></v-icon>
          </v-row>
          <v-row class="mx-auto mb-16 pb-16">
              Preferred Delivery Method: {{ this.singleListing.method_name }}
              <v-icon v-if="singleListing.delivery_id==1" size="x-large" color="info" icon="mdi-account-group"></v-icon>
              <v-icon v-else-if="singleListing.delivery_id==2" size="x-large" color="info" icon="mdi-email-fast"></v-icon>
              <v-icon v-else-if="singleListing.delivery_id==3" size="x-large" color="info" icon="mdi-truck-delivery"></v-icon>
          </v-row>
          <v-row class="mx-auto">
              CHAT INFO HERE
          </v-row>
        </v-col>
      </v-row>
    </v-container>
    </v-sheet>
  </div>
</template>

<script>
  import store from '@/stores';

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
@media (min-width: 100%) {
  .listing {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
