<template>
  <div class="HelloWorld">
    <h1>
      Nom des Employés
    </h1>
    <br/>
    <h2>JSON des employés</h2>
    <p>{{employes}}</p>
    <div v-for="(employe) in employes" :key="employe.id">
      <h2>JSON de l'employé {{employe.id}}</h2>
      <p>{{employe}}</p>
    </div>
    <h2>donée des employes</h2>
    <p>{{employes}}</p>
    <div v-for="(employe) in employes" :key="employe.id">
      <h2>JSON de l'employé {{employe.id}}</h2>
      <p>Nom: {{employe.name}}</p>
      <p>Description: {{employe.description}}</p>
    </div>
    
    
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'HelloWorld',
  data(){
    return{
      employes:null,
    }
  },
  mounted(){
    axios
    .get('http://127.0.0.1:8000/employee/')
    .then((reponse) => {
      this.employes=reponse.data;
      console.log(this.employes);
      })
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
