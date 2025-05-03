<template>
  <div id="wrapper">
    <nav class="navbar is-primary" :style="{ backgroundColor: navbarColor }">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <img src="./assets/Bessahel.png" alt="logo">
        </router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu"
          @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <template v-if="$store.state.admin">
        <div class="navbar-menu" id="navbar-menu" :class="{ 'is-active': showMobileMenu }">
          <div class="navbar-start"></div>
          <div class="navbar-center">
            
            <router-link to="/admin" class="navbar-item ">home</router-link>

            <router-link to="/categories" class="navbar-item">CATEGORIES</router-link>
          </div>
          <div class="navbar-item">


            <router-link to="#">
              <img class="rounded-image" src="./assets/pic1.jpg" alt="Bulma">
            </router-link>
          </div>

        </div>
      </template>

      <template v-else>
        <div class="navbar-menu" id="navbar-menu" :class="{ 'is-active': showMobileMenu }">
          <div class="navbar-start"></div>
          <div class="navbar-center">

            <router-link to="/Shop" class="navbar-item ">SHOP</router-link>

            <router-link to="/categories" class="navbar-item">CATEGORIES</router-link>

            <router-link to="/Stores" class="navbar-item">STORES</router-link>

            <router-link to="/About" class="navbar-item">ABOUT US</router-link>

            <router-link to="/Contact" class="navbar-item">CONTACT US</router-link>
          </div>
          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-account" class="button is-light">My account</router-link>
                <router-link to="/cart" class="button is-success">
                  <span class="icon"><i class="fa fa-shopping-cart"></i></span>
                  <span>Cart</span>
                </router-link>
              </template>
              <template v-else>
                <router-link to="/sign-up" class="button is-Light">Sign up</router-link>
                <router-link to="/log-in" class="button is-Light">Log in</router-link>

                <router-link to="/cart" class="button" style="background-color: orange; color: white;">
                 <span style="padding-right: 12px;"><i class="fa-solid fa-cart-shopping" style="color: white; "></i></span> 
                  <!-- <span class="icon"><i class="fas fa-shopping-cart" style="color: white;"></i></span> -->
                  
                  <span>Cart</span>
                </router-link>
                
              </template>



            </div>
          </div>

        </div>
      </template>

    </nav>
    <section class="section">
      <router-view />
    </section>

    <!--footer starts from here-->
    <footer>
      <div class="container">
        <div class="columns">
          <div class="column">
            <h5 class="title is-5 has-text-white">Find Us</h5>
            <p class="has-text-white-ter mb-5">
              Lorem Ipsum is simply dummy rem
              <br />
              Lorem ipsum dolor sit amet.
            </p>
            <p class="has-text-white-ter">
              <span class="icon"><i class="fas fa-location-arrow"></i></span>
              9878/25 sec 9 rohini 35
            </p>
            <p class="has-text-white-ter">
              <span class="icon"><i class="fas fa-phone"></i></span>
              +91-9999878398
            </p>
            <p class="has-text-white-ter">
              <span class="icon"><i class="fas fa-envelope"></i></span>
              info@example.com
            </p>
          </div>

          <div class="column">
            <h5 class="title is-5 has-text-white">Quick Links</h5>
            <ul class="menu-list">
              <li><a href="/">Home</a></li>
              <li><a href="#">Shop</a></li>
              <li><a href="#">About us</a></li>
              <li><a href="#">Contact us</a></li>
            </ul>
          </div>

          <div class="column">
            <h5 class="title is-5 has-text-white">Follow Us</h5>
            <p class="has-text-white-ter">
              <span class="icon"><i class="fab fa-facebook"></i></span>
              Follow us on Facebook
            </p>
            <p class="has-text-white-ter">
              <span class="icon"><i class="fab fa-linkedin"></i></span>
              Follow us on LinkedIn
            </p>

            <p class="has-text-white-ter">
              <span class="icon"><i class="fab fa-instagram"></i></span>
              Follow us on Instagram
            </p>

            <p class="has-text-white-ter">
              <span class="icon"><i class="fab fa-twitter"></i></span>
              Follow us on Twitter
            </p>
          </div>
        </div>
      </div>
      <div
        style="
          display: flex;
          justify-content: center;
          align-items: center;
          padding-top: 100px;
        "
      >
        <p class="has-text-white-ter has-text-centered">
          Copyright @2023 | Designed By
          <b style="color: orange">Besahel </b>Team
        </p>
      </div>
      <ul class="payment_icons_ul" style="color: orange">
        <li>
          <a href="#" style="color: white"><i class="fab fa-cc-visa"></i></a>
        </li>
        <li>
          <a href="#"  style="color: white"><i class="fab fa-cc-mastercard"></i></a>
        </li>
        <li>
          <a href="#" style="color: white"><i class="fab fa-cc-paypal"></i></a>
        </li>
      </ul>
    </footer>
  </div>
</template>

<script>
import { ref } from "vue";
export default {
  data() {
    return {
      showMobileMenu: false,
      navbarColor: "transparent",
    };
  },

  watch: {
  $route(to) {
      // Update navbarColor based on the current route
      if (to.path === "/") {
        this.navbarColor = "transparent";
      } else {
        this.navbarColor = "black"; // Default color for other routes
      }
    },
  },
};
</script>



<style lang="scss">
/*$orange: orange;

$primary: $orange;*/

@import "../node_modules/bulma";



footer {
  padding: 100px;
  background-color: hsl(0, 0, 21%);
}

.menu-list li a {
  color: white;
}

.payment_icons_ul {
  display: flex;
  justify-content: center; /* To center the icons horizontally */
  list-style: none; /* To remove the bullet points */
  margin: 0;
  padding: 0;
}

.payment_icons_ul li {
  margin: 0 10px; /* To add spacing between the icons */
}

.payment_icons_ul li a i {
  
  padding-top: 20px;
  font-size: 160%;
}

.navbar-center {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-grow: 1;
}

 .navbar-center .navbar-item{
    color: #ffffff;
 }

.navbar-center .navbar-item:hover {
  background: none;
  color: orange;
}

.navbar-end {
  display: flex;
  justify-content: flex-end;
  align-items: center;
}

// .navbar-brand img{
//  width: 50px;
//  height: auto;
// }

.navbar {
  height: 80px;
}

.navbar-item {
  position: relative;
}

.navbar-center .navbar-item::after {
  content: "";
  position: absolute;
  bottom: -5px;
  left: 50%;
  transform: translateX(-50%);
  width: 0;
  height: 2.5px;
  background-color: orange;
  transition: width 0.2s ease-in-out;
}

.navbar-item:hover::after {
  width: 100%;
}

.navbar {
  height: 100px;
}

</style>
