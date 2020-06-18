<?php
	include("../includes/session.php"); //include session file
	$auditSessions = $heritage->getAllSession($con); //call users sessions function
	$auditTrail = $heritage->getAllAudit($con); //call audit trail function
	$arrActions = array("Session","Insert","Update","Delete");
?>
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
    <title>Audit Trail | Limpopo e-Heritage</title>
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
    <!-- Bootstrap Select Css -->
    <link href="plugins/bootstrap-select/css/bootstrap-select.css" rel="stylesheet" />
    <!-- Custom Css -->
    <link href="css/style.css" rel="stylesheet">

    <!-- AdminBSB Themes. You can choose a theme from css/themes instead of get all themes -->
    <link href="css/themes/all-themes.css" rel="stylesheet" />
	<style>
		.select_user
		{
			cursor:pointer;
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
                    AUDIT TRAIL
                    <small></small>
                </h2>
            </div>
            <!-- Exportable Table -->
            <div class="row clearfix">
                <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                    <div class="card">
                        <div class="header">
						<div class="row">
							<div class="col-lg-4">
                            <h2>
                                AUDIT TRAIL
                            </h2>
							</div>
							<div class="col-lg-6">
							  <select class="form-control show-tick" id="per_status">
								<?php
								foreach($arrActions as $row)
								{
									?>
										<option value="<?php echo $row ?>"><?php echo strtoupper($row) ?></option>
									<?php
								}
								?>
							  </select>
							</div>	
							<div class="col-lg-2">
								<button type="button" class="btn btn-default pull-right daterange-btn1">
									<span>
									  <i class="material-icons">date_range</i>
									</span>
								</button>
							</div>
						</div>	
                        </div>
                        <div class="body">
                            <div class="table-responsive" id="tblSession" style="display:none">
                                <table class="table table-bordegreen table-striped table-hover dataTable js-basic-example">
                                    <thead>
                                        <tr>
                                            <th>Name</th>
                                            <th>Date</th>
											<th>Time In</th>
											<th>Time Out</th>
											<th>Session Out Action</th>	
                                        </tr>
                                    </thead>
                                    <tbody>
										<?php
											foreach($auditSessions as $row)
											{
												$id = $row['id'];
												$usr = $heritage->userbyid($con,$row['uid']);									
												?>
												<tr>
													<td><?php echo $usr['names'] ?></td>
													<td><?php echo date('M d,Y',$row['timeIn']) ?></td>
													<td><?php echo date('h:i:s',$row['timeIn']) ?></td>
													<td><?php if($row['timeOut'] > 0)echo date('h:i:s',$row['timeOut']) ?></td>
													<td><?php echo $row['timeOutAction'] ?></td>
												</tr>												
												<?php
											}
										?>

                                    </tbody>
                                </table>
							</div>
							<div class="table-responsive" id="tblTrail" >
                                <table class="table table-bordegreen table-striped table-hover dataTable js-exportable">
                                    <thead>
                                        <tr>
                                            <th>Date</th>
											<th>Action</th>
											<th>Form</th>
											<th>Field Name</th>	
											<th>Affected</th>	
											<th>New Value</th>	
											<th>Old Value</th>	
                                        </tr>
                                    </thead>
                                    <tbody>
										<?php
											foreach($auditTrail as $row)
											{
												$id = $row['id'];
												$affectedRow = $newval = $oldval = "";
												 
												$usr = $heritage->userbyid($con,$row['uid']);	
												if($row['tablename'] == "eherit_rights")
												{
													$newval = $heritage->funcbyid($con,$row['newvalue'])['functions'];	
													if($row['fieldname'] == 'privilege')
													{
														$affectedRow = $heritage->getrolebyid($con,$row['recordid'])['role'];
													}
														
												}
												else if($row['tablename'] == "eherit_users")
												{			
													if($row['fieldname'] == 'role')
													{
														$newval = $heritage->getrolebyid($con,$row['newvalue'])['role'];
														$oldval = $heritage->getrolebyid($con,$row['oldvalue'])['role'];
														$affectedRow = $heritage->userbyid($con,$row['recordid'])['names'];
													}
													else
													{
														$newval = $row['newvalue'];
														$oldval = $row['oldvalue'];
														$affectedRow = $heritage->userbyid($con,$row['recordid'])['names'];
													}
												}
												else if($row['tablename'] == "eherit_mapmarkers")
												{
													$affectedRow = $heritage->getMapMarkerById($con,$row['recordid'])['name'];
												}
												?>
												<tr title="<?php echo $usr['names'] ?>">
													<td><?php echo date('M d,Y',$row['audittime']) ?></td>
													<td><?php echo $row['action'] ?></td>
													<td><?php echo str_replace("eherit_","",$row['tablename']); ?></td>
													<td><?php echo $row['fieldname'] ?></td>
													<td><?php echo $affectedRow ?></td>
													<td><?php echo $newval ?></td>
													<td><?php echo $oldval ?></td>
												</tr>												 
												<?php
											}
										?>

                                    </tbody>
                                </table>								
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

    <!-- Custom Js -->
    <script src="js/admin.js"></script>
    <script src="js/pages/tables/jquery-datatable.js"></script>

    <!-- Demo Js -->
    <script src="js/demo.js"></script>
	<script src="../assets/js/jquery-migrate-1.1.1.js"></script>
</body>

</html>