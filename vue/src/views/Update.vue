<template>
	<div class="Admin-page">

		<body>
			<div>
				<adminsidebare />
			</div>
			<section id="content">
				<main>
					<div class="head-title">
						<div class="left">
							<h1>Update</h1>
							<ul class="breadcrumb">
								<li>
									<a href="#">Update</a>
								</li>
								<li><i class='bx bx-chevron-right'></i></li>
								<li>
									<a class="active" href="admin.vue">Home</a>
								</li>
							</ul>
						</div>
					</div>
					<ul class="box-info">
						<li>
							<profileCards />
						</li>
						<li style="width: 70%;">
							<form>
								<div class="from">
									<label for="">First name</label>
									<input type="text" name="first">
								</div>
								<div class="from">
									<label for="">Last name</label>
									<input type="text" name="last">
								</div>
								<div class="from">
									<label for="">Date of birth</label>
									<input type="text" name="dob">
								</div>
								<div class="from">
									<label for="">Username</label>
									<input type="text" name="username">
								</div>
								<div class="from">
									<label for="">Password</label>
									<input type="text" name="password">
								</div>
								<div class="from">
									<label for="">Address</label>
									<input type="text" name="address">
								</div>
								<div class="from">
									<label for="">Email</label>
									<input type="text" name="email">
								</div>
								<div class="from">
									<label for="">Phone Number</label>
									<input type="text" name="phone_number">
								</div>
								<div class="from">
									<label for="">Privileges</label>
									<input type="text" name="privileges">
								</div>
								<div class="buttons">
									<button class="action update">Update</button>
									<button class="action cancel">Cancel</button>
								</div>
							</form>
						</li>

					</ul>


				</main>

			</section>

		</body>
	</div>
</template>
<script setup >
</script>
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
			Admins: [],
			api: 'http://127.0.0.1:8000/'
		};
	},
	created() {
		this.getAPI();
	},
	methods: {

		getAPI() {
			axios
				.get(this.api + 'admins/Admins/')
				.then((response) => {
					this.Admins = response.data;
					alert('Data fetched successfully.');
				})
				.catch((error) => {
					console.error(error);
					alert('An error occurred while fetching the data.');
				});
		}
	}
}

</script>

<style> @import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Poppins:wght@400;500;600;700&display=swap');

 #content main .box-info li {
 	padding: 24px;
 	/* background: var(--light); */
 	border-radius: 20px;
 	display: flex;
 	align-items: center;
 	grid-gap: 24px;
 }

 *,
 *::before,
 *::after {
 	padding: 0;
 	margin: 0;
 	box-sizing: border-box;
 }

 :root {

 	--orange: #ff6e31;

 }

 html {
 	overflow-x: hidden;
 }

 body.dark {
 	--light: #0C0C1E;
 	--grey: #060714;
 	--dark: #FBFBFB;
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

 button {
 	border: none;
 	font-size: 1.3rem;
 	text-align: center;
 	min-width: 3.7rem;
 	display: grid;
 	grid-template-columns: 1fr;
 	grid-template-rows: 1fr;

 }

 .icon {
 	font-size: 1.3rem;
 	text-align: center;
 	min-width: 3.7rem;
 	display: grid;
 	grid-template-columns: 1fr;
 	grid-template-rows: 1fr;
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


 .buttens {
 	font-size: 10px;
 	padding: 6px 16px;
 	border-radius: 20px;
 	font-weight: 700;
 	display: flex;
 }

 .action.cansel {
 	background: var(--yellow);
 }

 .action.Update {
 	background: var(--orange);
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
