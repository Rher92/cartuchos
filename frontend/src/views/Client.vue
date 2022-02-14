<template>
  <section>
    <form @submit.prevent="onSubmit">
      <b-overlay :show="show_overlay" rounded="sm" @shown="onShown" @hidden="onHidden">

      <template #overlay>
        <div class="text-center">
          <b-icon icon="stopwatch" font-scale="3" animation="cylon"></b-icon>
          <h3 d="cancel-label" class="text-center">Procesando Información, por favor espere...</h3>
          <b-button
            ref="cancel"
            variant="outline-danger"
            size="sm"
            aria-describedby="cancel-label"
            @click="show_overlay = false"
          >
            Cancel
          </b-button>
        </div>
      </template>

      <!-- CLIENTE -->
      <div class="bg-light">
        <div class="row">
          <h3 class="text-center" style="margin: 5px">Cliente</h3>
          <div class="col-md col-sm form-group">
            <label for="cifrc" class="form-label">CIFRC:</label>
            <div ref="show" id="cifrc">
              <v-select
                label="cifrc"
                :debounce="250"
                :filterable="false"
                :options="options"
                @input="setSelectedShort"
                @search="onSearchCifrc"
                v-model="form.cifrc"
                v-bind:class="{'form-control':true, 'is-invalid' : !validInputTexts(form.cifrc)  && form.fieldsBlured}"
                v-on:blur="form.fieldsBlured = true">
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
                :filterable="false"
                :options="options"
                @input="setSelectedShort"
                @search="onSearchNombre"
                v-model="form.name"
                v-bind:class="{'form-control':true, 'is-invalid' : !validInputTexts(form.name)  && form.fieldsBlured}"
                v-on:blur="form.fieldsBlured = true">
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
        <div class="row">
          <div class="col-md col-sm form-group">
              <label for="address" class="form-label">Dirección:</label>
              <span class="input-group-text" id="basic-addon3" v-if="!this.form.address">-</span>
              <span class="input-group-text" id="basic-addon3" v-else>{{form.address}}</span>
          </div>
        </div>
        <div class="row">
          <div class="col-md col-sm form-group">
              <label for="address" class="form-label">Población:</label>
              <span class="input-group-text" id="basic-addon3" v-if="!this.form.community">-</span>
              <span class="input-group-text" id="basic-addon3" v-else>{{form.community}}</span>
          </div>
          <div class="col-md col-sm form-group">
              <label for="number" class="form-label">País:</label>
              <span class="input-group-text" id="basic-addon3 " v-if="!this.form.country">-</span>
              <span class="input-group-text" id="basic-addon3 " v-else>{{form.country}}</span>
          </div>
        </div>
        <div class="row">
          <div class="col-md col-sm form-group">
              <label for="address" class="form-label">Zona geografica:</label>
              <span class="input-group-text" id="basic-addon3" v-if="!this.form.geoZone">-</span>
              <span class="input-group-text" id="basic-addon3" v-else>{{form.geoZone}}</span>
          </div>
          <div class="col-md col-sm form-group">
              <label for="number" class="form-label">Provincia:</label>
              <span class="input-group-text" id="basic-addon3 " v-if="!this.form.province">-</span>
              <span class="input-group-text" id="basic-addon3 " v-else>{{form.province}}</span>
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
              <label for="rate" class="form-label">Tarifa asignada:</label>
              <span class="input-group-text" id="basic-addon3" v-if="!this.form.assignedRate">-</span>
              <span class="input-group-text" id="basic-addon3" v-else>{{form.assignedRate}}</span>
          </div>
        </div>
      </div>

        <!-- DESCARTABLES -->
        <div class="bg-light">
        <div class="row" style="margin-top: 15px">
          <h3 class="text-center" style="margin: 5px">Información del albarán</h3>
          <div class="col-md col-sm form-group">
              <label for="salesman" class="form-label">Vendedor:</label>
              <span class="input-group-text" id="basic-addon3">{{user.user.username}}</span>
          </div>
          <div class="col-md col-sm form-group">
            <label for="weight" class="form-label">Peso Caja(Kg):</label>
            <input
              type="number" min="0"
              v-model="form.weight" 
              v-bind:class="{'form-control':true, 'is-invalid' : !validInputNumberGreaterThanZero(form.weight)  && form.fieldsBlured}"
              v-on:blur="fieldsBlured = true"
              v-on:input="calculateWeightTotals">
            <div class="invalid-feedback">Peso es requerido y ser mayor 0</div>
          </div>
        </div>
        <div class="row">
          <div class="col-md col-sm form-group">
            <label for="total_items" class="form-label">Artículos en total:</label>
              <span class="input-group-text" id="basic-addon3">{{form.total_items}}</span>
            <div class="invalid-feedback">Artículos en total es requerido</div>
          </div>
          <div class="col-md col-sm form-group">
            <label for="total_weight" class="form-label">Peso Total Albaran(Kg):</label>
              <span class="input-group-text" id="basic-addon3">{{form.total_weight}}</span>
            <div class="invalid-feedback">Peso Total es requerido</div>
          </div>
        </div>
        <div class="row">
          <div class="col-md col-sm form-group">
            <label for="laser_residual" class="form-label">Laser Residual(%):</label>
            <input
              type="number" min="0" max="100"
              v-model="form.laser_residual" 
              v-bind:class="{'form-control':true, 'is-invalid' : !validInputNumber(form.laser_residual)  && form.fieldsBlured}"
              v-on:blur="fieldsBlured = true"
              v-on:input="calculateWeightRemainingFromLaser">
            <div class="invalid-feedback">Laser Residual es requerido</div>
          </div>
          <div class="col-md col-sm form-group">
            <label for="inkject_residual" class="form-label">Inkject Residual(%):</label>
            <input 
              type="number" min="0" max="100"
              v-model="form.inkject_residual" 
              v-bind:class="{'form-control':true, 'is-invalid' : !validInputNumber(form.inkject_residual)  && form.fieldsBlured}"
              v-on:blur="fieldsBlured = true"
              v-on:input="calculateWeightRemainingFromInkjet">
            <div class="invalid-feedback">Inkject Residual es requerido</div>          
          </div>
        </div>
        <div class="row">
          <div class="col-md col-sm form-group">
            <label for="laser_weight" class="form-label">Peso Laser(Kg) Sobrante:</label>
              <span class="input-group-text" id="basic-addon3">{{form.laser_weight}}</span>
            <div class="invalid-feedback">Peso Laser es requerido</div>
          </div>
          <div class="col-md col-sm form-group">
            <label for="inkjet_weight" class="form-label">Peso Inkject(Kg) Sobrante:</label>
            <span class="input-group-text" id="basic-addon3">{{form.inkjet_weight}}</span>
          </div>
        </div>
        <div class="row">
          <div class="col-md col-sm form-group">
            <label for="laser_weight" class="form-label">Peso Laser(Kg) seleccionado en albaran:</label>
              <span class="input-group-text" id="basic-addon3">{{form.laser_weight}}</span>
            <div class="invalid-feedback">Peso Laser es requerido</div>
          </div>
          <div class="col-md col-sm form-group">
            <label for="inkjet_weight" class="form-label">Peso Inkject(Kg) seleccionado en albaran:</label>
            <span class="input-group-text" id="basic-addon3">{{form.inkjet_weight}}</span>
          </div>
        </div>
      </div>

      <!-- NOTA DEL ALMACEN -->
    <div class="bg-light" style="margin-top: 15px">
      <h3 class="text-center">Nota del almacén</h3>
      <template>
        <div>
          <b-form-textarea
            id="textarea"
            v-model="form.note"
            placeholder="Escriba nota adicional..."
            rows="3"
            max-rows="6"
          ></b-form-textarea>
        </div>
      </template>
    </div>

   <!-- CARTUCHOS -->
<div class="bg-light">
  <h3 class="text-center" style="margin: 15px">Cartuchos</h3>
  
  <div class="row">
    <div class="col-md col-sm form-group">
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
    </div>

    <div class="col-md col-sm form-group">
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
          v-on:change="familyFilter"
        ></b-form-select>
      </b-form-group>
    </div>

    <div class="col-md col-sm form-group">
      <b-form-group
        label="Filtro general:"
        label-cols-md="4"
      >
        <b-form-input class="w-75 p-1" v-on:input="generalFilter" v-model="general_filters.filter" type="search" placeholder="Escribe al menos 1 caracter">
        </b-form-input>
      </b-form-group>
    </div>

    <b-table
      :items="cartridge.items"
      :fields="cartridge.fields"
      :select-mode="selectMode"
      responsive="sm"
      ref="selectableTable"
      selectable
      @row-selected="onRowSelected"
      striped hover
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

    </div>
        <div class="overflow-auto">
      <!-- Use text in props -->
        <b-pagination
          v-model="cartridge.currentPage"
          :total-rows="cartridge.rows"
          :per-page="cartridge.perPage"
          @input= "updatePage(cartridge.currentPage)"
          first-text="First"
          prev-text="Prev"
          next-text="Next"
          last-text="Last"
        ></b-pagination>
      </div>
</div>

    <!-- CARTUCHOS SELECCIONADOS -->
  <div class="bg-light" style="margin-top: 15px">
      <h3 class="text-center">Cartuchos Seleccionados</h3>

      <div v-if="!validateLenghtArray(selected_cartridge.items)  && form.fieldsBlured">
        <span class="text-danger">Debe seleccionar al menos 1 cartucho</span>
      </div>

      <b-table
        :items="selected_cartridge.items"
        :fields="selected_cartridge.fields"
        :select-mode="selectMode"
        :per-page="selected_cartridge.perPage"
        :current-page="selected_cartridge.currentPage"
        v-bind:class="{'form-control':true, 'is-invalid' : !validateLenghtArray(selected_cartridge.items)  && form.fieldsBlured}"
        responsive="sm"
        ref="selectableTable"
        class="form-control"
        selectable
        striped hover
      >

        <template v-slot:cell(peso)="row">
          <div class="w-25">
            <template v-if="row.item.peso_total == 0 && selected_cartridge.weitgh_editable == false">
              <b-form-input type="number" min="0" v-model="row.item.peso" @keyup.enter.native="setWeightCartridge(row.index)"/>
            </template>
            <template v-else>
              <span >{{row.item.peso}}</span>
            </template>
          </div>
        </template>

        <template v-slot:cell(cantidad)="row">
          <div class="w-25">
            <b-form-input type="number" min="0" v-model="row.item.cantidad" v-on:change="setWeightCartridge(row.index)"/>
          </div>
        </template>

        <template #cell(borrar)="row">
          <b-button class="delete-button" variant="danger" @click="removeRowHandler(row.index)">X</b-button>
        </template>

      </b-table>

      <div class="overflow-auto">
        <b-pagination
          v-model="selected_cartridge.currentPage"
          :total-rows="selected_cartridge_rows"
          :per-page="selected_cartridge.perPage"
          first-text="First"
          prev-text="Prev"
          next-text="Next"
          last-text="Last"
        ></b-pagination>
      </div>

  </div>

    <div style="float:right; margin-top: 15px" class="">
     <b-button type="submit" block variant="primary">Guardar Albaran</b-button>
    </div>

    </b-overlay>

    <div>
      <b-modal id="modal-error" title="ERROR" ok-only>
        <p class="my-4">algún error ha ocurrido. intente de nuevo.</p>
      </b-modal>
    </div>

    <div>
      <b-modal id="modal-success" title="EXITO" ok-only>
        <p class="my-4">Se ha guaradado correctamente el Albarán.</p>
      </b-modal>
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
import { mapGetters } from 'vuex';


export default {
  name: 'Albaran',

  data() {
    return {
      endpoint: process.env.VUE_APP_BASE_URL,
      options: [],

      show_overlay: false,
      selectMode: 'multi',

      selected_cartridge: {
        perPage: 10,
        currentPage: 1,
        'fields': ['modelo', 'peso', 'marca', 'familia', 'cantidad', 'peso_total', 'borrar'],
        'items': [],
        'weitgh_editable': false,
        'weitgh': 0
      },

      cartridge: {
        next_cartridge: '',
        previous_cartridge: '',
        total: '',
        fields: ['selected', 'codigo', 'marca', 'familia', 'subfamilia', 'modelo', 'referencia', 'peso'], 
        items: [],
        items_selected: [],
        items_selected_ids: [],
        selected: [],
        rows: '',
        perPage: '',
        currentPage: 1,
      },

      general_filters: {
        filter: '',
        query: '',
        MIN_CHAR: 1
      },

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
        client_id: '',
        cifrc: '',
        name:'',

        // INFORMACION
        number: '',
        address: '',
        telephone: '',
        email: '',
        contact: '',
        rate: '',
        country: '',
        assignedRate: '',
        province: '',
        geoZone: '',
        community: '',

        // DESCARTABLES
        salesman: '',
        weight: 0,
        laser_residual: 0,
        inkject_residual: 0,
        laser_weight: 0,
        inkjet_weight: 0,
        total_weight: 0,
        total_items: 0,

        note: '',
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
              form.client_id = json.id,
              form.address = json.direccion.toUpperCase(),
              form.telephone = json.telefono.toUpperCase(),
              form.email = json.email.toUpperCase(),
              form.contact = json.persona_contacto.toUpperCase(),
              form.rate = json.clasificacion.toUpperCase(),
              form.number = json.id,
              form.country = json.pais.toUpperCase(),
              form.assignedRate = json.tarifa_asignada.toUpperCase(),
              form.province = json.provincia.toUpperCase(),
              form.geoZone = json.zona_geografica.toUpperCase(),
              form.community = json.poblacion.toUpperCase())
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

        if (this.general_filters.filter.length >= this.general_filters.MIN_CHAR){
          ep = ep + `&${this.general_filters.query}`
        }
        
        fetch(ep, {
            method: 'get',
            // headers: {
            //   "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
            // },
          })
          .then(res => {
            res.json().then( json =>(
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
        if (this.general_filters.filter.length >= this.general_filters.MIN_CHAR){
          ep = ep + `&${this.general_filters.query}`
        }
        
        fetch(ep, {
            method: 'get',
            // headers: {
            //   "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
            // },
          })
          .then(res => {
            res.json().then( json =>(
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
            if(['client_id', 'cifrc', 'name',
                'number', 'address', 'telephone',
                'email', 'contact', 'rate', 'country',
                'assignedRate', 'province', 'geoZone',
                'community'].includes(items)){
              this.form[items] = ''
            }
          }
        } 
    },

    validate: function(){
      this.form.fieldsBlured = true;
      let _return = false
      if (
          this.validInputTexts(this.form.cifrc) &&
          this.validInputTexts(this.form.name) &&
          this.validateLenghtArray(this.selected_cartridge.items) &&
          !this.show_overlay){
            _return = true
      }
      return _return
    },

    validateLenghtArray: function(array){
        let _return = false;
        if (array.length > 0){
          _return = true
        }
        return _return;
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
    
    validInputNumberGreaterThanZero : function(field) {
      if (field !== '' && field !== null && field !== undefined){ 
        let _return = false;
        if (field > 0){
          _return = true
        }
        return _return;
      }
    },

    validInputNumber : function(field) {
      if (field !== '' && field !== null && field !== undefined){
        let _return = false;
        if (field >= 0){
          _return = true
        }
        return _return;
      }
    },

    onRowSelected(items) {
      this.cartridge.selected = items
      items.forEach(element =>{
          if (!(JSON.parse(JSON.stringify(this.cartridge.items_selected_ids.includes(element.id))))){
            var cantidad = 1
            this.cartridge.items_selected_ids.push(element.id)
            this.selected_cartridge.items.push({
              'modelo': element.modelo,
              'marca': element.marca,
              'peso': element.peso,
              'cantidad': cantidad,
              'peso_total': (element.peso/1000) * cantidad,
              'familia': element.familia,
              'id': element.id
            })
          }
        this.calculateWeightTotals()
      })
    },

    subFamilyFilter: function (event) {
      if (event != this.subfamily.last_selected) {
        this.subfamily.last_selected = event
        this.subfamily.filter = `family_intern__name=${event}`
        this.getCartridgesRecharge(true)
      }
    },

    familyFilter: function (event) {
      if (event != this.family.last_selected) {
        this.family.last_selected = event
        this.family.filter = `family__name=${event}`
        this.getCartridgesRecharge(true)
      }
    },

    calculateWeightTotals: function(){
      let cartridges = this.selected_cartridge.items
      this.form.total_weight = 0
      this.form.total_items = 0
      this.form.inkjet_weight = 0
      this.form.laser_weight = 0

      cartridges.forEach(element =>{
          this.form.total_weight += element.peso_total
          this.form.total_items += parseInt(element.cantidad)
      })
      this.calculateWeightRemaining()
    },

    calculateWeightRemainingFromInkjet: function(){
      if(parseInt(this.form.inkject_residual) >= 100){
          this.form.laser_residual = 0
          this.form.inkject_residual = 100
        } else if(this.form.inkject_residual == ''){
            this.form.inkject_residual = 0
            this.form.laser_residual = 100
        } else {
          this.form.laser_residual = 100 - parseInt(this.form.inkject_residual)
        }
      this.calculateWeightRemaining()
    },

    calculateWeightRemainingFromLaser: function(){
      if(this.form.laser_residual >= 100){
          this.form.inkject_residual = 0
          this.form.laser_residual = 100
        } else if(this.form.laser_residual == ''){
            this.form.laser_residual = 0
            this.form.inkject_residual = 100
        } else {
          this.form.inkject_residual = 100 - parseFloat(this.form.laser_residual)
        }
        this.calculateWeightRemaining()
    },

    calculateWeightRemaining: function(){
      if (parseInt(this.form.total_weight) < parseInt(this.form.weight)){
        let remaining_weight = parseFloat(this.form.weight) - parseFloat(this.form.total_weight)
        let inkject_percent = parseFloat(this.form.inkject_residual) / 100
        let laser_percent = parseFloat(this.form.laser_residual) / 100
        this.form.laser_weight = laser_percent * remaining_weight
        this.form.inkjet_weight = inkject_percent * remaining_weight
      } else {
        this.form.laser_residual = 0
        this.form.inkject_residual = 0
        this.form.laser_weight = 0
        this.form.inkjet_weight = 0
      }
    },

    setWeightCartridge: function (index) {
      let cartridge = this.selected_cartridge.items[index]
      cartridge.peso_total = (cartridge.peso/1000) * cartridge.cantidad
      this.calculateWeightTotals()
    },

    generalFilter: function () {
      if (this.general_filters.filter.length >= this.general_filters.MIN_CHAR){
        this.general_filters.query = `&search=${this.general_filters.filter}`
      } else {
        this.general_filters.query = ''
      }
      this.getCartridgesRecharge(true)
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
    },

    removeRowHandler(index) {
        if (index > -1) {
          this.selected_cartridge.items.splice(index, 1); // 2nd parameter means remove one item only
          this.cartridge.items_selected_ids.splice(index, 1);
        }
        this.calculateWeightTotals()
    },

    onSubmit(event) {
      event.preventDefault()

      let send_request = this.validate()

      if (send_request){
        this.show_overlay = true
        let cartridges = []
        this.selected_cartridge.items.forEach(element => {
          let item = {
            'cartridge': element.id,
            'quantity': parseInt(element.cantidad),
            'weight': parseFloat(element.peso)
          }
          cartridges.push(item)
        })

        let body = {
          'client': this.form.client_id,
          'salesman': this.user.user.pk,
          'box_weight': parseInt(this.form.weight),
          'laser_percent': parseFloat(this.form.laser_residual),
          'laser_weight': parseFloat(this.form.laser_weight),
          'inkjet_percent': parseFloat(this.form.inkject_residual),
          'inkjet_weight': parseFloat(this.form.inkjet_weight),
          'total_weight': parseFloat( this.form.total_weight),
          'total_items': parseInt(this.form.total_items),
          'note': this.form.note,
          'cartridges': cartridges
        }
        this.sendAlbaran(body)
      }
    },

    sendAlbaran(body){
      let ep = `${this.endpoint}/api/notes/`

      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body)
      };
      fetch(ep, requestOptions)
        .then(res => {
            this.show_overlay = false
            if (res.status == 201){
              this.$bvModal.show('modal-success')
              this.$router.go(this.$router.currentRoute)  // refresh page.
            } else {
              this.$bvModal.show('modal-error')
            }
          })
        .then(function (data) {
          console.log('Request succeeded with JSON response', data);
        })
        .catch(function (error) {
          console.log('Request failed', error);
        });
    },

    onShown() {
        // Focus the cancel button when the overlay is showing
      this.$refs.cancel.focus()
    },

    onHidden() {
        // Focus the show button when the overlay is removed
      this.$refs.show.focus()
    }

  },

  components:{
    vSelect
  },

  mounted() {
    this.getCartridgesRecharge()
    this.getSubFamilies()
    this.getFamilies()
  },

  computed: {
    ...mapGetters({user: 'stateUser' }),

    selected_cartridge_rows() {
        return this.selected_cartridge.items.length
      }

  },

}

</script>

<style scoped>
  label{
    margin-top: 15px;
  }
  h3{
    margin-top: 5px;
  }
    .add-button {
        margin-bottom: 10px;
    }
    .delete-button {
        margin-left: 5px;
    }
</style>



