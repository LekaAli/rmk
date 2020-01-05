<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <!-- Viewport Meta Tag -->
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>
      Limpopo E-Heritage
    </title>
    <!-- Bootstrap -->
    <link rel="stylesheet" type="text/css" href="assets/css/bootstrap.min.css">
    <!-- Main Style -->
    <link rel="stylesheet" type="text/css" href="assets/css/main.css">
    <!-- Slicknav Css -->
    <link rel="stylesheet" type="text/css" href="assets/css/slicknav.css">

    <!-- Responsive Style -->
    <link rel="stylesheet" type="text/css" href="assets/css/responsive.css">
    <!--Fonts-->
    <link rel="stylesheet" media="screen" href="assets/fonts/font-awesome/font-awesome.min.css">
    <link rel="stylesheet" media="screen" href="assets/fonts/simple-line-icons.css">    
     
    <!-- Extras -->
    <link rel="stylesheet" type="text/css" href="assets/extras/owl/owl.carousel.css">
    <link rel="stylesheet" type="text/css" href="assets/extras/owl/owl.theme.css">
    <link rel="stylesheet" type="text/css" href="assets/extras/animate.css">
    <link rel="stylesheet" type="text/css" href="assets/extras/normalize.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/baguettebox.js/1.8.1/baguetteBox.min.js"></script>

    <!-- Color CSS Styles  -->
    <link rel="stylesheet" type="text/css" href="assets/css/colors/green.css" media="screen" />       
    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js">
    </script>
    <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js">
    </script>
    <![endif]-->
<style>
#myCarousel .list-inline {
    white-space:nowrap;
    overflow-x:auto;
}

#myCarousel .carousel-indicators {
    position: static;
    left: initial;
    width: initial;
    margin-left: initial;
}

#myCarousel .carousel-indicators > li {
    width: initial;
    height: initial;
    text-indent: initial;
}

#myCarousel .carousel-indicators > li.active img {
    opacity: 0.7;
}

.bs-calltoaction{
    position: relative;
    width:auto;
    padding: 8px 110px;
    border: 1px solid black;
    margin-top: 0px;
    margin-bottom: 0px;
    margin-bottom: 0px;
    border-radius: 0px;
}

    .bs-calltoaction > .row{
        display:table;
        width: calc(100% + 30px);
    }
     
        .bs-calltoaction > .row > [class^="col-"],
        .bs-calltoaction > .row > [class*=" col-"]{
            float:none;
            display:table-cell;
            vertical-align:middle;
        }

            .cta-contents{
                padding-top: 10px;
                padding-bottom: 10px;
            }

                .cta-title{
                    margin: 0 auto 15px;
                    padding: 0;
                }

                .cta-desc{
                    padding: 0;
                }

                .cta-desc p:last-child{
                    margin-bottom: 0;
                }

            .cta-button{
                padding-top: 10px;
                padding-bottom: 10px;
            }

@media (max-width: 991px){
    .bs-calltoaction > .row{
        display:block;
        width: auto;
    }

        .bs-calltoaction > .row > [class^="col-"],
        .bs-calltoaction > .row > [class*=" col-"]{
            float:none;
            display:block;
            vertical-align:middle;
            position: relative;
        }

        .cta-contents{
            text-align: center;
        }
}



.bs-calltoaction.bs-calltoaction-default{
    color: #333;
    background-color: #fff;
    border-color: #ccc;
}

.bs-calltoaction.bs-calltoaction-primary{
      color: #fff;
    background-color: #ff8a06;
    border-color: #ff8a06;
}
}

.bs-calltoaction.bs-calltoaction-info{
    color: #fff;
    background-color: #5bc0de;
    border-color: #46b8da;
}

.bs-calltoaction.bs-calltoaction-success{
    color: #fff;
    background-color: #5cb85c;
    border-color: #4cae4c;
}

.bs-calltoaction.bs-calltoaction-warning{
    color: #fff;
    background-color: #f0ad4e;
    border-color: #eea236;
}

.bs-calltoaction.bs-calltoaction-danger{
    color: #fff;
    background-color: #d9534f;
    border-color: #d43f3a;
}

.bs-calltoaction.bs-calltoaction-primary .cta-button .btn,
.bs-calltoaction.bs-calltoaction-info .cta-button .btn,
.bs-calltoaction.bs-calltoaction-success .cta-button .btn,
.bs-calltoaction.bs-calltoaction-warning .cta-button .btn,
.bs-calltoaction.bs-calltoaction-danger .cta-button .btn{
    border-color:#fff;
}

</style>	
  </head>
  <body>
 <!-- Top Bar -->
  <div class="top-bar fixed-top" >
    <div class="container"> 
		<div class="row">
			  <div class="col">
				  <div class="float-right">
					<strong><a href="portal/"><i class="icon icon-lock"></i> Login</a> | 
					<a href="portal/?register"><i class="icon icon-user"></i> Register</a></strong>
               <div class="float-left">
              
               
               </div>
				  </div>
			  </div>
		</div>  
    </div>
  </div>  
    <!-- Header area wrapper starts -->
 <?php include("header.php"); ?>
    <!-- Header-wrap Section End -->
<div id="carousel-area">
        <div id="carousel-slider" class="carousel slide" data-ride="carousel">
          <ol class="carousel-indicators">
            <li data-target="#carousel-slider" data-slide-to="0" class="active"></li>
            <li data-target="#carousel-slider" data-slide-to="1"></li>
            <li data-target="#carousel-slider" data-slide-to="2"></li>
          </ol>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img class="d-block w-100" src="assets/img/slider/sl1.jpg" alt="">
              <div class="carousel-caption">
                <h2 class="fadeInUp wow" data-sppb-wow-delay="0.8s">
                 50+ Heritage Site
                </h2>
                <h3 class="fadeInUp wow" data-sppb-wow-delay="1.2s"></h3>
                <!--a class="btn btn-lg btn-common fadeInUp wow" data-sppb-wow-delay="1.4s" href="#">
                  <i class="fa fa-download">
                  </i>
                  Purchase
                </a-->
              </div>
            </div>
            <div class="carousel-item">
              <img class="d-block w-100" src="assets/img/slider/sl2.jpg" alt="">
              <div class="carousel-caption">
                <h2 class="fadeInUp wow" data-sppb-wow-delay="0.8s">
                  Develop Heritage Site
                </h2>
                <h3 class="fadeInUp wow" data-sppb-wow-delay="1.2s">
                 
                </h3>
                <a class="btn btn-lg btn-common fadeInUp wow" data-sppb-wow-delay="1.4s" href="#">
                  <i class="fa fa-coffee">
                  </i>
                  Learn More
                </a>
              </div>
            </div>
            <div class="carousel-item">
              <img class="d-block w-100" src="assets/img/slider/sl3.jpg" alt="">
              <div class="carousel-caption">
                <h2 class="fadeInUp wow" data-sppb-wow-delay="0.8s">
                 100+ Heritage objects
                </h2>
                <h3 class="fadeInUp wow" data-sppb-wow-delay="1.2s">
                 
                </h3>
                <!--a class="btn btn-lg btn-common fadeInUp wow" data-sppb-wow-delay="1.4s" href="#">
                  <i class="fa fa-download">
                  </i>
                  Download
                </a-->
              </div>
            </div>
          </div>
          <a class="carousel-control-prev" href="#carousel-slider" role="button" data-slide="prev">
            <span class="carousel-control carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
          </a>
          <a class="carousel-control-next" href="#carousel-slider" role="button" data-slide="next">
            <span class="carousel-control carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
          </a>
        </div>
      </div>
    <!-- About Us Section Start --><!-- About Us Section Ends --><!-- Other Services Section End -->   
	<section>
 <div class="bs-calltoaction bs-calltoaction-primary">
                    <div class="row">
                        <div class="col-md-9 cta-contents">
                            <h1 class="cta-title">Welcome to Limpopo E-Heritage Portal </h1>
                            <div class="cta-desc">
                         <p>Need to apply for Permit? Click apply and start with the process </p>
                            </div>
                        </div>
                        <div class="col-md-3 cta-button">
                            <a href="#" class="btn btn-lg btn-block btn-primary">Apply Permit now </a>
                        </div>
                     </div>
                </div>
	</section>	
    <!-- Portfolio Section -->
  <section id="cool-facts" class="section">
      <!-- Container Starts -->
    <div class="container">
        <h1 class="section-title wow fadeInUpQuick" data-wow-delay=".3s">
          Gallery
        </h1>
    
          <!-- Portfolio Recent Projects -->
         <div class="tz-gallery">

        <div class="row">

            <div class="col-sm-12 col-md-4">
                <a class="lightbox" href="gallery/images/bridge.jpg">
                    <img src="gallery/images/bridge.jpg" alt="Bridge">
                </a>
            </div>
            <div class="col-sm-6 col-md-4">
                <a class="lightbox" href="gallery/images/park.jpg">
                    <img src="gallery/images/park.jpg" alt="Park">
                </a>
            </div>
            <div class="col-sm-6 col-md-4">
                <a class="lightbox" href="gallery/images/tunnel.jpg">
                    <img src="gallery/images/tunnel.jpg" alt="Tunnel">
                </a>
            </div>
            <div class="col-sm-6 col-md-4">
                <a class="lightbox" href="gallery/images/traffic.jpg">
                    <img src="gallery/images/traffic.jpg" alt="Traffic">
                </a>
            </div>
            <div class="col-sm-6 col-md-4">
                <a class="lightbox" href="gallery/images/coast.jpg">
                    <img src="gallery/images/coast.jpg" alt="Coast">
                </a>
            </div> 
            <div class="col-sm-6 col-md-4">
                <a class="lightbox" href="gallery/images/rails.jpg">
                    <img src="gallery/images/rails.jpg" alt="Rails">
                </a>
            </div>

        </div>

    </div>
         <div class="col-md-12">
            <!-- End Portfolio Recent Projects -->
            <div class="text-center loadmore-button wow fadeInUpQuick" data-wow-delay=".6s"></div>
         </div>
        </div>
      </div>
      <!-- Container Ends -->
    </section>
    <!-- Portfolio Section Ends -->        

    <!-- Pricing Table  End -->    
    
    <!-- Cool Facts Section --><!-- Cool Facts Section End -->     
<div class="col-md-12">
<h1 class="section-title mb-3 wow fadeInUp" data-wow-delay="0.3s">Navigate Heritage Site Locations</h1>
          </div>	
  <?php include("sites.php");?>
    <!-- Blog Section -->
    <section class="section">
      <!-- Carousel With Image -->
    	
    </section>
    <!-- blog Section End -->

    <!-- Clients Section -->
    <section id="clients" class="section">
      <!-- Container Ends -->
      <div class="container">
        <h1 class="section-title wow fadeInUpQuick" data-wow-delay=".5s">
          Limpopo E-Heritage Partners
        </h1>
        <div class="wow fadeInUpQuick" data-wow-delay="0.3s">
          <!-- Row and Scroller Wrapper Starts -->
          <div class="row" id="clients-scroller">
            <div class="client-item-wrapper">
              <img src="assets/img/clients/img1.png" alt="">
            </div>
            <div class="client-item-wrapper">
              <img src="assets/img/clients/img2.png" alt="">
            </div>
            <div class="client-item-wrapper">
              <img src="assets/img/clients/img3.png" alt="">
            </div>
            <div class="client-item-wrapper">
              <img src="assets/img/clients/img4.png" alt="">
            </div>
            <div class="client-item-wrapper">
              <img src="assets/img/clients/img5.png" alt="">
            </div>
            <div class="client-item-wrapper">
              <img src="assets/img/clients/img6.png" alt="">
            </div>
          </div><!-- Row and Scroller Wrapper Starts -->
        </div>
      </div><!-- Container Ends -->
    </section>
    <!-- Client Section End -->        
    
    <!-- Footer Section -->
    <?php include("footer.php");?>
    <!-- Footer Section End-->
    
    <!-- Go To Top Link -->
    <a href="#" class="back-to-top">
      <i class="fa fa-angle-up">
      </i>
    </a> 

    <!-- JavaScript & jQuery Plugins -->
    <script src="assets/js/jquery-min.js"></script>
    <script src="assets/js/popper.min.js"></script>
    <script src="assets/js/bootstrap.min.js"></script>
    <script src="assets/js/jquery.mixitup.js"></script>
    <script src="assets/js/smoothscroll.js"></script>
    <script src="assets/js/wow.js"></script>
    <script src="assets/js/owl.carousel.js"></script> 
    <script src="assets/js/waypoints.min.js"></script>
    <script src="assets/js/jquery.counterup.min.js"></script>
    <script src="assets/js/jquery.slicknav.js"></script>
    <script src="assets/js/jquery.appear.js"></script>
    <script src="assets/js/form-validator.min.js"></script>
    <script src="assets/js/contact-form-script.min.js"></script>
    <script src="assets/js/main.js"></script> 
	<script>
		jQuery(document).ready(function() {

		  let activeTab = $('#myTabs a').filter('.active');

		  $('#myTabs a').click(function(e) {
			e.preventDefault();

			activeTab.removeClass('active');
			$(activeTab.attr('href')).removeClass('active');

			activeTab = $(this);

			activeTab.addClass("active");
			$(activeTab.attr('href')).addClass('active');
		  });
		});
	</script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/baguettebox.js/1.8.1/baguetteBox.min.js"></script>
  </body>
</html>