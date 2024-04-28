<template>
  <h1>Account View</h1>
  Your name is {{ this.user_name }}
  {{ this.user_info }}
</template>

<script>
// import SearchBar from '../components/SearchBar.vue'
import axios from 'axios'
import store from '@/stores';
import router from '@/router';

export default {
  name: 'ListingsArray',
  data() {
    return {
      user_info: {},
      user_name: null
    };
  },
  mounted() {
    // this.getUsername(),
    this.getUserInfo();
  },
  methods: {
    getUsername() {
      store.dispatch('callGetUser')
        .then((res) => this.user_name = res)
    },
    getUserInfo() {
      const url = "http://127.0.0.1:5000/user/getUserInfo"
      let userForm = new FormData()
      store.dispatch('callGetUser')
        .then((res) => {
          this.user_name = res
          userForm.append("username", this.user_name)
          axios.post(url, userForm)
            .then((res) => {
              // console.log("RESULT FOUND ", res);
              console.log("USER DATA IS", res.data)
              this.user_info = res.data;
              // console.log("RESULT SHOULD BE THE SAME", this.result);
            })
        })

    }
  }
}
</script>

<!-- <template>
    <div class="account">
      <h1>This is an account page</h1>

        <ImgUpload/>
        <ImgListing/>
    </div>
  </template>
  <script>
    import ImgUpload from '../components/ImgUpload.vue'
    import ImgListing from '../components/ImgListing.vue'
  export default {
    name: "AccountView",
    components: {
        ImgUpload,
        ImgListing
    },
  };
  </script>

  <style>
  @media (min-width: 1024px) {
    .search {
      min-height: 100vh;
      display: flex;
      align-items: center;
    }
  }
  </style> -->