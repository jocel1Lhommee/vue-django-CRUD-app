import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import EvenementielView from "../views/EvenementielView.vue";
import LocationView from "../views/LocationView.vue";
import TraiteurView from "../views/TraiteurView.vue";
import AboutView from "../views/AboutView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/location",
    name: "location",
    component: LocationView,
  },
  {
    path: "/evenementiel",
    name: "evenementiel",
    component: EvenementielView,
  },
  {
    path: "/traiteur",
    name: "traiteur",
    component: TraiteurView,
  },
  {
    path: "/about",
    name: "about",
    component: AboutView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
