<?php
class eheritage_class 
{
	var $badge;
	//destroy session
	public function setUserSessionExpiry($con,$timeout,$uid)
	{		 
		// Check if the timeout field exists.
		if(isset($_SESSION['timeout'])) {
			// See if the number of seconds since the last
			// visit is larger than the timeout period.
			$duration = time() - (int)$_SESSION['timeout'];
			if($duration > $timeout) {
				// Destroy the session and restart it.
				$session = $this->loadUserSession($con,$uid);
				$exp = $this->updateAuditSession($con,$session['id'],'session_expired');
				 
				if($exp > 0)
				{
					unset($uid);
					session_destroy();
					session_start();
					$_SESSION['url'] = $_SERVER['REQUEST_URI']; // i.e. "about.php"	
					$this->checkUserSession($uid);
				}
			}
		}
		 
		// Update the timout field with the current time.
		$_SESSION['timeout'] = time();			
	}
	//load user's session
	public function loadUserSession($con,$uid)
	{
		$query = mysqli_query($con,"SELECT * FROM eherit_auditSession where uid = '$uid' order by id desc");
		return mysqli_fetch_assoc($query);		
	}		
	//destroy session
	public function checkUserSession($uid)
	{
		if(!$uid)
		{
			
			header('location:'.ROOT_PATH.'admin/sign-in.php');
			exit;		
		}		
	}		
	//load user rights
	public function userrights($con)
	{
		$query = mysqli_query($con,"SELECT * FROM eherit_roles");
		while($row = mysqli_fetch_assoc($query))
			$data[] = $row;
		return $data;	
	}
	//load number users per role
	public function numOfUsersPerRole($con,$typeid)
	{
		$query = mysqli_query($con,"SELECT * FROM eherit_users WHERE usertype = '$typeid'");
		return mysqli_num_rows($query);
	}		
	//insert users into db
	public function insert_user($con,$uid,$fnames,$email,$cell,$usertype,$position,$pwd,$id)
	{
		$date_created = time();
		$pwd = md5($pwd);
		
		//check if user is already registered by id
	  	$query = mysqli_query($con,"SELECT * FROM eherit_users WHERE id = '$id'")or die(mysqli_error());
		if (mysqli_num_rows($query) < 1)
		{		
			//insert user
			$res = mysqli_query($con,"INSERT INTO eherit_users(uid,names,email,cell,usertype,position,pwd,date_added)
			VALUES('$uid','$fnames','$email','$cell','$usertype','$position','$pwd','$date_created')")or die(mysqli_error());	
			//call audit function
			
			if($res)
			{
				$message = "Hi ".$fnames.",<br> You have been added to eheritage System,
					 <br> please click the link below to setup your credentials<br>";
				$message .= '<a href="'.ROOT_PATH."create-password.php?token=".base64_encode($email).'">'.
					ROOT_PATH."create-password.php?token=".base64_encode($email).'</a>';
				$subject = "eHeritage User Registration";	
				
				if($this->sendMail($email,$subject,$message))
					return $this->recAuditTrail($con,$uid,'INSERT','eherit_users','','','','');
			}
	
		}else
		{
			//update user
			$res = mysqli_query($con,"UPDATE eherit_users SET uid = '$uid',names = '$fnames',email = '$email',cell = '$cell',usertype = '$usertype',position = '$position' where id = '$id'")or die(mysqli_error());
			
			//call audit function
			$rwOld = mysqli_fetch_assoc($query);
			$recid = $rwOld['id'];
			if($res)
			{
				if($fnames  != $rwOld['names'])
					$audit = $this->recAuditTrail($con,$uid,'UPDATE','eherit_users','names',$recid,$fnames,$rwOld['names']);
				else if($email  != $rwOld['email'])
					$audit = $this->recAuditTrail($con,$uid,'UPDATE','eherit_users','email',$recid,$email,$rwOld['email']);
				else if($cell  != $rwOld['cell'])
					$audit = $this->recAuditTrail($con,$uid,'UPDATE','eherit_users','cell',$recid,$cell,$rwOld['cell']);
				else if($usertype  != $rwOld['usertype'])
					$audit = $this->recAuditTrail($con,$uid,'UPDATE','eherit_users','role',$recid,$usertype,$rwOld['usertype']);	
				else if($position  != $rwOld['position'])
					$audit = $this->recAuditTrail($con,$uid,'UPDATE','eherit_users','position',$recid,$position,$rwOld['position']);

				return $audit;	
			}							
		}
	}
	//check if user exists
	public function checkUserComplete($con,$email)
	{
		$query = mysqli_query($con,"SELECT * FROM eherit_users WHERE email = '$email' and complete = 0");
		return mysqli_num_rows($query);		
	}	
	//check if user exists
	public function check_username($con,$email)
	{
		$query = mysqli_query($con,"SELECT * FROM eherit_users WHERE email = '$email'");
		return mysqli_num_rows($query);		
	}	
	//check if coordinates exists
	public function checkSiteCoordinates($con,$lat,$long)
	{
		$query = mysqli_query($con,"SELECT * FROM eherit_mapmarkers WHERE latitude = '$lat' and longitude = '$long'");
		return mysqli_num_rows($query);		
	}	
	//check if coordinates exists
	public function checkSiteById($con,$id)
	{
		$query = mysqli_query($con,"SELECT * FROM eherit_mapmarkers WHERE id = '$id'");
		return mysqli_num_rows($query);		
	}	
	//load user by email
	public function userByEmail($con,$email)
	{
		$query = mysqli_query($con,"SELECT * FROM eherit_users WHERE email = '$email'");
		return mysqli_fetch_assoc($query);		
	}
	//Add Password to the user
	public function UpdatePass($con,$pass,$uid) 
	{
		$pass = md5($pass);
		return mysqli_query($con,"UPDATE eherit_users SET pwd = '$pass',complete = 1 where id = '$uid' and disabled = 0")or die(mysqli_error());			
	}	
	//Send Password reset link
	public function sendResetPass($con,$uid) 
	{
		$u = $this->userbyid($con,$uid);	
		$email = $u['email'];

		$message = "Hi,<br>please click the link below to reset your password<br>";
		$message .= '<a href="'.ROOT_PATH."create-password.php?token=".base64_encode($email).'">'.
				ROOT_PATH."create-password.php?token=".base64_encode($email).'</a>';			
			
		$subject = "e-Heritage Password Reset";
		//return $this->sendMail($email,$subject,$message);	
		if($this->sendMail($email,$subject,$message))
			return mysqli_query($con,"UPDATE eherit_users SET complete = 0 where id = '$uid' and disabled = 0")or die(mysqli_error());					
	}	 
	//load users 
	public function users($con)
	{
		$query = mysqli_query($con,"SELECT * FROM eherit_users");
		while($row = mysqli_fetch_assoc($query))
			$data[] = $row;
		return $data;	
	}	
	//load user by id
	public function userbyid($con,$id)
	{
		$query = mysqli_query($con,"SELECT * FROM eherit_users where id = '$id'");
		return mysqli_fetch_assoc($query);
	}
	
	public function getrolebyid($con,$id)
	{
		$query = mysqli_query($con,"SELECT * FROM eherit_roles where id = '$id'");
		return mysqli_fetch_assoc($query);
	}
	//current user's role
	public function loaduserRole($con,$id)
	{
		$u = $this->userbyid($con,$id);
		$type = $this->getrolebyid($con,$u['usertype']); 
		return $type['role'];
	}
	//ger user's name
	public function nameoftheuser($con,$id)
	{
		$u = $this->userbyid($con,$id);
		return $u['names'];
	}
	//delete user
	public function deleteuser($con,$id,$uid,$action)
	{
		$num = 0;
		$status = "RESTORE";
		if ($action == "REMOVE")
		{
			$num = 1;
			$status = "DELETE";	
		}
		
		$res = mysqli_query($con,"UPDATE eherit_users SET disabled = '$num' where id = '$id'");
		if($res > 0)
			return $this->recAuditTrail($con,$uid,$status,'eherit_users','',$id,'','');
	}
	//insert delete record
	public function insDeleteRecord($con,$id,$uid,$reason)
	{
		$curr_date = time();
		//insert query
		return mysqli_query($con,"INSERT INTO eherit_trash(fkid,uid,reason,date)
			VALUES('$id',$uid,'$reason','$curr_date')")or die(mysqli_error());
	}		
	//check valid login
	public function check_validLogin($con,$email,$password)
	{
		$query = mysqli_query($con,"select * from eherit_users where email = '".$email."' and pwd = '".$password."' and disabled = 0")
		or die(mysqli_error());
		return mysqli_num_rows($query);		
	}
	
	//load user
	public function load_userbyemail($con,$email)
	{
		$query = mysqli_query($con,"SELECT * FROM eherit_users WHERE email = '$email'");
		return mysqli_fetch_array($query);		
	}	
	//load system functions
	public function load_functions($con)
	{
		$query = mysqli_query($con,"SELECT * FROM eherit_functions");
		while($row = mysqli_fetch_assoc($query))
			$data[] = $row;
		return $data;	
	}	
	//load system functions
	public function funcbyid($con,$id)
	{
		$query = mysqli_query($con,"SELECT * FROM eherit_functions where id = '$id'");
		return mysqli_fetch_assoc($query);
	}	
	//load rights by roleid
	public function rightsbyroleid($con,$id)
	{
		$query = mysqli_query($con,"SELECT * FROM eherit_rights where roleid = '$id'");
		while($row = mysqli_fetch_assoc($query))
			$data[] = $row;
		if(isset($data))
		return $data;	
	}		
	public function rightsbyrolefuncid($con,$fid,$roleid)
	{
		$query = mysqli_query($con,"SELECT * FROM eherit_rights where roleid = '$roleid' and funcid = '$fid'");
		return mysqli_fetch_assoc($query);		
	}
//custom rights	
	public function customRights($con,$fid,$rid,$action,$uid)
	{
		if($action == 'add')
		{
			$res = mysqli_query($con,"INSERT INTO eherit_rights(roleid,funcid)
			VALUES('$rid','$fid')")or die(mysqli_error());	
			if($res > 0)
				return $this->recAuditTrail($con,$uid,'INSERT','eherit_rights','privilege',$rid,$fid,'');			
		}
		else if($action == 'rem')
		{
			$res = mysqli_query($con,"DELETE FROM eherit_rights WHERE roleid = '$rid' and funcid = '$fid'");
			if($res > 0)
				return $this->recAuditTrail($con,$uid,'DELETE','eherit_rights','privilege',$rid,$fid,'');				
		}
	}
//insert site
	public function insertMapMarker($con,$uid,$title,$address,$filename,$lat,$long,$id)
	{	
		$address = mysqli_real_escape_string($con,$address);
		if($this->checkSiteCoordinates($con,$lat,$long) > 0)
			return false;
		else
		{
			if($this->checkSiteById($con,$id) > 0)
			{
				return mysqli_query($con,"UPDATE eherit_mapmarkers SET name = '$title', address = '$address', latitude = '$lat', longitude = '$long' WHERE id = '$id'")or die(mysqli_error());
			}else
			{
				return mysqli_query($con,"INSERT INTO eherit_mapmarkers(name,address,img,latitude,longitude) 
					VALUES('$title','$address','$filename','$lat','$long')")or die(mysqli_error());	
				/*if($res > 0)
				{
					$last_id = mysqli_insert_id($con);
					return $this->recAuditTrail($con,$uid,'INSERT','eherit_mapmarkers','',$last_id,'','');
				}*/
			}			
		}			
	}		
//load map markers
	public function getMapMarkers($con)
	{	
		$query = mysqli_query($con,"SELECT * FROM eherit_mapmarkers");
		while($row = mysqli_fetch_assoc($query))
			$data[] = $row;
		return $data;					
	}	
//load map marker by id
	public function getMapMarkerById($con,$id)
	{	
		$query = mysqli_query($con,"SELECT * FROM eherit_mapmarkers where id = '$id'");
		return mysqli_fetch_assoc($query);					
	}	

//record audit session	
	public function recAuditSession($con,$uid)	
	{	
		$auditTime = time();
		return mysqli_query($con,"INSERT INTO eherit_auditSession(uid,timeIn) 
			VALUES('$uid','$auditTime')")or die(mysqli_error());			
	}
//update audit session	
	public function updateAuditSession($con,$id,$action)	
	{	
		$auditTime = time();
		return mysqli_query($con,"UPDATE eherit_auditSession SET timeOut = '$auditTime', timeOutAction = '$action'
			WHERE id = '$id'")or die(mysqli_error());			
	}
//load audit trail
	public function getAllSession($con) 
	{	
		$query = mysqli_query($con,"SELECT * FROM eherit_auditSession order by timeIn desc");
		while($row = mysqli_fetch_assoc($query))
			$data[] = $row;
		return $data;					
	}		
//record audit trail	
	public function recAuditTrail($con,$uid,$action,$tblname,$fieldname,$recid,$new,$old)
	{	
		$auditTime = time();
		return mysqli_query($con,"INSERT INTO eherit_audit(uid,action,tablename,fieldname,recordid,oldvalue,newvalue,audittime)
			VALUES('$uid','$action','$tblname','$fieldname','$recid','$old','$new','$auditTime')")or die(mysqli_error());			
	}	
//load audit trail
	public function getAllAudit($con)
	{	
		$query = mysqli_query($con,"SELECT * FROM eherit_audit");
		while($row = mysqli_fetch_assoc($query))
			$data[] = $row;
		return $data;					
	}	
	//send email
	public function sendMail($email,$subject,$message)
	{	
		$from = 'From: Support <limpopoeheritage@limeheritage.co.za>' . "\r\n";
	// boundary
		$semi_rand = md5(time());
		$mime_boundary = "==Multipart_Boundary_x{$semi_rand}x";	

		$headers =  'MIME-Version: 1.0' . "\r\n";  
		$headers .= $from;
				  
		$headers .= "Content-Type: multipart/mixed;\r\n" . " boundary=\"{$mime_boundary}\"";		
		
			// multipart boundary
		$message = "This is a multi-part message in MIME format.\n\n" . "--{$mime_boundary}\n" . 
		"Content-Type: text/html; charset=\"iso-8859-1\"\n" . "Content-Transfer-Encoding: 7bit\n\n" . $message . "\n\n";
		
		return mail($email,$subject,$message,$headers);	
	}	
//user status
	public function userStatus($complete,$disabled)
	{	
		if($disabled > 0)
		{
			$status = "Suspended";
			$badge = "bg-pink";
		}
		else
		{
			if($complete > 0)
			{
				$status = "Active";
				$badge = "bg-green";
			}
			else
			{
				$status = "Incomplete Registration";
				$badge = "bg-teal";
			}
		}	
		$this->badge = $badge;
		return $status;	
	} 
	//badge info 
	public function badgeStatus()
	{
		return $this->badge;
	}	

	//===========================================start permits=============================
	//insert permit application
	public function insertPermitApplication($con,$uid,$req,$stateId,$cityId,$streetName,$code,$subject,$message)
	{
		$date = time();
		if(!$this->checkPermitExist($con,$uid,$req,$streetName) > 0)
		{
			$res = mysqli_query($con,"INSERT INTO eherit_permits (uid,request,address,stateid,cityid,code,subject,Description,date)
				VALUES('$uid','$req','$streetName','$stateId','$cityId','$code','$subject','$message','$date')");// or die mysql_error();	
			if($res > 0)
			{
				$last_id = mysqli_insert_id($con);
				return $this->insertPermitProcess($con,$last_id,$date);	
			}
		}				
	}
	//insert permit process
	public function insertPermitProcess($con,$last_id,$date)
	{			
		return mysqli_query($con,"INSERT INTO eherit_permitProcess (permit_id,receiving,receiveTime)
				VALUES('$last_id','1','$date')");// or die mysql_error();			
	}	
	public function insertFiles($con,$last_id,$filename,$filetype,$filetype)
	{
		return mysqli_query($con,"INSERT INTO eherit_files (fk_tid,fname,ftype,fsize)
						VALUES('$last_id','$filename','$filetype','$filetype')")or die(mysqli_error());			
	}	
	//check permit process
	public function checkPermitExist($con,$uid,$req,$streetName)
	{
		$query = mysqli_query($con,"SELECT * FROM eherit_permits where uid = '$uid' and request = '$req' and address = '$streetName'");
		return mysqli_num_rows($query);
	}		
	//load permits
	public function getPermits($con)
	{
		$query = mysqli_query($con,"SELECT * FROM eherit_permits");
		while($row = mysqli_fetch_assoc($query))
			$data[] = $row;
		return $data;		
	}	
	//check permit process
	public function checkPermitProcess($con,$id)
	{
		$query = mysqli_query($con,"SELECT * FROM eherit_permitProcess where permit_id = '$id'");
		return mysqli_num_rows($query);
	}	
	//check permit process
	public function permitStatus($con,$id,$status)
	{			
		$query = mysqli_query($con,"SELECT * FROM eherit_permitProcess where permit_id = '$id' and $status = 1");
		return mysqli_num_rows($query);
	}
	//check permit process
	public function numOfActiveStatus($con,$id)
	{
		$i=0;
		foreach($this->permitStages() as $row)
		{	
			if ($this->permitStatus($con,$id,$row) > 0)
				$i++;
		}	
		return $i;
	}	
	public function getPermitById($con,$id)
	{
		$query = mysqli_query($con,"SELECT * FROM eherit_permits where id = '$id'");
		return mysqli_fetch_assoc($query);		
	}	
	public function permitStages()
	{
		return array("receiving","Assessment","Feedback","capturing","closing");
	}
	public function getStageTime($stage)
	{
		if($stage == 'Assessment')
			$stageTime = 'assessTime';
		else if($stage == 'Feedback')
			$stageTime = 'feedbackTime';
		else if($stage == 'capturing')
			$stageTime = 'captureTime';	
		else if($stage == 'closing')
			$stageTime = 'closeTime';	
		else if($stage == 'rejected')
			$stageTime ='rejectTime';
		else
			$stageTime = 'receiveTime';
		
		return $stageTime;
	}
	public function nextStage($con,$id,$stage)
	{
		$currTime = time();
		$stageTime = $this->getStageTime($stage);
		
		return mysqli_query($con,"UPDATE eherit_permitProcess SET $stage = 1, $stageTime = '$currTime'
			WHERE permit_id = '$id'")or die(mysqli_error());		
	}
	public function addPermComment($con,$id,$stage,$comm)
	{
		$comm = mysqli_real_escape_string($con,$comm);
		$currTime = time();
		$res = mysqli_query($con,"INSERT INTO eherit_permComment(pid,status,comment,date)
			VALUES('$id','$stage','$comm','$currTime')")or die(mysqli_error());
		if($res > 0)
		{		
			if($stage == 'rejected')
				return $this->nextStage($con,$id,$stage);
			else
				return $res;
		}		
	}
	public function loadPermComment($con,$id,$stage)
	{
		$query = mysqli_query($con,"SELECT * FROM eherit_permComment where pid = '$id' and status = '$stage'");
		while($row = mysqli_fetch_assoc($query))
			$data[] = $row;
		return $data;			
	}			
	//===========================================end permits=============================
	
	public function getCity($con,$id)
	{
		$query = mysqli_query($con,"SELECT * FROM city WHERE state_id = '$id'");
		while($row = mysqli_fetch_assoc($query))
			$data[] = $row;
		return $data;		
	}		
	//send reg verification via email
	public function reg_verification($email,$names,$root)
	{
		$subject = "Account Creation to ".$email;
		$message = 'Hi '.$names.'<br>Thank you for registering.<br>this email was sent
		to confirm your email address<br>
		Click the link below for confirmation<br>'.$root.'email_confirmation.php?token='.base64_encode($email);
		$this->sendMail($email,$subject,$message);	
	}	
	
	


	//check verification code
	public function checkVerificationCode($email,$code)
	{
		$query = mysql_query("SELECT * FROM verificationcode WHERE v_email = '$email' and v_code = '$code'");
		return mysql_num_rows($query);			
	}
	//delete verification code
	public function deleteVerificationCode($email,$code)
	{
		return mysql_query("DELETE FROM verificationcode WHERE v_email = '$email' and v_code = '$code'");	
	}	
	public function tlds()
	{
		$arrtlds = array(".co.za" => "80",".com" => "125",".org" => "199"); 
		return $arrtlds;	
	}		
}
?>	