<template>
  <div class="categories">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-3 has-text-centered" style="padding-bottom:20px">Our categories</h2>
      </div>
      <div class="column is-3" v-for="category in categories" :key="category.id">
        <div class="box" @click="goToCategory(category.slug)">
          <figure class="image is-square mb-4 custom-effect">
            <img :src="`http://localhost:8000${category.thumbnail}`" />
          </figure>
          <h3 class="is-size-4 has-text-centered category-name">
            {{ category.name }}
          </h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import router from '../router/index.js';



export default {
  name: "categories",
  data() {
    return {
      categories: [],
    };
  },
  components: {},
  mounted() {
    this.getCategories();
  },
  methods: {
    getCategories() {
      axios
        .get("http://localhost:8000/api/v1/categories/")
        .then((response) => {
          this.categories = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    goToCategory(categorySlug) {
  this.$router.push({ name: "procat", params: { categorySlug } });
},

  },
};

//inkscape
</script>

<style scoped>
.categories{
  padding: 20px;
}
.box {
  position: relative;
}

.category-name {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  z-index: 3;
}

.custom-effect {
  position: relative;
}

.custom-effect::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: black;
  opacity: 0.3; /* Adjust the opacity as desired */
  z-index: 1;
}

</style>
