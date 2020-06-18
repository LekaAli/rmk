<?php
include("../includes/connect.php");
include("../includes/functions.php");
$heritage = new eheritage_class();
session_start();
$session = $heritage->loadUserSession($con,$_SESSION['id']);
$exp = $heritage->updateAuditSession($con,$session['id'],'logout');
if($exp > 0)
{
	unset($_SESSION['id']);
	session_destroy();
	header("location:".ROOT_PATH."admin/sign-in.php");
}
?>