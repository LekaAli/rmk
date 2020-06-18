<?php
	session_start();
	include("connect.php");
	include("functions.php");
	
	$heritage = new eheritage_class();
	$uid = $_SESSION['id'];
	$heritage->setUserSessionExpiry($con,10000,$uid);
	$heritage->checkUserSession($uid);
	$u = $heritage->userbyid($con,$uid);
?>