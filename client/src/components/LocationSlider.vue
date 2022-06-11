<template>
  <div class="LocationSlider">
    <image-slider class="imageSlider">
      <div class="imageSlider-nav">
        <div class="prev" @click="prev">
          <a class="prev fa-solid fa-chevron-left"></a>
        </div>
        <div class="next" @click="next">
          <a class="next fas fa-chevron-right" @click="next"></a>
        </div>
      </div>
      <transition-group name="fade" tag="div">
        <div
          class="imageSlider-wrapper"
          v-for="number in [currentNumber]"
          :key="number"
        >
          <img
            class="imageSlider-item"
            :src="currentImage"
            @mouseover="stopRotation"
            @mouseout="startRotation"
          />
        </div>
      </transition-group>
    </image-slider>
  </div>
</template>

<script>
export default {
  name: "LocationSlider",
  components: {},
  props: {},
  el: "image-slider",
  data() {
    return {
      images: [
        "https://images.pexels.com/photos/374906/pexels-photo-374906.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        "https://images.pexels.com/photos/8700/wall-animal-dog-pet.jpg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        "https://images.pexels.com/photos/248307/pexels-photo-248307.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
      ],
      currentNumber: 0,
      timer: null,
    };
  },
  mounted: function () {
    this.startRotation();
  },
  methods: {
    startRotation: function () {
      this.timer = setInterval(this.next, 7000);
    },
    stopRotation: function () {
      clearTimeout(this.timer);
      this.timer = null;
    },
    next: function () {
      this.currentNumber += 1;
    },
    prev: function () {
      if (this.currentNumber <= 0) {
        this.currentNumber = 2;
      } else {
        this.currentNumber -= 1;
      }
    },
  },
  computed: {
    currentImage: function () {
      return this.images[Math.abs(this.currentNumber) % this.images.length];
    },
  },
};
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,700");

$base-duration: 250ms;

// Colors
$primary: #42b983;
$accent: #46627f;
$red: #e74c3c;
$white: whitesmoke;

$max-width: 1200px;
// Breakpoints
$sm: 20rem;
$med: 48rem;
$lg: 64rem;

*,
*:before,
*:after {
  box-sizing: border-box;
  outline: none;
}

.LocationSlider {
  padding-left: 5vw;
}

html {
  font-family: "Source Sans Pro", sans-serif;
  font-size: 16px;
  font-smooth: auto;
  font-weight: 300;
  line-height: 1.5;
  color: #444;
}

body {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  width: 100%;
  height: 100vh;
}
h1 {
  margin-bottom: 15px;
  > span {
    display: inline-block;
    transform: translateY(-2px);
    color: $red;
    font-size: 24px;
  }
}
.timer {
  position: absolute;
  bottom: -100px;
}
.imageSlider {
  position: relative;
  display: block;
  width: 90vw;
  height: 45vh;
  //overflow: hidden;
  .imageSlider-nav {
    position: absolute;
    bottom: 0;
    right: 0;
    display: flex;
    z-index: 9;
    .next,
    .prev {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 40px;
      height: 40px;
      background-color: rgba(white, 0.3);
      color: $primary;
      cursor: pointer;
      &:hover {
        background-color: rgba(white, 0.8);
      }
    }
    .prev {
      margin-right: 1px;
    }
  }
  .imageSlider-wrapper {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }
  .imageSlider-item {
    position: relative;
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: 50% 50%;
    //transform: translateY(-25%);
  }
}

.fade-enter-active,
.fade-leave-active {
  //position: absolute;
  transition: all 0.8s ease;
  overflow: hidden;
  visibility: visible;
  opacity: 1;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
  visibility: hidden;
}
</style>
