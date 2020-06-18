<?php
	include("../includes/session.php"); //include session file
	$maps = $heritage->getMapMarkers($con);
	
	$siteAdded = "";
	if(isset($_POST['title']))
	{
		$filename = $_FILES['upldFile']['name'];
		
		if(isset($_POST['siteid']))
			$id = $_POST['siteid'];	
		
		$res = $heritage->insertMapMarker($con,$uid,$_POST['title'],$_POST['address'],$filename,$_POST['lat'],$_POST['long'],$id);
		if($res > 0)
		{
			$last_id = mysqli_insert_id($con);
			$uploaddir = $_SERVER['DOCUMENT_ROOT'].'/admin/sites_images/';
			$uploadfile = $uploaddir . $last_id.'-'.$filename;
						
			if (move_uploaded_file($_FILES['upldFile'.$i]['tmp_name'], $uploadfile)) {
				$result = 1;
				$siteAdded = "<div class='alert alert-success'>Site is successfully added</div>";
			}			
		}
	}	
?>
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
    <title>Sites | e-Heritage</title>

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

    <!-- Colorpicker Css -->
    <link href="plugins/bootstrap-colorpicker/css/bootstrap-colorpicker.css" rel="stylesheet" />

    <!-- Dropzone Css -->
    <link href="plugins/dropzone/dropzone.css" rel="stylesheet">

    <!-- Multi Select Css -->
    <link href="plugins/multi-select/css/multi-select.css" rel="stylesheet">

    <!-- Bootstrap Spinner Css -->
    <link href="plugins/jquery-spinner/css/bootstrap-spinner.css" rel="stylesheet">

    <!-- Bootstrap Tagsinput Css -->
    <link href="plugins/bootstrap-tagsinput/bootstrap-tagsinput.css" rel="stylesheet">

    <!-- Bootstrap Select Css -->
    <link href="plugins/bootstrap-select/css/bootstrap-select.css" rel="stylesheet" />

    <!-- noUISlider Css -->
    <link href="plugins/nouislider/nouislider.min.css" rel="stylesheet" />

    <!-- Custom Css -->
    <link href="css/style.css" rel="stylesheet">

    <!-- AdminBSB Themes. You can choose a theme from css/themes instead of get all themes -->
    <link href="css/themes/all-themes.css" rel="stylesheet" />
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
                <h2></h2>
            </div>
            <div class="row">

                <div class="col-lg-3 col-md-3 col-sm-6 col-xs-12 btnNewSite">
                    <div class="info-box-4" style="cursor:pointer">
                        <div class="icon">
                            <i class="material-icons col-red">add_box</i>
                        </div>
                        <div class="content">
                            <div class="text">ADD NEW SITE</div>
                            <!--div class="number count-to" data-from="0" data-to="125" data-speed="1000" data-fresh-interval="20">125</div-->
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-md-3 col-sm-6 col-xs-12">
                    <div class="info-box-4 btnManageSite" style="display:none;cursor:pointer;">
                        <div class="icon">
                            <i class="material-icons col-indigo">local_library</i>
                        </div>
                        <div class="content">
                            <div class="text">MANAGE SITES</div>
                            <div class="number count-to" data-from="0" data-to="257" data-speed="1000" data-fresh-interval="20"><?php echo count($maps) ?></div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-md-3 col-sm-6 col-xs-12">
					<?php echo $siteAdded ?>
                </div>				
            </div>			
            <!-- Basic Card -->
            <div class="row clearfix manageSite">
                <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                    <div class="card">
                        <div class="header">
                            <h2>
                                SITES
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
                            <select class="form-control selSite" style="height:300px;border-radius:0px" multiple="multiple">
							<optgroup label="Limpopo">
							<?php 
								$i = 0;
								foreach($maps as $row)
								{
									?>
									
                                    <option value="<?php echo $row['id'] ?>" id="<?php echo $row['name'] ?>"><?php echo $row['name'] ?></option>
                                
								<?php	
									$i++;
								}
							?>
							</optgroup>	
                            </select>
                        </div>
                    </div>
                </div>

                <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
				<?php
					$map = $heritage->getMapMarkerById($con,1);
				?>	
                    <div class="card">
                        <div class="header">
                            <h2 class="siteName" style="text-transform:uppercase">
                                <?php //echo $map['name'] ?>
                            </h2>
                            <ul class="header-dropdown m-r--5">
                                <li>
                                    <a href="javascript:void(0);">
                                        <i class="material-icons">mic</i>
                                    </a>
                                </li>
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
							<div id="mapPanel">	
							</div>	
                        </div>
                    </div>
                </div>
            </div>			
            <!-- #END# File Upload | Drag & Drop OR With Click & Choose -->
            <!-- #END# Masked Input -->
            <!-- Input Group -->
            <div class="row clearfix newsite" style="display:none">
                <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                    <div class="card">
                        <div class="header">
                            <h2>
                                ADD SITE
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
							<form id="addSiteFrm" enctype="multipart/form-data" method="post">
                            
                            <div class="row clearfix">
                                <div class="col-md-4">
                                    <div class="input-group">
                                        <span class="input-group-addon">
                                            <i class="material-icons">title</i>
                                        </span>
                                        <div class="form-line">
                                            <input type="text" class="form-control" placeholder="Site Name" name="title" required>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-10">
                                    <div class="input-group">
                                        <span class="input-group-addon">
                                            <i class="material-icons">location_on</i>
                                        </span>									
                                        <div class="form-line">
                                            <input type="text" class="form-control" placeholder="Address" name="address" required>
                                        </div>
                                    </div>
                                </div>	
                                <div class="col-md-10">
                                    <div class="input-group">
                                        <span class="input-group-addon">
                                            <i class="material-icons">photo</i>
                                        </span>									
                                        <div class="">
                                            <input type="file" id="upldFile" name="upldFile" class="docs" style="display:none" required>
											<span class="dispFile"></span>
											<button type="button" onclick="document.getElementById('upldFile').click()" class="btn btn-primary upld">Upload Image</button>
											
                                        </div>
                                    </div>
                                </div>									
                            </div>

                            <h2 class="card-inside-title">Coordinates</h2>
                            <div class="row clearfix">
                                <div class="col-md-5">
                                    <div class="input-group">
                                        <span class="input-group-addon">
                                            <i class="material-icons"></i>
                                        </span>
                                        <div class="form-line">
                                            <input type="text" class="form-control" placeholder="Latitude" name="lat" required>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-5">
                                    <div class="input-group">
                                        <span class="input-group-addon">
                                            <i class="material-icons"></i>
                                        </span>
                                        <div class="form-line">
                                            <input type="text" class="form-control" placeholder="Longitude" name="long" required>
                                        </div>
                                    </div>
                                </div>
								<div class="col-md-5">
									<button type="submit" class="btn btn-success btn-block btnAddSite">ADD</button>
								</div>
                            </div>
							</form>
                        </div>
                    </div>
                </div>
            </div>
            <!-- #END# Input Group -->

        </div>
    </section>
            <div class="modal fade" id="defaultModal" tabindex="-1" role="dialog">
                <div class="modal-dialog modal-lg" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h4 class="modal-title" id="defaultModalLabel"></h4>
                        </div>
                        <div class="modal-body">
							<textarea></textarea>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-link waves-effect" data-dismiss="modal">CLOSE</button>
                        </div>
                    </div>
                </div>
            </div>
    <!-- Jquery Core Js -->
	<script src="../assets/js/jquery-2.0.0.js"></script>

    <!-- Bootstrap Core Js -->
    <script src="plugins/bootstrap/js/bootstrap.js"></script>
	<!-- E-Heritage javascript -->
	<script src="../assets/js/eheritage.js"></script> 
    <!-- Select Plugin Js >
    <script src="plugins/bootstrap-select/js/bootstrap-select.js"></script-->

    <!-- Slimscroll Plugin Js -->
    <script src="plugins/jquery-slimscroll/jquery.slimscroll.js"></script>

    <!-- Bootstrap Colorpicker Js -->
    <script src="plugins/bootstrap-colorpicker/js/bootstrap-colorpicker.js"></script>

    <!-- Dropzone Plugin Js -->
    <script src="plugins/dropzone/dropzone.js"></script>

    <!-- Input Mask Plugin Js -->
    <script src="plugins/jquery-inputmask/jquery.inputmask.bundle.js"></script>

    <!-- Multi Select Plugin Js -->
    <script src="plugins/multi-select/js/jquery.multi-select.js"></script>

    <!-- Jquery Spinner Plugin Js -->
    <script src="plugins/jquery-spinner/js/jquery.spinner.js"></script>

    <!-- Bootstrap Tags Input Plugin Js -->
    <script src="plugins/bootstrap-tagsinput/bootstrap-tagsinput.js"></script>

    <!-- noUISlider Plugin Js -->
    <script src="plugins/nouislider/nouislider.js"></script>

    <!-- Waves Effect Plugin Js -->
    <script src="plugins/node-waves/waves.js"></script>

    <!-- Custom Js -->
    <script src="js/admin.js"></script>
    <script src="js/pages/forms/advanced-form-elements.js"></script>
    <!-- Validation Plugin Js -->
    <script src="plugins/jquery-validation/jquery.validate.js"></script>
    <!-- Demo Js -->
    <script src="js/demo.js"></script>
    <script src="tinymce/js/tinymce/tinymce.js"></script>
    <script src="tinymce/js/tinymce/jquery.tinymce.min.js"></script>	
	
	<script src="../assets/js/jquery-migrate-1.1.1.js"></script>
    <script>
      
        $('textarea').tinymce({});
      
    </script>	
</body>

</html>
