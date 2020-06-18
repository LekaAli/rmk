<?php
	include("../includes/session.php"); //include session file
	$roles = $heritage->userrights($con); //load all user roles
?>
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
    <title>Sign Up | Bootstrap Based Admin Template - Material Design</title>
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
                <div class="spinner-layer pl-red">
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
	<?php include("sidebar.php") ?>
    </section>	
    <section class="content">
        <div class="container-fluid">
            <div class="block-header">
                <h2>ADD USER</h2>
            </div>

            <!-- Widgets -->
            <div class="row clearfix">
		<div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">	
    <div class="signup-box">
        <div class="card">
            <div class="body">
                <form id="sign_upform" method="POST">
                    <div class="input-group">
                        <span class="input-group-addon">
                            <i class="material-icons">person</i>
                        </span>
                        <div class="form-line">
                            <input type="text" class="form-control" name="fnames" placeholder="Name Surname" required autofocus>
                        </div>
                    </div>
                    <div class="input-group">
                        <span class="input-group-addon">
                            <i class="material-icons">email</i>
                        </span>
                        <div class="form-line">
                            <input type="email" class="form-control" name="email" placeholder="Email Address" required>
                        </div>
                    </div>
                    <div class="input-group">
                        <span class="input-group-addon">
                            <i class="material-icons">phone</i>
                        </span>
                        <div class="form-line">
                            <input type="text" class="form-control" name="cell" placeholder="Cellphone" required>
                        </div>
                    </div>	
                    <div class="input-group">
                        <span class="input-group-addon">
                            <i class="material-icons">accessibility</i>
                        </span>
                        <div class="form-line">
							<select name="usertype" class="form-control" required>
							<?php
								echo '<option value="">Type of user</option>';
								foreach($roles as $row)
								{
									echo '<option value="'.$row['id'].'">'.$row['role'].'</option>';
								}
							?>	
							</select>
                        </div>
                    </div>						
                    <div class="input-group">
                        <span class="input-group-addon">
                            <i class="material-icons">perm_identity</i>
                        </span>
                        <div class="form-line">
							<input type="text" name="position" class="form-control" placeholder="Position" required>
                        </div>
                    </div>	

                    <button class="btn btn-block btn-lg bg-green waves-effect btnadduser" type="submit">ADD USER</button>
                </form>
            </div>
        </div>
    </div>
	</div>
	</div>
	</div>
	</section>

    <!-- Jquery Core Js -->
    <script src="../assets/js/jquery-2.0.0.js"></script>

	<!-- E-Heritage javascript -->
	<script src="../assets/js/eheritage.js"></script> 
	
    <!-- Bootstrap Core Js -->
    <script src="plugins/bootstrap/js/bootstrap.js"></script>

    <!-- Waves Effect Plugin Js -->
    <script src="plugins/node-waves/waves.js"></script>

    <!-- Validation Plugin Js -->
    <script src="plugins/jquery-validation/jquery.validate.js"></script>

    <!-- Custom Js -->
    <script src="js/admin.js"></script>
    <script src="js/pages/examples/sign-up.js"></script>
	<script src="../assets/js/jquery-migrate-1.1.1.js"></script>
</body>

</html>