<template>
  <h3 v-if="error_message">Error: {{ error_message }}</h3>
  <v-container>
    <v-row>
      <h1 v-if="user_name">Welcome, {{ this.user_name }}</h1>
    </v-row>
    <v-row>
      <v-sheet :elevation="24" :width="700" :height="400" :rounded="'xl'" color="green-lighten-3">
        <v-form @submit.prevent="submitOther">
          <v-row>
            <v-text-field v-model="fname" :rules="first_name_rules" label="First Name" readonly>
            </v-text-field>
            <v-text-field v-model="lname" :rules="last_name_rules" label="Last Name" readonly>
            </v-text-field>
          </v-row>
          <v-row>
            <v-text-field v-model="computing_id" label="Computing ID" readonly>
            </v-text-field>
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
          <h4 v-if="success_message">{{ success_message }}</h4>
          <v-btn type="submit" block>
            Update User
          </v-btn>
        </v-form>
      </v-sheet>
    </v-row>
    <v-row>
      <v-sheet :elevation="24" :width="700" :height="300" :rounded="'xl'" color="green-lighten-3">
        <v-form @submit.prevent="submitPassword">
          <v-row>
            <v-col>
              <v-text-field v-model="curr_password" label="Current Password" :rules="password_rules"
                :append-icon="show_curr ? 'mdi-eye' : 'mdi-eye-off'" :type="show_curr ? 'text' : 'password'"
                @click:append="show_curr = !show_curr" :counter="100">
              </v-text-field>
            </v-col>
            <v-col>
              <v-text-field v-model="unconf_new_password" label="New Password" :rules="password_rules"
                :append-icon="show_new_unconf ? 'mdi-eye' : 'mdi-eye-off'" :type="show_new_unconf ? 'text' : 'password'"
                @click:append="show_new_unconf = !show_new_unconf" :counter="100">
              </v-text-field>
              <v-text-field v-model="conf_new_password" label="Confirm New Password" :rules="password_rules"
                :append-icon="show_new_conf ? 'mdi-eye' : 'mdi-eye-off'" :type="show_new_conf ? 'text' : 'password'"
                @click:append="show_new_conf = !show_new_conf" :counter="100">
              </v-text-field>
            </v-col>
          </v-row>
          <h4 v-if="password_error_message"> {{ this.password_error_message }}</h4>
          <v-btn type="submit" block>
            Update Password
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
import bcrypt from 'bcryptjs'

export default {
  name: 'ListingsArray',
  data() {
    return {
      user_name: null,
      stored_password: null,
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
      password_error_message: null,
      curr_password: "",
      show_curr: true,
      show_new_unconf: true,
      show_new_conf: true,
      unconf_new_password: "",
      conf_new_password: "",
      success_message: "",
      password_rules: [
        value => {
          if (value) return true
          return 'Password can not be empty'
        },
        value => {
          if (value?.length <= 100) return true

          return 'Password must be less than 100 characters'
        },
        
      ]
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
              // console.log("USER DATA IS", res.data)
              this.address = res.data.address
              this.computing_id = res.data.computing_id
              this.fname = res.data.fname
              this.lname = res.data.lname
              this.phone_number = res.data.phone_number
              this.stored_password = res.data.password
              // console.log("RESULT SHOULD BE THE SAME", this.result);
            })
        })
    },
    async submitOther() {
      this.success_message = "";
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
        this.success_message = "Succesfully updated!"
      }
      else {
        this.error_message = "Sorry, an issue has occurred. Please refresh and try again."
      }
    },
    async submitPassword() {
      if (this.unconf_new_password == this.conf_new_password) {
        // unhashed new vs hashed old
        // console.log(bcrypt.compareSync(this.conf_new_password, this.stored_password))
        if (!bcrypt.compareSync(this.curr_password, this.stored_password)) {
          // current password and stored do not match
          this.password_error_message = "Invalid current password"
        }
        else if (bcrypt.compareSync(this.conf_new_password, this.stored_password)) {
          // new password and stored do match
          this.password_error_message = "Old and New Passwords must be different"
        }
        else {
          const saltRounds = 10;
          const hashed_conf_new_password = await bcrypt.hash(this.conf_new_password, saltRounds)
          const url = "http://127.0.0.1:5000/user/updatePassword"

          let passForm = new FormData()
          passForm.append("computing_id", this.computing_id)
          passForm.append("password", hashed_conf_new_password)

          let response = await axios.post(url, passForm)
          if (response.status != 200) {
            this.password_error_message = "Sorry, an issue has occurred. Please refresh and try again."
          }
          else{
            this.curr_password = ""
            this.unconf_new_password = ""
            this.conf_new_password = ""
            this.password_error_message = "Successfully changed password"
          }
        }
      }
      else {
        this.password_error_message = "New Passwords do not match"
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