import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Product from '../views/Product.vue'
import ProCat from  '../views/ProCat.vue'
import Shop from '../views/Shop.vue'
import Stores from '../views/Stores.vue'
import SingleStore from '../views/SingleStore.vue';
import About from '../views/About.vue'
import Contact from '../views/Contact.vue'
import StarRating from '../views/StarRating.vue'
import Cart from '../views/Cart.vue'
import Checkout from '../views/Checkout.vue'
import Success from '../views/Success.vue'
import Paymentmethod from '@/components/Paymentmethod.vue'
import UserManger from '../views/usermanager.vue'
import admin from '../views/admin.vue'
import update from '@/components/AdminUpdateComp.vue'
import storedemands from '@/components/StoresDemands.vue'
import addAdmin from '@/components/addAdmin.vue'
import complaines from '@/components/complaines.vue'
import store from "../store";




const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/categories',
    name: 'categories',
    component: () => import('../views/Categories.vue')
  },
  {
    path: '/:category_slug/:product_slug',
    name: 'Product',
    component: Product
  },
  {
    path: '/Stores/:slug', 
    name: 'SingleStore',
    component: SingleStore,
    
  },
  {
    path: '/complaines', 
    name: 'complaines',
    component: complaines,
    
  },
  {
    path: "/procat/:categorySlug",
    name: "procat",
    component: ProCat,
  },
  {
    path: "/Shop",
    name: "Shop",
    component: Shop,
  },
  {
    path: "/Stores",
    name: "Stores",
    component: Stores,
  },
  {
    path: "/About",
    name: "About",
    component: About,
  },
  {
    path: "/Contact",
    name: "Contact",
    component: Contact,
  },
  {
    path: "/StarRating",
    name: "StarRating",
    component: StarRating,
  },
 
  {
    path: '/storedemands',
    name: 'storedemands',
    component: storedemands
  },
  
  {
    path: "/sign-up",
    name: "SignUp",
    component: () => import("../views/SignUp.vue"),
  },
  {
    path: "/log-in",
    name: "LogIn",
    component: () => import("../views/LogIn.vue"),
  },
  {
    path: '/UserManger',
    name: 'UserManger',
    component: UserManger
  },

  {
    path: '/my-account',
    name: 'MyAccount',
    component: () => import("../views/MyAccount.vue"),
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/admin',
    name: 'admin',
    component: admin
  },

  {
    path: '/UserManger',
    name: 'UserManger',
    component: UserManger
  },
  {
    path: '/admin/:id/update',
    name: 'update',
    component: update

  },
  {
    path: '/addAdmin',
    nam: 'addAdmin',
    component: addAdmin
  },
  {
    path: '/Paymentmethod',
    nam: 'Paymentmethod',
    component: Paymentmethod

  },
  {
    path: "/my-account",
    name: "MyAccount",
    component: () => import("../views/MyAccount.vue"),
    meta: {
      requireLogin: true,
    },
    props: true,
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/cart/success',
    name: 'Success',
    component: Success
  },
  {
    path: '/cart/checkout',
    name: 'Checkout',
    component: Checkout,
    meta: {
        requireLogin: true
    }
  
  },


];
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});
router.beforeEach((to, from, next) => {
  if (
    to.matched.some((record) => record.meta.requireLogin) &&
    !store.state.isAuthenticated
  ) {
    next({ name: "LogIn", query: { to: to.path } });
  } else {
    next();
  }
});
export default router;
