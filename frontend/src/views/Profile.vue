<template>
  <section>
    <h1>Your Profile</h1>
    <hr/><br/>
    <div>
      <p><strong>Username:</strong> <span>{{ user.username }}</span></p>
      <p><strong>Email:</strong> <span>{{ user.email }}</span></p>
      <!-- <p><button @click="deleteAccount()" class="btn btn-primary">Delete Account</button></p> -->
      <p><button @click="deleteAccount()" class="btn btn-primary">Delete Account</button></p>
    </div>
  </section>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  name: 'Profile',
  created: function() {
    return this.$store.dispatch('viewMe');
  },
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
