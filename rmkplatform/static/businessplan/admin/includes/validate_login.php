<?php
	include("connect.php");
	include("functions.php");
	
	$heritage = new eheritage_class();	
	//login validations
	if (isset($_POST['uname']))
	{
		$email = $_POST['uname'];
		$password = $_POST['password'];
		$password = md5($password);

		$valid = $heritage->check_validLogin($con,$email,$password);
		if ($valid > 0)
		{		
			$u = $heritage->load_userbyemail($con,$email);
			if($u['complete'] > 0)
			{
				session_start();
				$_SESSION['id'] = $u['id'];	
					
				echo $heritage->recAuditSession($con,$_SESSION['id']);
			}	
			else
				echo 'not ver';
		}
		else{
			echo $valid;
		}
	}
	else if (isset($_GET['pass']))
	{	 
		echo $heritage->UpdatePass($con,$_GET['pass'],$_GET['uid']);	
	}
	else if(isset($_POST['selreq']))
	{	
		$uid = 55;	

		$req = $_POST['selreq'];
		$stateId = $_POST['state'];	
		$cityId = $_POST['city'];
		$streetName =$_POST['streetName'];
		$code = $_POST['code'];
		$subject =$_POST['subject'];	
		$message =$_POST['message'];	
		$numfiles =$_POST['numfiles'];
		
		$status = "Pending";

		$uploaddir = $_SERVER['DOCUMENT_ROOT'].'/admin/user_forms/';

		$sub_ticket = $heritage->insertPermitApplication($con,$uid,$req,$stateId,$cityId,$streetName,$code,$subject,$message);	
		if($sub_ticket)
		{
			$result = $sub_ticket;
			$last_id = mysqli_insert_id($con);

			for($i = 1; $i <= $numfiles; $i++)
			{
				$filename = basename($_FILES['suppot_docs'.$i]['name']);
				$filetype = basename($_FILES['suppot_docs'.$i]['type']);
				$filesize = basename($_FILES['suppot_docs'.$i]['size']);
				
				if($filename)
				{
					$heritage->insertFiles($con,$last_id,$filename,$filetype,$filetype);	
					$uploadfile = $uploaddir . $last_id.'-'.$filename;
						
					if (move_uploaded_file($_FILES['suppot_docs'.$i]['tmp_name'], $uploadfile)) {
						$result = 1;
					}
				}
					//echo 'Here is some more debugging info:';
					//print_r($_FILES); 
			}
		}
		

		echo $result;
		

	}		

?>