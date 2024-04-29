<template>
  <div class="account">
    <h1>Chat about {{ convo.host_fname }}'s {{ convo.title }}</h1>
    <v-btn @click="viewListing">View Listing</v-btn>
    <v-btn color='red'>Delete Chat</v-btn>
    <v-sheet elevation="24" width="100vh" height="80vh" rounded="xl" color="green-lighten-3" overflow-y-auto>
      <v-container fluid height="100%">

        <div v-for="message in messages.slice().reverse()">

          <div v-if="message.author_id != uid">
            <v-col>

              <v-card class="pa-1 my-1" max-width='50%'>
                {{ message.text }}
              </v-card>

            </v-col>
          </div>
          <div v-else>
            <v-col>

              <v-row justify="end">
                <v-card class="pa-1 my-1" max-width='50%'>
                  {{ message.text }}
                </v-card>
              </v-row>

            </v-col>
          </div>
        </div>
      </v-container>

      <v-container justify="end">
        <v-col justify="end">
          <v-row justify="end">
            <v-form @submit.prevent="submit">
              <v-textarea clearable label="Type Message" variant="solo-filled" v-model="new_message"
                bg-color="grey-lighten-2" counter :rules="rules" no-resize></v-textarea>
              <v-btn type="submit">
                Send
              </v-btn>
            </v-form>
          </v-row>
        </v-col>
      </v-container>

    </v-sheet>


  </div>
</template>



<script>

import axios from 'axios'
import store from '@/stores';
import router from '@/router';

export default {


  name: 'Chat',
  data() {
    return {
      convo: [],
      messages: [],
      new_message: "",
      rules: [v => v.length <= 256 || "Max 256 chracters", v => v.length > 0 || "Can't send an empty message"],
    };
  },
  mounted() {
    this.getConvo(this.$route.params.id)
  },
  computed: {
    uid: function () { return store.getters.get_user }

  },
  methods: {
    getConvo(id) {
      const headers = {
        "Access-Control-Allow-Origin": "*",
        "Content-Type": "application/jsonp"
      }

      const url = "http://127.0.0.1:5000/conversations/" + id;

      axios.get(url, { headers })

        .then((res) => {
          console.log("Convo DATA IS", res.data)
          if (this.uid != res.data['host_id'] && this.uid != res.data['customer_id']) {
            this.$router.push("/chats");
          }
          this.convo = res.data;
          this.messages = res.data['message_array']

        })
    }, async submit(event) {
      const results = await event;
      console.log("I got", results.valid, " value is", this.new_message)

      if (results.valid) {
        let UserForm = new FormData()

        UserForm.append('listing_id', this.convo['listing_id'])
        UserForm.append('host_id', this.convo['host_id'])
        UserForm.append('customer_id', this.convo['customer_id'])
        UserForm.append('new_message', this.new_message)
        UserForm.append('user_id',  this.uid)
        let res = await axios.post('conversations/send', UserForm)

        console.log(res)
        this.getConvo(this.$route.params.id)
      }

    },
    viewListing() {
      this.$router.push("/listing/" + this.convo['listing_id']);
    }
  }
}
</script>