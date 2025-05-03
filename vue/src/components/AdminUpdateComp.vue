<template>
    <div class="Admin-page">

        <body>
            <div>
                <adminsidebare />
            </div>
            <section id="midel">
                <main>

                    <ul class="boxs">
                        <li style="box-shadow:none">
                            <profileCards />
                        </li>
                        <li style="width: 70%;">
                            <form v-on:@submit="updateAdmin">
                                <div class="from">
                                    <label for="">FirstName</label>
                                    <input v-model="admins.nom">
                                </div>
                                <div class="from">
                                    <label for="">Username</label>
                                    <input v-model="admins.username">
                                </div>
                                <div class="from">
                                    <label for="">Password</label>
                                    <input type="text" v-model="admins.password">
                                </div>

                                <div class="from">
                                    <label for="">Privileges</label>
                                    <input type="text" name="privileges" v-model="admins.type_Admin">
                                </div>
                                <div id="buttons">
                                    <button class="action Update" type="submit" @click.prevent="updateAdmin">Update</button>
                                </div>
                            </form>
                        </li>

                    </ul>


                </main>

            </section>

        </body>
    </div>
</template>
<script>
import axios from 'axios';
import adminsidebare from '@/components/adminsidebare'
import profileCards from '@/components/profileCards'

export default {
    components: {
        adminsidebare,
        profileCards,
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
    mounted() {
        this.updateAdmin();
    },
    methods: {
        updateAdmin() {
            const adminId = this.$route.params.id;
            const adminData = {


                nom: this.admins.nom,
                type_Admin: this.admins.type_Admin,
                user: {
                    username: this.admins.username,
                    password: this.admins.password,
                },
            };


            axios
                .put(`http://127.0.0.1:8000/api/admin/${adminId}/`, adminData)
                .then((response) => {
                    this.getAPI();
                    alert('Admin updated successfully.');
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    },
};


</script>
<style> @import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Poppins:wght@400;500;600;700&display=swap');



 :root {

     --orange: #ff6e31;

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

 #midel main .boxs {
     display: grid;
     grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
     grid-gap: 24px;
     margin-top: 36px;
 }

 #midel main .boxs li {
     padding: 24px;
     box-shadow: 1px 2px 8px 4px rgba(196, 196, 196, 0.523);

     border-radius: 20px;
     display: flex;
     align-items: center;
     grid-gap: 24px;
 }

 #midel main .boxs li .bx {
     width: 80px;
     height: 80px;
     border-radius: 10px;
     font-size: 36px;
     display: flex;
     align-items: center;
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
 