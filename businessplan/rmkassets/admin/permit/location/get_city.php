<?php
	include("../../includes/connect.php");
	include("../../includes/functions.php");
	$heritage = new eheritage_class();
	
if($_POST['id'])
{
	$id=$_POST['id'];
	$stmt = $heritage->getCity($con,$id);
	
	?>
	<select name="city" class="form-control contact-control" required data-error="Please Select City">
	<option selected="selected" value="">Select City :</option>
	<?php foreach($stmt as $row)
	{
		?>
		<option value="<?php echo $row['city_id']; ?>"><?php echo $row['city_name']; ?></option>
		<?php
	}
	?>
	</select>
	<div class="help-block with-errors"></div>
	<?php
}
?>