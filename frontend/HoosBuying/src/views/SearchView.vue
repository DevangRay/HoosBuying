<template>
          <div>
            <div v-for="listing in result" :key="listing.listing_id">
              <v-col>
                <v-card>
                  <v-card-item>
                    <v-card-title>{{listing.title}}</v-card-title>
                    <v-card-subtitle>${{ listing.price }}</v-card-subtitle>
                  </v-card-item>

                  <v-card-item>
                    Sale Status: {{listing.status_name}}

                    <v-icon v-if="listing.status_id==1" size="x-large" color="success" icon="mdi-cart"></v-icon>
                    <v-icon v-else-if="listing.status_id==2" size="x-large" color="warning" icon="mdi-cart"></v-icon>
                    <v-icon v-else-if="listing.status_id==3" size="x-large" color="error" icon="mdi-cart"></v-icon>
                  </v-card-item>
                  <!-- <v-icon color="success" icon="mdi-account-group"></v-icon> -->
                  <v-card-item>
                    Preferred Method of Delivery: {{listing.method_name}}

                    <v-icon v-if="listing.delivery_id==1" size="x-large" color="info" icon="mdi-account-group"></v-icon>
                    <v-icon v-else-if="listing.delivery_id==2" size="x-large" color="info" icon="mdi-email-fast"></v-icon>
                    <v-icon v-else-if="listing.delivery_id==3" size="x-large" color="info" icon="mdi-truck-delivery"></v-icon>
                  </v-card-item>
                </v-card>
              </v-col>
            </div>
          </div>
</template>

<style>
@media (min-width: 1024px) {
  .search {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>

<script>
    import axios from 'axios'

    export default{
        name: 'ListingsArray',
        data() {
            return {
                result: [],
            };
        },
        props: {
            msg: String
        },
        mounted() {
            this.getListings();
        },
        methods: {
          getListings() {
              const headers = {
                "Access-Control-Allow-Origin":"*",
                "Content-Type": "application/jsonp"
              }
            const url = "http://127.0.0.1:5000/listings/getAll"
            axios.get(url, {headers})

            .then((res) => {
                // console.log("RESULT FOUND ", res);
                console.log("DATA IS", res.data)
                this.result = res.data;
                // console.log("RESULT SHOULD BE THE SAME", this.result);
            })
          }
      }
    }
</script>