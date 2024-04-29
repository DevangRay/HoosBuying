<template>
  <div class="account">
    <h1>This is a chat page</h1>


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
    };
  },
  mounted() {
    this.getConvo(this.$route.params.id)
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
          this.convo = res.data;
        })
    },
  }
}
</script>