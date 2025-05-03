<template>
  <div class="page-product">
    <div class="columns is-multiline">
      <!-- <div class="column is-6">
        <figure class="image mb-6">
          <img v-bind:src="product.get_image" class="product-image" />
        </figure>
      </div> -->
      <div class="column is-1 ">
        <div class="box" >
          <figure class="image is-square mb-1 custom-effect">
            <img v-bind:src="product.get_image" class="product-image" />
          </figure>
        </div>
        <div class="box" >
          <figure class="image is-square mb-1 custom-effect">
            <img v-bind:src="product.get_image" class="product-image" />
          </figure>
        </div>
        <div class="box" >
          <figure class="image is-square mb-1 custom-effect">
            <img v-bind:src="product.get_image" class="product-image" />
          </figure>
        </div>
      </div>
      
      <div class="column is-3 cnt">

        <div class="box" style="padding: 50px;"  >
          <figure class="image is-square mb-4 custom-effect">
            <img v-bind:src="product.get_image" class="product-image" />
          </figure>
        </div>
        </div>


      <div class="column is-6">
        <h1 class="title">{{ product.name }}</h1>

        <div class="product-info">
          <p>{{ product.description }}</p>
          <p style="font-size: 20px; margin-bottom: 1rem">
            <strong>Price: </strong>{{ product.price }} DA
          </p>
          <div class="field is-horizontal">
            <div class="field-label is-normal">
              <label class="label">Size:</label>
            </div>
            <div class="field-body">
              <div class="field">
                <div class="control">
                  <div class="select">
                    <select v-model="selectedSize">
                      <option v-for="size in product.sizes" :key="size.id">
                        {{ size.name }}
                      </option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="field is-horizontal">
            <div class="field-label is-normal">
              <label class="label">Color:</label>
            </div>
            <div class="field-body">
              <div class="field">
                <div class="control">
                  <div class="select">
                    <select v-model="selectedColor">
                      <option v-for="color in product.colors" :key="color.id">
                        {{ color.name }}
                      </option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="field has-addons mt-6">
            <div class="control">
                <input type="number" class="input" min="1" v-model="quantity">
                <a class="button" style="background-color: orange; color: white;" @click="addToCart()">Add to cart</a>
            </div>
        </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from 'bulma-toast'

export default {
  name: "Product",
  data() {
    return {
      product: {},
      quantity: 1,
      category_slug: "",
    };
  },
  mounted() {
    this.getProduct();
  },
  methods: {
    getProduct() {
      const category_slug = this.$route.params.category_slug;
      const product_slug = this.$route.params.product_slug;
      axios
        .get(
          `http://localhost:8000/api/v1/products/${category_slug}/${product_slug}`
        )
        .then((response) => {
          this.product = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }

            const item = {
                product: this.product,
                quantity: this.quantity
            }

            this.$store.commit('addToCart', item)

            toast({
                message: 'The product was added to the cart',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        }
  },
};
</script>

<style>

.page-product{
  padding: 50px;
}
.product-info {
  margin-top: 2rem;
  margin-right: 10rem;
}

.product-info p {
  padding-top: 5%;
}
.cnt{
  margin-left: 100px;
  margin-right: 100px;
  
}
.button{
  margin-left: 22px;
}



</style>
