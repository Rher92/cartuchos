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
                label="cifrc"
                :debounce="250"
                :filterable="false"
                :options="options"
                @input="setSelectedShort"
                @search="onSearchCifrc"
                v-model="form.cifrc"
                v-bind:class="{'form-control':true, 'is-invalid' : !validInputTexts(form.cifrc)  && form.fieldsBlured}"
                v-on:blur="fieldsBlured = true">
                <template slot="no-options">
                  Escribe para buscar clientes..
                </template>
                <template slot="option" slot-scope="option">
                  <div class="d-center">
                    {{ option.cifrc }}
                    </div>
                </template>
                <template slot="selected-option" slot-scope="option">
                  <div class="selected d-center">
                    {{ option.cifrc }}
                  </div>
                </template>
              </v-select>
              <div class="invalid-feedback">CIFRC es requerido</div>
            </div>
          </div>
          <div class="col-md col-sm form-group">
            <label for="name" class="form-label">Nombre:</label>
              <v-select
                label="nombre_razon_social"
                :debounce="250"
                @input="setSelectedShort"
                @search="onSearchNombre"
                :filterable="false"
                :options="options"
                v-model="form.name"
                v-bind:class="{'form-control':true, 'is-invalid' : !validInputTexts(form.nombre_razon_social)  && form.fieldsBlured}"
                v-on:blur="fieldsBlured = true">
                <template slot="no-options">
                  Escribe para buscar clientes..
                </template>
                <template slot="option" slot-scope="option">
                  <div class="d-center">
                    {{ option.nombre_razon_social }}
                    </div>
                </template>
                <template slot="selected-option" slot-scope="option">
                  <div class="selected d-center">
                    {{ option.nombre_razon_social }}
                  </div>
                </template>
              </v-select>
            <div class="invalid-feedback">Nombre es requerido</div>
          </div>
        </div>


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



  <div>
   <b-form-group
      label="Subfamilia:"
      label-for="table-select-mode-select"
      label-cols-md="4"
    >
      <b-form-select
        id="table-select-mode-select"
        v-model="subfamily.selected"
        :options="subfamily.items"
        class="mb-3"
        v-on:change="subFamilyFilter"
      ></b-form-select>
    </b-form-group>

  <b-form-group
    label="familia:"
    label-for="table-select-mode-select"
    label-cols-md="4"
  >
    <b-form-select
      id="table-select-mode-select"
      v-model="family.selected"
      :options="family.items"
      class="mb-3"
      v-on:change="FamilyFilter"
    ></b-form-select>
  </b-form-group>


    <b-table
      :items="cartridge.items"
      :fields="cartridge.fields"
      :select-mode="selectMode"
      responsive="sm"
      ref="selectableTable"
      selectable
      @row-selected="onRowSelected"
    >
      <!-- Example scoped slot for select state illustrative purposes -->
      <template #cell(selected)="{ rowSelected }">
        <template v-if="rowSelected">
          <span aria-hidden="true">&check;</span>
          <!-- <span class="sr-only">Selected</span> -->
        </template>
        <template v-else>
          <span aria-hidden="true">&nbsp;</span>
          <!-- <span class="sr-only">Not selected</span> -->
        </template>
      </template>
    </b-table>
    <p>
      <b-button size="sm" @click="selectAllRows">Select all</b-button>
      <b-button size="sm" @click="clearSelected">Clear selected</b-button>
    </p>
    <p>
      Selected Rows:<br>
      {{ cartridge.selected }}
      {{ cartridge.items_selected }}
    </p>
  </div>

    <div class="overflow-auto">
    <!-- Use text in props -->
      <b-pagination
        v-model="cartridge.currentPage"
        @input= "updatePage(cartridge.currentPage)"
        :total-rows="cartridge.rows"
        :per-page="cartridge.perPage"
        first-text="First"
        prev-text="Prev"
        next-text="Next"
        last-text="Last"
      ></b-pagination>
    </div>

    </form>
  </section>
</template>

<script>
import vSelect from "vue-select"
import "vue-select/dist/vue-select.css";
import { mapActions } from 'vuex';
import debounce from 'lodash/debounce';
import axios from 'axios';


export default {
  name: 'Albaran',

  data() {
    return {
      endpoint: process.env.VUE_APP_BASE_URL,
      options: [],

        modes: ['multi', 'single', 'range'],
        // _fields: ['selected', 'familia', 'subfamilia', 'modelo', 'referencia', 'peso', 'marca', 'codigo'],
        fields: ['selected', 'isActive', 'age', 'first_name', 'last_name'],
        items: [
          { isActive: true, age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
          { isActive: false, age: 21, first_name: 'Larsen', last_name: 'Shaw' },
          { isActive: false, age: 89, first_name: 'Geneva', last_name: 'Wilson' },
          { isActive: true, age: 38, first_name: 'Jami', last_name: 'Carney' }
        ],
        // _items: [],
        selectMode: 'multi',
        selected: [],

      cartridge: {
        next_cartridge: '',
        previous_cartridge: '',
        total: '',
        fields: ['selected', 'familia', 'subfamilia', 'modelo', 'referencia', 'peso', 'marca', 'codigo'],
        items: [],
        items_selected: [],
        items_selected_ids: [],
        selected: [],
        rows: '',
        perPage: '',
        currentPage: '',
      },

      filters: '',

      subfamily: {
        items: [],
        selected: 'TODOS',
        last_selected: 'TODOS',
        filter: 'family_intern__name=TODOS'
      },

      family: {
        items: [],
        selected: 'TODOS',
        last_selected: 'TODOS',
        filter: 'family__name=TODOS'
      },

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
    ...mapActions(['getClients']),

    onSearchCifrc(search, loading) {
      if(search.length) {
        loading(true);
        var ep = `/api/clients/short/?cifrc=${search}`
        this.search(loading, ep, this)
      }
    },

    onSearchNombre(search, loading) {
      if(search.length) {
        loading(true);
        var ep = `/api/clients/short/?nombre_razon_social__nombre=${search}`
        this.search(loading, ep, this);
      }
    },

    getClientFull(id, form) {
        var ep = `${this.endpoint}/api/clients/${id}`
        fetch(ep, {
            method: 'get',
            // headers: {
            //   "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
            // },
          })
          .then(res => {
            res.json().then( json =>(
              // console.log('Request succeeded with JSON response', json),
              form.address = json.direccion,
              form.telephone = json.telefono,
              form.email = json.email,
              form.contact = json.persona_contacto,
              form.rate = json.clasificacion.nombre,
              form.number = json.id)
            )
          })
          .catch(function (error) {
            console.log('Request failed', error);
          });
    },

    getCartridgesRecharge(filter=false){
        var ep = `${this.endpoint}/api/cartridges`
        if (filter == true){
          ep = `${this.endpoint}/api/cartridges/?${this.subfamily.filter}&${this.family.filter}`
        }
        
        fetch(ep, {
            method: 'get',
            // headers: {
            //   "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
            // },
          })
          .then(res => {
            res.json().then( json =>(
                // console.log('Request succeeded with JSON response', json),
                this.cartridge.next_cartridge = json.next,
                this.cartridge.previous_cartridge = json.previous,
                this.cartridge.total = json.count,
            
                this.cartridge.items = json.results,

                this.cartridge.rows = this.cartridge.total,
                this.cartridge.perPage = json.results.length,
                this.cartridge.currentPage = 1

              )
            )
          })
          .catch(function (error) {
            console.log('Request failed', error);
          });
    },

    getCartridges(page=null){
        var ep = `${this.endpoint}/api/cartridges/?${this.subfamily.filter}&${this.family.filter}`
        if (page !== null){
          ep = `${this.endpoint}/api/cartridges/?page=${page}&${this.subfamily.filter}&${this.family.filter}`
        }

        this.cartridge.selected.forEach(element => {
          if (!(JSON.parse(JSON.stringify(this.cartridge.items_selected_ids.includes(element.id))))){
            this.cartridge.items_selected.push(element)
            this.cartridge.items_selected_ids.push(element.id)
          }
        });
        
        fetch(ep, {
            method: 'get',
            // headers: {
            //   "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
            // },
          })
          .then(res => {
            res.json().then( json =>(
                // console.log('Request succeeded with JSON response', json),
                this.cartridge.next_cartridge = json.next,
                this.cartridge.previous_cartridge = json.previous,
                this.cartridge.total = json.count,
            
                this.cartridge.items = json.results

              )
            )
          })
          .catch(function (error) {
            console.log('Request failed', error);
          });
    },

    updatePage(currentPage){
      var page = null
      if (currentPage > 1){
        page = currentPage
      }
      this.getCartridges(page)
    },

    search: debounce((loading, ep, vm) => {
      axios
      .get(ep)
      .then(
        response => {
          vm.options = response.data.results
          // vm.options = this.getClients(search);  why it does not work.
        } 
      ).catch(
        error => {
          console.log(error)
        })
      loading(false);
    }, 350),

    setSelectedShort(value){
        if(value != null){
          this.form.cifrc = value.cifrc
          this.form.name = value.nombre_razon_social
          this.form.number = value.id
          this.getClientFull(value.id, this.form)
        } else {
          for (let items in this.form){
            this.form[items] = ''
          }
        } 
    },

    // setSelected(value){
    //     let data = this.getClientFull(value)
    //     console.log(data)
    //     this.form.address = data.direccion
    //     this.form.telephone = data.telefono
    //     this.form.email = data.email
    //     this.form.contact = data.persona_contacto
    //     this.form.rate = data.clasificacion.nombre
    //     this.form.number = data.id
    //   },


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
      if (field !== '' && field !== null && field !== undefined){ 
        let _return = false;
        if (field.length > 0){
          _return = true
        }
        return _return;
        }
    },
    
    validInputNumber : function(field) {
      if (field !== '' && field !== null && field !== undefined){ 
        let _return = false;
        if (field > 0){
          _return = true
        }
        return _return;
      }
    },

    onRowSelected(items) {
      this.cartridge.selected = items
    },
    selectAllRows() {
      this.$refs.selectableTable.selectAllRows()
    },
    clearSelected() {
      this.$refs.selectableTable.clearSelected()
    },
    selectThirdRow() {
      // Rows are indexed from 0, so the third row is index 2
      this.$refs.selectableTable.selectRow(2)
    },
    unselectThirdRow() {
      // Rows are indexed from 0, so the third row is index 2
      this.$refs.selectableTable.unselectRow(2)
    },

    subFamilyFilter: function (event) {
      if (event != this.subfamily.last_selected) {
        this.subfamily.last_selected = event
        this.subfamily.filter = `family_intern__name=${event}`
        this.cartridge.selected.forEach(element => {
          if (!(JSON.parse(JSON.stringify(this.cartridge.items_selected_ids.includes(element.id))))){
            this.cartridge.items_selected.push(element)
            this.cartridge.items_selected_ids.push(element.id)
          }
        });
        this.getCartridgesRecharge(true)
      }
    },

    FamilyFilter: function (event) {
      if (event != this.family.last_selected) {
        this.family.last_selected = event
        this.family.filter = `family__name=${event}`
        this.cartridge.selected.forEach(element => {
          if (!(JSON.parse(JSON.stringify(this.cartridge.items_selected_ids.includes(element.id))))){
            this.cartridge.items_selected.push(element)
            this.cartridge.items_selected_ids.push(element.id)
          }
        });
        this.getCartridgesRecharge(true)
      }
    },

    getSubFamilies: function(){
        var ep = `${this.endpoint}/api/cartridges/subfamily_name`
        fetch(ep, {
            method: 'get',
            // headers: {
            //   "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
            // },
          })
          .then(res => {
            res.json().then( json =>(
                this.subfamily.items = json
              )
            )
          })
          .catch(function (error) {
            console.log('Request failed', error);
          });
    },

    getFamilies: function(){
        var ep = `${this.endpoint}/api/cartridges/family_name`
        fetch(ep, {
            method: 'get',
            // headers: {
            //   "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
            // },
          })
          .then(res => {
            res.json().then( json =>(
                this.family.items = json
              )
            )
          })
          .catch(function (error) {
            console.log('Request failed', error);
          });
    }

  },

  components:{
    vSelect
  },

  mounted() {
    // console.log(this.$el.querySelectorAll('a'));
    this.getCartridgesRecharge()
    this.getSubFamilies()
    this.getFamilies()
  },

}

</script>


