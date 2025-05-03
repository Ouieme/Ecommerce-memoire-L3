import { createStore } from "vuex";
import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

export default createStore({
  state: {
    //----userinoo -->
    user: null,
    //admin
    admin:null,
    //--cart
    cart: {
      items: [],
    },
    isAuthenticated: false,
    token: "",
    isLoading: false,
  },
  //---user---
  mutations: {
    setUser(state, user) {
      state.user = user;
    },

      setAdmin(state, value) {
        state.admin = value;
      },

    initializeStore(state) {
      if (localStorage.getItem("cart")) {
        state.cart = JSON.parse(localStorage.getItem("cart"));
      } else {
        localStorage.setItem("cart", JSON.stringify(state.cart));
      }

      if (localStorage.getItem("token")) {
        state.token = localStorage.getItem("token");
        state.isAuthenticated = true;
      } else {
        state.token = "";
        state.isAuthenticated = false;
      }

    },
    //-----cart-----
    addToCart(state, item) {
      const exists = state.cart.items.filter(
        (i) => i.product.id === item.product.id
      );
      if (exists.length) {
        exists[0].quantity =
          parseInt(exists[0].quantity) + parseInt(item.quantity);
      } else {
        state.cart.items.push(item);
      }

      localStorage.setItem("cart", JSON.stringify(state.cart));
    },
    setIsLoading(state, status) {
      state.isLoading = status;
    },
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.token = "";
      state.isAuthenticated = false;
    },
    clearCart(state) {
      state.cart = { items: [] };

      localStorage.setItem("cart", JSON.stringify(state.cart));
    },
  },
  actions: {
    //----user---
    fetchUser({ commit }, userId) {
      return axios
        .get(`http://localhost:8000/api/v1/user/${userId}`)
        .then((response) => {
          commit("setUser", response.data);
        })
        .catch((error) => {
          console.error(error);
          alert("An error occurred while fetching the user data.");
        });
    },
    //----admin---
    fetchadmin({ commit }, userId) {
      return axios
        .get(`http://localhost:8000/api/v2/admin/${userId}`)
        .then((response) => {
          commit("setadmin", response.data);
        })
        .catch((error) => {
          console.error(error);
          alert("An error occurred while fetching the user data.");
        });
    },
  },
  getters: {
    getUser: (state) => state.user,
    getadmin: (state) => state.admin,

  },
 
  modules: {},
});