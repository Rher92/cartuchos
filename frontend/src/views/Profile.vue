<template>
  <section>
    <h1>Perfil</h1>
    <hr/><br/>
    <div>
      <p><strong>Usuario:</strong> <span>{{ user.user.username }}</span></p>
      <p><strong>Email:</strong> <span>{{ user.user.email }}</span></p>
      <!-- <p><button @click="deleteAccount()" class="btn btn-primary">Delete Account</button></p> -->
      <!-- <p><button @click="deleteAccount()" class="btn btn-primary">Delete Account</button></p> -->
    </div>
  </section>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  name: 'Profile',
  // created: function() {
  //   return this.$store.mapGetters('viewMe');
  // },
  computed: {
    ...mapGetters({user: 'stateUser' }),
  },
  methods: {
    ...mapActions(['deleteUser']),
    async deleteAccount() {
      try {
        await this.deleteUser(this.user.id);
        await this.$store.dispatch('logOut');
        this.$router.push('/');
      } catch (error) {
        console.error(error);
      }
    }
  },
}
</script>
