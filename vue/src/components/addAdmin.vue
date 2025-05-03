<template>
    <div class="Add_Admin page">

        <body>
            <div>
                <adminsidebare />
            </div>
            <section id="Add_AdminPage">
                <main>
                    <div class="Addform">
                        <form v-on:submit.prevent="addAdmin()">
                            <div class="from">
                                <label for="">FisrtName</label>
                                <input v-model="admins.nom">
                            </div>
                            <div class="from">
                                <label for="">Username</label>
                                <input v-model="admins.username">
                            </div>
                            <div class="from">
                                <label for="">Password</label>
                                <input v-model="admins.password">
                            </div>

                            <div class="from">
                                <label for="">Privileges</label>
                                <input type="text" name="privileges" v-model="admins.type_Admin">
                            </div>
                            <div id="buttons">
                                <button class="action Update" type="submit">Add</button>
                            </div>
                        </form>
                    </div>
                </main>

            </section>


        </body>
    </div>
</template>

<script>
import axios from 'axios';
import adminsidebare from '@/components/adminsidebare'


export default {
    components: {
        adminsidebare,

    },
    data() {
        return {

            admins: {
                nom: "",
                username: "",
                password: "",
                type_Admin: "",

            },

        };
    },
    mounted: function () {
        this.getAdmin()

    },
    methods: {
        submitForm() {
            this.errors = [];
            if (this.nom === "") {
                this.errors.push("The first name is missing");
            }
            if (this.username === "") {
                this.errors.push("The username is missing");
            }
            if (this.password === "") {
                this.errors.push("The password is too short");
            }
            if (this.password !== this.password2) {
                this.errors.push("The passwords doesn't match");
            }
            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password,
                    nom: this.nom,
                    type_Admin: this.type_Admin,
                }
            }
        },
        addAdmin() {
            axios
                .post('http://127.0.0.1:8000/api/admin/', {
                    user: {
                        username: this.admins.username,
                        password: this.admins.password,
                    },
                    nom: this.admins.nom,
                    type_Admin: this.admins.type_Admin,
                })
                .then((response) => {
                    this.getAPI();
                    alert('Admin added successfully.');
                })
                .catch((err) => {
                    this.loading = tre;
                    console.log(err);
                });
        },

    },
}
</script>

<style> @import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Poppins:wght@400;500;600;700&display=swap');

 #Add_AdminPage {
     padding: 20px;
     padding-right: 60%;
     padding-left: 40px;
 }

 #buttons .action.Update {
     font-size: 10px;
     border: none;
     padding: 6px 16px;
     background-color: orangered;
     color: antiquewhite;
     border-radius: 20px;
     font-weight: 700;
 }

 .Addform {
     padding: 57px;
     box-shadow: 1px 2px 8px 4px rgba(196, 196, 196, 0.523);
     border-radius: 20px;
     display: flex;
     align-items: center;
     grid-gap: 24px;

 }

 input {
     width: 100%;
     padding: 12px 20px;
     margin: 8px 0;
     display: inline-block;
     border: 1px solid #ccc;
     border-radius: 4px;
     box-sizing: border-box;
 }

 form label {
     color: black;
     align-items: start;

 }

 form label input {
     color: black;



 }

 .from input {
     display: inline-block;
     margin-right: 10px;

 }
</style>
 

