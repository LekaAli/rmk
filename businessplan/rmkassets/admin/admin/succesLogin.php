<?php
	session_start();
	if(isset($_SESSION['url'])) 
	   $url = $_SESSION['url']; // holds url for last page visited.
	else 
	   $url = "http://164.160.91.13/~limpopoeheritage/admin/"; // default page for 

	header("Location: ".$url); // perform correct redirect.
?>