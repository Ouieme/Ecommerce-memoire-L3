<template>
  <section class="section-contact">
    <div class="hero-contact">
      <div class="hero-bag-cnt">
        <img src="../assets/christin.jpg">
      </div>
      <div class="hero-content-cnt">

        <h6>Contact <span style="color: orange;">US</span></h6>
        <p style="color: white; font-weight: bold;">Get <span style="color: orange;">24/7</span> Support</p>
      </div>
    </div>
  </section>

  <section class="section contact-from-section mt-6 mb-6">
    <div class="container">
      <div class="columns">
        <div class="column is-two-thirds">
          <div class="form-title">
            <h2 style="font-weight: bold;">Have you any question?</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur, ratione! Laboriosam est, assumenda.
              Perferendis, quo alias quaerat aliquid. Corporis ipsum minus voluptate? Dolore, esse natus!</p>
          </div>
          <div id="form_status"></div>
          <div class="contact-form">
            <form @submit.prevent="submitForm">
              <div class="field is-horizontal">
                <div class="field-body">
                  <div class="field">
                    <p class="control">
                      <input class="input" type="text" placeholder="Name" v-model="name">
                    </p>
                  </div>
                  <div class="field">
                    <p class="control">
                      <input class="input" type="email" placeholder="Email" v-model="email">
                    </p>
                  </div>
                </div>
              </div>
              <div class="field is-horizontal">
                <div class="field-body">
                  <div class="field">
                    <p class="control">
                      <input class="input" type="tel" placeholder="Phone" v-model="phone">
                    </p>
                  </div>
                  <div class="field">
                    <p class="control">
                      <input class="input" type="text" placeholder="Subject" v-model="subject">
                    </p>
                  </div>
                </div>
              </div>
              <div class="field">
                <p class="control">
                  <textarea class="textarea" placeholder="Message" rows="5" v-model="message"></textarea>
                </p>
              </div>
              <input type="hidden" name="token" value="FsWga4&@f6aw" />
              <div class="field">
                <p class="control">
                  <button class="button submit" type="submit">Submit</button>
                </p>
              </div>
            </form>

          </div>
        </div>
        <div class="column">
          <div class="contact-form-wrap">
            <div class="contact-form-box">
              <h4><i class="fas fa-map"></i> Shop Address</h4>
              <p>34/8, East Hukupara<br>Gifirtok, Sadan.<br>Country Name</p>
            </div>
            <div class="contact-form-box">
              <h4><i class="far fa-clock"></i> Shop Hours</h4>
              <p>MON - FRIDAY: 8 to 9 PM<br>SAT - SUN: 10 to 8 PM</p>
            </div>
            <div class="contact-form-box">
              <h4><i class="fas fa-address-book"></i> Contact</h4>
              <p>Phone: +00 111 222 3333<br>Email: support@Bessahel.com</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <div class="find-location hero is-dark" style="margin-bottom: 5px;">
    <div class="container">
      <div class="columns is-centered">
        <div class="column is-full">
          <p class="has-text-centered"><i class="fas fa-map-marker-alt"></i> Find Our Location</p>
        </div>
      </div>
    </div>
  </div>


  <div class="embed-responsive embed-responsive-21by9">
    <iframe
      src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d186948.49263565145!2d6.598934790378195!3d36.365610587098324!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x12e4acdafbc1a741%3A0x44691f1f3d7761a7!2sConstantine%2C%20Algeria!5e0!3m2!1sen!2sbd!4v1622711982789!5m2!1sen!2sbd"
      width="100%" height="450" frameborder="0" style="border:0;" allowfullscreen="true" aria-hidden="false" tabindex="0"
      class="embed-responsive-item"></iframe>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  methods: {
    submitForm() {
      // Get the form data
      const formData = {
        name: this.name,
        email: this.email,
        phone: this.phone,
        subject: this.subject,
        message: this.message,
      };

      // Send the form data to the backend
      axios.post("http://localhost:8000/api/v1/Contact/", formData, {
        headers: {
          'Content-Type': 'application/json',
        },
        
      })
    }
  }
}
</script>

<style>
.section {
  padding: 0;
}

.hero-contact {
  position: relative;
  height: 300px;
  /* Set the height to the desired value */
  overflow: hidden;
}

.hero-bag-cnt {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.hero-bag-cnt img {
  position: absolute;
  object-fit: cover;
  object-position: center;
  width: 100%;
  height: 100%;
}

.hero-content-cnt {
  position: absolute;
  bottom: 100px;
  /* Adjust the value to position the content */
  left: 50%;
  transform: translateX(-50%);
  text-align: center;

}

.hero-content-cnt h6 {
  color: white;
  font-weight: bold;
  font-size: 50px;
}


.contact-from-section {
  padding: 20px;
}

.form-title {
  margin-bottom: 25px;
}

.form-title h2 {
  font-size: 25px;
}

.form-title p {
  font-size: 15px;
  line-height: 1.8;
}



.contact-form form p input[type=text],
.contact-form form p input[type=tel],
.contact-form form p input[type=email] {
  width: 100%;
  margin-bottom: -0.5px;
  margin-top: -0.5px;
  margin-left: 1px;
  border: 1px solid #ddd;
  border-radius: 3px;
}

.contact-form form p textarea {
  border: 1px solid #ddd;
  border-radius: 3px;
  width: 100%;
  resize: none;
}

.contact-form-wrap {
  background-color: #FBFBFB;
  padding: 45px 30px;
  border-radius: 5px;
}

.contact-form-box {
  padding-left: 40px;
  margin-bottom: 30px;
}

.contact-form-box h4 {
  font-size: 20px;
  font-weight: 600;
  position: relative;
  margin-bottom: 10px;
}

.contact-form-box h4 i {
  position: absolute;
  left: -13%;
  color: orange;
  top: 2px;
}

.contact-form-box p {
  line-height: 1.8;
  opacity: 0.8;
}

.contact-form-wrap .contact-form-box:last-child {
  margin: 0;
}

.find-location p {
  color: #fff;
  font-size: 40px;
  margin: 0;
  font-weight: 600;
  padding: 95px 0;
}

.submit {
  background-color: orange;
  color: white;

}
</style>
