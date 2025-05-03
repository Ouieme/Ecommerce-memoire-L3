<template>
  <div class="star-rating-box">
    <div class="star-rating-box__rating">
      <div class="star-rating-box__stars">
        <span
          v-for="star in stars"
          :key="star"
          class="star-rating-box__star"
          :class="{ 'star-rating-box__star--filled': star <= rating }"
          @mouseover="hoverRating(star)"
          @mouseleave="resetRating()"
          @click="selectRating(star)"
        >
          <i class="fas fa-star"></i>
        </span>
      </div>
    </div>
    <div class="star-rating-box__selected-rating">
      <!-- <span v-if="selectedRating > 0">Selected Rating: {{ selectedRating }}</span> -->
      <!-- <span v-else>No rating selected</span> -->
    </div>
  </div> 
</template>

<script>
export default {
  name: 'StarRatingBox',
  props: {
    maxRating: {
      type: Number,
      default: 5,
    },
  },
  data() {
    return {
      rating: 0,
      selectedRating: 0,
    };
  },
  computed: {
    stars() {
      return Array(this.maxRating).fill().map((_, index) => index + 1);
    },
  },
  methods: {
    hoverRating(star) {
      this.rating = star;
    },
    resetRating() {
      this.rating = this.selectedRating;
    },
    selectRating(star) {
      this.selectedRating = star;
    },
  },
};
</script>

<style scoped>
.star-rating-box {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.star-rating-box__stars {
  display: flex;
  justify-content: center;
}

.star-rating-box__star {
  color: gray;
  transition: color 0.3s;
  cursor: pointer;
}

.star-rating-box__star--filled {
  color: gold;
}
</style>
