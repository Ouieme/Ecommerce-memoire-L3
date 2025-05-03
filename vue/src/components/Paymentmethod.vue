
<template>
    <div>
        <adminsidebare />
    </div>
    <div class="container " style="display: flex;  justify-content: space-between; ">

        <div class="column is-3  ">
            <div class="card elevation-4 mt-3 ">
                <div class="card-content ">

                    <h4 class="title is-4 has-text-centered">
                        Add carde
                    </h4>
                    <form @submit="addcared">
                        <div class="field columns is-multiline">
                            <div class="control column">
                                <input type="text" class="input is-blue" placeholder="name" autocomplete="off"
                                    v-model="card.nom" />
                            </div>
                        </div>
                        <div class="field columns is-multiline">
                            <div class="control column">
                                <input type="text" class="input is-blue" placeholder="value" autocomplete="off"
                                    v-model="card.valeur" />
                            </div>
                        </div>
                        <div class="field columns is-multiline">
                            <div class="control column">
                                <input type="date" class="input is-blue" placeholder="date of expiry" autocomplete="off"
                                    v-model="card.date_expirée" />
                            </div>
                        </div>
                        <div class="button-container">
                            <button type="submit" class="button is-blue"
                                style="background-color: #ff6e31; margin-right: 10px;">
                                <span style="color: #fff" @click="addcared">Add</span>
                            </button>
                            <router-link to="/">
                                <button class="button is-blue" style="margin-right: 10px;">
                                    <span style="color: #ff6e31">Cancel</span>
                                </button>
                            </router-link>
                        </div>
                    </form>
                </div>
            </div>
        </div>

        <!-- problem form -->
        <div class="towforms">
            <div class="container" style="display: grid; grid-template-columns: repeat(auto-fit); gap: 12px;">

                <!-- delet form -->
                <div class="column is-6">
                    <div class="card elevation-4 mt-3">
                        <div class="card-content">
                            <h4 class="title is-4 has-text-centered">
                                Delete Cards
                            </h4>
                            <form @submit.prevent="submitForm">

                                <div class="control column ">
                                    <input type="text" class="input is-blue" placeholder="name" autocomplete="false"
                                        v-model="card.nom" />
                                </div>
                                <div class="button-container">
                                    <button class="button is-blue" style="background-color: #ff6e31; margin-right: 10px;">
                                        <span style="color: #fff">Delete</span>
                                    </button>
                                </div>
                                <a @click="deleteExpiredCards" style="text-align: center;">
                                    Delete all expired Cards
                                </a>
                            </form>

                        </div>
                    </div>
                </div>
                <div class="column is-6">
                    <div class="card elevation-4 mt-3">
                        <div class="card-content">
                            <h4 class="title is-4 has-text-centered">
                                Problems
                            </h4>
                            <div>
                                <div class="control column">
                                    <input type="text" class="input is-blue" placeholder="code" autocomplete="off"
                                        v-model="code" />
                                </div>
                                <div class="button-container">
                                    <button class="button is-blue" @click="getRowByCode"
                                        style="background-color: #ff6e31; margin-right: 10px;">
                                        <span style="color: #fff">Search</span>
                                    </button>
                                </div>
                                <div class="card-container">
                                    <div v-for="row in rows" :key="row.id" class="card">
                                        <div class="card-content">
                                            <div class="content">
                                                <p><strong>Name:</strong> {{ row.nom }}</p>
                                                <p><strong>Code:</strong> {{ row.code }}</p>
                                                <p><strong>Value:</strong> {{ row.valeur }}</p>
                                                <p><strong>Expiration Date:</strong> {{ row.date_expiree }}</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import axios from 'axios';
import adminsidebare from '@/components/adminsidebare'
import { toast } from "bulma-toast";

export default {
    components: {
        adminsidebare,

    },
    data() {
        return {
            code: '',
            card: {
                id: "",
                nom: "",
                valeur: "",
                date_expirée: ""
            },
        };
    },
    methods: {
        submitForm() {
            const formData = {
                nom: this.card.nom,
                valeur: this.card.valeur,
                date_expirée: this.card.date_expirée
            };
        },
        // get cards by code   `http://127.0.0.1:8000/api/v1/get_row_by_code/${this.code}/`
        //  delet all expiers cards
        deleteExpiredCards() {
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]');

            axios.defaults.headers.common['X-CSRFToken'] = csrfToken;

            axios.get('http://127.0.0.1:8000/api/v1/delete_expired_cards/')
                .then(response => {
                    // Handle success response
                    console.log(response.data);
                })
                .catch(error => {
                    // Handle error response
                    console.error(error);
                });
        }
    },
    // add cards        
    addcared() {
        axios
            .post("http://127.0.0.1:8000/api/mode_de_paiement/", {
                nom: this.card.nom,
                valeur: this.card.valeur,
                date_expirée: this.card.date_expirée,
            })
            .then((response) => {
                // Reset the input fields
                this.card = {
                    nom: '',
                    valeur: '',
                    date_expirée: '',
                };

                // Show success message
                this.$toast.success("Card added", {
                    duration: 2000,
                    position: "bottom-center",
                });
            })
            .catch((error) => {
                console.error(error);
                // Show error message
                this.$toast.error("Failed to add card", {
                    duration: 2000,
                    position: "bottom-center",
                });
            });
    }
    ,
}
</script>

  
<style scoped>
.v-application .rounded-bl-xl {
    border-bottom-left-radius: 300px !important;
}

.v-application .rounded-br-xl {
    border-bottom-right-radius: 300px !important;
}

::placeholder {
    color: #889397;
}

.hr-spacing {
    margin-bottom: 0.5em;
}

.towforms {
    width: 55%;
    /* Adjust the value to set your desired padding */
}

.button-container {
    display: flex;
    justify-content: center;
    margin-top: 10px;
    /* Adjust as needed */
}

.result-container {
    margin-top: 20px;
}

.result {
    margin-bottom: 20px;
}

.no-result {
    margin-top: 20px;
    font-weight: bold;
}
</style>