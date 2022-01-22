<template>
  <section>
    <form @submit.prevent="submit">
      
      <!-- CLIENTE -->
      <div class="bg-light">
        <div class="row">
          <h3 class="text-center" style="margin: 5px">Cliente</h3>
          <div class="col-md col-sm form-group">
              <label for="cifrc" class="form-label">CIFRC:</label>
              <input type="text" name="cifrc" v-model="form.cifrc" class="form-control" />
          </div>
          <div class="col-md col-sm form-group">
              <label for="name" class="form-label">Nombre:</label>
              <input type="text" name="name" v-model="form.name" class="form-control" />
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
              <input type="text" name="salesman" v-model="form.salesman" class="form-control" />
          </div>
          <div class="col-md col-sm form-group">
              <label for="weight" class="form-label">Peso:</label>
              <input type="text" name="weight" v-model="form.weight" class="form-control" />
          </div>
        </div>
        <div class="row">
          <div class="col-md col-sm form-group">
              <label for="laser_residual" class="form-label">Laser Residual:</label>
              <input type="text" name="laser_residual" v-model="form.laser_residual" class="form-control" />
          </div>
          <div class="col-md col-sm form-group">
              <label for="inkject_residual" class="form-label">Inkject Residual:</label>
              <input type="text" name="inkject_residual" v-model="form.inkject_residual" class="form-control" />
          </div>
        </div>
        <div class="row">
          <div class="col-md col-sm form-group">
              <label for="laser_weight" class="form-label">Peso Laser(Kg):</label>
              <input type="text" name="laser_weight" v-model="form.laser_weight" class="form-control" />
          </div>
          <div class="col-md col-sm form-group">
              <label for="inkjet_weight" class="form-label">Peso Inkject(Kg):</label>
              <input type="text" name="inkjet_weight" v-model="form.inkjet_weight" class="form-control" />
          </div>
        </div>
        <div class="row">
          <div class="col-md col-sm form-group">
              <label for="total_items" class="form-label">Artículos en total:</label>
              <input type="text" name="total_items" v-model="form.total_items" class="form-control" />
          </div>
          <div class="col-md col-sm form-group">
              <label for="total_weight" class="form-label">Peso Total(Kg):</label>
              <input type="text" name="total_weight" v-model="form.total_weight" class="form-control" />
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
        cifrc: '',
        name:'',
        number: '',
        address:'',
        telephone: '',
        email:'',
        contact: '',
        rate:'',
        weight: '',
        salesman:'',
        laser_residual: '',
        inkject_residual:'',
        laser_weight: '',
        inkjet_weight:'',
        total_weight: '',
        total_items:'',
      }
    };
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
}
</script>
