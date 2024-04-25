<script>
  // import SearchBar from '../components/SearchBar.vue'
  import axios from 'axios'
  import store from '@/stores';

  export default{
      name: 'ListingsArray',
    //   components: {
    //     SearchBar
    // },
      data() {
          return {
              listing_result: [],
              tag_result: [],
              all_clicked_tags: [],
          };
      },
      props: {
          msg: String
      },
      mounted() {
          this.getListings();
          this.getTags();
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
              // console.log("listing_result FOUND ", res);
              console.log("LISTING DATA IS", res.data)
              this.listing_result = res.data;
              // console.log(listing_result SHOULD BE THE SAME, this.listing_result);
          })
        },
        getTags() {
            const headers = {
                "Access-Control-Allow-Origin":"*",
                "Content-Type": "application/jsonp"
            }
            const url = "http://127.0.0.1:5000/tags/"
            axios.get(url, {headers})

            .then((res) => {
                // console.log("RESULT FOUND ", res);
                console.log("TAG DATA IS", res.data)
                this.tag_result = res.data;
                // console.log("RESULT SHOULD BE THE SAME", this.result);
                })
            },
        change_selected_tag(tag_id) {
                store.dispatch('callChangeTags', tag_id)
                .then(() => {
                  this.get_selected_tags();
                })
                .finally(() => {
                  this.getFilteredListings();
                });
            },
        get_selected_tags() {            
                store.dispatch('callTagGetter')
                .then((res) => {
                    this.all_clicked_tags = res;
                })
                return
            },
        getFilteredListings() {
          // if (this.all_clicked_tags.length === 0) {
          //   return
          // }
          // else{
          //   axios.post("listings/filter", this.all_clicked_tags)
          // .then((res) => {
          //   console.log("FILTERED LISTING DATA IS", res.data);
          //   this.listing_result = res.data;
          // })
          // }
          this.get_selected_tags()
          console.log("about to send to listings/filter")
          console.log(this.all_clicked_tags)
          axios.post("listings/filter", this.all_clicked_tags)
          .then((res) => {
            console.log("FILTERED LISTING DATA IS", res.data);
            this.listing_result = res.data;
          })
        },
        shouldListingShow(tag_id) {
            return this.all_clicked_tags.length === 0 || this.all_clicked_tags.includes(tag_id);
        }
    }
  }
</script>

<template>
          <!-- Narrow Search: <SearchBar /> -->
          <div>
            <div v-for="selected_tag in all_clicked_tags" :key="selected_tag[0]">
              <p>{{ selected_tag }}</p>
            </div>

            <v-card-text class="d-flex justify-space-between">
              <v-chip-group 
                v-for="tag in tag_result" 
                :key="tag.tag_id"
                column
                multiple
                selected-class="text-primary"
              >
                  <v-chip 
                  variant="elevated"
                  filter
                  @click="change_selected_tag(tag.tag_id)"
                  >
                      {{ tag.tag_name }}
                  </v-chip>
                </v-chip-group>
             </v-card-text>
          </div>

          <br/>
          
          <div>
            <div v-for="listing in listing_result" :key="listing.listing_id">
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
                    Tag: {{ listing.tag_id }}
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