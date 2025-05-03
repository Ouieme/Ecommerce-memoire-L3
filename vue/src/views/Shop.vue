<template>
  <div class="shop">
    <div class="columns is-multiline" >
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered"><span style="color: orange;">Our</span>  products</h2>
      </div>
      <div class="column is-2 " >
        <div class="field">
          <div class="control has-text-centered">
            <label for="">Search</label>
            <input
              class="input"
              type="text"
              v-model="searchQuery"
              @input="filterProducts"
              placeholder="Search"
            />
            <label for="">Price</label>
            <input
              type="range"
              class="form-control-range"
              id="intervalle"
              v-model="minPrice"
              min="0"
              max="9999.1"
              step="0.1"
              @input="filterProducts"
            />
            <p>Price Range: {{ selectedPrice }}</p>
          </div>
        </div>
      </div>

      <div
        class="column is-2"
        v-for="product in filteredProducts"
        :key="product.id"
      >
      <section >
        <div class="box">
          <figure class="image is-square mb-2">
            <div class="image-container">
              <img :src="product.get_thumbnail" />
            </div>
          </figure>

          <h3 class="is-size-6">{{ product.name }}</h3>
          <p class="is-size-6 has-text-grey">{{ product.price }}DA</p>

          <div class="button-container">
            <router-link
              :to="product.get_absolute_url"
              class="button is-dark mt-3"
            >
              <p>View Details</p>
            </router-link>
          </div>
        </div>
      </section>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Shop",
  data() {
    return {
      Products: [],
      searchQuery: "",
      minPrice: 0,
      maxPrice: 0,
      selectedPrice: 0,
    };
  },
  computed: {
    filteredProducts() {
      return this.Products.filter((product) => {
        const nameMatch = product.name
          .toLowerCase()
          .includes(this.searchQuery.toLowerCase());
        const priceMatch =
          product.price >= this.minPrice && product.price <= this.maxPrice;
        return nameMatch && priceMatch;
      });
    },
    maxProductPrice() {
      return Math.max(...this.Products.map((product) => product.price));
    },
  },
  components: {},
  mounted() {
    this.getProducts();
  },
  methods: {
    getProducts() {
      axios
        .get("http://localhost:8000/api/v1/Shop/")
        .then((response) => {
          this.Products = response.data;
          this.maxPrice = this.maxProductPrice;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    filterProducts() {},
  },
};
</script>

<style>
.shop{
  padding: 20px;
}
.button p {
  font-size: 13px;
}

.input {
  margin: 1.5rem;
  width: 70%;
}

.button-container {
  display: flex;
  justify-content: center;
  margin-top: 1.5rem;
}
/*
.container{
  background-color: red;
  
}

.field {
  display: flex;
  justify-content: center;
  margin: 1.5rem;
} */

.form-control-range {
  width: 100%;
  margin: 1rem;
}


</style>
