<template>
    <div class="listing">
        <v-sheet :elevation="24" :width="700" :height="800" :rounded="'xl'" color="green-lighten-3">
            <v-container fluid>
                <v-row class="mx-auto px-16 pt-16">
                    <v-col>
                        <v-row>
                            <h1>{{ this.singleListing.title }}</h1>
                        </v-row>
                        <v-row class="mx-auto  mb-16 pb-16">
                            <h3>${{ this.singleListing.price }}</h3>
                        </v-row>

                        <v-row class="mx-auto pt-5">
                            <!-- <ImgListing v-if=this.singleListing.listing_id ref="imgs"
                                :listing_id=this.singleListing.listing_id /> -->
                        </v-row>
                    </v-col>

                    <v-col>
                        <v-btn color="error" @click="deleteFunc">Delete</v-btn>
                        <v-row class="mx-auto py-16">
                            Description: {{ this.singleListing.description }}
                        </v-row>
                        <v-row class="mx-auto">
                            Status: {{ this.singleListing.status_name }}
                            <v-icon v-if="singleListing.status_id == 1" size="x-large" color="success"
                                icon="mdi-cart"></v-icon>
                            <v-icon v-else-if="singleListing.status_id == 2" size="x-large" color="warning"
                                icon="mdi-cart"></v-icon>
                            <v-icon v-else-if="singleListing.status_id == 3" size="x-large" color="error"
                                icon="mdi-cart"></v-icon>
                        </v-row>
                        <v-row class="mx-auto pb-16">
                            Preferred Delivery Method: {{ this.singleListing.method_name }}
                            <v-icon v-if="singleListing.delivery_id == 1" size="x-large" color="info"
                                icon="mdi-account-group"></v-icon>
                            <v-icon v-else-if="singleListing.delivery_id == 2" size="x-large" color="info"
                                icon="mdi-email-fast"></v-icon>
                            <v-icon v-else-if="singleListing.delivery_id == 3" size="x-large" color="info"
                                icon="mdi-truck-delivery"></v-icon>
                        </v-row>
                        <v-row>
                            <v-form @submit.prevent="submit">
                                <v-radio-group v-model="delivery_method" label="Preferred Delivery Method" inline
                                    required>
                                    <v-radio label="In-person Hand Off" :value="1"></v-radio>
                                    <v-radio label="Delivery" :value="2"></v-radio>
                                    <v-radio label="Pick-up" :value="3"></v-radio>
                                </v-radio-group>
                                <v-radio-group v-model="status_id" label="Listing Status" inline required>
                                    <v-radio label="On Sale" :value="1"></v-radio>
                                    <v-radio label="There is Interest" :value="2"></v-radio>
                                    <v-radio label="Sold" :value="3"></v-radio>
                                </v-radio-group>
                                <v-btn type="submit">
                                    Send
                                </v-btn>
                            </v-form>
                        </v-row>
                    </v-col>
                </v-row>
            </v-container>
        </v-sheet>
    </div>
</template>

<script>
import store from '@/stores';
import ImgListing from '../components/ImgListing.vue'
import axios from 'axios'


export default {
    name: 'myListing',
    components: {
        ImgListing
    },
    data() {
        return {
            rules: [v => v.length <= 256 || "Max 256 chracters", v => v.length > 0 || "Can't send an empty message"],
            singleListing: {},
            delivery_method: null,
            status_id: null,
            user_name: null,
        };
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
                    this.delivery_method = result.delivery_id;
                    this.status_id = result.status_id;
                    store.dispatch('callGetUser')
                        .then((res) => this.user_name = res)
                })
        },
        async submit(event) {
            const results = await event;
            console.log("I got", results.valid, " delivery_method value is", this.delivery_method, "and status_id is", this.status_id)

            if (results.valid) {
                let listingForm = new FormData();
                listingForm.append("delivery_id", this.delivery_method)
                listingForm.append("status_id", this.status_id)
                listingForm.append("listing_id", this.singleListing.listing_id)

                let response = await axios.post('http://127.0.0.1:5000/listings/update', listingForm)
                if (response.status = 200) {
                    this.$router.push("/myListings");
                }
                else {
                    this.error_message = "Sorry, an issue has occurred. Please refresh and try again."
                }
            }
        },
        async deleteFunc() {
            console.log("deleting")
            let deleteForm = new FormData();
            deleteForm.append("listing_id", this.singleListing.listing_id)

            let response = await axios.post('http://127.0.0.1:5000/listings/delete', deleteForm)
            if (response.status = 200) {
                this.$router.push("/myListings");
            }
            else {
                this.error_message = "Sorry, an issue has occurred. Please refresh and try again."
            }
        }
    }
}
</script>