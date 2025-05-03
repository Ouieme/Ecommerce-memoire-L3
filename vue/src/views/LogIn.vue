<template class="hero is-info is-fullheight">
  <div class="hero-body">
    <div class="container">
      <div class="columns is-centered">
        <div class="column is-two-fifths">
          <div class="card">
            <div class="card-content" v-if="!forgotPassword">
              <h1 class="title is-4 has-text-centered mb-2">Welcome back</h1>
              <p class="has-text-centered mb-5">
                Log in to Bessahel to get started
              </p>
              <form @submit.prevent="submitForm">
                <div class="field">
                  <label class="label">Username</label>
                  <div class="control">
                    <input class="input" type="username" placeholder="Enter your username" v-model="username" />
                  </div>
                </div>

                <div class="field">
                  <label class="label">Password</label>
                  <div class="control">
                    <input class="input" :type="inputType" placeholder="Enter your password" v-model="password" />
                    <label class="icon is-pulled-right">
                      <i :class="[
                        showPassword ? 'fas fa-eye-slash' : 'fas fa-eye',
                      ]" @click="showPassword = !showPassword"></i>
                    </label>
                  </div>
                </div>
                <div class="notification is-danger has-text-danger mt-3" v-if="errors.length"
                  style="background-color: white; border: 1px solid red">
                  <button class="delete"></button>
                  <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>

                <div class="container mb-6">
                  <form>
                    <div class="field">
                      <label class="is-pulled-left is-size-7-mobile">
                        <input type="checkbox" />
                        Remember Me
                      </label>
                    </div>
                    <div class="field">
                      <a class="is-pulled-right is-size-7-mobile" href="#" @click="forgotPassword = true">
                        Forgot password?
                      </a>
                    </div>
                  </form>
                </div>
                <div class="mt-6">
                  <button class="button is-block is-info is-fullwidth" style="background-color: #ff6e31">
                    <span class="icon is-small">
                      <i class="fas fa-sign-in-alt"></i>
                    </span>
                    <span>Log in</span>
                  </button>
                </div>
              </form>

              <p class="has-text-centered mt-3 mb-1">Or Log in using</p>
              <div class="field is-grouped is-justify-content-center">
                <button class="button is-outlined mr-2">
                  <img
                    src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/2008px-Google_%22G%22_Logo.svg.png"
                    alt="Google" style="height: 24px" />
                </button>
                <button class="button is-outlined mr-2">
                  <img
                    src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/2021_Facebook_icon.svg/2048px-2021_Facebook_icon.svg.png"
                    alt="Facebook" style="height: 24px" />
                </button>
                <button class="button is-outlined">
                  <img src="https://img.freepik.com/free-icon/twitter_318-674515.jpg" alt="Twitter"
                    style="height: 24px" />
                </button>
              </div>
              <p class="has-text-centered mt-4">
                Don't Have an Account Yet?
                <router-link to="/sign-up">Sign Up!</router-link>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- forget password form -->

    <div class="columns is-centered">
      <div class="column is-two-fifths">
        <div class="card">
          <div class="card-content" v-if="forgotPassword">
            <h1 class="title is-4 has-text-centered mb-2">
              You forget your password !
            </h1>
            <p class="has-text-centered mb-5">Las't retrieve the password</p>
            <form>
              <div class="field">
                <label class="label">Email</label>
                <div class="control">
                  <input class="input" type="email" placeholder="Enter your email" v-model="email" />
                </div>
              </div>
            </form>
            <div class="mt-5">
              <button class="button is-block is-info is-fullwidth" style="background-color: #ff6e31">
                <span>Send</span>
              </button>
            </div>
            <div class="mt-3">
              <button class="button" @click="forgotPassword = false"
                style="background-color: white; color: #ff6e31; width: 150px">
                <span class="icon">
                  <i class="fas fa-arrow-left"></i>
                </span>
                <span>Go Back</span>
              </button>
            </div>
          </div>
        </div>
      </div>
      .
    </div>
  </div>
</template>

<!-- scripts-->

<script>
import axios from "axios";
import jwt_decode from "jwt-decode";
export default {
  name: "Home",
  data() {
    return {
      username: "",
      password: "",
      errors: [],
      showPassword: false,
      forgotPassword: false, // add this property
    };
  },
  mounted() {
    document.title = "Log In ";
  },
  methods: {
    async submitForm() {
      console.log("sub");
      axios.defaults.headers.common["Authorization"] = "";

      localStorage.removeItem("token");
      const formData = {
        username: this.username,
        password: this.password,
      };
      await axios
        .post("http://localhost:8000/api/token/", formData)
        .then(async (response) => {
          const token = response.data.access;
          this.$store.commit("setToken", token);
          axios.defaults.headers.common["Authorization"] = "Token " + token;
          localStorage.setItem("token", token);
          // Retrieve the user's information
          var decodedtoken = jwt_decode(response.data.access);
          const userResponse = await axios.get(
            `http://localhost:8000/api/v1/user/${decodedtoken.user_id}`
          );
          var type;
          if (userResponse.data.compte === null) {
            type = userResponse.data.admin.type_Admin;
          } else {
            type = userResponse.data.compte.typeC;
          }

          if (type === "stormanager") {
            this.$router.push({
              path: "/my-account",
              query: { id: decodedtoken.user_id },
            });
            console.log("111");
          } else if (type === "costomer") {
            this.$router.push({
              path: "/my-account",
              query: { id: decodedtoken.user_id },
            });
          } else if (type === "super") {
            this.$store.commit("setAdmin", true); // Set the admin state to true in Vuex store
            this.$router.push("/admin");
          } else {
            // Redirect to a default page if the user's role is not recognized
            this.$router.push("/");
          }
        })
        .catch((error) => {
          if (error.response) {
            this.errors.push("try again");
          } else {
            this.errors.push("Something went wrong. Please try again");

            console.log(JSON.stringify(error));
          }
        });
    },
  },
  computed: {
    inputType() {
      return this.showPassword ? "text" : "password";
    },
  },
};
</script>

<!-- style-->

<style>
.password-input {
  position: relative;
}

.toggle-password {
  position: absolute;
  top: 50%;
  right: 10px;
  transform: translateY(-50%);
  cursor: pointer;
}
</style>