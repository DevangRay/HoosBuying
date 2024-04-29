<template>
    <div class="register">
      <div>
        <form @submit.prevent="submit">
          <div>
            <label for="username">Username:</label>
            <input type="text" name="username" v-model="form.username" />
          </div>
          <div>
            <label for="fname">First Name:</label>
            <input type="text" name="fname" v-model="form.fname" />
          </div>
          <div>
            <label for="lname">Last Name:</label>
            <input type="text" name="lname" v-model="form.lname" />
          </div>
          <div>
            <label for="computing_id">Computing ID:</label>
            <input type="text" name="computing_id" v-model="form.computing_id" />
          </div>
          <div>
            <label for="address">Address:</label>
            <input type="text" name="address" v-model="form.address" />
          </div>
          <div>
            <label for="phone_number">Phone Number:</label>
            <input type="text" name="phone_number" v-model="form.phone_number" />
          </div>
          <div>
            <label for="password">Password:</label>
            <input type="password" name="password" v-model="form.password" />
          </div>
          <div>
            <label for="password">Re-Enter Password:</label>
            <input type="password" name="rePassword" v-model="form.rePassword" />
          </div>
          <button type="submit">Register</button>
        </form>
      </div>
      <p v-if="showError" id="error">{{ errorMessage }}</p>
      <router-link to="/login">Already a user? Log in.</router-link>
    </div>
  </template>
  
  <script>
  import { mapActions } from "vuex";
  
  export default {
    name: "Register",
    components: {},
    data() {
      return {
        form: {
          username: "",
          password: "",
          rePassword: "",
          fname: "",
          lname: "",
          computing_id: "",
          address: "",
          phone_number: "",
        },
        showError: false,
        errorMessage: ""
      };
    },
    methods: {
      ...mapActions(["Register"]),
      async submit() {
        this.showError = false;
        this.errorMessage = "";
        if(this.form.password != this.form.rePassword){
          this.showError = true;
          this.errorMessage = "Passwords do not match"
        }
        try {
          await this.Register(this.form);
          this.$router.push("/");
          this.showError = false
        } catch (error) {
          // console.log(error)
          this.errorMessage = "Failed to create new user!"
          this.showError = true
        }
      },
    },
  };
  </script>
  <style scoped>
  * {
    box-sizing: border-box;
  }
  
  label {
    padding: 12px 12px 12px 0;
    display: inline-block;
  }
  
  button[type="submit"] {
    background-color: #4caf50;
    color: white;
    padding: 12px 20px;
    cursor: pointer;
    border-radius: 30px;
  }
  
  button[type="submit"]:hover {
    background-color: #45a049;
  }
  
  input {
    margin: 5px;
    box-shadow: 0 0 15px 4px rgba(0, 0, 0, 0.06);
    padding: 10px;
    border-radius: 30px;
  }
  #error {
    color: red;
  }
  </style>