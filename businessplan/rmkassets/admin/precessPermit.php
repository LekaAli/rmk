<?php
	include("../includes/session.php"); //include session file
	$p_id = base64_decode($_GET['pid']);
	$perm = $heritage->getPermitById($con,$p_id); //call function load users
	$arrStatus = $heritage->permitStages();
?>
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
    <title>Manage Users | Limpopo e-Heritage</title>
    <!-- Favicon-->
    <link rel="icon" href="favicon.ico" type="image/x-icon">

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Roboto:400,700&subset=latin,cyrillic-ext" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" type="text/css">

    <!-- Bootstrap Core Css -->
    <link href="plugins/bootstrap/css/bootstrap.css" rel="stylesheet">

    <!-- Waves Effect Css -->
    <link href="plugins/node-waves/waves.css" rel="stylesheet" />

    <!-- Animation Css -->
    <link href="plugins/animate-css/animate.css" rel="stylesheet" />
   <!-- Sweetalert Css -->
    <link href="plugins/sweetalert/sweetalert.css" rel="stylesheet" />	

    <!-- JQuery DataTable Css -->
    <link href="plugins/jquery-datatable/skin/bootstrap/css/dataTables.bootstrap.css" rel="stylesheet">

    <!-- Custom Css -->
    <link href="css/style.css" rel="stylesheet">

    <!-- AdminBSB Themes. You can choose a theme from css/themes instead of get all themes -->
    <link href="css/themes/all-themes.css" rel="stylesheet" />
	<style>
		.select_user
		{
			cursor:pointer;
		}
.wizard {
    margin: 20px auto;
    
}

.wizard .nav-tabs {
    position: relative;
    margin: 0px auto;
}

.wizard > div.wizard-inner {
    position: relative;
}

.connecting-line {
    height: 1px;
    background: #e0e0e0;
    position: absolute;
    width: 80%;
    margin: 0 auto;
    left: 0;
    right: 0;
    top: 50%;
    z-index: 1;
}

.wizard .nav-tabs > li.active > a,
.wizard .nav-tabs > li.active > a:hover,
.wizard .nav-tabs > li.active > a:focus {
    color: #555555;
    cursor: default;
    border: 0;
    border-bottom-color: transparent;
}

span.round-tab {
    width: 50px;
    height: 50px;
    line-height: 50px;
    display: inline-block;
    border-radius: 100px;
    background: #fff;
    border: 2px solid #e0e0e0;
    z-index: 2;
    position: absolute;
    left: 0;
    text-align: center;
    font-size: 14px;
}

span.round-tab i {
    color: #555555;
}

.wizard li a.active span.round-tab {
    background: #fff;
    border: 2px solid #5bc0de;

}

.wizard li a.active span.round-tab i {
    color: #5bc0de;
}

span.round-tab:hover {
    color: #333;
    border: 2px solid #333;
}

.wizard .nav-tabs > li {
    width: 20%;
}

.wizard li a:after {
    content: " ";
    position: relative;
	left: 46%;
	top: -20px;
    opacity: 0;
    margin: 0 auto;
    bottom: 0px;
    border: 5px solid transparent;
    border-bottom-color: #5bc0de;
    transition: 0.1s ease-in-out;
}

.wizard li.active.nav-item:after {
    content: " ";
    position: relative;
	left: 44%;
	top: -20px;
    opacity: 1;
    margin: 0 auto;
    bottom: 0px;
    border: 10px solid transparent;
    border-bottom-color: #5bc0de;
}

.wizard .nav-tabs > li a {
    width: 50px;
    height: 50px;
    margin: 10px auto;
	margin-bottom:10px;
    border-radius: 100%;
    padding: 0;
    position: relative;
}

.wizard .nav-tabs > li a:hover {
    background: transparent;
}

.wizard .tab-pane {
    position: relative;
    padding-top: 50px;
}

.wizard h3 {
    margin-top: 0;
}

@media( max-width: 585px) {

    .wizard {
        width: 90%;
        height: auto !important;
    }

    span.round-tab {
        font-size: 16px;
        width: 50px;
        height: 50px;
        line-height: 50px;
    }

    .wizard .nav-tabs > li a {
        width: 50px;
        height: 50px;
        line-height: 50px;
    }

    .wizard li.active:after {
        content: " ";
        position: absolute;
        left: 35%;
    }
}		
	</style>
</head>

<body class="theme-green">
    <!-- Page Loader -->
    <div class="page-loader-wrapper">
        <div class="loader">
            <div class="preloader">
                <div class="spinner-layer pl-green">
                    <div class="circle-clipper left">
                        <div class="circle"></div>
                    </div>
                    <div class="circle-clipper right">
                        <div class="circle"></div>
                    </div>
                </div>
            </div>
            <p>Please wait...</p>
        </div>
    </div>
    <!-- #END# Page Loader -->
    <!-- Overlay For Sidebars -->
    <div class="overlay"></div>
    <!-- #END# Overlay For Sidebars -->
    <!-- Search Bar -->
    <div class="search-bar">
        <div class="search-icon">
            <i class="material-icons">search</i>
        </div>
        <input type="text" placeholder="START TYPING...">
        <div class="close-search">
            <i class="material-icons">close</i>
        </div>
    </div>
    <!-- #END# Search Bar -->
    <!-- Top Bar -->
	<?php include("header.php") ?>
    <!-- #Top Bar -->
    <section>
        <!-- Left Sidebar -->
		<?php include("sidebar.php") ?>
        <!-- #END# Right Sidebar -->
    </section>

    <section class="content">
        <div class="container-fluid">
            <div class="block-header">
                <h2>
                    PERMIT PROGRESS
                    <small></small>
                </h2>
            </div>
            <div class="row clearfix">
                <div class="col-lg-10 col-md-10 col-sm-12 col-xs-12">
<form class="form cf">
                    <div class="wizard">
                        <div class="wizard-inner">
                            <div class="connecting-line"></div>
                            <ul class="nav nav-tabs" role="tablist">

								<?php
									$i=1;
									foreach($arrStatus as $st)
									{
										$active = "disabled";
										$bg = "";
										$rj = false;
										if ($heritage->permitStatus($con,$p_id,$st) > 0)
										{
											$active = "success";
											$bg = "bg-green";
											$rj = false;
											if($i == $heritage->numOfActiveStatus($con,$p_id))
											{
												$active = "active";
												$bg = "bg-blue";
												$rj = true;												
											}
										}
										if($rj)
										{
											if ($heritage->permitStatus($con,$p_id,'rejected') > 0)
												$bg = "bg-pink";
										}
									?>
                                <li role="presentation" class="nav-item"><div class="text-center"><?php echo ucwords($st) ?></div>
                                    <a href="#step<?php echo $i ?>" data-toggle="tab" aria-controls="step<?php echo $i ?>" role="tab" title="<?php echo ucwords($st) ?>" class="nav-link <?php echo $active  ?>">
                                <span class="round-tab <?php echo $bg ?>">
                                    <i class="fa fa-building"></i><?php echo $i ?>
                                </span>
                            </a>
                                </li>									
									<?php
									$i++;
									}									
								?>							

                               
                            </ul>
                        </div>

                        <div class="tab-content">						
                            <div class="tab-pane active" role="tabpanel" id="step1">
								<div class="row">
									<div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
											<div class="card">
												<div class="header">
													<h2 class="text-md-left">
														Receiving Process
													</h2>
													<ul class="header-dropdown m-r--5">
														<li class="dropdown">
															<a href="javascript:void(0);" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
																<i class="material-icons">more_vert</i>
															</a>
															<ul class="dropdown-menu pull-right">
																<li><a href="javascript:void(0);">Action</a></li>
																<li><a href="javascript:void(0);">Another action</a></li>
																<li><a href="javascript:void(0);">Something else here</a></li>
															</ul>
														</li>
													</ul>
												</div>
												<div class="body">
														<?php
														if($heritage->permitStatus($con,$p_id,'Assessment') > 0)
														{
															echo '<div class="alert bg-green alert-dismissible"><strong>Received!</strong> - The order was received</div>';
														}else
														{
															?>
														<div class="button-demo">
															<button type="button" class="btn btn-primary waves-effect" onclick="permitNextStage('Assessment',this.id)" id="<?php echo $p_id ?>">ACCEPT</button>
															<button type="button" class="btn btn-danger waves-effect">DECLINE</button>
																				
														</div>	
														<?php
														}
														?>
													 
												</div>
											</div>							
									</div>	
								</div>	
                            </div>
                            <div class="tab-pane" role="tabpanel" id="step2">
								<?php include("assessStage.php"); ?>	
                            </div>
                            <div class="tab-pane" role="tabpanel" id="step3">
								<div class="row">
									<div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
											<div class="card">
												<div class="header">
													<h2 class="text-md-left">
														Feedback Process
													</h2>
													<ul class="header-dropdown m-r--5">
														<li class="dropdown">
															<a href="javascript:void(0);" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
																<i class="material-icons">more_vert</i>
															</a>
															<ul class="dropdown-menu pull-right">
																<li><a href="javascript:void(0);">Action</a></li>
																<li><a href="javascript:void(0);">Another action</a></li>
																<li><a href="javascript:void(0);">Something else here</a></li>
															</ul>
														</li>
													</ul>
												</div>
												<div class="body">
														<?php
				if($heritage->permitStatus($con,$p_id,'capturing') > 0)
				{
					echo '<span class="badge bg-green">Approved</span>';
				}else if($heritage->permitStatus($con,$p_id,'rejected') > 0) 
				{
					$comments = $heritage->loadPermComment($con,$p_id,'rejected');
					echo '<div class="alert bg-pink alert-dismissible"><strong>Rejected!</strong> - '.$comments[0]['comment'].'</div>';
				}else
				{
				?>												
					<div class="button-demo feedbackBtn">
						<button type="button" class="btn btn-primary waves-effect" onclick="permitNextStage('capturing',this.id)" id="<?php echo $p_id ?>">APPROVE</button>
						<button type="button" class="btn btn-danger waves-effect enableReject" data-type="prompt">REJECT</button>
																				
					</div>	
				<div id="rejectComment" style="display:none">								
                    <div class="input-group">
                        <span class="input-group-addon">
                            <i class="material-icons">comment</i>
                        </span>
                        <div class="form-line">
							<textarea class="form-control" name="assessComment" id="assessComment" placeholder="Comment" required></textarea>
                        </div>
                    </div>
					<div class="button-demo">
						<button class="btn bg-pink waves-effect btnaddComment" dir="rejected" id="<?php echo $p_id ?>" type="button">REJECT</button>
						<button class="btn btn-default waves-effect disableReject" dir="Assessment" id="<?php echo $p_id ?>" type="button">CANCEL</button>
					</div>	
				</div>						
				<?php
				}
				?>
													
												</div>
											</div>							
									</div>	
								</div>
                            </div>
                            <div class="tab-pane" role="tabpanel" id="step4">
								<div class="row">
									<div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
											<div class="card">
												<div class="header">
													<h2 class="text-md-left">
														Capturing Process
													</h2>
													<ul class="header-dropdown m-r--5">
														<li class="dropdown">
															<a href="javascript:void(0);" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
																<i class="material-icons">more_vert</i>
															</a>
															<ul class="dropdown-menu pull-right">
																<li><a href="javascript:void(0);">Action</a></li>
																<li><a href="javascript:void(0);">Another action</a></li>
																<li><a href="javascript:void(0);">Something else here</a></li>
															</ul>
														</li>
													</ul>
												</div>
												<div class="body">
													
													<div class="row">
													   

													</div>
													<ul class="list-inline text-md-center">
		<li><button type="button" onclick="permitNextStage('closing',this.id)" id="<?php echo $p_id ?>" class="btn btn-lg btn-common">Next Step</button></li>
													</ul>
													
												</div>
											</div>							
									</div>	
								</div>
                            </div>
                            <div class="tab-pane" role="tabpanel" id="step5">
								<div class="row">
									<div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
											<div class="card">
												<div class="header">
													<h2 class="text-md-left">
														Closing Process
													</h2>
													<ul class="header-dropdown m-r--5">
														<li class="dropdown">
															<a href="javascript:void(0);" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
																<i class="material-icons">more_vert</i>
															</a>
															<ul class="dropdown-menu pull-right">
																<li><a href="javascript:void(0);">Action</a></li>
																<li><a href="javascript:void(0);">Another action</a></li>
																<li><a href="javascript:void(0);">Something else here</a></li>
															</ul>
														</li>
													</ul>
												</div>
												<div class="body">
													
													<div class="row">
													   

													</div>
													<ul class="list-inline text-md-center">
		<li><button type="button" onclick="permitNextStage('closing',this.id)" id="<?php echo $p_id ?>" class="btn btn-lg btn-common">Close</button></li>
													</ul>
													
												</div>
											</div>							
									</div>	
								</div>
                            </div>							
                            <div class="clearfix"></div>
                        </div>

                    </div>
                </form>	
</div>
</div>				
            <!-- #END# Exportable Table -->
        </div>
    </section>

    <!-- Jquery Core Js -->
    <script src="../assets/js/jquery-2.0.0.js"></script>

    <!-- Bootstrap Core Js -->
    <script src="plugins/bootstrap/js/bootstrap.js"></script>
	<!-- E-Heritage javascript -->
	<script src="../assets/js/eheritage.js"></script> 
    <!-- Select Plugin Js -->
    <script src="plugins/bootstrap-select/js/bootstrap-select.js"></script>

    <!-- Slimscroll Plugin Js -->
    <script src="plugins/jquery-slimscroll/jquery.slimscroll.js"></script>

    <!-- Waves Effect Plugin Js -->
    <script src="plugins/node-waves/waves.js"></script>

    <!-- Jquery DataTable Plugin Js -->
    <script src="plugins/jquery-datatable/jquery.dataTables.js"></script>
    <script src="plugins/jquery-datatable/skin/bootstrap/js/dataTables.bootstrap.js"></script>
    <script src="plugins/jquery-datatable/extensions/export/dataTables.buttons.min.js"></script>
    <script src="plugins/jquery-datatable/extensions/export/buttons.flash.min.js"></script>
    <script src="plugins/jquery-datatable/extensions/export/jszip.min.js"></script>
    <script src="plugins/jquery-datatable/extensions/export/pdfmake.min.js"></script>
    <script src="plugins/jquery-datatable/extensions/export/vfs_fonts.js"></script>
    <script src="plugins/jquery-datatable/extensions/export/buttons.html5.min.js"></script>
    <script src="plugins/jquery-datatable/extensions/export/buttons.print.min.js"></script>
    <!-- SweetAlert Plugin Js -->
    <script src="plugins/sweetalert/sweetalert.min.js"></script>	
    <!-- JQuery Steps Plugin Js -->
    <script src="plugins/jquery-steps/jquery.steps.js"></script>
    <!-- Custom Js -->
    <script src="js/admin.js"></script>
    <script src="js/pages/forms/form-wizard.js"></script>
	<script src="js/pages/ui/dialogs.js"></script>

    <!-- Demo Js -->
    <script src="js/demo.js"></script>
	<script src="../assets/js/jquery-migrate-1.1.1.js"></script>
	<script>
	var $active = $('.wizard .nav-tabs .nav-item .active');
    var $activeli = $active.parent("li");
	$($activeli).find('a[data-toggle="tab"]').click();	
		      

	
 //Initialize tooltips
 $('.nav-tabs > li a[title]').tooltip();

 //Wizard
 $('a[data-toggle="tab"]').on('show.bs.tab', function (e) {

     var $target = $(e.target);

     if ($target.hasClass('disabled')) {
         return false;
     }
 });


 $(".next-step").click(function (e) {
     var $active = $('.wizard .nav-tabs .nav-item .active');
     var $activeli = $active.parent("li");

     $($activeli).next().find('a[data-toggle="tab"]').removeClass("disabled");
     $($activeli).next().find('a[data-toggle="tab"]').click();
 });


 $(".prev-step").click(function (e) {

     var $active = $('.wizard .nav-tabs .nav-item .active');
     var $activeli = $active.parent("li");

     $($activeli).prev().find('a[data-toggle="tab"]').removeClass("disabled");
     $($activeli).prev().find('a[data-toggle="tab"]').click();

 });
			
		
	</script>
</body>

</html>