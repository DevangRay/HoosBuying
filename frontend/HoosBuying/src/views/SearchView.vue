<template>
  <div class="search">
    <h1>This is a search page</h1>
    <p v-for="listing in result" :key="listing.listing_id">{{ listing.title }}</p>
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
                console.log("RESULT FOUND ", res);
                console.log("DATA IS", res.data)
                this.result = res.data;
                console.log("RESULT SHOULD BE THE SAME", this.result);
            })
          }
      }
    }
</script>