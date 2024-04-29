<template>

  <v-container  fluid class="red ma-0">
    
      <v-row>
        <v-select label="Messages" v-model="filter" :items="['All', 'Only Buying', 'Only Selling']" />
      </v-row>
      <div v-for="convo in conversations" :key="convo.convo_id">


          <v-col>
          <v-card @click="goToConversation(convo.convo_id)">
            <v-card-item>
              <v-card-title>{{ convo.title }} </v-card-title>

              Sale Status: {{ convo.status_name }}

              <v-icon v-if="convo.status_id == 1" size="x-large" color="success" icon="mdi-cart"></v-icon>
              <v-icon v-else-if="convo.status_id == 2" size="x-large" color="warning" icon="mdi-cart"></v-icon>
              <v-icon v-else-if="convo.status_id == 3" size="x-large" color="error" icon="mdi-cart"></v-icon>


              <v-card-subtitle v-if="convo.customer_id == uid">{{ convo.host_fname }} {{ convo.host_lname
                }}</v-card-subtitle>
              <v-card-subtitle v-else>{{ convo.cust_fname }} {{ convo.cust_lname }}</v-card-subtitle>
            </v-card-item>

            <v-card-item>
              <p>{{ convo.message_array[0].text }}</p>
            </v-card-item>
            <v-card-item>
              <small>Last Message {{ convo.last_updated }}</small>
            </v-card-item>
          </v-card>
        </v-col>

      </div>
    
  </v-container>
  <div v-if="!this.conversations || this.conversations.length === 0">
    <h1>No Conversations Yet!</h1>
  </div>

</template>


<script>
// import SearchBar from '../components/SearchBar.vue'
import axios from 'axios'
import store from '@/stores';
import router from '@/router';

export default {
  name: 'ChatListView',
  data() {
    return {
      conversations: [],
      filter: "All"
    };
  },
  watch: {
    filter(val) {
      this.filter = val;
      this.getConversations();
    }
  },
  computed: {
    uid: function () { return store.getters.get_uid }
  },
  mounted() {


    this.getConversations();
  },
  methods: {
    getConversations() {
      this.conversations = [];
      const headers = {
        "Access-Control-Allow-Origin": "*",
        "Content-Type": "application/jsonp"
      }

      let url = "";
      if (this.filter == 'Only Buying') {
        // console.log("Only Buying")
        url = "http://127.0.0.1:5000/conversations/getCustomer/" + this.uid;
      }
      else if (this.filter == 'Only Selling') {
        // console.log("Only Selling")
        url = "http://127.0.0.1:5000/conversations/getOwner/" + this.uid;
      }
      else
        url = "http://127.0.0.1:5000/conversations/getAll/" + this.uid;

      axios.get(url, { headers })

        .then((res) => {
          // console.log("LISTING DATA IS", res.data)
          this.conversations = res.data;
        })
    },
    goToConversation(convo_id) {
      this.$router.push("/chats/" + convo_id);
    },
  }
}
</script>


<style>
@media (min-width: 1024px) {
  .chat {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
