<template>
    {{ this.error_message }}
    <v-sheet :elevation="24" :width="700" :height="600" :rounded="'xl'" color="green-lighten-3">
      <v-form @submit.prevent="submit">
        <!-- title -->
        <v-text-field
            v-model="title"
            label="Listing Title"
            :counter="100"
            :rules="titleRules"
            required>
        </v-text-field>
        <!-- price -->
        <v-text-field
            v-model="price"
            label="price"
            prefix="$"
            :rules="priceRules"
            >
        </v-text-field>
        <!-- tags -->
         <v-select label="Listing Tag"
         :items="['Furniture', 'Technology', 'Storage', 'Diningware', 'Textbooks', 'Clothes', 'Accessories', 'Miscellaneous']"
         required
         v-model="tag">
        </v-select>
        <!-- description -->
        <v-textarea
            v-model="description"
            label="Listing Description"
            :counter="512"
            :rules="descriptionRules"
            required
            clearable
            no-resize>
        </v-textarea>
        <!-- delivery -->
        <v-radio-group v-model = "delivery_method" label="Preferred Delivery Method" inline required>
            <v-radio label="In-person Hand Off" :value="1"></v-radio>
            <v-radio label="Delivery" :value="2"></v-radio>
            <v-radio label="Pick-up" :value="3"></v-radio>
        </v-radio-group>
        <v-btn
            type="submit"
            block> 
            Create New Listing
        </v-btn>
      </v-form>
    </v-sheet>
</template>

<script>
import axios from 'axios';
import store from '@/stores';

export default{
      name: 'SingleListing',
    //   components: {
    //     SearchBar
    // },
      data() {
          return {
              title: "",
              titleRules: [
                value => {
                    if (value) return true
                    return 'Title is required'
                },
                value => {
                    if (value?.length <= 100) return true

                    return 'Title must be less than 100 characters'
                }
              ],
              price: 0.0,
              priceRules: [
                value => {
                    if (isNaN(value) || value <= 0) return 'Please enter a valid price'
                    return true 
                }
              ],
              tag: 'Miscellaneous',
              description: "",
              descriptionRules: [
                value => {
                    if (value) return true
                    return 'Description is required'
                },
                value => {
                    if (value?.length <= 512) return true

                    return 'Description must be less than 512 characters'
                }
              ],
              delivery_method: 1,
              status: 1,
              user_name: null,
              error_message: null
          };
      },
      props: {
          msg: String
      },
      mounted() {
        this.getUser()
      },
      methods: {
        getUser() {
            store.dispatch('callGetUser')
            .then((res) => this.user_name = res)
        },
        async submit(event) {
        const results = await event;
        console.log("I got", results.valid)

        if (results.valid) {
          // SEND MESSAGE HERE
          let tag_id = 0;
          if (this.tag === "Furniture") {
            tag_id = 1;
          }
          else if (this.tag === "Technology") {
            tag_id = 2;
          }
          else if (this.tag === "Storage") {
            tag_id = 3;
          }
          else if (this.tag === "Diningware") {
            tag_id = 4;
          }
          else if (this.tag === "Textbooks") {
            tag_id = 5;
          }
          else if (this.tag === "Clothes") {
            tag_id = 6;
          }
          else if (this.tag === "Accessories") {
            tag_id = 7;
          }
          else if (this.tag === "Miscellaneous") {
            tag_id = 8;
          }
          
          let listingForm = new FormData()
          listingForm.append('description', this.description)
          listingForm.append('status_id', this.status)
          listingForm.append('delivery_id', this.delivery_method)
          listingForm.append('title', this.title)
          listingForm.append('price', this.price)
          listingForm.append('tag_id', tag_id)
          listingForm.append('owner_uname', this.user_name)
          let response = await axios.post('http://127.0.0.1:5000/listings/insert', listingForm)
          if (response.status = 200) {
            this.$router.push("/");
          }
          else{
            this.error_message = "Sorry, an issue has occurred. Please refresh and try again."
          }
        }
        
      }
    }
  }
</script>