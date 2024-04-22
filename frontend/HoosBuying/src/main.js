import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import store from './stores';
import axios from 'axios';
const app = createApp(App)
axios.defaults.baseURL = "http://127.0.0.1:5000/";


app.use(createPinia())
app.use(store)
app.use(router)

app.mount('#app')
