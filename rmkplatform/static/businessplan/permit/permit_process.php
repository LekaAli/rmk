<?php 
	//create array of requests 
	$arrRequests = array("Request to register a heritage site","Request to register a heritage object","Request to develop a site","Request for exemption to develop a site");
?>
<!DOCTYPE html>
<html lang="en">
  <head>
  <meta charset="utf-8">
    <!-- Viewport Meta Tag -->
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>
      E-Heritage
    </title>
    <!-- Bootstrap -->
    <link rel="stylesheet" type="text/css" href="../assets/css/bootstrap.min.css">
    <!-- Main Style -->
    <link rel="stylesheet" type="text/css" href="../assets/css/main.css">
    <!-- Slicknav Css -->
    <link rel="stylesheet" type="text/css" href="../assets/css/slicknav.css">

    <!-- Responsive Style -->
    <link rel="stylesheet" type="text/css" href="../assets/css/responsive.css">
    <!--Fonts-->
    <link rel="stylesheet" media="screen" href="../assets/fonts/font-awesome/font-awesome.min.css">
    <link rel="stylesheet" media="screen" href="../assets/fonts/simple-line-icons.css">    
     
    <!-- Extras -->
    <link rel="stylesheet" type="text/css" href="../assets/extras/owl/owl.carousel.css">
    <link rel="stylesheet" type="text/css" href="../assets/extras/owl/owl.theme.css">
    <link rel="stylesheet" type="text/css" href="../assets/extras/animate.css">
    <link rel="stylesheet" type="text/css" href="../assets/extras/normalize.css">
    

    <!-- Color CSS Styles  -->  
    <link rel="stylesheet" type="text/css" href="../assets/css/colors/green.css" media="screen" />
	<!-- Permit Progress bar Style -->
	<link rel="stylesheet" type="text/css" href="../assets/css/progress.css">    
    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js">
    </script>
    <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js">
    </script>
    <![endif]-->
	<style>
		.caps
		{
			text-transform:uppercase;
		}
		.apply_process
		{
			display:none;
		}
	</style>
  </head>
  <body>
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
<header id="header-wrap"> 
      <!-- Navbar Starts --> 
      <nav class="navbar navbar-expand-md fixed-top scrolling-navbar nav-bg" style="top:30px">
	 
        <div class="container">
          <!-- Brand and toggle get grouped for better mobile display -->
          <div class="navbar-header">
            <a class="navbar-brand" href="http://www.limeheritage.co.za">
              <img src="../assets/img/Logo1.png" alt="">
            </a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#main-menu" aria-controls="main-menu" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>           
          </div>
          <div class="collapse navbar-collapse" id="main-menu">
            <ul class="navbar-nav mr-auto w-100 justify-content-end">
              <li class="nav-item">
                <a class="nav-link active" href="http://www.limeheritage.co.za" >
                  Home
                </a>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">About us</a>
                <div class="dropdown-menu">
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/management.php">Management</a>
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/abouteheritage.php">About E-Heritage</a>
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/contacts.php">Contact information</a>
                </div> 
              </li>
			  <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Permit</a>
                <div class="dropdown-menu">
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/permit/">Apply for Permit</a>
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/permit/permit_process.php">Permit Application Process</a>
                </div> 
		
        
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Publications</a>
                <div class="dropdown-menu">
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/mediarelease.php">Media release</a>
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/promotional.php">Promotional</a>
                  <a class="dropdown-item" href="phttp://www.limeheritage.co.za/resentation.php">Presentation</a>
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/reports.php">Reports</a>
                </div>
              </li>	
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Heritage</a>
                <div class="dropdown-menu">
                <a class="dropdown-item" href="http://www.limeheritage.co.za/worldheritage.php">Word Heritage Sites</a>
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/provincialheritage.php">Provincial Heritage Sites</a>
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/districtsites.php">Sites per District</a>
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/communityheritage.php">Community heritage</a>
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/heritagetourism.php">Heritage site with tourist attraction</a>
                     <a class="dropdown-item" href="http://www.limeheritage.co.za/sculputures.php">Sculptures</a>
                </div>
              </li>	 		  
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Gallery</a>
                <div class="dropdown-menu">
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/galleryevents.php">Previous Events</a>
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/gallerytourism.php">Tourism Attraction </a>
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/gallery.php">All Photos</a>
        
                </div>
              </li>			  
           		     <li class="nav-item">
                <a class="nav-link" href="http://www.limeheritage.co.za/feedback.php">Feedback</a> 
              </li>		
       
            </ul>
            <form class="form-inline">
              <div class="top_search_con">
                <input class=" mr-sm-2" type="text" placeholder="Search Here ...">
                <span class="top_search_icon"><i class="icon-magnifier"></i></span>
              </div>            
            </form>
          </div>

          <!-- Mobile Menu Start -->
          <ul class="wpb-mobile-menu">
              <li class="nav-item">
                <a class="nav-link active" href="http://www.limeheritage.co.za" >
                  Home
                </a>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">About us</a>
                <div class="dropdown-menu">
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/management.php">Management</a>
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/abouteheritage.php">About E-Heritage</a>
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/contacts.php">Contact information</a>
                </div> 
              </li>
			  <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Permit</a>
                <div class="dropdown-menu">
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/permit/">Apply for Permit</a>
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/permit/permit_process.php">Permit Application Process</a>
                </div> 
		
        
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Publications</a>
                <div class="dropdown-menu">
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/mediarelease.php">Media release</a>
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/promotional.php">Promotional</a>
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/presentation.php">Presentation</a>
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/reports.php">Reports</a>
                </div>
              </li>	
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Heritage</a>
                <div class="dropdown-menu">
                <a class="dropdown-item" href="http://www.limeheritage.co.za/worldheritage.php">Word Heritage Sites</a>
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/provincialheritage.php">Provincial Heritage Sites</a>
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/districtsites.php">Sites per District</a>
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/communityheritage.php">Community heritage</a>
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/heritagetourism.php">Heritage site with tourist attraction</a>
                     <a class="dropdown-item" href="http://www.limeheritage.co.za/sculputures.php">Sculptures</a>
                </div>
              </li>	 		  
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Gallery</a>
                <div class="dropdown-menu">
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/galleryevents.php">Previous Events</a>
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/gallerytourism.php">Tourism Attraction </a>
                  <a class="dropdown-item" href="http://www.limeheritage.co.za/gallery.php">All Photos</a>
        
                </div>
              </li>			  
           		     <li class="nav-item">
                <a class="nav-link" href="http://www.limeheritage.co.za/feedback.php">Feedback</a> 
              </li>		
       
            </ul>
          <!-- Mobile Menu End -->
        </div>
      </nav>
    </header>
    <!-- Header-wrap Section End -->
    <br>
    <!-- Page Header -->
    <div class="page-header-section">
      <div class="container">
        <div class="row">
          <div class="page-header-area">
            <div class="page-header-content">
              <h2>Track your Permit Order</h2>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Page Header End -->

    <section class="contact2-section section">
      <div class="container">
        <div class="row justify-content-center">
			<div class="col-md-6 track_case">
              <h3 class="small-title mb-3"><i class="fa fa-globe icon-round-border icon-md"></i>ENTER CASE NUMBER</h3>
              <!-- Block level buttons -->
              <div class="row block-level-buttons clearfix">
				<div class="col-md-12">
					<form method="post" role="form" class="mt-30 shake" id="frmtrack" name="frmtrack" data-toggle="validator">
						<div class="form-group input-group-lg">
							<input type="text" placeholder="Case number" style="border-radius:0px !important" id="caseno" class="form-control contact-control" name="caseno" required data-error="Please enter your case number">
								<div class="help-block with-errors"></div>	
						</div>
						<div class="form-group">
							<button class="btn btn-common btn-lg btn-block btnTrack" name="btnTrack" type="button"><i class="fa fa-globe"></i> Track</button>	
						</div>	
					</form>		
				</div>	
              </div>				
			</div>

          <div class="col-md-12 apply_process">
            <h4 class="section-title text-left">PERMIT APPLICATION PROGRESS</h4>
            <p class="section-subcontent mb-30 text-left">Hi Applicant<br>
			Thank you for your application, our team are busy assessing your application.</p>

            <div class="row bs-wizard" style="border-bottom:0;">
                
                <div class="col-xs-3 bs-wizard-step complete">
                  <div class="text-center bs-wizard-stepnum">Received</div>
                  <div class="progress"><div class="progress-bar"></div></div>
                  <a href="#" class="bs-wizard-dot"></a>
                  <div class="bs-wizard-info text-center">Application was submitted Successfully.</div>
                </div>
                
                <div class="col-xs-3 bs-wizard-step active"><!-- complete -->
                  <div class="text-center bs-wizard-stepnum">Assessment</div>
                  <div class="progress"><div class="progress-bar"></div></div>
                  <a href="#" class="bs-wizard-dot"></a>
                  <div class="bs-wizard-info text-center">Assessment in progress</div>
                </div>
                
                <div class="col-xs-3 bs-wizard-step disabled"><!-- complete -->
                  <div class="text-center bs-wizard-stepnum">Assessment Results</div>
                  <div class="progress"><div class="progress-bar"></div></div>
                  <a href="#" class="bs-wizard-dot"></a>
                  <div class="bs-wizard-info text-center">Approval or Denial</div>
                </div>
                
                <div class="col-xs-3 bs-wizard-step disabled"><!-- active -->
                  <div class="text-center bs-wizard-stepnum">Capture Details</div>
                  <div class="progress"><div class="progress-bar"></div></div>
                  <a href="#" class="bs-wizard-dot"></a>
                  <div class="bs-wizard-info text-center">Approved and ready to be captured</div>
                </div>
            </div>
        
        
        
        
        
	</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer Section -->
    <footer>
      <!-- Container Starts -->
      <div class="container">
        <!-- Row Starts -->
        <div class="row section">
          <!-- Footer Widget Starts -->
          <div class="footer-widget col-md-6 col-lg-3 col-xs-12">
            <h3 class="small-title">
              About Us
            </h3>
            <p>
              Etiam ornare condimentum massa et scelerisque. Mauris nibh ipsum, laoreet at venenatis ac, 
            </p> 
            <ul class="mb-3">
              <li><i class="fa fa-map-marke"></i> Nash Street , Dearborn, Michigan</li>
              <li><i class="fa fa-phone"></i> +68 313-240-405</li>
              <li><i class="fa fa-phone"></i> +68 32-543-876</li>              
            </ul>   
          </div><!-- Footer Widget Ends -->
          
          <!-- Footer Widget Starts -->
          <div class="footer-widget col-md-6 col-lg-3 col-xs-12">
            <h3 class="small-title">
              Quick Links
            </h3>
            <ul class="menu">
              <li><a href="#">About Us</a></li>
              <li><a href="#">Team</a></li>
              <li><a href="#">Terms of Service</a></li>
              <li><a href="#">Sitemap</a></li>
              <li><a href="#">FAQ</a></li>
              <li><a href="#">Events</a></li>
              <li><a href="#">Contact</a></li>
              <li><a href="#">Blog</a></li>
              <li><a href="#">Branches</a></li>
              <li><a href="#">Press Kits</a></li>
            </ul>
          </div>
          <!-- Footer Widget Ends -->

          <!-- Footer Widget Starts -->
          <div class="footer-widget col-md-6 col-lg-3 col-xs-12">
            <h3 class="small-title">
              Popular Posts
            </h3>
            <ul class="image-list">
              <li>
                <figure class="overlay">
                  <img class="img-fluid" src="../assets/img/art/a1.jpg" alt="">
                </figure>
                <div class="post-content">
                  <h6 class="post-title"> <a href="blog-single.html">Business Management Tutorials</a> </h6>
                  <div class="meta">
                    <span class="date">5 Comments</span>
                  </div>
                </div>
              </li>
              <li>
                <figure class="overlay">
                  <img class="img-fluid" src="../assets/img/art/a2.jpg" alt="">
                </figure>
                <div class="post-content">
                  <h6 class="post-title"><a href="blog-single.html">Top 10 Business Apps and Web Tools</a></h6>
                  <div class="meta">
                    <span class="date">2 Comments</span>
                  </div>
                </div>
              </li>
            </ul>
          </div>
          <!-- Footer Widget Ends -->

          <!-- Footer Widget Starts -->
          <div class="footer-widget col-md-6 col-lg-3 col-xs-12">
            <h3 class="small-title">
              Newsletter
            </h3>
            <form>
              <input type="text" placeholder="Email here">
              <button type="submit"><i class="fa fa-paper-plane-o"></i></button>
            </form>
            <div class="flicker-gallery">
              <h3 class="small-title">
                Instagram
              </h3>
              <a href="#" title="Pan Masala"><img src="../assets/img/flicker/img1.jpg" alt=""></a>
              <a href="#" title="Sports Template for Joomla"><img src="../assets/img/flicker/img2.jpg" alt=""></a>
              <a href="" title="Apple Keyboard"><img src="../assets/img/flicker/img3.jpg" alt=""></a>
            </div>
          </div><!-- Footer Widget Ends -->
        </div><!-- Row Ends -->
      </div><!-- Container Ends -->
      
      <!-- Copyright -->
      <div id="copyright">
        <div class="container">
          <div class="row">
            <div class="col-md-6 col-sm-6">
              <p class="copyright-text">
                © 2018 Engage All right reserved, Designed by <a href="#">GrayGrids</a>
              </p>
            </div>
            <div class="col-md-6 col-sm-6">
              <div class="social-footer text-right">
                <a href="#"><i class="fa fa-facebook icon-round"></i></a>
                <a href="#"><i class="fa fa-twitter icon-round"></i></a>
                <a href="#"><i class="fa fa-linkedin icon-round"></i></a>
                <a href="#"><i class="fa fa-google-plus icon-round"></i></a>
              </div>       
            </div>
          </div>
        </div>
      </div>
      <!-- Copyright  End-->
      
    </footer>
    <!-- Footer Section End-->
    
    <!-- Go To Top Link -->
    <a href="#" class="back-to-top">
      <i class="fa fa-angle-up">
      </i>
    </a>
    
    <!-- JavaScript & jQuery Plugins -->
<script src="//code.jquery.com/jquery-1.11.1.min.js"></script>		
<script src="//netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>

    <!--script src="../assets/js/jquery-min.js"></script-->
    <script src="../assets/js/popper.min.js"></script>
    <!--script src="../assets/js/bootstrap.min.js"></script-->
    <script src="../assets/js/jquery.mixitup.js"></script>
    <script src="../assets/js/smoothscroll.js"></script>
    <script src="../assets/js/wow.js"></script>
    <script src="../assets/js/owl.carousel.js"></script> 
    <script src="../assets/js/waypoints.min.js"></script>
    <script src="../assets/js/jquery.counterup.min.js"></script>
    <script src="../assets/js/jquery.slicknav.js"></script>
    <script src="../assets/js/jquery.appear.js"></script>
    <script src="../assets/js/form-validator.min.js"></script>
    <script src="../assets/js/contact-form-script.min.js"></script>
    <script src="../assets/js/main.js"></script> 
    <script>
		/*
		- function to call the chosen request 
		- unhide an application form based on the chosen request
		*/
		$(document).ready(function(){
			$(".btnTrack").click(function(){
				$(".apply_process").fadeIn('slow');
				$(".track_case").slideUp('slow');
				return false;	
			});				
		});
	
	</script>
  </body>
</html>>