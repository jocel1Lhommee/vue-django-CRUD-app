<template>
  <div id="home">
    <h1>Villa Charlestine</h1>
    <img
      src="http://127.0.0.1:8000/media/post_img/Home.jpg"
      alt="photo trincipale de la maison"
    />

    <p id="message">
      "La villa Charlestine vous souhaite la bienvenue,on vous y invite afin d’y
      séjourner, d’organiser vos évennements de touts types, On vous propose
      également un service Traiteur qui livre dans Yaoundé a partir de 10 plats
      ou lors de vos receptions”
    </p>

    <h2>Offre de location</h2>
    <div class="CardContainer">
      <router-link to="/location">
        <LocationCard titre="Grande Villa" />
      </router-link>
      <router-link to="/location">
        <LocationCard titre="Petite Villa" />
      </router-link>
    </div>
    <router-view />
    <h2>Organisation d'évenementiels:</h2>
    <div class="CardContainer">
      <EvenementCard />
      <EvenementCard />
      <EvenementCard />
      <EvenementCard />
    </div>
    <h2>Un Traiteur pour vos évenements</h2>
    <h3>~Entrée~</h3>
    <p>Salade de crudités</p>
    <p>Avocat pamplemousse</p>
    <h3>~Plat~</h3>
    <p>Ndolè</p>
    <p>Brochette de boeuf</p>
    <p>Brochette de poisson</p>
    <p>Poulet DG</p>
    <h3>~Dessert~</h3>
    <p>Brochette de fruits</p>
    <p>tarte aux pommes</p>
    <p>Fondant au chocolat</p>
    <FooterView />
  </div>
</template>

<script>
import LocationCard from "../components/LocationCard.vue";
import EvenementCard from "../components/EvenementCard.vue";
import FooterView from "../components/FooterView.vue";

export default {
  name: "HomeView",
  components: {
    LocationCard,
    EvenementCard,
    FooterView,
  },
};
</script>

<style lang="scss">
a {
  text-decoration: none;
}
</style>

<style lang="scss" scoped>
#home {
  margin: 0;
  padding: 0;
  border: 0;

  .CardContainer {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
  }

  h1 {
    position: absolute;
    top: 7vw;
    margin: 0;
    padding-left: 17vw;
    padding-top: 3vw;
    font-size: 110px;
    z-index: -1;
    text-decoration: underline;
  }

  img {
    top: 5vw;
    left: 0;
    /* Préserve le ratio de l'image */
    min-width: 100%;
    position: absolute;
    width: 100%;
    z-index: -2;
  }

  h2 {
    font-size: 68px;
    text-decoration: underline;
    margin: 2vw 8.6vw;
  }

  #message {
    font-size: 26px;
    margin-top: 55vw;
    text-justify: auto;
    text-align: center;
    padding: 2vw 20vw;
    background-color: #b4bec9;
  }

  h3 {
    padding-top: 2vw;
    font-size: 42px;
    text-align: center;
    text-decoration: underline;
    margin-bottom: 0;
  }

  p {
    text-align: center;
    font-size: 26px;
  }
}
</style>

<style>
#LocationCard {
  text-decoration: none;
}
</style>
