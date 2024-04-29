import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import store from '../stores'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/SearchView.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/account',
      name: 'account',
      component:  () => import('../views/AccountView.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/Login.vue'),
      meta: { guest:true},
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/Register.vue'),
      meta: { guest:true},
    },
    {
      path: '/search',
      name: 'search',
      component: () => import('../views/SearchView.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/chats',
      name: 'chats',
      component: () => import('../views/ChatListView.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/chats/:id',
      name: 'chat',
      component: () => import('../views/ConversationView.vue'),
      props: true,
      meta: { requiresAuth: true },
    },
    {
      path: '/listing/:id',
      name: 'listing',
      component: () => import('../views/ListingView.vue'),
      props: true,
      meta: { requiresAuth: true },
    },
    {
      path: '/insertListing',
      name: 'insertListing',
      component: () => import('../views/InsertListing.vue'),
      props: true,
      meta: { requiresAuth: true },
    },
    {
      path: '/myListings',
      name: 'myListings',
      component: () => import('../views/MyListing.vue'),
      props: true,
      meta: { requiresAuth: true },
    },
    {
      path: '/myListing/:id',
      name: 'myListing',
      component: () => import('../views/MySingleListing.vue'),
      props: true,
      meta: { requiresAuth: true },
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/logout',
      name: 'logout',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/LogoutView.vue')
    },
    {
      path: '/searchBar',
      name: 'searchBar',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../components/SearchBar.vue')
    },
    {
      path: '/getAllUsers',
      name: 'getAllUsers',
      component: () => import('../views/UsersView.vue'),
      meta: { requiresAuth: true },
    }
  ],
  
})

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      // check token
      console.log("checking token");
      store.dispatch('checkToken')
      .then((res) => {
        if (!res){
          console.log(res, "is result")
          store.dispatch("LogOut");
        }
      });
      console.log("finished checking token");
      next();
      return;
    }
    next("/login");
  } else {
    next();
  }
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.guest)) {
    if (store.getters.isAuthenticated) {
      next("/");
      return;
    }
    next();
  } else {
    next();
  }
});

export default router
