<template>
  <div class="location">
    <h1>Grande Villa</h1>
    <LocationSlider />
    <h1>Petite Villa</h1>
    <LocationSlider />
    <p>
      La Villa Charlestine, est une grande concession où se trouve une grande
      villa 06 pièces, ainsi qu'une petite villa elle aussi en location meublée.
      Magnifiquement arborée et sécurisée, avec un accès facile par route
      bitumée, ces villas disposent de chambres climatisées(2 pour la petite
      Villa et 4 pour la grande Villa), d'un salon, d'une cuisine équipée, une
      douche(3 pour la Grande Villa) et un WC(2 pour la Grande Villa). Vous
      disposerez des avantages de la concession: groupe électrogène, réserve
      d'eau, buanderie, gardiennage de jour comme de nuit, grand terrain de jeux
      pour enfant, balançoire. Pour visiter la villa c'est de 8h à 15h Vous y
      trouverez une ambiance détendue et chaleureuseainsi qu'une équipe
      disponible et attentive au service de sa clientèle. Une seule adresse:
      Villa Charlestine, We are the "Best" Thuss A très bientôt !
    </p>
  </div>
</template>

<script>
import LocationSlider from "../components/LocationSlider.vue";

export default {
  name: "LocationView",
  components: {
    LocationSlider,
  },
};
</script>

<style lang="scss" scoped>
p {
  font-size: 26px;
  text-justify: auto;
  text-align: justify;
  padding: 2vw 5vw;
  background-color: #b4bec9;
}

h1 {
  font-size: 68px;
  text-decoration: underline;
  padding-left: 7vw;
  padding-top: 3vw;
  margin: 0;
}

.location {
  padding-top: 8vw;
}
</style>
