<template>
    <div v-for="listing in listing_result" :key="listing.listing_id">
        <v-col>
            <v-card @click="goToListing(listing.listing_id)">
                <v-card-item>
                    <v-card-title>{{ listing.title }} | {{ listing.listing_id }}</v-card-title>
                    <v-card-subtitle>${{ listing.price }}</v-card-subtitle>
                </v-card-item>

                <v-card-item>
                    Sale Status: {{ listing.status_name }}

                    <v-icon v-if="listing.status_id == 1" size="x-large" color="success" icon="mdi-cart"></v-icon>
                    <v-icon v-else-if="listing.status_id == 2" size="x-large" color="warning" icon="mdi-cart"></v-icon>
                    <v-icon v-else-if="listing.status_id == 3" size="x-large" color="error" icon="mdi-cart"></v-icon>
                </v-card-item>
                <!-- <v-icon color="success" icon="mdi-account-group"></v-icon> -->
                <v-card-item>
                    Preferred Method of Delivery: {{ listing.method_name }}
                    <!-- Tag: {{ listing.tag_id }} -->
                    <v-icon v-if="listing.delivery_id == 1" size="x-large" color="info"
                        icon="mdi-account-group"></v-icon>
                    <v-icon v-else-if="listing.delivery_id == 2" size="x-large" color="info"
                        icon="mdi-email-fast"></v-icon>
                    <v-icon v-else-if="listing.delivery_id == 3" size="x-large" color="info"
                        icon="mdi-truck-delivery"></v-icon>
                </v-card-item>
            </v-card>
        </v-col>
    </div>
    <div v-if="this.listing_result.length === 0">
        <h1>No results yet!</h1>
    </div>
</template>

<script>
// import SearchBar from '../components/SearchBar.vue'
import axios from 'axios'
import store from '@/stores';
import router from '@/router';

export default {
    name: 'ListingsArray',
    //   components: {
    //     SearchBar
    // },
    data() {
        return {
            listing_result: [],
            user_name: null
        };
    },
    mounted() {
        this.getListings();
    },
    methods: {
        async getListings() {
            this.user_name = await store.dispatch('callGetUser')
            let listingForm = new FormData();
            listingForm.append("username", this.user_name)
            const url = "http://127.0.0.1:5000/listings/getOwned"
            let result = await axios.post(url, listingForm)
            this.listing_result = result.data
            // console.log("listing_result is", this.listing_result)
        },
        goToListing(listing_id) {
            this.$router.push("/myListing/" + listing_id);
        },
    }
}
</script>