<?php
  	header('Content-type: application/json');
	include("../includes/session.php"); //include session file
	
	/*if(isset($_GET['lost_email']))
		$email = trim(strtolower($_GET['lost_email']));
	else*/
	if(isset($_POST['email']))
	{
		$email = trim(strtolower($_POST['email']));
		$valid = 'true';
		if ($heritage->check_username($con,$email) > 0)
			$valid = 'false';
	}
	echo $valid;
?>