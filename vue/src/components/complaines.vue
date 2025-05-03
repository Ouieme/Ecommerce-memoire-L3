
<template>
    <div>
        <adminsidebare />
    </div>
    <div class="card-content card-radius">

        <table class="table">
            <thead>
                <tr>
                    <th>compte</th>
                    <th>type</th>
                    <th>msg</th>
                    <th>date</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="reclamation in reclamation" v-bind:key="reclamation.id">
                    <td>
                        <figure class="image is-128x128">
                            <img class="is-rounded" :src="getImageUrl(reclamation.compte_picture)">
                        </figure>
                    </td>
                    <td>{{ reclamation.type_reclm }}</td>
                    <td>
                        <p>{{ reclamation.message }}</p>
                    </td>
                    <td>{{ reclamation.date_reclamation }}</td>
                </tr>

            </tbody>
        </table>
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
            reclamation: []
        };
    },
    created() {
        this.getAPI();
    },
    methods: {
        getAPI() {
            axios
                .get('http://127.0.0.1:8000/api/v1/complaines_and_comptes_pic/')
                .then((response) => {
                    this.reclamation = response.data;
                    alert('Data fetched successfully.');
                })
                .catch((error) => {
                    console.error(error);
                    alert('An error occurred while fetching the data.');
                });
        },
        getImageUrl(imagePath) {
            return "http://127.0.0.1:8000" + imagePath;

        }
    }
}
</script>

<style>
td {
    height: 90px;
    /* Set the desired height */
    overflow-y: auto;
    /* Enable vertical scrolling if needed */
}

table tbody tr:hover {
    background: var(--grey);
}

table td {
    padding: 16px 0;
}
</style>