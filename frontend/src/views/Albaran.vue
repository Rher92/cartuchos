<template>
  <section>
    <form @submit.prevent="submit">
      
      <!-- CLIENTE -->
      <div class="bg-light">
        <div class="row">
          <h3 class="text-center" style="margin: 5px">Cliente</h3>
          <div class="col-md col-sm form-group">
            <label for="cifrc" class="form-label">CIFRC:</label>
            <input 
              v-model="form.cifrc" 
              v-bind:class="{'form-control':true, 'is-invalid' : !validInputTexts(form.cifrc)  && form.fieldsBlured}"
              v-on:blur="fieldsBlured = true">
            <div class="invalid-feedback">CIFRC es requerido</div>
          </div>
          <div class="col-md col-sm form-group">
            <label for="name" class="form-label">Nombre:</label>
            <input 
              v-model="form.name" 
              v-bind:class="{'form-control':true, 'is-invalid' : !validInputTexts(form.name)  && form.fieldsBlured}"
              v-on:blur="fieldsBlured = true">
            <div class="invalid-feedback">Nombre es requerido</div>
          </div>
        </div>
        
        <!-- INFORMACION -->
        <div class="row" style="margin-top: 15px">
          <h3 class="text-center" style="margin: 5px">Información</h3>
          <div class="col-md col-sm form-group">
              <label for="number" class="form-label">Número:</label>
              <span class="input-group-text" id="basic-addon3">Número</span>
          </div>
          <div class="col-md col-sm form-group">
              <label for="address" class="form-label">Dirección:</label>
              <span class="input-group-text" id="basic-addon3">Dirección</span>
          </div>
        </div>
        <div class="row">
          <div class="col-md col-sm form-group">
              <label for="contact" class="form-label">Persona de Contacto:</label>
              <span class="input-group-text" id="basic-addon3">Persona de Contacto</span>
          </div>
          <div class="col-md col-sm form-group">
              <label for="telephone" class="form-label">Teléfono:</label>
              <span class="input-group-text" id="basic-addon3">Teléfono</span>
          </div>
          <div class="col-md col-sm form-group">
              <label for="email" class="form-label">Correo:</label>
              <span class="input-group-text" id="basic-addon3">Correo</span>
          </div>
          <div class="col-md col-sm form-group">
              <label for="rate" class="form-label">Rate:</label>
              <span class="input-group-text" id="basic-addon3">Rate</span>
          </div>
        </div>

        <!-- DESCARTABLES -->
        <div class="row" style="margin-top: 15px">
          <h3 class="text-center" style="margin: 5px">Descartables</h3>
          <div class="col-md col-sm form-group">
              <label for="salesman" class="form-label">Vendedor:</label>
              <input 
                v-model="form.salesman" 
                v-bind:class="{'form-control':true, 'is-invalid' : !validInputTexts(form.salesman)  && form.fieldsBlured}"
                v-on:blur="fieldsBlured = true">
              <div class="invalid-feedback">Vendedor es requerido</div>
          </div>
          <div class="col-md col-sm form-group">
            <label for="weight" class="form-label">Peso:</label>
            <input
              type="number"
              v-model="form.weight" 
              v-bind:class="{'form-control':true, 'is-invalid' : !validInputTexts(form.weight)  && form.fieldsBlured}"
              v-on:blur="fieldsBlured = true">
            <div class="invalid-feedback">Peso es requerido</div>
          </div>
        </div>
        <div class="row">
          <div class="col-md col-sm form-group">
            <label for="laser_residual" class="form-label">Laser Residual:</label>
            <input
              type="number"
              v-model="form.laser_residual" 
              v-bind:class="{'form-control':true, 'is-invalid' : !validInputTexts(form.laser_residual)  && form.fieldsBlured}"
              v-on:blur="fieldsBlured = true">
            <div class="invalid-feedback">Laser Residual es requerido</div>
          </div>
          <div class="col-md col-sm form-group">
            <label for="inkject_residual" class="form-label">Inkject Residual:</label>
            <input 
              type="number"
              v-model="form.inkject_residual" 
              v-bind:class="{'form-control':true, 'is-invalid' : !validInputTexts(form.inkject_residual)  && form.fieldsBlured}"
              v-on:blur="fieldsBlured = true">
            <div class="invalid-feedback">Inkject Residual es requerido</div>          
          </div>
        </div>
        <div class="row">
          <div class="col-md col-sm form-group">
            <label for="laser_weight" class="form-label">Peso Laser(Kg):</label>
            <input
              type="number"
              v-model="form.laser_weight" 
              v-bind:class="{'form-control':true, 'is-invalid' : !validInputTexts(form.laser_weight)  && form.fieldsBlured}"
              v-on:blur="fieldsBlured = true">
            <div class="invalid-feedback">Peso Laser es requerido</div>
          </div>
          <div class="col-md col-sm form-group">
            <label for="inkjet_weight" class="form-label">Peso Inkject(Kg):</label>
            <input
              type="number"
              v-model="form.inkjet_weight" 
              v-bind:class="{'form-control':true, 'is-invalid' : !validInputTexts(form.inkjet_weight)  && form.fieldsBlured}"
              v-on:blur="fieldsBlured = true">
            <div class="invalid-feedback">Peso Inkject es requerido</div>
          </div>
        </div>
        <div class="row">
          <div class="col-md col-sm form-group">
            <label for="total_items" class="form-label">Artículos en total:</label>
            <input
              type="number"
              v-model="form.total_items" 
              v-bind:class="{'form-control':true, 'is-invalid' : !validInputTexts(form.total_items)  && form.fieldsBlured}"
              v-on:blur="fieldsBlured = true">
            <div class="invalid-feedback">Artículos en total es requerido</div>
          </div>
          <div class="col-md col-sm form-group">
            <label for="total_weight" class="form-label">Peso Total(Kg):</label>
            <input
              type="number"
              v-model="form.total_weight" 
              v-bind:class="{'form-control':true, 'is-invalid' : !validInputTexts(form.total_weight)  && form.fieldsBlured}"
              v-on:blur="fieldsBlured = true">
            <div class="invalid-feedback">Peso Total es requerido</div>
          </div>
        </div>
      </div>

      <div class="col-md col-sm d-grid gap-2 d-md-flex justify-content-md-end">
        <button type="submit" class="btn btn-primary " style="margin-top: 15px; margin-bottom: 15px;">Siguiente</button>
      </div>

    </form>
  </section>
</template>

<script>
// import { mapActions } from 'vuex';
export default {
  name: 'Albaran',
  data() {
    return {
      form: {
        fieldsBlured : false,
        valid : false,
        submitted : false,

        // CLIENT
        cifrc: '',
        name:'',

        // INFORMACION
        number: '',
        address:'',
        telephone: '',
        email:'',
        contact: '',
        rate:'',

        // DESCARTABLES
        salesman:'',
        weight: '',
        laser_residual: '',
        inkject_residual: '',
        laser_weight: '',
        inkjet_weight: '',
        total_weight: '',
        total_items: '',
      }
    };
  },
  methods : {
    validate : function(){
      this.form.fieldsBlured = true;

      cifrcv = this.validInputTexts(this.form.cifrc)
      namev = this.validInputTexts(this.form.name)
      salesmanv = this.validInputTexts(this.form.salesman)

      weightv = this.validInputNumber(this.form.weight)
      laser_residualv = this.validInputNumber(this.form.laser_residual)
      inkject_residualv = this.validInputNumber(this.form.inkject_residual)
      laser_weightv = this.validInputNumber(this.form.laser_weight)
      inkjet_weightv = this.validInputNumber(this.form.inkjet_weight)
      total_weightv = this.validInputNumber(this.form.total_weight)
      total_itemsv = this.validInputNumber(this.form.total_items)
       if(namev && cifrcv){
          this.valid = true;
       }
    },
    validInputTexts : function(field) {
      let _return = false;
      if (field.length > 0){
        _return = true
      }
      return _return;
    },
    validInputNumber : function(field) {
      let _return = false;
      if (field > 0){
        _return = true
      }
      return _return;
    },
    submit : function(){
        this.validate();
        if(this.form.valid){
          //THIS IS WHERE YOU SUBMIT DATA TO SERVER
          this.form.submitted = true;
        }
      } //end submit
  }
  // methods: {
  //   ...mapActions(['logIn']),
  //   async submit() {
  //     const User = new FormData();
  //     User.append('username', this.form.username);
  //     User.append('password', this.form.password);
  //     await this.logIn(User);
  //     this.$router.push('/profile').catch((e) => console.log(e));;
  //   }
  // }
}
</script>
