var BaseUrl = "http://"+window.location.hostname+"/~limpopoeheritage";
var url = BaseUrl+"/includes/process_ajax_requests.php";
function add_user(dataString,btn)
{
	jQuery.ajax({
		type: "POST",
		url: url,
		data: dataString,
		dataType: 'html',
		cache: false,
		success: function(response)
		{
			alert(response)
			if(response > 0)
				$(btn).html("successful");
			//$('form[name="add_user"]')[0].reset();*/
		}	
	});		
}
function enableBtn(field,sel)
{
	if(sel.value != 'clid')
	{	
		$("."+field).removeAttr('disabled');
	}
}


function permitNextStage(stage,id)
{
	$.post(url+'?perm_id='+id+'&stage='+stage,function(data){
		if(data > 0)
			location.reload()	
	});	
}

$(document).ready(function(){
	//Portal registration submit button
    $("#btnRegister").live("click",function(){
		if ($("#formRegister").valid()) //check if the form inputs are all entered
		{
			$(this).prop('disabled',true);
			var dataString = $("#formRegister").serialize(); //get form input values
			add_user(dataString,$(this));
		}
		
    });	

	//dashboard user registration submit button
    $(".btnadduser").live("click",function(){
		var id = $(this).attr('id');
		
		if ($("#sign_upform").valid()) //check if the form inputs are all entered
		{
			$(this).prop('disabled',true);
			var dataString = $("#sign_upform").serialize()+"&usid="+id; //get form input values
			add_user(dataString,$(this));	
		}
		return false;
    });	
	//trigger create password button
		$('.create_pass').live("click",function(){
			var id = $(this).attr('id');
			var pass = $('#password').val();
			var r_pass = $('#confirm_password').val();
			
			if (!pass || !r_pass)
				alert('all fields are required!');
			else if(pass != r_pass)
				alert('password fields must match!');	
			else
			{  
				$('.mp_loading').show();
				$(this).prop('disabled',true);
				$.post(BaseUrl+"/includes/validate_login.php?pass="+pass+"&uid="+id,function(data)
				{
					//$('.error_field').html('');
					$('.create_pass').html("password created successfully");
					//$('.mp_loading').hide();
					setInterval(function(){ window.location = BaseUrl+"/admin/"; }, 500);		
				});				
			}
		});	
		
	//send reset link
    $(".btnSendReset").live("click",function(){
		var id = $(this).attr('id');
		//$(this).prop("disabled",true);
		$.post(url+"?resetid="+id,function(response){
			alert(response)
		});		
    });		

	//select user
    $(".select_user").live("click",function(){
		var id = $(this).attr('id');
		location.href = "user_profile.php?userid="+id;
    });	
	//delete user
    $(".btndeluser").live("click",function(){
		var id = $(this).attr('id');
		var action = $(this).attr('dir'); //delete or restore action
		var reason = $('#rmreason').val();
	
		$.post(url+"?delid="+id+"&delreason="+reason+"&suspAction="+action,function(response){
			alert(response)
		});
    });		
	//add user rights
    $(".addrights").live("click",function(){
		var role = $(this).attr('id');
		var id = $(this).attr('dir'); 
		$('.modal-title').html(role);
		$.post(url+"?roleid="+id,function(response){
			$('.modal-body').html(response);
		});
    });	
	
	//custom rights
	$(".add_field").live("click",function()
	{
		var selfield = $('#inactivePnl').val();
		var id = $('#inactivePnl option:selected').attr('id');
		var rid = $(this).attr('id');
		$.post(url+"?addfield="+id+"&rid="+rid);
		$('#activePnl').append($('<option>', {
			value:selfield,
			id:id,
			text: selfield
		}));
		$('#inactivePnl option[value="'+selfield+'"]').remove();
		$(this).prop("disabled",true);
	});		
	$(".rem_field").live("click",function()
	{
		var selfield = $('#activePnl').val();
		var id = $('#activePnl option:selected').attr('id');
		var rid = $(this).attr('id');

		$.post(url+"?remfield="+id+"&rid="+rid);
		$('#inactivePnl').append($('<option>', {
			value:selfield,
			id:id,
			text: selfield
		}));
		$('#activePnl option[value="'+selfield+'"]').remove();
		$(this).prop("disabled",true);
	});
	
	//request selected site
	$(".selSite").live("change",function()
	{	
		var siteid = $(this).val();
		var siteName = $(".selSite option:selected").attr('id');
		
		var url = "sitesfrm.php";
		$.post(url+'?mapid='+siteid,function(data){
			$('.siteName').html(siteName);
			$('#mapPanel').html(data);
		});
	});
	$(".selSite").prop("selectedIndex", 0).change();
	//open site form
	$(".btnNewSite").live("click",function()
	{
		$(".newsite").css("display","block");
		$(".manageSite").css("display","none");
		$(".btnManageSite").fadeIn('slow');
		$('#mapPanel').html("");
		$(this).slideUp('slow');
	});	
	//open manage site
	$(".btnManageSite").live("click",function()
	{
		$(".newsite").css("display","none");
		$(".manageSite").css("display","block");
		$(this).slideUp('slow');
		$(".btnNewSite").fadeIn('slow');
		$(".selSite").prop("selectedIndex", 0).change();
	});	
	//Trigger Add site function
	$(".btnAddSite").live("click",function()
	{
		var id = $(this).attr('id');
		if(!id)
			id = "";
		
		if ($("#addSiteFrm").valid()) //check if the form inputs are all entered
		{
			return true;
			/*$(this).prop('disabled',true);
			var dataString = $("#addSiteFrm").serialize()+"&siteid="+id; //get form input values
			add_user(dataString,$(this));
			return false*/
		}
		return false
	});

	//--------------------permit procees---------------------	
	//checkProcess
	$(".processPermit").live("click",function()
	{
		var id = $(this).attr('id');
		
		location.href = "precessPermit.php?pid="+id;
	});	
	$(".btnaddComment").live("click",function()
	{
		var id = $(this).attr('id');
		var pstage = $(this).attr('dir');
		var comm = $("#assessComment").val();
		if(!comm)
			alert('Please type your comment!')
		else
		{
			$.post(url+'?pstage='+pstage+'&comm='+comm+'&commId='+id,function(data){
				if(data > 0)
					location.reload();
			});
		}
	});	
	$('.docs').live('change', function() { 
		var img = document.getElementById("upldFile").files[0].name	
		$('.upld').html("Change");
		$('.dispFile').html('<button type="button" class="btn btn-success">'+img+'</button>');
	});	
	
	$(".enableReject").live("click",function()
	{
		$(".feedbackBtn").css("display","none");
		$("#rejectComment").fadeIn('slow');
	});	
	$(".disableReject").live("click",function()
	{
		$("#rejectComment").css("display","none");
		$(".feedbackBtn").fadeIn('slow');
	});		
		
		
});