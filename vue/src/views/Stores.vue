<template>
  <div class="stores">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-3 has-text-centered" style="padding-bottom: 20px">
          Our Stores
        </h2>
      </div>
      <div class="column is-3" v-for="Magasin in Magasins" :key="Magasin.id" @click="goToStore(Magasin.slug)">
        <div class="box">
          <figure class="image is-square mb-4 custom-effect">
            <img :src="`http://localhost:8000${Magasin.thumbnail}`" />
          </figure>
          <h3 class="is-size-5 store-name">{{ Magasin.nom }}</h3>
          <div>{{ Magasin.category }}</div>
          <star-rating-box :max-rating="5"></star-rating-box>
        </div>
      </div>     
    </div>
  </div>
</template>

<script>
import axios from "axios";
import StarRatingBox from "./StarRating.vue";
import router from "../router/index.js";

export default {
  name: 'SingleStore',
  data() {
    return {
      Magasins: [],      
    };
  },
  components: {
    StarRatingBox,

  },
  mounted() {
    this.getMagasins();
    this.getCategoryStore() ;
    
  },
 methods: {
    getMagasins() {
      axios
        .get("http://localhost:8000/api/v1/Stores/")
        .then((response) => {
          this.Magasins = response.data;
          this.getCategoryStore();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getCategoryStore() {
      axios
        .get("http://localhost:8000/api/v1/categoryStore/")
        .then((categoryResponse) => {
          this.Magasins.forEach((magasin) => {
            const categoryData = categoryResponse.data.find(
              (item) => item.magasin === magasin.id
            );
            if (categoryData) {
              magasin.category = categoryData.category;
            }
          });
        })
        .catch((error) => {
          console.log(error);
        });
    },
    
    goToStore(slug) {
    this.$router.push({ name: 'SingleStore', params: {  slug } });
  },
},
};
</script>

<style scoped>
.stores{
  padding: 30px;
}
.box {
  position: relative;
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
