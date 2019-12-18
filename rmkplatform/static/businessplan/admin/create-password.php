<?php
	include("includes/connect.php"); //include connect file
	include('includes/functions.php');
	$heritage = new eheritage_class();			
	$email = base64_decode($_GET['token']);	
	$u = $heritage->userByEmail($con,$email);
	$uid = $u['id'];
	if (!$heritage->checkUserComplete($con,$email) > 0)
	{
		header('location:'.ROOT_PATH.'admin/');
	}else
	{
?>
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
    <title>Forgot Password | Bootstrap Based Admin Template - Material Design</title>
    <!-- Favicon-->
    <link rel="icon" href="favicon.ico" type="image/x-icon">

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Roboto:400,700&subset=latin,cyrillic-ext" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" type="text/css">

    <!-- Bootstrap Core Css -->
    <link href="admin/plugins/bootstrap/css/bootstrap.css" rel="stylesheet">

    <!-- Waves Effect Css -->
    <link href="admin/plugins/node-waves/waves.css" rel="stylesheet" />

    <!-- Animation Css -->
    <link href="admin/plugins/animate-css/animate.css" rel="stylesheet" />

    <!-- Custom Css -->
    <link href="admin/css/style.css" rel="stylesheet">
</head>

<body class="fp-page">
    <div class="fp-box">
        <div class="logo">
            <a href="javascript:void(0);">Admin<b>BSB</b></a>
            <small>Admin BootStrap Based - Material Design</small>
        </div>
        <div class="card">
            <div class="body">
                <form id="forgot_password" method="POST">
                    <div class="msg">
						Create your password
                    </div>
                    <div class="input-group">
                        <span class="input-group-addon">
                            <i class="material-icons">lock</i>
                        </span>
                        <div class="form-line">
                            <input type="password" class="form-control" id="password" name="password" minlength="6" placeholder="Password" required>
                        </div>
                    </div>
                    <div class="input-group">
                        <span class="input-group-addon">
                            <i class="material-icons">lock</i>
                        </span>
                        <div class="form-line">
                            <input type="password" class="form-control" id="confirm_password" name="confirm" minlength="6" placeholder="Confirm Password" required>
                        </div>
                    </div>					

                    <button class="btn btn-block btn-lg bg-pink waves-effect create_pass" id="<?php echo $uid ?>" type="button">CREATE PASSWORD</button>

                    <div class="row m-t-20 m-b--5 align-center">
                        <a href="sign-in.html">Sign In!</a>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <!-- Jquery Core Js -->
	<script src="assets/js/jquery-2.0.0.js"></script>

    <!-- Bootstrap Core Js -->
    <script src="admin/plugins/bootstrap/js/bootstrap.js"></script>
	<!-- E-Heritage javascript -->
	<script src="assets/js/eheritage.js"></script> 
    <!-- Waves Effect Plugin Js -->
    <script src="admin/plugins/node-waves/waves.js"></script>

    <!-- Validation Plugin Js -->
    <script src="admin/plugins/jquery-validation/jquery.validate.js"></script>

    <!-- Custom Js -->
    <script src="admin/js/admin.js"></script>
	<script src="assets/js/jquery-migrate-1.1.1.js"></script>
<script type="text/javascript">
	$(document).ready(function(){

	});
</script> 
</body>

</html>
<?php
	}
?>	