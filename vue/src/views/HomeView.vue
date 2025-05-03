<template>
  <div class="home">
    <!-- header section -->
    <section class="section">
      <div class="hero is-primary" style="height: 500px;">
        <div class="hero-background">
          <img src="../assets/slider3.jpg" alt="Background Image">
        </div>
        <div class="hero-content">
          <p style="color: orange;"><b>DISCOVER & SHOP THE TREND</b></p>
          <h1 class="title">Get All Your Needs Bessahel</h1>
          <a href="/Shop" class="button is-primary is-rounded">Shop now</a>
          <a href="/Contact" class="button is-rounded contact">Contact Us</a>
        </div>
      </div>
    </section>
    <!-- list section -->
    <section >
      <div class="list-section pt-80 pb-80">
        <div class="container">
          <div class="columns is-multiline">
            <div class="column is-4">
              <div class="list-box is-flex is-align-items-center">
                <div class="list-icon">
                  <i class="fas fa-shipping-fast"></i>
                </div>
                <div class="content">
                  <h3>Free Shipping</h3>
                  <p>When order over $75</p>
                </div>
              </div>
            </div>
            <div class="column is-4">
              <div class="list-box is-flex is-align-items-center">
                <div class="list-icon">
                  <i class="fas fa-phone-volume"></i>
                </div>
                <div class="content">
                  <h3>24/7 Support</h3>
                  <p>Get support all day</p>
                </div>
              </div>
            </div>
            <div class="column is-4">
              <div class="list-box is-flex justify-content-start is-align-items-center">
                <div class="list-icon">
                  <i class="fas fa-sync"></i>
                </div>
                <div class="content">
                  <h3>Refund</h3>
                  <p>Get refund within 3 days!</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

    </section>

    <!-- latest products section -->
    <section>
      <div class="columns is-multiline" style="padding: 20px;">
  
        <div class="column is-12">
          <h2 class="is-size-2 has-text-centered" ><span style="color: orange;">Latest</span> Products</h2><hr class="title-underline">
          <p class="has-text-centered">Lorem ipsum dolor sit amet consectetur adipisicing elit. Non, quam.</p>
        </div>
  
        <div class="column is-2" v-for="product in LatestProducts" v-bind:key="product.id">
          <div class="box">
            
            <figure class="image is-square mb-2">
              <div class="image-container">
                <img :src="product.get_thumbnail" />
              </div>
            </figure>
  
            <h3 class="is-size-5">{{ product.name }}</h3>
            <p class="is-size-6 has-text-grey">{{ product.price }}DA</p>
  
            <div class="has-text-centered"> 
              <router-link v-bind:to="product.get_absolute_url" class="button is-small mt-5" style="background-color: orange; color: white; font-weight: 500;">view details</router-link>
            </div>
          </div>
        </div>
      </div>
</section>
  
  <section class="shop-banner " >
    <div class="container " style="padding-left: 10px;" >
      <h3>June sale is on! <br> with big <span style="color: orange; font-weight: bold;">Discount...</span></h3>
      <div class="sale-percent"><span>Sale! <br> Upto</span>50% <span>off</span></div>
    </div>
  </section>
  
  <section class="abt-section mb-5">
    <div class="container">
      <h2 class="is-size-2 has-text-centered " style="padding-bottom: 20px; font-weight: bold; margin-top: 50px;">About <span style="color: orange;">Us</span></h2>
      <hr class="title-underline">
      <div class="columns">
        <div class="column is-6" >
          <div class="abt-bg">
            <a href="https://www.youtube.com/watch?v=qwBP2FQv5Pk" class="video-play-btn popup-youtube"><i class="fas fa-play"></i></a>
          </div>
        </div>
        <div class="column is-6">
          <div class="abt-text">
            <p class="top-sub">Since Year 2023</p>
            <h2>We are <span class="orange-text">Bessahel</span></h2>
            <p>Welcome to Bessahel, where passion meets quality. Since our establishment in 2023, we have been dedicated to providing our customers with an exceptional shopping experience.
               Our journey began with a simple idea: to offer the finest products that enrich lives and bring joy to every Algerian customer.
                Guided by our core values of integrity, innovation, and customer satisfaction, we meticulously handpick each item in our collection,
                 ensuring superior quality and craftsmanship. We take pride in offering a diverse range of products that cater to various interests
                  and preferences. Whether you're searching for stylish fashion pieces, innovative gadgets, or unique home decor, 
                  we've got you covered. Our commitment to excellence extends beyond our product selection; we strive to create a seamless shopping journey, providing exceptional customer service and a secure online environment. 
                  Join us on this exciting adventure,
                   and discover the perfect blend of quality, style, and convenience with Bessahel."</p>
            
            <a href="/About" class="button mt-4"  style="background-color: orange; color: white;">know more</a>
          </div>
        </div>
      </div>
    </div>
  </section>
  
  
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Home",
  data() {
    return {
      LatestProducts: [],
    };
  },
  components: {},
  mounted() {
    this.getLatestProducts();
  },
  methods: {
    getLatestProducts() {
      axios
        .get("http://localhost:8000/api/v1/latest-products/")
        .then((response) => {
          this.LatestProducts = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>


<style scoped>
/* .image {
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
} */

/* is-5by4 {
  width: 338.3px;
  height: 500px;
} */

.hero-background {
  position: relative;
  overflow: hidden;
}

.hero-background::before {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background: rgba(0, 0, 0, 0.3);
}



.hero-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.hero-background img {
  object-fit: cover;
  object-position: center;
  width: 100%;
  height: 100%;
}

.hero-content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;

}

.hero-content h1 {
  font-size: 3rem;
}

.hero-content .button {
  font-size: 1rem;
  background-color: orange;
  color: white;
}

.hero-content .contact {
  background-color: transparent;
  margin-left: 15px;
}

.list-section {
  background-color: #f5f5f5;
  margin-bottom: 30px;
  margin-top: 50px;
  margin-left: -10px;
  margin-right: 0px;
  padding-top: 100px;
  padding-bottom: 2.5%;
  
}

.list-section .container {
  padding-left: 0;
  padding-right: 0;
  width: 100%;
  height: 100%;
}

.list-section .columns {
  margin-left: 0; /* Remove left margin */
  margin-right: 0; /* Remove right margin */
}
.list-box {
  overflow: hidden;
  letter-spacing: 0.5px;
}

.list-box .content h3 {
  display: block;
  line-height: 22px;
  font-size: 18px;
  margin-bottom: 4px;
}

.list-box .content p {
  margin-bottom: 0px;
  opacity: 0.75;
}

.list-box .list-icon i {
  display: block;
  font-size: 24px;
  margin-right: 15px;
  color: orange;
  width: 65px;
  height: 65px;
  text-align: center;
  line-height: 60px;
  border: 2px orange dotted;
  border-radius: 999px;
}

.column h2{
  font-weight: 700;
}


.shop-banner {
  position: relative;
  background-image: url(../assets/cart2.jpg);
  background-size: cover;
  padding: 120px 0 100px 0;
  margin-top: 10%;
 
  
}

.shop-banner h3 {
  position: relative;
  font-size: 50px;
  line-height: 1.2em;
  margin-bottom: 0px;
}

.shop-banner .sale-percent {
  position: relative;
  font-size: 60px;
  font-weight: 700;
  color: orange;
}

.shop-banner .sale-percent span {
  position: relative;
  font-size: 24px;
  line-height: 1.1em;
  color: #051922;
  font-weight: 400;
  text-align: center;
  margin-right: 10px;
  display: inline-block;
}

a.video-play-btn {
  position: absolute;
 background-color: #e3e3e375;
  color: #ffffff;
  width: 90px;
  height: 90px;
  text-align: center;
  line-height: 92px;
  border-radius: 50%;
  font-size: 30px;
  padding-left: 5px;
  display: block;
  z-index: 2;
  top: 50%;
  margin-top: -45px;
  -webkit-box-shadow: 0 0 20px #adadad;
  box-shadow: 0 0 20px #adadad;
  left: 50%;
  margin-left: -45px;
  
}

.abt-bg {
  background-image: url(../assets/work3.jfif);
  height: 100%;
  width: 100%;
  background-size: cover;
  background-position: center;
  border-top-right-radius: 10px;
  border-bottom-left-radius: 10px;
  position: relative;
  z-index: 1;
  overflow: hidden;
}

.abt-bg:after {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  content: "";
  background-color: #051922;
  opacity: 0.3;
}

.abt-section .abt-text {
  padding: 50px;
  padding-left: 30px;
}

.abt-text p {
  font-size: 15px;
  line-height: 1.6;
  margin-bottom: 10px;
}

.abt-text p.top-sub {
  opacity: 0.8;
  margin-bottom: 10px;
}

.abt-text p:last-child {
  margin-bottom: 0;
}

.title-underline {
  border: none;
  border-top: 3px solid orange;
  width: 8%;
  margin: auto;
  border-radius: 2px;
  margin-bottom: 30px;
}


</style>








