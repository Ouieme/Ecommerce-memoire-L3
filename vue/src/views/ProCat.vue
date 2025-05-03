<template>
  <div>
    <h2 class="is-size-3 has-text-centered" style="padding: 5rem;">
      <span style="color: orange;">{{ categoryName }}</span> Products
    </h2>
    
    <div class="column is-2" v-for="product in products" :key="product.id">
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
</template>

<script>
import axios from "axios";

export default {
  name: "procat",
  data() {
    return {
      categoryName: "",
      products: [],
    };
  },
  mounted() {
    this.getCategoryDetails();
  },
  methods: {
    getCategoryDetails() {
      const categorySlug = this.$route.params.categorySlug;
      axios
        .get(`http://localhost:8000/api/v1/procat/${categorySlug}`)
        .then((response) => {
          this.categoryName = response.data.category_name;
          this.products = response.data.products;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
