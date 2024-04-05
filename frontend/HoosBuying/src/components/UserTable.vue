<template>
    <div class="about">
      <h1>User table starts</h1>
      <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>username</th>
                    <th>password</th>
                    <th>first name</th>
                    <th>last name</th>
                    <th>computing ID</th>
                    <th>Address</th>
                    <th>Phone Number</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="user in result" :key="user.id">
                    <td>{{user.uid}}</td>
                    <td>{{user.username}}</td>
                    <td>{{user.password}}</td>
                    <td>{{user.fname}}</td>
                    <td>{{user.lname}}</td>
                    <td>{{user.computing_id}}</td>
                    <td>{{user.address}}</td>
                    <td>{{user.phone_number}}</td>

                    <!-- <td>Doe</td>
                    <td>john@example.com</td> -->
                </tr>
            </tbody>
        </table>
    </div>
  </template>
  
  <style>
  @media (min-width: 1024px) {
    .about {
      min-height: 100vh;
      display: flex;
      align-items: center;
    }
  }
  </style>
  
<script>
    import axios from 'axios'

    export default{
        name: 'UserTable',
        data() {
            return {
                result: [],
            };
        },
        props: {
            msg: String
        },
        mounted() {
            this.GetEmployee();
        },
        methods: {
            GetEmployee() {
                const headers = {
                    "Access-Control-Allow-Origin":"*",
                    "Content-Type": "application/jsonp"
                }
                const url = "http://127.0.0.1:5000/getAllUsers"
                axios.get(url, {headers})
                .then((res) => {
                    console.log("RESULT FOUND ", res);
                    console.log("DATA IS", res.data)
                    this.result = res.data;
                    console.log("RESULT SHOULD BE THE SAME", this.result);
                })
            }
        }
    }
</script>