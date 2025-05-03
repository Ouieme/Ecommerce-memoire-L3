<template>
  <div class="container">
    <div class="columns is-centered">
      <div class="column is-10">
        <div class="card elevation-6 mt-10">
          <div class="card-content">
            <div v-show="step === 1">
              <div class="columns">
                <div class="column is-half">
                  <h4 class="title is-4 has-text-centered">
                    Welcome To Bessahel
                  </h4>
                  <h6 class="subtitle is-6 has-text-centered">
                    Get Start Shopping
                  </h6>
                  <form @submit.prevent="submitForm">
                    <div class="field columns is-multiline">
                      <div class="control column is-half">
                        <input
                          type="text"
                          class="input is-blue"
                          placeholder="First name"
                          autocomplete="false"
                          v-model="firstname"
                        />
                      </div>
                      <div class="control column is-half">
                        <input
                          type="text"
                          class="input is-blue"
                          placeholder="Last name"
                          autocomplete="false"
                          v-model="lastname"
                        />
                      </div>
                      <div class="control column is-half">
                        <label class="label"></label>
                        <div class="control">
                          <input
                            type="datetime"
                            class="input is-blue"
                            placeholder="Date of birth"
                            autocomplete="false"
                            v-model="date_nes"
                          />
                        </div>
                      </div>
                      <div class="control column is-half">
                        <label class="label"></label>
                        <div class="control">
                          <input
                            type="number"
                            class="input is-blue"
                            placeholder="phone"
                            autocomplete="false"
                            v-model="phone"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="field">
                      <label class="label"></label>
                      <div class="control">
                        <input
                          type="text"
                          class="input is-blue"
                          placeholder="Adresse"
                          autocomplete="false"
                          v-model="adresse"
                        />
                      </div>
                    </div>
                    <div class="field columns is-multiline">
                      <div class="control column is-half">
                        <label class="label"></label>
                        <div class="control">
                          <input
                            type="email"
                            class="input is-blue"
                            placeholder="Email"
                            autocomplete="false"
                            v-model="email"
                          />
                        </div>
                      </div>
                      <div class="control column is-half">
                        <label class="label"></label>
                        <div class="control">
                          <input
                            type="text"
                            class="input is-blue"
                            placeholder="User name"
                            autocomplete="false"
                            v-model="username"
                          />
                        </div>
                      </div>
                      <div class="control column is-half">
                        <label class="label"></label>
                        <div class="control">
                          <input
                            type="password"
                            class="input is-blue"
                            placeholder="Password"
                            autocomplete="false"
                            v-model="password"
                          />
                        </div>
                      </div>
                      <div class="control column is-half">
                        <label class="label"></label>
                        <div class="control">
                          <input
                            type="password"
                            class="input is-blue"
                            placeholder="Repet Password"
                            autocomplete="false"
                            v-model="password2"
                          />
                        </div>
                      </div>
                    </div>
                    <!-- test-->
                    <div class="field">
                      <label class="label"></label>
                      <div class="control">
                        <input type="hidden" v-model="role" />
                      </div>
                    </div>

                    <div
                      class="notification is-danger has-text-danger mt-3"
                      v-if="errors.length"
                      style="background-color: white; border: 1px solid red"
                    >
                      <button class="delete"></button>
                      <p v-for="error in errors" v-bind:key="error">
                        {{ error }}
                      </p>
                    </div>

                    <button
                      class="button is-blue is-fullwidth mt-6"
                      style="background-color: #ff6e31"
                    >
                      <span class="icon" style="color: #fff"
                        ><i class="fas fa-user-plus"></i
                      ></span>
                      <span style="color: #fff">Sign Up</span>
                    </button>
                  </form>

                  <div class="mt-2 is-pulled-right">
                    <router-link to="/">
                      <button
                        class="button"
                        style="
                          background-color: white;
                          color: #ff6e31;
                          width: 150px;
                        "
                      >
                        <span>Cancel</span>
                      </button>
                    </router-link>
                  </div>
                  <div class="has-text-centered">
                    <h5 class="subtitle is-5 mt-6 mb-3">Or SignUp using</h5>
                  </div>

                  <div class="field is-grouped is-justify-content-center">
                    <button class="button is-outlined mr-2">
                      <img
                        src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/2008px-Google_%22G%22_Logo.svg.png"
                        alt="Google"
                        style="height: 24px"
                      />
                    </button>
                    <button class="button is-outlined mr-2">
                      <img
                        src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/2021_Facebook_icon.svg/2048px-2021_Facebook_icon.svg.png"
                        alt="Facebook"
                        style="height: 24px"
                      />
                    </button>
                    <button class="button is-outlined">
                      <img
                        src="https://img.freepik.com/free-icon/twitter_318-674515.jpg"
                        alt="Twitter"
                        style="height: 24px"
                      />
                    </button>
                  </div>
                  <hr class="hr-spacing" />
                  Already have an account?<router-link to="/log-in"
                    >Login</router-link
                  >
                </div>

                <!-- Stor manager -->
                <div
                  class="column is-half rounded-bl-xl"
                  style="background-color: #f5f5f5"
                >
                  <h3 class="title is-3 has-text-centered mt-6">
                    You Are Store Manager !
                  </h3>
                  <h6 class="subtitle is-6 has-text-centered mt-3 mb-6">
                    If you wont to create a stor.......
                  </h6>
                  <div
                    :class="{ 'is-active': step === 2 }"
                    @click="step = 2"
                    class="is-flex is-justify-content-center"
                  >
                    <button
                      class="button is-blue"
                      style="background-color: #ff6e31"
                    >
                      <a>
                        <span style="color: #fff">Create Stor</span>
                      </a>
                    </button>
                  </div>
                </div>
              </div>
            </div>
            <div v-show="step === 2">
              <div class="columns">
                <div
                  class="column is-half rounded-bl-xl"
                  style="background-color: #f5f5f5"
                >
                  <h3 class="title is-3 has-text-centered mt-6">
                    You Are Costomer !
                  </h3>
                  <h6 class="subtitle is-6 has-text-centered mt-3 mb-6">
                    If you wont to create account......
                  </h6>
                  <div
                    :class="{ 'is-active': step === 1 }"
                    @click="step = 1"
                    class="is-flex is-justify-content-center"
                  >
                    <button
                      class="button is-blue"
                      style="background-color: #ff6e31"
                    >
                      <a>
                        <span style="color: #fff">Create a new account</span>
                      </a>
                    </button>
                  </div>
                </div>
                <div class="column is-half">
                  <h4 class="title is-4 has-text-centered">
                    Welcome To Bessahel
                  </h4>
                  <h6 class="subtitle is-6 has-text-centered">
                    Sign up to create your stor
                  </h6>
                  <form @submit.prevent="submitForm2">
                    <div class="field columns is-multiline">
                      <div class="control column is-half">
                        <input
                          type="text"
                          class="input is-blue"
                          placeholder="First name"
                          autocomplete="false"
                          v-model="firstname"
                        />
                      </div>
                      <div class="control column is-half">
                        <input
                          type="text"
                          class="input is-blue"
                          placeholder="Last name"
                          autocomplete="false"
                          v-model="lastname"
                        />
                      </div>
                      <div class="control column is-half">
                        <label class="label"></label>
                        <div class="control">
                          <input
                            type="date"
                            class="input is-blue"
                            placeholder="Date of birth"
                            autocomplete="false"
                            v-model="date_nes"
                          />
                        </div>
                      </div>
                      <div class="control column is-half">
                        <label class="label"></label>
                        <div class="control">
                          <input
                            type="number"
                            class="input is-blue"
                            placeholder="phone"
                            autocomplete="false"
                            v-model="phone"
                          />
                        </div>
                      </div>
                      <div class="control column is-half">
                        <label class="label"></label>
                        <div class="control">
                          <input
                            type="text"
                            class="input is-blue"
                            placeholder="Adresse"
                            autocomplete="false"
                            v-model="adresse"
                          />
                        </div>
                      </div>
                      <div class="control column is-half">
                        <label class="label"></label>
                        <div class="control">
                          <input
                            type="number"
                            class="input is-blue"
                            placeholder="Identification number"
                            autocomplete="false"
                            v-model="num_ident"
                          />
                        </div>
                      </div>
                      <div class="control column is-half">
                        <label class="label"></label>
                        <div class="control">
                          <input
                            type="email"
                            class="input is-blue"
                            placeholder="Email"
                            autocomplete="false"
                            v-model="email"
                          />
                        </div>
                      </div>
                      <div class="control column is-half">
                        <label class="label"></label>
                        <div class="control">
                          <input
                            type="text"
                            class="input is-blue"
                            placeholder="User name"
                            autocomplete="false"
                            v-model="username"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="field">
                      <label class="label"></label>
                      <div class="control">
                        <input
                          type="password"
                          class="input is-blue"
                          placeholder="Password"
                          autocomplete="false"
                          v-model="password"
                        />
                      </div>
                    </div>
                    <div class="field">
                      <label class="label"></label>
                      <div class="control">
                        <input type="hidden" v-model="role" />
                      </div>
                    </div>

                    <div class="field">
                      <label class="label"></label>
                      <div class="control">
                        <input
                          type="password"
                          class="input is-blue"
                          placeholder="Repet Password"
                          autocomplete="false"
                          v-model="password2"
                        />
                      </div>
                    </div>
                    <div
                      class="notification is-danger has-text-danger mt-3"
                      v-if="errors.length"
                      style="background-color: white; border: 1px solid red"
                    >
                      <button class="delete"></button>
                      <p v-for="error in errors" v-bind:key="error">
                        {{ error }}
                      </p>
                    </div>

                    <button
                      class="button is-blue is-fullwidth mt-6"
                      style="background-color: #ff6e31"
                    >
                      <span class="icon" style="color: #fff"
                        ><i class="fas fa-user-plus"></i
                      ></span>
                      <span style="color: #fff">Sign Up</span>
                    </button>
                  </form>
                  <div class="mt-2 is-pulled-right">
                    <router-link to="/">
                      <button
                        class="button"
                        style="
                          background-color: white;
                          color: #ff6e31;
                          width: 150px;
                        "
                      >
                        <span>Cancel</span>
                      </button>
                    </router-link>
                  </div>
                  <div class="has-text-centered">
                    <h5 class="subtitle is-5 mt-6 mb-3">Or SignUp using</h5>
                  </div>
                  <div class="field is-grouped is-justify-content-center">
                    <button class="button is-outlined mr-2">
                      <img
                        src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/2008px-Google_%22G%22_Logo.svg.png"
                        alt="Google"
                        style="height: 24px"
                      />
                    </button>
                    <button class="button is-outlined mr-2">
                      <img
                        src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/2021_Facebook_icon.svg/2048px-2021_Facebook_icon.svg.png"
                        alt="Facebook"
                        style="height: 24px"
                      />
                    </button>
                    <button class="button is-outlined">
                      <img
                        src="https://img.freepik.com/free-icon/twitter_318-674515.jpg"
                        alt="Twitter"
                        style="height: 24px"
                      />
                    </button>
                  </div>

                  <hr class="hr-spacing" />
                  Already have an account?<router-link to="/log-in"
                    >Login</router-link
                  >
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

export default {
  data: () => ({}),
  props: {
    source: String,
  },
  name: "About",
  data() {
    return {
      firstname: "",
      lastname: "",
      email: "",
      username: "",
      password: "",
      password2: "",
      num_ident: "",
      date_nes: "",
      phone: "",
      adresse: "",
      errors: [],
      step: 1,
    };
  },
  mounted() {
    document.title = "Sign Up | Besahel";
  },
  methods: {
    submitForm() {
      this.errors = [];
      if (this.firstname === "") {
        this.errors.push("The first name is missing");
      }
      if (this.lastname === "") {
        this.errors.push("The last name is missing");
      }
      if (this.email === "") {
        this.errors.push("The email is missing");
      }
      if (this.username === "") {
        this.errors.push("The username is missing");
      }
      if (this.password === "") {
        this.errors.push("The password is too short");
      }
      if (this.password !== this.password2) {
        this.errors.push("The passwords doesn't match");
      }
      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password,
          email: this.email,
          telephone: this.phone,
          firstname: this.firstname,
          lastname: this.lastname,
          adresse: this.adresse,

          date_nes: this.date_nes,
          role: "costomer",
        };
        console.log(formData);
        axios
          .post("http://localhost:8000/api/v1/create/", formData)

          .then((response) => {
            debugger;
            toast({
              message: "Account created, please log in!",
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: "bottom-center",
            });
            this.$router.push("/log-in");
          })
          .catch((error) => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(
                  `${property}: ${error.response.data[property]}`
                );
              }
              console.log(JSON.stringify(error.response.data));
            } else if (error.message) {
              this.errors.push("Something went wrong. Please try again");

              console.log(JSON.stringify(error));
            }
          });
      }
    },
    submitForm2() {
      this.errors = [];
      if (this.firstname === "") {
        this.errors.push("The first name is missing");
      }
      if (this.lastname === "") {
        this.errors.push("The last name is missing");
      }
      if (this.email === "") {
        this.errors.push("The email is missing");
      }
      if (this.username === "") {
        this.errors.push("The username is missing");
      }
      if (this.password === "") {
        this.errors.push("The password is too short");
      }
      if (this.password !== this.password2) {
        this.errors.push("The passwords doesn't match");
      }
      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password,
          email: this.email,
          firstname: this.firstname,
          lastname: this.lastname,
          adresse: this.adresse,
          phone: this.phone,
          date_nes: this.date_nes,
          num_ident: this.num_ident,
          role: "stormanager",
        };
        axios
          .post("http://localhost:8000/api/v1/create/", formData)
          .then((response) => {
            toast({
              message: "Account created, please log in!",
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: "bottom-center",
            });
            this.$router.push("/log-in");
          })
          .catch((error) => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(
                  `${property}: ${error.response.data[property]}`
                );
              }
              console.log(JSON.stringify(error.response.data));
            } else if (error.message) {
              this.errors.push("Something went wrong. Please try again");

              console.log(JSON.stringify(error));
            }
          });
      }
    },
  },
};
</script>

<style scoped>
.v-application .rounded-bl-xl {
  border-bottom-left-radius: 300px !important;
}
.v-application .rounded-br-xl {
  border-bottom-right-radius: 300px !important;
}
::placeholder {
  color: #889397;
}
.hr-spacing {
  margin-bottom: 0.5em;
}
</style>