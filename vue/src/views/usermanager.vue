<template>
	<div class="Admin-page">

		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<title>UserManger Page</title>
		</head>

		<body>
			<div>
				<adminsidebare />
			</div>
			<section id="content">

				<main>
					<ul class="box-info">
						<li>

							<i class='bx bx-user'></i>


							<span class="text">
								<h3>Up date</h3>
								<p>My profile</p>
							</span>
						</li>

						<li>
							<i class='bx bx-store-alt'></i>
							<router-link to="/storedemands">
								<span class="text">
									<h3>Stors </h3>
									<p>Stors demands</p>
								</span>
							</router-link>
						</li>
						<li>

							<i class='bx bx-message-error'></i>
							<router-link to="/complaines">
								<span class="text">
									<h3>Complins</h3>
									<p>What wrong withe our web </p>
								</span>
							</router-link>
						</li>


					</ul>


					<div class="Team" id="team-section">

						<div class="order">
							<div class="head">
								<h3>Users</h3>
								<i class='bx bx-plus'></i>
							</div>
							<table>
								<thead>
									<tr>
										<th>Name</th>
										<th>Type</th>
										<th>Action</th>

									</tr>
								</thead>

								<tbody>
									<tr v-for="compte in Comptes" :key="compte.id">
										<td>
											<!-- <img :src="getImageUrl(compte.image)" alt="compte Image"> -->
											<p>{{ compte.username }}</p>
										</td>
										<td>{{ compte.typeC }}</td>

										<td>
											<span class="status Accepte">
												<a href="#" style="color: aliceblue;"
													@click="deleteCompte(compte.id)">Delete</a>
											</span>
											<!-- <button class="action Delete" @click="deleteCompte(compte.id)">Delete</button> -->
											<span class="status annuler">
												<a href="#" style="color: aliceblue;"
													@click="deleteCompte(compte.id)">Sanction</a>
											</span>

										</td>
									</tr>
								</tbody>
							</table>
						</div>
						<div class="Stat">


							<div class="order">
								<div class="head">
									<h3>Stor</h3>
									<i class='bx bx-plus'></i>
								</div>
								<table>
									<thead>
										<tr>
											<th>Name</th>
											<th>owner</th>
											<th>Action</th>

										</tr>
									</thead>

								</table>
							</div>
						</div>
					</div>
				</main>
				<!-- MAIN -->
			</section>

		</body>
	</div>
</template>
<script setup >
import ChartCompent from '@/components/ChartCompent.vue'


</script>
<script>
import axios from 'axios';
import adminsidebare from '@/components/adminsidebare'

export default {
	components: {
		adminsidebare,
	},
	data() {
		return {
			Comptes: [],
			// ownerAndStoreData: null,
		};
	},
	created() {
		this.getAPI();
		// this.getOwnerAndStore();
	},
	methods: {
		getAPI() {
			axios
				.get('http://127.0.0.1:8000/api/getCompts/')
				.then((response) => {
					this.Comptes = response.data;
					alert('Data fetched successfully.');
				})
				.catch((error) => {
					console.error(error);
					alert('An error occurred while fetching the data.');
				});
		}
	},


	// getOwnerAndStore() {
	// 	axios
	// 		.get('http://127.0.0.1:8000/stor/owner-and-store/')
	// 		.then((response) => {
	// 			this.ownerAndStoreData = response.data;
	// 			console.log('Store fetched successfully.');
	// 		})
	// 		.catch((error) => {
	// 			console.error(error);
	// 			alert('An error occurred while fetching the data.');
	// 		});
	// },
	deleteCompte(id) {
		axios
			.delete(`http://127.0.0.1:8000/api/getCompts/${id}/`)
			.then(response => {
				console.log(response.data);
				const index = this.Comptes.findIndex(Comptes => Comptes.id === id);
				if (index !== -1) {
					this.Comptes.splice(index, 1);
				}
				alert('Comptes deleted successfully.');
			})
			.catch(error => {
				console.error(error);
				alert('Failed to delete Comptes.');
			});
	}




}


</script>
<style> @import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Poppins:wght@400;500;600;700&display=swap');



 a {
 	text-decoration: none;
 }

 li {
 	list-style: none;
 }

 :root {
 	--poppins: 'Poppins', sans-serif;
 	--lato: 'Lato', sans-serif;
 	--light: #F9F9F9;
 	--orang-pal: orangered;
 	--dark: #342E37;

 	--yellow: #FFCE26;

 	--orange: orangered;
 	--light-orange: #FFE0D3;
 	--main-color: orangered;
 	--main-color-dark: #ffdecf;
 	--main-color-light: rgba(255, 68, 0, 0.872);
 	--text-color: #cfcde7;
 }


 body.dark {
 	--light: #0C0C1E;
 	--grey: #060714;
 	--dark: #FBFBFB;
 }


 #content main .head-title {
 	display: flex;
 	align-items: center;
 	justify-content: space-between;
 	grid-gap: 16px;
 	flex-wrap: wrap;
 }

 #content main .head-title .left h1 {
 	font-size: 36px;
 	font-weight: 600;
 	margin-bottom: 10px;
 	color: var(--dark);
 }

 #content main .head-title .left .breadcrumb {
 	display: flex;
 	align-items: center;
 	grid-gap: 16px;
 }

 #content main .head-title .left .breadcrumb li {
 	color: var(--dark);
 }

 #content main .head-title .left .breadcrumb li a {
 	color: var(--dark-grey);
 	pointer-events: none;
 }

 #content main .head-title .left .breadcrumb li a.active {
 	color: var(--blue);
 	pointer-events: unset;
 }


 #content main .box-info {
 	display: grid;
 	grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
 	grid-gap: 24px;
 	margin-top: 36px;
 }

 #content main .box-info li {
 	width: 265px;
 	height: 123px;
 	padding: 24px;
 	border-radius: 20px;
 	display: flex;
 	align-items: center;
 	grid-gap: 5px;
 	box-shadow: 1px 2px 8px 4px rgba(255, 68, 0, 0.614);
 }

 #content main .box-info li .bx {
 	width: 40px;
 	height: 40px;
 	color: orangered;
 	border-radius: 10px;
 	font-size: 36px;
 	display: flex;
 	justify-content: center;
 	align-items: center;
 }


 #content main .box-info li .text h3 {
 	font-size: 24px;
 	font-weight: 600;
 	color: var(--dark);
 }

 #content main .box-info li .text {
 	color: var(--dark);
 }

 #content main .Team {
 	display: flex;
 	flex-wrap: wrap;
 	grid-gap: 24px;
 	margin-top: 24px;
 	width: 100%;
 	color: var(--dark);
 }

 #content main .Team>div {
 	border-radius: 20px;
 	background: var(--light);
 	padding: 24px;
 	overflow-x: auto;
 }

 #content main .Team .head {
 	display: flex;
 	align-items: center;
 	grid-gap: 16px;
 	margin-bottom: 24px;
 }

 #content main .Team .head h3 {
 	margin-right: auto;
 	font-size: 24px;
 	font-weight: 600;
 }

 #content main .Team .head .bx {
 	cursor: pointer;
 }

 #content main .Team .order {
 	flex-grow: 1;
 	flex-basis: 500px;
 }

 #content main .Team .order table {
 	width: 100%;
 	border-collapse: collapse;
 }

 #content main .Team .order table th {
 	padding-bottom: 12px;
 	font-size: 13px;
 	text-align: left;
 	border-bottom: 1px solid var(--grey);
 }

 #content main .Team .order table td {
 	padding: 16px 0;
 }

 #content main .Team .order table tr td:first-child {
 	display: flex;
 	align-items: center;
 	grid-gap: 12px;
 	padding-left: 6px;
 }

 #content main .Team .order table td img {
 	width: 36px;
 	height: 36px;
 	border-radius: 50%;
 	object-fit: cover;
 }

 #content main .Team .order table tbody tr:hover {
 	background: var(--grey);
 }

 #content main .Team .order table tr td .action {
 	font-size: 10px;
 	padding: 6px 16px;
 	color: var(--light);
 	border-radius: 20px;
 	font-weight: 700;
 }

 #content main .Team .order table tr td .action.Delet {
 	border: none;
 	background: var(--yellow);
 }

 #content main .Team .order table tr td .action.Update {
 	background: var(--orange);
 }

 #content main .Team .Stat {
 	flex-grow: 1;
 	flex-basis: 300px;
 }

 #content main .Team .Stat .Stat-list {
 	width: 100%;
 }

 #content main .Team .Stat .Stat-list li {
 	width: 100%;
 	margin-bottom: 16px;
 	background: var(--grey);
 	border-radius: 10px;
 	padding: 14px 20px;
 	display: flex;
 	justify-content: space-between;
 	align-items: center;
 }

 #content main .Team .Stat .Stat-list li .bx {
 	cursor: pointer;
 }

 #content main .Team .Stat .Stat-list li.completed {
 	border-left: 10px solid var(--blue);
 }

 #content main .Team .Stat .Stat-list li.not-completed {
 	border-left: 10px solid var(--orange);
 }

 #content main .Team .Stat .Stat-list li:last-child {
 	margin-bottom: 0;
 }

 @media screen and (max-width: 768px) {


 	#content {
 		width: calc(100% - 60px);
 		left: 200px;
 	}


 }

 @media screen and (max-width: 576px) {

 	#content main .box-info {
 		grid-template-columns: 1fr;
 	}

 	#content main .Team .head {
 		min-width: 420px;
 	}

 	#content main .Team .order table {
 		min-width: 420px;
 	}


 }

 #buttons {
 	border: none;
 	display: flex;
 }

 .hide {
 	transition: opacity 0.3s 0.2s;
 }

 body.shrink .hide {
 	opacity: 0;
 	pointer-events: none;
 	transition-delay: 0s;
 }

 body.shrink .shrink-btn i {
 	transform: rotate(-180deg);
 }

 body.shrink .account {
 	opacity: 1;
 	pointer-events: all;
 	transition: opacity 0.3s 0.3s, color 0.3s 0s;
 }

 body.shrink .admin-profile {
 	max-width: 0;
 	transition: opacity 0.3s 0s, max-width 0.7s 0s ease-in-out;
 }

 body.shrink .tooltip {
 	display: grid;
 }

 a {
 	text-decoration: none;
 }

 ul {
 	list-style: none;
 }

 .icon i {
 	grid-column: 1 / 2;
 	grid-row: 1 / 2;
 	transition: 0.3s;
 }

 .icon i:last-child {
 	opacity: 0;
 	color: #fff;
 }

 .active-tab {
 	width: 100%;
 	height: 53px;
 	background-color: var(--main-color-dark);
 	border-radius: 10px;
 	position: absolute;
 	top: 2.5px;
 	left: 0;
 	transition: top 0.3s;
 }

 .account {
 	display: flex;
 	align-items: center;
 	justify-content: center;
 	font-size: 1.3rem;
 	color: var(--text-color);
 	height: 53px;
 	width: 3.7rem;
 	opacity: 0;
 	pointer-events: none;
 	transition: opacity 0.3s 0s, color 0.3s 0s;
 }

 .account:hover {
 	color: #fff;
 }

 .admin-user {
 	display: flex;
 	align-items: center;
 }

 .admin-profile {
 	white-space: nowrap;
 	max-width: 100%;
 	transition: opacity 0.3s 0.2s, max-width 0.7s 0s ease-in-out;
 	display: flex;
 	align-items: center;
 	flex: 1;
 	overflow: hidden;
 }

 .admin-user img {
 	width: 2.9rem;
 	border-radius: 50%;
 	margin: 0 0.4rem;
 }

 .admin-info {
 	padding-left: 0.3rem;
 }

 .admin-info h3 {
 	font-weight: 500;
 	font-size: 1rem;
 	line-height: 1;
 }

 .admin-info h5 {
 	font-weight: 400;
 	font-size: 0.75rem;
 	color: var(--text-color);
 	margin-top: 0.3rem;
 	line-height: 1;
 }

 /* When the menu shrinks */
 .hide {
 	transition: opacity 0.3s 0.2s;
 }

 body.shrink .hide {
 	opacity: 0;
 	pointer-events: none;
 	transition-delay: 0s;
 }

 body.shrink .shrink-btn i {
 	transform: rotate(-180deg);
 }

 body.shrink .account {
 	opacity: 1;
 	pointer-events: all;
 	transition: opacity 0.3s 0.3s, color 0.3s 0s;
 }

 body.shrink .admin-profile {
 	max-width: 0;
 	transition: opacity 0.3s 0s, max-width 0.7s 0s ease-in-out;
 }

 tr td .status {
 	font-size: 10px;
 	padding: 6px 16px;
 	color: var(--light);
 	border-radius: 20px;
 	font-weight: 700;
 }

 table tr td .status.Accepte {
 	background: orangered;
 }

 table tr td .status.annuler {
 	background: var(--yellow);
 }
</style>