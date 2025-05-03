<template>
 
  <section class="section-contact">
    <div class="hero-contact">
      <div class="hero-bag-cnt">
        <img src="../assets/clark-street-mercantile-qnKhZJPKFD8-unsplash.jpg">
      </div>
      <div class="hero-content-cnt">
        <h6>About <span style="color: orange;">US</span></h6>
      </div>
    </div>
  </section>

  <section class="section feature-bg">
    <div class="container">
      <div class="columns">
        <div class="column is-7">
          <div class="featured-text">
            <h2 class="title">Why <span style="color: orange;">Bessahel</span></h2>
            <div class="columns is-multiline">
              <div class="column is-6">
                <div class="list-box">
                  <div class="list-icon">
                    <i class="fas fa-shipping-fast"></i>
                  </div>
                  <div class="content">
                    <h3>Home Delivery</h3>
                    <p>sit voluptatem accusantium dolore mque laudantium, totam rem aperiam, eaque ipsa quae ab illo.</p>
                  </div>
                </div>
              </div>
              <div class="column is-6">
                <div class="list-box">
                  <div class="list-icon">
                    <i class="fas fa-money-bill-alt"></i>
                  </div>
                  <div class="content">
                    <h3>Best Price</h3>
                    <p>sit voluptatem accusantium dolore mque laudantium, totam rem aperiam, eaque ipsa quae ab illo.</p>
                  </div>
                </div>
              </div>
              <div class="column is-6">
                <div class="list-box">
                  <div class="list-icon">
                    <i class="fas fa-briefcase"></i>
                  </div>
                  <div class="content">
                    <h3>Custom Box</h3>
                    <p>sit voluptatem accusantium dolore mque laudantium, totam rem aperiam, eaque ipsa quae ab illo.</p>
                  </div>
                </div>
              </div>
              <div class="column is-6">
                <div class="list-box">
                  <div class="list-icon">
                    <i class="fas fa-sync-alt"></i>
                  </div>
                  <div class="content">
                    <h3>Quick Refund</h3>
                    <p>sit voluptatem accusantium dolore mque laudantium, totam rem aperiam, eaque ipsa quae ab illo.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="team mt-5">
    <div class="container">
      <div class="columns is-centered">
        <div class="column is-8">
          <div class="has-text-centered">
            <h3 class="title is-3">Our <span style="color: orange;">Team</span></h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquid, fuga quas itaque eveniet beatae optio.</p>
          </div>
        </div>
      </div>
      <div class="columns is-centered">
        <div class="column is-4">
          <div class="single-team-item">
            <div class="team-bg team-bg-1"></div>
            <h4>Yessad Ouieme <span class="is-size-6">Developer</span></h4>
            <ul class="social-link-team">
              <li><a href="https://www.facebook.com/profile.php?id=100011504110398" target="_blank"><i class="fab fa-facebook-f"></i></a></li>
              <li><a href="#" target="_blank"><i class="fab fa-twitter"></i></a></li>
              <li><a href="#" target="_blank"><i class="fab fa-instagram"></i></a></li>
            </ul>
          </div>
        </div>
        <div class="column is-4">
          <div class="single-team-item">
            <div class="team-bg team-bg-2"></div>
            <h4>Bourkaib Lyna <span class="is-size-6">Developer</span></h4>
            <ul class="social-link-team">
              <li><a href="https://www.facebook.com/ta.nile.9022" target="_blank"><i class="fab fa-facebook-f"></i></a></li>
              <li><a href="#" target="_blank"><i class="fab fa-twitter"></i></a></li>
              <li><a href="#" target="_blank"><i class="fab fa-instagram"></i></a></li>
            </ul>
          </div>
        </div>
        <div class="column is-4">
          <div class="single-team-item">
            <div class="team-bg team-bg-3"></div>
            <h4>Guelib IKram <span class="is-size-6">Developer</span></h4>
            <ul class="social-link-team">
              <li><a href="https://www.facebook.com/profile.php?id=100015289397293" target="_blank"><i class="fab fa-facebook-f"></i></a></li>
              <li><a href="#" target="_blank"><i class="fab fa-twitter"></i></a></li>
              <li><a href="#" target="_blank"><i class="fab fa-instagram"></i></a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>

  <br><br><br>
  
  
</template>


<style>

.feature-bg {
  position: relative;
  margin: 150px 20px;
  
}
.feature-bg:after {
  background-image: url(../assets/Best-online-stores-to-shop-for-sales-now1.png);
  position: absolute;
  right: 0;
  top: 0;
  width:30%;
  height: 100%;
  content: "";
  background-size: cover;
  background-position: center;
  border-radius: 5px;
  box-shadow: 0 0 20px #cacaca;
  border-bottom-left-radius: 5px;
  margin-right: 1%;
 
}


.featured-text .list-box {
  display: flex;
  align-items: start;
  padding: 20px;
  
}

.featured-text .list-box .list-icon {
  margin-right: 20px;
  font-size: x-large;
  
}

.featured-text .list-box .list-icon i {
  color: orange;
  border: 2px orange dotted;
  border-radius: 999px;
  line-height: 55px;
  width: 55px;
  height: 55px;
  text-align: center;
  
 
}

.featured-text .title{
  font-size: 30px;
  font-weight: bold;

}


.team-bg-1 {
   background-image: url(../assets/Bewerbungsfotos-btc-photography_de.png);
}

.team-bg-2 {
  background-image: url(../assets/download-_1_.png);}

.team-bg-3 {
  background-image: url(../assets/Foto-para-usar-em-artes-com-_Título-Leia-a-legenda_.png);
}


.team-bg {
  height: 400px;
  background-size: cover;
  background-position: center;
  border-radius: 5px;
  background-color: #ddd;
}

.single-team-item {
  position: relative;
}

.single-team-item h4 {
  font-size: 20px;
  font-weight: 600;
  text-align: center;
  margin-top: 15px;
  margin-bottom: 10px;
}

.single-team-item h4 span {
  font-size: 70%;
  display: block;
  margin-top: 10px;
  opacity: 0.7;
}

ul.social-link-team {
  position: absolute;
  bottom: 80px;
  left: 0;
  right: 0;
  margin: 0;
  padding: 0;
  list-style: none;
  text-align: center;
}

ul.social-link-team li {
  display: inline-block;
}

ul.social-link-team li a {
  color: #fff;
  background-color: orange;
  width: 25px;
  height: 25px;
  line-height: 25px;
  font-size: small;
  text-align: center;
  border-radius: 50%;
  display: block;
  margin: 5px;
}

.team{
  padding: 20px;
}

</style>


