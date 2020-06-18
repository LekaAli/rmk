								<div class="row">
									<div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
											<div class="card">
												<div class="header">
													<h2 class="text-md-left">
														Assessment Process
													</h2>
													<ul class="header-dropdown m-r--5">
														<li class="dropdown">
															<a href="javascript:void(0);" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
																<i class="material-icons">more_vert</i>
															</a>
															<ul class="dropdown-menu pull-right">
																<li><a href="javascript:void(0);">Action</a></li>
																<li><a href="javascript:void(0);">Another action</a></li>
																<li><a href="javascript:void(0);">Something else here</a></li>
															</ul>
														</li>
													</ul>
												</div>
												<div class="body">
<div class="row">
    <div class="col-xs-12 ol-sm-12 col-md-12 col-lg-12">
        <span>COMMENTS</span>
		<?php $comments = $heritage->loadPermComment($con,$p_id,'Assessment'); 
			$count = count($comments);	
		?>
        <div class="panel-group" id="accordion_1" role="tablist" aria-multiselectable="true">
	<?php 
	
	$i = 1;	
	foreach($comments as $com)
	{
		$in = "";
		if($i == $count)
			$in = 'in';
		?>
                                        <div class="panel panel-default">
                                            <div class="panel-heading" role="tab" id="heading<?php echo $i ?>_1">
                                                <h4 class="panel-title">
                                                    <a class="collapsed" role="button" data-toggle="collapse" data-parent="#accordion_1" href="#collapse<?php echo $i ?>_1" aria-expanded="false"
                                                       aria-controls="collapse<?php echo $i ?>_1">
                                                        <?php echo date('Y M d',$com['date']) ?>
                                                    </a>
                                                </h4>
                                            </div>
                                            <div id="collapse<?php echo $i ?>_1" class="panel-collapse collapse <?php echo $in ?>" role="tabpanel" aria-labelledby="heading<?php echo $i ?>_1">
                                                <div class="panel-body">
                                                    <?php echo $com['comment'] ?>.
                                                </div>
                                            </div>
                                        </div>		
		<?php
		$i++;
	}
	if(!$heritage->permitStatus($con,$p_id,'Feedback') > 0)
	{		
	?>
            <div class="panel panel-default">
                <div class="panel-heading" role="tab" id="headingTwo_1">
                    <h4 class="panel-title">
						<a role="button" data-toggle="collapse" data-parent="#accordion_1" href="#collapseTwo_1" aria-expanded="true" aria-controls="collapseTwo_1"> Add Comment</a>
                    </h4>
                </div>
                <div id="collapseTwo_1" class="panel-collapse collapse <?php if(!$count > 0)echo 'in'; ?>" role="tabpanel" aria-labelledby="headingTwo_1">
                                                <div class="panel-body">
				<form id="frmAddComment" method="post">								
                    <div class="input-group">
                        <span class="input-group-addon">
                            <i class="material-icons">comment</i>
                        </span>
                        <div class="form-line">
							<textarea class="form-control" name="assessComment" id="assessComment" placeholder="Comment" required></textarea>
                        </div>
                    </div>
					<button class="btn btn-block btn-lg bg-green waves-effect btnaddComment" dir="Assessment" id="<?php echo $p_id ?>" type="button">COMMENT</button>
				</form>		
            </div>
        </div>
    </div>	
	<?php
	}
	?>
                                    </div>
                                </div>	
</div>	
<div class="row">
	<div class="col-xs-12 ol-sm-12 col-md-12 col-lg-12">													
		<?php
		if($heritage->permitStatus($con,$p_id,'Feedback') > 0)
		{
			echo '<div class="alert bg-green alert-dismissible"><strong>Successful!</strong> - The order was assessed</div>';
		}else if($count > 0)
		{
		?>
		<div class="button-demo">
			<button type="button" class="btn btn-warning waves-effect" onclick="permitNextStage('Feedback',this.id)" id="<?php echo $p_id ?>">NEXT STEP</button>																		
		</div>	
														<?php
														}
														?>
	</div>													
</div>													
																											
												</div>
											</div>							
									</div>	
								</div>
														