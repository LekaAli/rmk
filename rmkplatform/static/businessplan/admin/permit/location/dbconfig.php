<?php

$DB_host = "localhost";
$DB_user = "limpopoeheritage_db";
$DB_pass = "SqXdO7R$CZDB";
$DB_name = "limpopoeheritage_db";

try
{
	$DB_con = new PDO("mysql:host={$DB_host};dbname={$DB_name}",$DB_user,$DB_pass);
	$DB_con->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	echo "success";
}
catch(PDOException $e)
{
	$e->getMessage();
	echo "success";
}