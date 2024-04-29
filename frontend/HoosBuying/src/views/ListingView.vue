<template>
  <div class="listing">
    <!-- <h1>This is a listing page</h1> -->
    <!-- {{ $route.params.id }} | {{ id }} | {{ this.singleListing }} -->
    <!-- {{this.singleListing}} -->
    <!-- USER ID: {{ this.user_name }} -->
    <v-sheet :elevation="24" :width="700" :height="600" :rounded="'xl'" color="green-lighten-3">
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
              <ImgListing v-if=this.singleListing.listing_id ref="imgs" :listing_id=this.singleListing.listing_id />
            </v-row>
          </v-col>

          <v-col>
            <v-row class="mx-auto py-16">
              {{ this.singleListing.description }}
            </v-row>
            <v-row class="mx-auto">
              Status: {{ this.singleListing.status_name }}
              <v-icon v-if="singleListing.status_id == 1" size="x-large" color="success" icon="mdi-cart"></v-icon>
              <v-icon v-else-if="singleListing.status_id == 2" size="x-large" color="warning" icon="mdi-cart"></v-icon>
              <v-icon v-else-if="singleListing.status_id == 3" size="x-large" color="error" icon="mdi-cart"></v-icon>
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
            <v-row v-if="singleListing['owner_id'] != this.uid">
              <v-form @submit.prevent="submit">
                <v-textarea clearable label="Start a conversation!" variant="solo-filled" v-model="placeholder"
                  bg-color="grey-lighten-2" :rules="rules" counter no-resize></v-textarea>
                <p v-if="errorMessage">{{ errorMessage }}</p>
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
  name: 'SingleListing',
  components: {
    ImgListing
  },
  data() {
    return {
      rules: [v => v.length <= 256 || "Max 256 chracters", v => v.length > 0 || "Can't send an empty message"],
      singleListing: {},
      user_name: null,
      placeholder: null,
      errorMessage:null,
    };
  },
  props: {
    msg: String
  },
  computed: {
    uid: function () { return store.getters.get_uid}
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
          store.dispatch('callGetUser')
            .then((res) => this.user_name = res)
          this.placeholder = "Hello, I am interested in " + String(result.title)
        })
    },
    async submit(event) {
      const results = await event;
      console.log("I got", results.valid, " value is", this.placeholder)

      if (results.valid) {
        // SEND MESSAGE HERE
        this.errorMessage = null;
        let UserForm = new FormData()

        UserForm.append('listing_id', this.singleListing['listing_id'])
        UserForm.append('host_id', this.singleListing['owner_id'])
        UserForm.append('customer_id', this.uid)
        UserForm.append('new_message', this.placeholder)
        UserForm.append('user_id', this.uid)
        try{
        let res = await axios.post('conversations/send', UserForm)
        console.log(res)
        this.$router.push("/chats/"+res.data['convo_id'])
        }
        catch(e){
          console.log(e)
          this.errorMessage = "Error sending message"
        }


        // MESSAGE IS IN this.placeholder variable
      }

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
