<?php
	include("../includes/session.php"); //include session file
	$roles = $heritage->userrights($con); //load all user roles
	$usrid = $uid;
	if(isset($_GET['userid']))
		$usrid = base64_decode($_GET['userid']);
	$sel_usr = $heritage->userbyid($con,$usrid);
	$type = $heritage->getrolebyid($con,$sel_usr['usertype']); 
	$usrrole = $type['role'];

	//remove user tab is shown	
	$suspTabName = '<i class="material-icons">delete</i>Remove this user';
	$suspndBtn = "REMOVE";
	if($sel_usr['disabled'] > 0) //but if user is disabled 
	{
		$suspTabName = '<i class="material-icons">launch</i>Restore this user'; //restore user tab is shown
		$suspndBtn = "RESTORE";
	}
?>
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
    <title><?php echo $heritage->nameoftheuser($con,$usrid) ?> | e-Heritage - user profile</title>
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

    <!-- JQuery DataTable Css -->
    <link href="plugins/jquery-datatable/skin/bootstrap/css/dataTables.bootstrap.css" rel="stylesheet">

    <!-- Custom Css -->
    <link href="css/style.css" rel="stylesheet">

    <!-- AdminBSB Themes. You can choose a theme from css/themes instead of get all themes -->
    <link href="css/themes/all-themes.css" rel="stylesheet" />
</head>

<body class="theme-red">
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
                <h2>
                    USER PROFILE
                    <small></small>
                </h2>
            </div>
            <!-- Exportable Table -->
            <div class="row clearfix">
                <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                    <div class="card">
                        <div class="header">
                            <h2>
                                <?php echo $sel_usr['names'] ?>
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
 <div class="row my-2">
        <div class="col-lg-8 order-lg-2">
            <ul class="nav nav-tabs">
                <li class="nav-item">
                    <a href="" data-target="#profile" data-toggle="tab" class="nav-link active"><i class="material-icons">accessibility</i>Activities</a>
                </li>
                <li class="nav-item">
                    <a href="" data-target="#edit" data-toggle="tab" class="nav-link"><i class="material-icons">edit</i>Edit this user</a>
                </li>
                <li class="nav-item">
                    <a href="" data-target="#pass" data-toggle="tab" class="nav-link"><i class="material-icons">lock</i>Password</a>
                </li>
                <li class="nav-item">
                    <a href="" data-target="#messages" data-toggle="tab" class="nav-link"><?php echo $suspTabName ?></a>
                </li>				
            </ul>
            <div class="tab-content py-4">
                <div class="tab-pane active" id="profile">
                    <div class="row">
                        <div class="col-md-12">
                            <h5 class="mt-2"><span class="fa fa-clock-o ion-clock float-right"></span> Recent Activity</h5>
                            <table class="table table-sm table-hover table-striped">
                                <tbody>                                    
                                    <tr>
                                        <td>
                                            <strong>Abby</strong> joined ACME Project Team in <strong>`Collaboration`</strong>
                                        </td>
                                    </tr>
                                 
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <!--/row-->
                </div>
                <div class="tab-pane" id="messages">
					<div class="input-group">
						<div class="form-line">
							<label>Provide Reason to <?php echo $suspndBtn.' '.$sel_usr['names'] ?></label>
							<textarea class="form-control" id="rmreason" placeholder="reason"></textarea>
						</div>
					</div>
                    <button class="btn btn-lg bg-pink waves-effect btndeluser" id="<?php echo $usrid ?>" dir="<?php echo $suspndBtn ?>" type="button"><?php echo $suspndBtn ?></button>					
                </div>
			
                <div class="tab-pane" id="edit">
				<div class="col-lg-8">
                <form id="sign_upform" method="POST"> 
                    <div class="input-group">
                        <span class="input-group-addon"> 
                            <i class="material-icons">person</i>
                        </span>
                        <div class="form-line">
                            <input type="text" class="form-control" value="<?php echo $sel_usr['names'] ?>" name="fnames" placeholder="Name Surname" required autofocus>
                        </div>
                    </div>
                    <div class="input-group">
                        <span class="input-group-addon">
                            <i class="material-icons">email</i>
                        </span>
                        <div class="form-line">
                            <input type="email" class="form-control" value="<?php echo $sel_usr['email'] ?>" name="email" placeholder="Email Address" required>
                        </div>
                    </div>
                    <div class="input-group">
                        <span class="input-group-addon">
                            <i class="material-icons">phone</i>
                        </span>
                        <div class="form-line">
                            <input type="text" class="form-control" value="<?php echo $sel_usr['cell'] ?>" name="cell" placeholder="Cellphone" required>
                        </div>
                    </div>	
                    <div class="input-group">
                        <span class="input-group-addon">
                            <i class="material-icons">accessibility</i>
                        </span>
                        <div class="form-line">
							<select name="usertype" class="form-control" required>
							<?php
								if($usrrole)
									echo '<option value="'.$type['id'].'">'.$usrrole.'</option>';
								else
									echo '<option value="">Type of user</option>';
								foreach($roles as $row)
								{
									if($usrrole != $row['role'])
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
							<input type="text" name="position" value="<?php echo $sel_usr['position'] ?>" class="form-control" placeholder="Position" required>
                        </div>
                    </div>	

                    <button class="btn btn-lg bg-pink waves-effect btnadduser" id="<?php echo $usrid ?>" type="button">SUBMIT</button>
                </form>
				</div>	
                </div>
				<div class="tab-pane" id="pass">
					<button class="btn btn-lg bg-pink btnSendReset" id="<?php echo $usrid ?>">Send Password Reset</button>
				</div>
            </div>
        </div>
        <div class="col-lg-4 order-lg-1 text-center">
            <img src="images/avatar_profile.png" class="mx-auto img-fluid img-circle d-block" alt="avatar">
            <label class="custom-file">
                <input type="file" id="file" style="display:none" class="custom-file-input">
            </label>
							<h4><?php echo $sel_usr['names'] ?></h4>
							<p><?php echo $usrrole ?></p>			
        </div>
    </div>
                        </div>
                    </div>
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
    <!-- Select Plugin Js >
    <script src="plugins/bootstrap-select/js/bootstrap-select.js"></script-->

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

    <!-- Custom Js -->
    <script src="js/admin.js"></script>
    <!-- Validation Plugin Js -->
    <script src="plugins/jquery-validation/jquery.validate.js"></script>

    <!-- Demo Js -->
    <script src="js/demo.js"></script>
	<script src="../assets/js/jquery-migrate-1.1.1.js"></script>
</body>

</html>