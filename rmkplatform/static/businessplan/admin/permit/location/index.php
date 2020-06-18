<?php
include_once 'dbconfig.php';
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>Dynamic Dependent Select Box using jQuery and PHP</title>
<script type="text/javascript" src="jquery-1.4.1.min.js"></script>
<script type="text/javascript">
$(document).ready(function()
{

	$("#loding1").hide();
	$("#loding2").hide();
	//$(".country").change(function()
	//{
		$("#loding1").show();
		var id=1;
		var dataString = 'id='+ id;
		$(".state").find('option').remove();
		$(".city").find('option').remove();
		$.ajax
		({
			type: "POST",
			url: "get_state.php",
			data: dataString,
			cache: false,
			success: function(html)
			{
				$("#loding1").hide();
				$(".state").html(html);
			} 
		});
	//});
	
	
	$(".state").change(function()
	{
		$("#loding2").show();
		var id=$(this).val();
		var dataString = 'id='+ id;
	
		$.ajax
		({
			type: "POST",
			url: "get_city.php",
			data: dataString,
			cache: false,
			success: function(html)
			{
				$("#loding2").hide();
				$(".city").html(html);
			} 
		});
	});
		
});
</script>
<style>
label
{
font-weight:bold;
padding:10px;
}
div
{
	margin-top:100px;
}
select
{
	width:200px;
	height:35px;
	border:2px solid #456879;
	border-radius:10px;
}

.color {
	color:green;
}

.link {
	color:red;
}
</style>
</head>

<body>
<h1 align="center" class="color"> Daynamic Dropdown in PHP &MySql Ajax And jQuery</h1>
<center>
<div>
<label>Country :</label> 
<select name="country" class="country">
<option selected="selected">--Select Country--</option>
<?php
	$stmt = $DB_con->prepare("SELECT * FROM country");
	$stmt->execute();
	while($row=$stmt->fetch(PDO::FETCH_ASSOC))
	{
		?>
        <option value="<?php echo $row['country_id']; ?>"><?php echo $row['country_name']; ?></option>
        <?php
	} 
?>
</select>
<br><br><br>
<label>State :</label> <select name="state" class="state">
<option selected="selected">--Select State--</option>
</select>
<img src="ajax-loader.gif" id="loding1"></img>
<br><br><br>
<label>City :</label> <select name="city" class="city">
<option selected="selected">--Select City--</option>
</select>
<img src="ajax-loader.gif" id="loding2"></img>
<br><br><br>
</div>
<br />
</center>
<h3 align="center"><a href="" class="link">Click Here For Tutorials</a></h3>
<h3 align="center"><a href="http://www.techsofttutorials.com/" class="link">www.TechsoftTutorials.com</a></h3>
</body>
</html>
