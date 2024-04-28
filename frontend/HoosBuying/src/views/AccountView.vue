<template>
  <h3 v-if="error_message">Error: {{ error_message }}</h3>
  <v-container>
    <v-row>
      <h1 v-if="user_name">Welcome, {{ this.user_name }}</h1>
    </v-row>
    <v-row>
      <v-sheet :elevation="24" :width="700" :height="600" :rounded="'xl'" color="green-lighten-3">
        <v-form @submit.prevent="submit">
          <v-row>
            <v-text-field v-model="fname" :rules="first_name_rules" label="First Name" readonly>
            </v-text-field>
            <v-text-field v-model="lname" :rules="last_name_rules" label="Last Name" readonly>
            </v-text-field>
          </v-row>
          <v-row>
            <!-- password -->
          </v-row>
          <v-row>
            <!-- phone number -->
            <v-text-field v-model="phone_number" :rules="phone_number_rules" label="Phone Number" required clearable>
            </v-text-field>
          </v-row>
          <v-row>
            <!-- Address -->
            <v-text-field v-model="address" :rules="address_rules" label="Address" required :counter="255" clearable>
            </v-text-field>
          </v-row>
          <v-btn type="submit" block>
            Update User
          </v-btn>
        </v-form>
      </v-sheet>
    </v-row>
  </v-container>
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
      user_name: null,
      address: null,
      address_rules: [
        value => {
          if (value) return true
          return 'Address is required'
        },
        value => {
          if (value?.length <= 255) return true

          return 'Address must be less than 255 characters'
        }
      ],
      computing_id: null,
      fname: null,
      first_name_rules: [
        value => {
          if (value) return true
          return 'First Name is required'
        },
        value => {
          if (value?.length <= 100) return true

          return 'First Name must be less than 100 characters'
        }
      ],
      lname: null,
      last_name_rules: [
        value => {
          if (value) return true
          return 'Last Name is required'
        },
        value => {
          if (value?.length <= 100) return true

          return 'Last Name must be less than 100 characters'
        }
      ],
      phone_number: null,
      phone_number_rules: [
        value => {
          if (value?.length == 12) return true

          return 'Please enter valid phone number'
        }
      ],
      error_message: null,
    };
  },
  mounted() {
    this.getUserInfo();
  },
  methods: {
    getUserInfo() {
      const url = "http://127.0.0.1:5000/user/getUserInfo"
      let userForm = new FormData()
      store.dispatch('callGetUser')
        .then((username) => {
          this.user_name = username
          userForm.append("username", this.user_name)
          axios.post(url, userForm)
            .then((res) => {
              // console.log("RESULT FOUND ", res);
              console.log("USER DATA IS", res.data)
              this.address = res.data.address
              this.computing_id = res.data.computing_id
              this.fname = res.data.fname
              this.lname = res.data.lname
              this.phone_number = res.data.phone_number
              // console.log("RESULT SHOULD BE THE SAME", this.result);
            })
        })
    },
    async submit() {
      const url = "http://127.0.0.1:5000/user/update"
      let userForm = new FormData()
      userForm.append("address", this.address)
      userForm.append("computing_id", this.computing_id)
      userForm.append("fname", this.fname)
      userForm.append("lname", this.lname)
      userForm.append("phone_number", this.phone_number)

      let response = await axios.post(url, userForm)
      if (response.status = 200) {
          this.getUserInfo();
        }
        else {
          this.error_message = "Sorry, an issue has occurred. Please refresh and try again."
        }
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