<?php
	include("session.php"); //include session page
	
	if(isset($_POST['fnames']))
	{
		$fnames = $_POST['fnames'];
		$email = $_POST['email'];
		$cell = $_POST['cell'];
		$usertype = $_POST['usertype'];	
		$position = $_POST['position'];	
		$id="";
		if(isset($_POST['usid']))
			$id = $_POST['usid'];	
		$pwd = "";
		if(isset($_POST['pwd1']))
			$pwd = $_POST['pwd1'];
		
		//call insert function and add parameters
		echo $heritage->insert_user($con,$uid,$fnames,$email,$cell,$usertype,$position,$pwd,$id);
	}	
	else if (isset($_GET['delid']))
	{
		$id = $_GET['delid'];
		$reason = $_GET['delreason'];
		$result = $heritage->deleteuser($con,$id,$uid,$_GET['suspAction']);
		if ($result > 0)
			echo $heritage->insDeleteRecord($con,$id,$uid,$reason);	
	}	
	else if (isset($_GET['roleid']))
	{
		$roleid = $_GET['roleid'];
		$functions = $heritage->load_functions($con);
		$Rights = $heritage->rightsbyroleid($con,$roleid);
		$r = $d = array();
		if(is_array($Rights))
		{
			foreach($Rights as $row)
				$r[] = $row['funcid'];	
		}			
				
		foreach($functions as $row)
			$d[] = $row['id'];
				
		$result=array_diff($d,$r);

		?>
		<div class="row">
			<div class="col-xs-5">
				<label>In-Active functions</label>
				<select class="form-control" id="inactivePnl" onchange="enableBtn('add_field',this)" size="5" style="height:300px;">
				<?php
				$r = $d = array();
				if(is_array($result))
				{
					foreach($result as $row)
					{					
						$id = $row;
						
						$r = $heritage->funcbyid($con,$id);
						echo '<option id="'.$id.'" value="'.$r['functions'].'">'.$r['functions'].'</option>';
					}
				}
				?>
				</select>
			</div>
			<div class="col-xs-2" >
				<div class="form-group" style="padding-top:7em">
					<button class="btn btn-warning add_field" style="width:100%;" disabled id="<?php echo $roleid ?>">&gt;&gt;</button>
				</div>
				<div class="form-group">
					<button class="btn btn-warning rem_field" style="width:100%;" disabled id="<?php echo $roleid ?>">&lt;&lt;</button>
				</div>				
			</div>
			<div class="col-xs-5">
				<label>Active functions</label>
				<select size="5" class="form-control" onchange="enableBtn('rem_field',this)" id="activePnl" style="height:300px;">
				<?php
				
				if(is_array($Rights))
				{					
					foreach($Rights as $row)
					{
						$id = $row['funcid'];
						
						$r = $heritage->funcbyid($con,$id);
						echo '<option id="'.$id.'" value="'.$r['functions'].'">'.$r['functions'].'</option>';
					}
				}
				?>
				</select>
			</div>			
		</div>			
		<?php
	}
	else if(isset($_GET['addfield']))
	{
		$fid = $_GET['addfield'];
		$rid = $_GET['rid'];
		$heritage->customRights($con,$fid,$rid,'add',$uid);
	}
	else if(isset($_GET['remfield']))
	{
		$fid = $_GET['remfield'];
		$rid = $_GET['rid'];
		$heritage->customRights($con,$fid,$rid,'rem',$uid);
	}
	else if(isset($_GET['resetid']))
	{
		echo $heritage->sendResetPass($con,$_GET['resetid']);
	}
	else if(isset($_POST['title']))
	{
		echo $_FILES['upldFile']['name'];
	/*	$id="";
		if(isset($_POST['siteid']))
			$id = $_POST['siteid'];	
		
		echo $heritage->insertMapMarker($con,$uid,$_POST['title'],$_POST['address'],$_POST['lat'],$_POST['long'],$id);*/
	}	
	else if(isset($_GET['perm_id']))
	{
		echo $heritage->nextStage($con,$_GET['perm_id'],$_GET['stage']);
	}
	else if(isset($_GET['pstage']))
	{
		echo $heritage->addPermComment($con,$_GET['commId'],$_GET['pstage'],$_GET['comm']);
	}
?>