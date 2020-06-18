<?php
	include("../includes/session.php"); //include session file
	$id = $_GET['mapid'];
	$map = $heritage->getMapMarkerById($con,$id);	
?>
<form id="addSiteFrm" method="post">
                            <div class="row clearfix">
                                <div class="col-md-10">
                                    <div class="input-group">
                                        <span class="input-group-addon">
                                            <i class="material-icons">title</i>
                                        </span>
                                        <div class="form-line">
                                            <input type="text" class="form-control" value="<?php echo $map['name'] ?>" placeholder="Site Name" name="title" required>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-10">
                                    <div class="input-group">
                                        <span class="input-group-addon">
                                            <i class="material-icons">location_on</i>
                                        </span>									
                                        <div class="form-line">
                                            <input type="text" class="form-control" value="<?php echo $map['address'] ?>"  placeholder="Address" name="address" required>
                                        </div>
                                    </div>
                                </div>								
                            </div>
                            <h2 class="card-inside-title">Coordinates</h2>
                            <div class="row clearfix">
                                <div class="col-md-5">
                                    <div class="input-group">
                                        <span class="input-group-addon">
                                            <i class="material-icons"></i>
                                        </span>
                                        <div class="form-line">
                                            <input type="text" class="form-control" value="<?php echo $map['latitude'] ?>" placeholder="Latitude" name="lat" required>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-5">
                                    <div class="input-group">
                                        <span class="input-group-addon">
                                            <i class="material-icons"></i>
                                        </span>
                                        <div class="form-line">
                                            <input type="text" class="form-control" value="<?php echo $map['longitude'] ?>"  placeholder="Longitude" name="long" required>
                                        </div>
                                    </div>
                                </div>
								<div class="col-md-5">
									<button type="button" id="<?php echo $id ?>" class="btn btn-success btn-block btnAddSite">UPDATE</button>
								</div>	
								<div class="col-md-5">
									<button type="button" data-toggle="modal" data-target="#defaultModal" id="<?php echo $id ?>" class="btn btn-info btn-block btnAddSite">SITE CONTENT</button>
								</div>									
                            </div>
</form>	

						