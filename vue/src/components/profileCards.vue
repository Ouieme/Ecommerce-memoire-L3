<template>
  <div class="container">
    <div class="background">
      <div class="ring">
        <div class="lds-ripple">
        </div>
      </div>
    </div>
    <div class="body__container">
      <div class="body__profile">
        <div class="body__profile__photo">
          <img src="../assets/pic2.jpg" alt="Perfil" />
        </div>
        <div id="demo">
          <transition name="fade">
            <!--English-->
            <div class="body__profile__title">
              <h1>Gabriela Costa</h1>
              <h2>UI/UX designer</h2>
              <h2>Front-end Web Developer</h2>
              <div class="body__profile__bio-pt">
                <p>IDK what to do im gonna die </p>
              </div>
            </div>
          </transition>
          <!--Social-->
          <div class="body__profile__icons">

            <img src="../assets/github-logo_icon-icons.com_73546.svg">


            <img src="../assets/google_mail_gmail_logo_icon_159346.svg" style=" width: 29cm;">

            <img src="../assets/in_linked_linkedin_media_social_icon_124259.svg ">

          </div>
        </div>



      </div>
    </div>
  </div>
</template>


<style>
/* #app {
  font-family: Orkney, sans-serif;
  font-size: 1.2em;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #303030;
  margin-top: 60px;
} */


blockquote:before,
blockquote:after,
q:before,
q:after {
  content: '';
  content: none;
}

table {
  border-collapse: collapse;
  border-spacing: 0;
}




.background {
  width: 50%;
  height: 50%;
  top: 0px;
  position: fixed;
  z-index: 10;
}

.ring {
  position: absolute;
  top: 50%;
  left: 50%;
  margin: 0 auto;
  height: 100%;
}

.lds-ripple {
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
}

.lds-ripple div {
  position: absolute;
  border: 4px solid #fff;
  opacity: 1;
  border-radius: 50%;
  animation: lds-ripple 1s cubic-bezier(0, 0.2, 0.8, 1) infinite;
}

.lds-ripple div:nth-child(2) {
  animation-delay: -0.5s;
}

@keyframes lds-ripple {
  0% {
    top: 36px;
    left: 36px;
    width: 0;
    height: 0;
    opacity: 1;
  }

  100% {
    top: 0px;
    left: 0px;
    width: 72px;
    height: 72px;
    opacity: 0;
  }
}

/*card*/
.body__container {
  margin: 0 auto;
  display: flex;
  justify-content: center;
  align-items: center;
}

.body__profile {
  background: white;
  border-radius: 50px;
  padding: 1.5em 1.75em;
  margin: 2em auto;
  max-width: 330px;
  box-shadow: 0px 3px 136px 0px rgba(88, 87, 119, 0.21);
}

/*Photo*/
.body__profile__photo img {
  border-radius: 50%;
  width: 170px;
  height: 165px;
  border: 6px solid #fff;
  top: -100px;
  position: relative;
  box-shadow: 1px 2px 18px 4px rgb(226, 226, 226);
}


.fade-enter,
.fade-leave-to
/* .fade-leave-active in <2.1.8 */

  {
  opacity: 0
}



.github {
  background-color: #d1a1f5;
}

.github:hover {
  background-color: #df2fe6;
}

.cv {
  background-color: #b9a9ff;
}

.cv:hover {
  background-color: #842fe6;
}


/*Portuguese*/
.body__profile__title {
  top: -20px;
  position: relative;
}

.body__profile__title h1 {
  font-size: 1.5em;
  font-weight: 900;
  text-align: center;
  color: rgb(84, 84, 84);
  margin: 0 0 0.5em 0;
}

.body__profile__title h2 {
  font-size: 0.75em;
  color: rgb(153, 153, 153);
  line-height: 1.391;
  font-weight: lighter;
  text-align: center;
  text-transform: uppercase;

}

.body__profile__bio-pt {
  font-size: 0.75em;
  color: rgb(171, 171, 171);
  font-weight: 900;
  line-height: 1.404;
  text-align: center;
  margin: 1em 0;
  padding: 1.25em 0;
  border-top: 4px solid whitesmoke;
  border-bottom: 4px solid whitesmoke;
  transition: all 0.5s ease-in-out;
}

.body__profile__bio-pt:hover {
  transition: all 0.5s ease-in-out;
}

/*English */
.body__profile__title {
  top: -20px;
  position: relative;
}

.body__profile__title h1 {
  font-size: 1.5em;
  font-weight: 900;
  text-align: center;
  color: rgb(84, 84, 84);
  margin: 0 0 0.5em 0;
}

.body__profile__title h2 {
  font-size: 0.75em;
  color: rgb(153, 153, 153);
  line-height: 1.391;
  font-weight: lighter;
  text-align: center;
  text-transform: uppercase;

}

.body__profile__bio-en {
  font-size: 0.75em;
  color: rgb(171, 171, 171);
  font-weight: 900;
  line-height: 1.404;
  text-align: center;
  margin: 1em 0;
  padding: 1.25em 0;
  border-top: 4px solid whitesmoke;
  border-bottom: 4px solid whitesmoke;
  transition: all 0.5s ease-in-out;
}

/*Social*/

.body__profile__icons {
  display: flex;
  width: 50px;
  height: 50px;
  position: relative;
  font-size: 3.5em;
  letter-spacing: 0.40em;
  top: -20px;

  align-items: center;
  grid-gap: 26px;

}
</style>