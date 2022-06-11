<template>
  <div id="app">
    <nav>
      <router-link to="/">
        <img
          src="http://127.0.0.1:8000/media/post_img/LOGO.png"
          alt="logo"
          height="116"
          width="159"
        />
      </router-link>
      <div id="mini-navbar">
        <router-link to="/">
          <span class="nav-routeur-txt">Home</span>
        </router-link>
        |
        <router-link to="/location">
          <span class="nav-routeur-txt">Locations</span>
        </router-link>
        |
        <router-link to="/evenementiel">
          <span class="nav-routeur-txt">Evenementiels</span>
        </router-link>
        |
        <router-link to="/traiteur">
          <span class="nav-routeur-txt">Service traiteur</span>
        </router-link>
        |
        <router-link to="/about">
          <span class="nav-routeur-txt">About</span>
        </router-link>
      </div>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
  data() {},
};
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  color: #2c3e50;
  margin: 0;
  padding: 0;
  border: 0;
}

#mini-navbar {
  font-size: 26px;
  top: 0;
  position: fixed;
  top: 4vw;
  left: 20vw;
}

nav {
  top: 0;
  height: 6vw;
  background-color: #d9d9d9;
  position: fixed;
  width: 100%;
  z-index: 1;
  a {
    font-weight: bold;
    color: #002333;
    img {
      width: 11vw;
      height: 8vw;
      margin-left: 4vw;
      margin-top: 1vw;
      z-index: 2;
    }

    .nav-routeur-txt {
      padding: 30px;
    }

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
