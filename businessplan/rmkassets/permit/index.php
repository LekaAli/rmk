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
		.apply_request
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
              <h2>Apply for Permit</h2>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Page Header End -->

    <section class="contact2-section section">
      <div class="container">
        <div class="row justify-content-center">
			<div class="col-md-6 choose_request">
              <h3 class="small-title mb-3"><i class="fa fa-cloud-download icon-round-border icon-md"></i>CHOOSE YOUR REQUEST</h3>
              <!-- Block level buttons -->
              <div class="row block-level-buttons clearfix">
				<div class="col-md-12">
					<?php 
					foreach($arrRequests as $row)
					{
						echo '<div class="form-group">
						  <a href="javascript:;" id="'.$row.'" onclick="chooseReq(this.id)" class="btn btn-common btn-lg btn-block caps" >'.$row.'</a>
						</div>';
					}
					?>					
				</div>	
              </div>				
			</div>

          <div class="col-md-8 apply_request">
            <h1 class="section-title text-left">PERMIT APPLICATION FORM</h1>
            <p class="section-subcontent mb-30 text-left">At vero eos et accusamus et iusto odio dignissimos ducimus qui <br> blanditiis praesentium</p>
            <form method="post" role="form" class="mt-30 shake" id="contactForm" name="contact-form" data-toggle="validator">
            <div class="row">
				<div class="col-md-12">
					<div class="form-group">
						<label for="request" class="sr-only">request</label>
						<select class="form-control contact-control selreq">
						<?php 
						foreach($arrRequests as $row)
						{
							echo '<option value="'.$row.'">'.$row.'</option>';
						}
						?>
						</select>					
						<div class="help-block with-errors"></div>
					</div>
				</div>
				<div class="col-md-4">	
					<div class="form-group">
						<label for="name" class="sr-only">Name</label>
						<input type="text" placeholder="Name" id="name" class="form-control contact-control" name="name" required data-error="Please enter your name">
						<div class="help-block with-errors"></div>
					</div>
				</div>
				<div class="col-md-4">	
                  <div class="form-group">
                    <label for="email" class="sr-only">Email</label>
                    <input type="email" placeholder="Email" id="email" class="form-control contact-control" name="email" required data-error="Please enter your Email">
                    <div class="help-block with-errors"></div>
                  </div>
				</div> 
				<div class="col-md-4">	
                  <div class="form-group">
                    <label for="email" class="sr-only">Cellphone</label>
                    <input type="text" placeholder="Cellphone" id="cell" class="form-control contact-control" name="cell" required data-error="Please enter your Email">
                    <div class="help-block with-errors"></div>
                  </div>
				</div>				
				<div class="col-md-12">	
                  <div class="form-group">
                    <label for="subject" class="sr-only">Subject</label>
                    <input type="text" placeholder="Subject" id="msg_subject" class="form-control contact-control" name="subject" required data-error="Please enter your message subject">
                    <div class="help-block with-errors"></div>
                  </div>
				</div>
              <div class="col-md-12">
                <div class="form-group">
                  <label for="message" class="sr-only">Message</label>
                  <textarea placeholder="Message" rows="6" id="message" class="form-control" name="message" required data-error="Write your message"></textarea>
                  <div class="help-block with-errors"></div>
                </div>
              </div>
              <div class="col-md-12">
               			  
				  <label class="control-label" for="title">Attachments</label>
	
			   <div style="display:none" id="addinput"></div>	
				<input id="numfiles" type="hidden" name="numfiles" />
				<div class="form-group col-xs-12">
					<button type="button" class="btn btn-common addfile"><i class="fa fa-plus"></i> Add File</button>
				</div>			  
            </div></div>
            <div class="form-group col-xs-12">
              <button class="btn btn-common btn-lg btn-block" name="submit" id="form-submit" type="submit"><i class="fa fa-envelope"></i> Submit</button>
            </div>
          </form>
          </div>
        </div-->
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
    <script src="../assets/js/jquery-min.js"></script>
    <script src="../assets/js/popper.min.js"></script>
    <script src="../assets/js/bootstrap.min.js"></script>
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
		function chooseReq(req)
		{
			$(".apply_request").fadeIn('slow');
			$(".choose_request").slideUp('slow');
			$(".selreq").val(req);
		}

	
	function forfiles(i)
	{
		var name = "suppot_docs"+i;
		$('#numfiles').val(i);
		$('#addinput').show();
		$('#addinput').append('<div class="form-group"><input type="file" name="'+name+'"></div>');		
	}
	$(document).ready(function(){
            $("#feedbackForm").submit(function(e){
				if ($("#feedbackForm").valid())
				{
				}else
					e.preventDefault(e);
            });		
	/*	$('#submitticket').click(function(){
			var dataString = $('#feedbackForm').serialize();
			
            $.ajax({
					type: "POST",
					url: "process_ticket.php",
					data: dataString,
					dataType: 'html',
					cache: false,
					success: function(response)
					{
						window.parent.successMsg(response);
						$('#ticket').click();
					}	
			});					
		});*/
		var i = 1;
		forfiles(i);
		$('.addfile').click(function(){	
			i++;
			forfiles(i);
		});
		
	});
	</script>	
  </body>
</html>>