<template>
  <div class="containe">
    <div class="columns has-fullheight">
      <div class=" sidebar column is-one-fifth mr-5 has-fullheight" style="
            background-color: #fff;
            border-right: px solid #b2b2b2;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
          ">
        <div class=" has-fullheight">
          <p class="menu-label is-size-5">
            <span class="icon">
              <i class="fas fa-user-circle"></i>
            </span>
            <span class="label-text has-text-success ml-2">{{
              CurrentUser.username
            }}</span>
          </p>
          <ul class="menu-list">
            <li :class="{ 'is-active': selectedOption === 'details' }">
              <a @click="selectOption('details')">
                <i class="fas fa-user"></i>
                <span class="menu-item">My Details</span>
              </a>
            </li>
            <li :class="{ 'is-active': selectedOption === 'orders' }">
              <a @click="selectOption('orders')">
                <i class="fas fa-file-invoice"></i>
                <span class="menu-item">My Orders</span>
              </a>
            </li>
            <li :class="{ 'is-active': selectedOption === 'reclamations' }">
              <a @click="selectOption('reclamations')">
                <i class="fas fa-exclamation-circle"></i>
                <span class="menu-item">My Reclamations</span>
              </a>
            </li>
            <li :class="{ 'is-active': selectedOption === 'settings' }">
              <a @click="selectOption('settings')">
                <i class="fas fa-cog"></i>
                <span class="menu-item">Settings</span>
              </a>
            </li>
            <li :class="{ 'is-active': selectedOption === 'checkout' }">
              <a class="logout-icon" @click="selectOption('checkout')">
                <i class="fas fa-sign-out-alt"></i>
                <span class="menu-item is-danger" @click="logout()">Log out</span>
              </a>
            </li>
          </ul>
        </div>
      </div>
      <!-- div of containe -->
      <div class="column" style="background-color: #fff">
        <!-- ditails containe  -->
        <form v-on:@submit="updateUserInformation">
          <div v-if="selectedOption === 'details'">
            <h2 class="title has-text-primary is-4">Profile Details</h2>
            <div class="details-content">
              <div class="field columns is-multiline">
                <div class="control column is-half">
                  <label class="label">First Name</label>
                  <input type="text" class="input is-blue" placeholder="First name" autocomplete="false"
                    v-model="CurrentUser.first_name" />
                </div>
                <div class="control column is-half">
                  <label class="label">Last Name</label>
                  <input type="text" class="input is-blue" placeholder="Last name" autocomplete="false"
                    v-model="CurrentUser.last_name" />
                </div>
                <div class="control column is-half">
                  <label class="label">Birth Date</label>
                  <div class="control">
                    <input type="datetime" class="input is-blue" placeholder="Date of birth" autocomplete="false"
                      v-model="CurrentCompte.date_nes" />
                  </div>
                </div>
                <div class="control column is-half">
                  <label class="label">Phone Number</label>
                  <div class="control">
                    <input type="number" class="input is-blue" placeholder="phone" autocomplete="false"
                      v-model="CurrentCompte.telephone" />
                  </div>
                </div>
                <div class="control column is-half">
                  <label class="label">Adresse</label>
                  <div class="control">
                    <input type="text" class="input is-blue" placeholder="User name" autocomplete="false"
                      v-model="CurrentCompte.adresse" />
                  </div>
                </div>
                <div class="control column is-half">
                  <label class="label">Identification Number</label>
                  <div class="control">
                    <input type="number" class="input is-blue" placeholder="Identification number" autocomplete="false"
                      v-model="CurrentCompte.num_ident" />
                  </div>
                </div>
                <div class="control column is-half">
                  <label class="label">Email</label>
                  <div class="control">
                    <input type="email" class="input is-blue" placeholder="Email" autocomplete="false"
                      v-model="CurrentUser.email" />
                  </div>
                </div>
                <div class="control column is-half">
                  <label class="label">User Name</label>
                  <div class="control">
                    <input type="text" class="input is-blue" placeholder="User name" autocomplete="false"
                      v-model="CurrentUser.username" />
                  </div>
                </div>
                <div class="control column is-half">
                  <label class="label">Current Password</label>
                  <div class="control">
                    <input ref="currentPassword" type="password" class="input is-blue" placeholder="Current Password"
                      autocomplete="false" v-model="CurrentUser.oldpassword" />
                  </div>
                </div>
                <div class="control column is-half">
                  <label class="label">New password</label>
                  <div class="control">
                    <input ref="newPassword" type="password" class="input is-blue" placeholder="New password"
                      autocomplete="false" v-model="CurrentUser.password" />
                  </div>
                </div>
              </div>
              <!-- button to make update -->
              <div class="field is-grouped mt-5">
                <div class="control ml-auto">
                  <button class="button" style="background-color: #ff6e31; color: white"
                    @click.prevent="updateUserInformation">
                    Update Details
                  </button>
                </div>
              </div>
            </div>
          </div>
        </form>
        <!-- orders containe  -->
        <div v-if="selectedOption === 'orders'">
          <h2>My Orders</h2>
          Add your orders content here
        </div>
        <!-- reclamation containe  -->
        <div v-if="selectedOption === 'reclamations'">
          <h2>My Reclamations</h2>
          Add your reclamations content here
        </div>
        <!-- settings containe  -->
        <div v-if="selectedOption === 'settings'">
          <h2>Settings</h2>
          Add your settings content here
        </div>
        <!-- checkout containe  -->
        <div v-if="selectedOption === 'checkout'">
          <h2>Checkout</h2>
          Add your checkout content here
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";
import store from "../store/index.js";

export default {
  name: "MyAccount",

  data() {
    return {
      isOpened: false,
      selectedOption: "details",
      userId: null,
    };
  },
  mounted() {
    const id = this.$route.query.id;
    if (id) {
      this.userId = id; // Assign the user ID to `this.userId`
      this.getcurrentCompte(id);
    }
  },
  computed: {
    ...mapGetters(["getUser"]),
    CurrentUser() {
      return (
        this.getUser || {
          first_name: "",
          last_name: "",
          date_nes: "",
          adresse: "",
          num_ident: "",
          email: "",
          username: "",
          password: "",
          oldpassword: "",
        }
      );
    },
    CurrentCompte() {
      return this.getUser
        ? this.getUser.compte || {
          id: "",
          date_nes: "",
          adresse: "",
          telephone: "",
          typeC: "",
          num_ident: "",
          user_id: "",
        }
        : {};
    },
  },

  methods: {
    getcurrentCompte(id) {
      console.log("affiche");

      this.$store.dispatch("fetchUser", id).then(() => {
        console.log(this.CurrentCompte);
        console.log(this.CurrentUser);
      });
    },

    updateUserInformation() {
      debugger;

      const currentPassword = this.$refs.currentPassword.value;
      const newPassword = this.$refs.newPassword.value;
      console.log(this.CurrentUser.oldpassword);

      // Verify current password
      if (currentPassword !== this.CurrentUser.oldpassword && currentPassword !== "") {
        alert("Current password is incorrect.");
        return;
      }

      const data = {
        username: this.CurrentUser.username,
        first_name: this.CurrentUser.first_name,
        last_name: this.CurrentUser.last_name,
        email: this.CurrentUser.email,
        password: newPassword, // Update the password with the new value
        date_nes: this.CurrentCompte.date_nes,
        adresse: this.CurrentCompte.adresse,
        telephone: this.CurrentCompte.telephone,
        typeC: this.CurrentCompte.typeC,
        num_ident: this.CurrentCompte.num_ident,
        admin: {},
        compte: {
          date_nes: this.CurrentCompte.date_nes,
          adresse: this.CurrentCompte.adresse,
          telephone: this.CurrentCompte.telephone,
          typeC: this.CurrentCompte.typeC,
          num_ident: this.CurrentCompte.num_ident,
        },
      };
      console.log(data.password);

      axios
        .put(`http://127.0.0.1:8000//api/user/${this.userId}/`, data)
        .then(() => {
          // Update the user data in the component's data
          this.CurrentCompte.date_nes = data.date_nes;
          this.CurrentCompte.adresse = data.adresse;
          this.CurrentCompte.telephone = data.telephone;
          this.CurrentCompte.num_ident = data.num_ident;
          this.CurrentUser.username = data.username;
          this.CurrentUser.first_name = data.first_name;
          this.CurrentUser.last_name = data.last_name;
          this.CurrentUser.email = data.email;
          this.CurrentUser.password = data.password; // Update the password
          alert("Details updated successfully.");
        })
        .catch((error) => {
          console.error(error);
        });
    },

    logout() {
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");
      localStorage.removeItem("username");
      localStorage.removeItem("userid");
      this.$store.commit("removeToken");
      this.$router.push("/");
    },
    selectOption(option) {
      this.selectedOption = option;
    },
  },
};
</script>

<style>
/*  log out  */
a.logout-icon {
  position: absolute;
  top: 50%;
  right: 20px;
  transform: translateY(-50%);
  color: #3273dc;
  /* Change the color as desired */
  font-size: 1.2em;
}

a.logout-icon:hover {
  color: #ff3860;
  /* Change the hover color as desired */
}
.sidebar {
  position: sticky;
  top: 0;
  height: 100vh;
  background-color: #fff;
  border-right: 1px solid #b2b2b2;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
  z-index: 1;
}

.sidebar .menu-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.sidebar li {
  padding: 17px;
}

.sidebar li a {
  display: flex;
  align-items: center;
  text-decoration: none;
  color: black;
  position: relative;
}

.sidebar li a::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 0;
  width: 3px;
  height: 0;
  background-color: #ff6e31;
  transform: translateY(-50%);
  opacity: 0;
  transition: height 0.3s, opacity 0.3s;
}

.sidebar li.is-active a::before {
  height: 100%;
  opacity: 1;
}

.sidebar li a i {
  margin-right: 10px;
}

.column {
  padding: 20px;
}
</style>