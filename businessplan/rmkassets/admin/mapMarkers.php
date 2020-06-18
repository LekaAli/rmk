<?php
	include("includes/connect.php");
	include("includes/functions.php");
	header("Content-type: application/json");
	
	$heritage = new eheritage_class();
		
	$maps = $heritage->getMapMarkers($con);

	$data = array();
	foreach($maps as $row)
	{
		//{lat: -23.9075257, lng: 29.45363759999998}
		$data[] = $row;//"{lat: ".$row['latitude'].", lng: ".$row['longitude']."}";
	}
	/*echo "<pre>";
		print_r($data);
	echo "</pre>";*/	
	echo json_encode($data);
?>