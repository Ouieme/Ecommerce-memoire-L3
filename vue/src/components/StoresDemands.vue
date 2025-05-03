<template>
    <div class="Stors_Domands page">

        <body>
            <div>
                <adminsidebare />
            </div>
            <section id="content">
                <main>
                    <div class="table-data">
                        <div class="order">
                            <div class="head">
                                <h3>Recent Orders</h3>
                                <i class='bx bx-search'></i>
                                <i class='bx bx-filter'></i>
                            </div>
                            <table>
                                <thead>
                                    <tr>
                                        <th>compte</th>
                                        <th>Name</th>
                                        <th>Motivation</th>
                                        <th>Categorie</th>
                                        <th>Status</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="Demand in Demand" v-bind:key="Demand.id">
                                        <td>

                                            <p>{{ Demand.compte_id }}</p>
                                        </td>
                                        <td>
                                            <p>{{ Demand.nom }}</p>
                                        </td>
                                        <td>
                                            <p>{{ Demand.Motivation }}</p>
                                        </td>
                                        <td>
                                            <p>{{ Demand.Categorie }}</p>
                                        </td>
                                        <td><span class="status Accepte">   
                                            <a href="#" style="color: aliceblue;" @click="sendEmail(Demand, 'Accepte')">Accepte</a>
                                             </span>
                                            <span class="status annuler">
                                                <a href="#" style="color: aliceblue;" @click="sendEmail(Demand, 'Refuse')">Refuse</a>
 
                                            </span>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>

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
            Demand: [],
        };
    },
    created() {
        this.getStrosDemands();
    },
    methods: {
        getStrosDemands() {
            axios
                .get('http://127.0.0.1:8000/api/Demandset/')
                .then((response) => {
                    this.Demand = response.data;
                    alert('Data fetched successfully.');
                })
                .catch((error) => {
                    console.error(error);
                    alert('An error occurred while fetching the data.');
                });
        },
        sendEmail(Demand, action) {
      const emailContent = `Dear ${Demand.nom}, your request  to create store has been ${action}.`;
      axios.post('/api/sendEmail', {
        to: Demand.email,
        subject: 'Request status',
        content: emailContent
      })
      .then(response => {
        console.log('Email sent successfully');
      })
      .catch(error => {
        console.error('Failed to send email:', error);
      });
    }
    }
}
const allSideMenu = document.querySelectorAll('#sidebar .side-menu.top li a');

allSideMenu.forEach(item => {
    const li = item.parentElement;

    item.addEventListener('click', function () {
        allSideMenu.forEach(i => {
            i.parentElement.classList.remove('active');
        })
        li.classList.add('active');
    })
});


</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Poppins:wght@400;500;600;700&display=swap');

:root {
    --poppins: 'Poppins', sans-serif;
    --lato: 'Lato', sans-serif;

    --light: #F9F9F9;
    --orang-pal: #e67a3c;
    --light-blue: #ffdecf;
    --grey: #eee;
    --dark-grey: #AAAAAA;
    --dark: #342E37;
    --red: #DB504A;
    --yellow: #FFCE26;
    --light-yellow: #FFF2C6;
    --orange: #FD7238;
    --light-orange: #FFE0D3;
}

html {
    overflow-x: hidden;
}

body.dark {
    --light: #0C0C1E;
    --grey: #060714;
    --dark: #FBFBFB;
}

#content main .table-data {
    display: flex;
    flex-wrap: wrap;
    grid-gap: 24px;
    margin-top: 24px;
    width: 100%;
    color: var(--dark);
}

#content main .table-data>div {
    border-radius: 20px;
    background: var(--light);
    padding: 24px;
    overflow-x: auto;
}

#content main .table-data .head {
    display: flex;
    align-items: center;
    grid-gap: 16px;
    margin-bottom: 24px;
}

#content main .table-data .head h3 {
    margin-right: auto;
    font-size: 24px;
    font-weight: 600;
}

#content main .table-data .head .bx {
    cursor: pointer;
}

#content main .table-data .order {
    flex-grow: 1;
    flex-basis: 500px;
}

#content main .table-data .order table {
    width: 100%;
    border-collapse: collapse;
}

#content main .table-data .order table th {
    padding-bottom: 12px;
    font-size: 13px;
    text-align: left;
    border-bottom: 1px solid var(--grey);
}

#content main .table-data .order table td {
    padding: 16px 0;
}

#content main .table-data .order table tr td:first-child {
    display: flex;
    align-items: center;
    grid-gap: 12px;
    padding-left: 6px;
}

#content main .table-data .order table td img {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    object-fit: cover;
}

#content main .table-data .order table tbody tr:hover {
    background: var(--grey);
}

#content main .table-data .order table tr td .status {
    font-size: 10px;
    padding: 6px 16px;
    color: var(--light);
    border-radius: 20px;
    font-weight: 700;
}

#content main .table-data .order table tr td .status.Accepte {
    background: orangered;
}

#content main .table-data .order table tr td .status.annuler {
    background: var(--yellow);
}


@media screen and (max-width: 768px) {
    #sidebar {
        width: 200px;
    }

    #content {
        width: calc(100% - 60px);
        left: 200px;
    }

    #content nav .nav-link {
        display: none;
    }
}

@media screen and (max-width: 576px) {
    #content nav form .form-input input {
        display: none;
    }

    #content nav form .form-input button {
        width: auto;
        height: auto;
        background: transparent;
        border-radius: none;
        color: var(--dark);
    }

    #content nav form.show .form-input input {
        display: block;
        width: 100%;
    }

    #content nav form.show .form-input button {
        width: 36px;
        height: 100%;
        border-radius: 0 36px 36px 0;
        color: var(--light);
        background: var(--red);
    }

    #content nav form.show~.notification,
    #content nav form.show~.profile {
        display: none;
    }

    #content main .box-info {
        grid-template-columns: 1fr;
    }

    #content main .table-data .head {
        min-width: 420px;
    }

    #content main .table-data .order table {
        min-width: 420px;
    }

}
</style>

 