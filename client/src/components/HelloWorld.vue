<template>
  <div class="HelloWorld">
    <h1>
      Nom des Employés
    </h1>
      <div :key="id" v-for="(employes,id) in employes">
        <h2>{{employes}}</h2>
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
    .get('http://127.0.0.1:8000/employee/1')
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
