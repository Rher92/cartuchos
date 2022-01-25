<template>
  <section>
    <form @submit.prevent="submit">
      
      <!-- CLIENTE -->
      <div class="bg-light">
        <div class="row">
          <h3 class="text-center" style="margin: 5px">Cliente</h3>
          <div class="col-md col-sm form-group">
            <label for="cifrc" class="form-label">CIFRC:</label>
            <div id="cifrc">
              <v-select 
                :options="response_short"
                @input="setSelectedShort"
                label="cifrc"
                v-model="form.cifrc" 
                v-bind:class="{'form-control':true, 'is-invalid' : !validInputTexts(form.cifrc)  && form.fieldsBlured}"
                v-on:blur="fieldsBlured = true">
              ></v-select>
              <div class="invalid-feedback">CIFRC es requerido</div>
            </div>
          </div>
          <div class="col-md col-sm form-group">
            <label for="name" class="form-label">Nombre:</label>
              <v-select 
                :options="response_short"
                @input="setSelectedShort"
                label="nombre_razon_social"
                v-model="form.name" 
                v-bind:class="{'form-control':true, 'is-invalid' : !validInputTexts(form.cifrc)  && form.fieldsBlured}"
                v-on:blur="fieldsBlured = true">
              ></v-select>
            <div class="invalid-feedback">Nombre es requerido</div>
          </div>
        </div>
        
        <!-- <div id="cifrc">
          <h1>Vue Select</h1>
          <v-select 
            :options="response_large"
            @input="setSelected"
            label="cifrc"
            v-model="form.cifrc" 
            v-bind:class="{'form-control':true, 'is-invalid' : !validInputTexts(form.cifrc)  && form.fieldsBlured}"
            v-on:blur="fieldsBlured = true">
          ></v-select>
        </div> -->

        <!-- INFORMACION -->
        <div class="row" style="margin-top: 15px">
          <h3 class="text-center" style="margin: 5px">Información</h3>
          <div class="col-md col-sm form-group">
              <label for="number" class="form-label">Número:</label>
              <span class="input-group-text" id="basic-addon3 " v-if="!this.form.number">-</span>
              <span class="input-group-text" id="basic-addon3 " v-else>{{form.number}}</span>
          </div>
          <div class="col-md col-sm form-group">
              <label for="address" class="form-label">Dirección:</label>
              <span class="input-group-text" id="basic-addon3" v-if="!this.form.address">-</span>
              <span class="input-group-text" id="basic-addon3" v-else>{{form.address}}</span>
          </div>
        </div>
        <div class="row">
          <div class="col-md col-sm form-group">
              <label for="contact" class="form-label">Persona de Contacto:</label>
              <span class="input-group-text" id="basic-addon3" v-if="!this.form.contact">-</span>
              <span class="input-group-text" id="basic-addon3" v-else>{{form.contact}}</span>
          </div>
          <div class="col-md col-sm form-group">
              <label for="telephone" class="form-label">Teléfono:</label>
              <span class="input-group-text" id="basic-addon3" v-if="!this.form.telephone">-</span>
              <span class="input-group-text" id="basic-addon3" v-else>{{form.telephone}}</span>
          </div>
          <div class="col-md col-sm form-group">
              <label for="email" class="form-label">Correo:</label>
              <span class="input-group-text" id="basic-addon3" v-if="!this.form.email">-</span>
              <span class="input-group-text" id="basic-addon3" v-else>{{form.email}}</span>
          </div>
          <div class="col-md col-sm form-group">
              <label for="rate" class="form-label">Rate:</label>
              <span class="input-group-text" id="basic-addon3" v-if="!this.form.rate">-</span>
              <span class="input-group-text" id="basic-addon3" v-else>{{form.rate}}</span>
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
import vSelect from "vue-select"
import "vue-select/dist/vue-select.css";

export default {
  name: 'Albaran',
  data() {
    return {

      response_short: [
        {
            "id": 53,
            "cifrc": "b99456931",
            "nombre_razon_social": "365 vozes s.l."
        },
        {
            "id": 54,
            "cifrc": "b29750445",
            "nombre_razon_social": "3b intermatic sl"
        },
      ],
      response_large: [
          {
              "id": 53,
              "cifrc": "b99456931",
              "direccion": "calle  escritor josé donoso, 11 ",
              "telefono": "876 030 299",
              "persona_contacto": "",
              "email": "agarcia@365vozes.com",
              "nombre_razon_social": {
                  "nombre": "365 vozes s.l."
              },
              "contrato_firmado": {
                  "nombre": "false"
              },
              "clasificacion": {
                  "nombre": "c*"
              }
          },
        {
            "id": 54,
            "cifrc": "b29750445",
            "direccion": "avda. ricardo soriano, 36, 1",
            "telefono": "34 952 82 65 51",
            "persona_contacto": "",
            "email": "comercial@3bgrupo.com",
            "nombre_razon_social": {
                "nombre": "3b intermatic sl"
            },
            "contrato_firmado": {
                "nombre": "false"
            },
            "clasificacion": {
                "nombre": "c*"
            }
        }
      ],

      form: {
        fieldsBlured : false,
        valid : false,
        submitted : false,

        // CLIENT
        cifrc: '',
        name:'',

        // INFORMACION
        number: '',
        address: '',
        telephone: '',
        email: '',
        contact: '',
        rate: '',

        // DESCARTABLES
        salesman: '',
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
    // selectedOption(){
    //   console.log("here")
    // },
    setSelectedShort(value){
        if(value != null){
          this.form.cifrc = value.cifrc
          this.form.name = value.nombre_razon_social
        } else {
          for (let items in this.form){
            this.form[items] = ''
          }
        } 
    },
    setSelected(value)
    {
      if(value != null){
        this.form.cifrc = value.cifrc
        this.form.name = value.nombre_razon_social.nombre
        this.form.number = value.nombre_razon_social.nombre
        this.form.address = value.direccion
        this.form.telephone = value.telefono
        this.form.email = value.email
        this.form.contact = value.persona_contacto
        this.form.rate = value.clasificacion.nombre
        this.form.number = value.id
      }else{
        for (let items in this.form){
          this.form[items] = ''
        }
      }

    },
    validate : function(){
      this.form.fieldsBlured = true;

      // let cifrcv = this.validInputTexts(this.form.cifrc)
      // let namev = this.validInputTexts(this.form.name)
      // salesmanv = this.validInputTexts(this.form.salesman)

      // weightv = this.validInputNumber(this.form.weight)
      // laser_residualv = this.validInputNumber(this.form.laser_residual)
      // inkject_residualv = this.validInputNumber(this.form.inkject_residual)
      // laser_weightv = this.validInputNumber(this.form.laser_weight)
      // inkjet_weightv = this.validInputNumber(this.form.inkjet_weight)
      // total_weightv = this.validInputNumber(this.form.total_weight)
      // total_itemsv = this.validInputNumber(this.form.total_items)
      //  if(namev && cifrcv){
      //     this.valid = true;
      //  }
    },
    validInputTexts : function(field) {
      if (field !== '' && field !== null){ 
        let _return = false;
        if (field.length > 0){
          _return = true
        }
        return _return;
        }
    },
    validInputNumber : function(field) {
      if (field !== '' && field !== null){ 
        let _return = false;
        if (field > 0){
          _return = true
        }
        return _return;
      }
    },
    submit : function(){
        this.validate();
        if(this.form.valid){
          //THIS IS WHERE YOU SUBMIT DATA TO SERVER
          this.form.submitted = true;
        }
      } //end submit
  },
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
  components:{
    vSelect
  },
}


</script>


