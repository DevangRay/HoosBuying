<template>
      <div class="search"></div>
        <h1>This is a search page</h1>
          <div v-for="listing in result" :key="listing.listing_id">
            <v-col>
              <v-card>
                <v-card-item>
                  <v-card-title>{{listing.title}}</v-card-title>

                    <v-card-subtitle>${{ listing.price }}</v-card-subtitle>
                </v-card-item>
    
                <v-card-text>
                  {{ listing.description }}
                </v-card-text>
                <v-icon color="error" icon="mdi-cart"></v-icon>
                <v-icon color="success" icon="mdi-account-group"></v-icon>
                <v-card-item>
                  {{listing.status_id}} : {{listing.status_name}}
                  
                  {{listing.delivery_id}} : {{listing.method_name}}
                </v-card-item>
              </v-card>
            </v-col>
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