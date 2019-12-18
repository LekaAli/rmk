	var BaseUrl = "http://"+window.location.hostname+"/~limpopoeheritage/";

	$(document).ready(function(){	
		//login submit
    	$('#sign_in').on('submit', function(e){
			//e.preventDefault();
				var url = BaseUrl+"/includes/validate_login.php";
				var results = jQuery.ajax({
				   type: "POST",
				   url: url,
				   data: $("#sign_in").serialize(),
				   cache: false,
				   async: false,
				   success: function(response)
				   {
					   results = response;
				   }  
				}).responseText;
				
				if(results == 1)
				{
					return true;
				}
				else
				{
					$('#action_logIn').html('<div class="alert alert-danger"><a href="javascript:;" class="close" data-dismiss="alert">&times;</a><strong>Error!</strong> bad username or password!.</div>');	
					return false;	
				}
									
		});
	     


	/*var login = $('#loginfrm');
	var recover = $('#recoverform');
	var speed = 400;*/

	$('#pwrdForgotclick').click(function(){
		
		$("#frm_signin").slideUp();
		$("#pwrd_frm").fadeIn();
		$("#backtologin").show();
		
		$(".helpbox").slideUp();
		$("#verifyfrm").hide();
	});
	$('#backtologin').click(function(){
		$(".helpbox").fadeIn();
		$("#pwrd_frm").hide();
		$("#frm_signin").fadeIn();
		$("#verify_frm").hide();
		$(this).hide();
	});
	
    
  /*  if($.browser.msie == true && $.browser.version.slice(0,3) < 10) {
        $('input[placeholder]').each(function(){ 
       
        var input = $(this);       
       
        $(input).val(input.attr('placeholder'));
               
        $(input).focus(function(){
             if (input.val() == input.attr('placeholder')) {
                 input.val('');
             }
        });
       
        $(input).blur(function(){
            if (input.val() == '' || input.val() == input.attr('placeholder')) {
                input.val(input.attr('placeholder'));
            }
        });
    });

        
        
    }*/
	$('#btn_send').click(function(){
		var lost_email = $('#recover_email').val();
		if(!lost_email)
			$('#action_forgot').html('<div class="alert alert-danger"><a href="javascript:;" class="close" data-dismiss="alert">&times;</a><strong>Error!</strong> Please enter your email address.</div>');
		else
		{		
		$.post('checkusername.php?lost_email='+lost_email,function(response){
			if(response == false)
			{
				$.post('process_user.php?recover_email='+lost_email,function(){
					$("#pwrd_frm").hide();
					$("#frm_signin").hide();
					$("#verify_frm").fadeIn();					
				});
			}else
			$('#action_forgot').html('<div class="alert alert-danger"><a href="javascript:;" class="close" data-dismiss="alert">&times;</a><strong>Error!</strong> email you entered does not exists!.</div>');			
		});
		}
		return false;
	});
	$('#verifylostpass').click(function(){
		var vercode = $('#vercode').val();
		var byemail = $('#recover_email').val();
		
		$.post('hstl_processes.php?vercode='+vercode+'&byemail='+byemail,function(data){
			if(data != 0)
				window.location = "resetPassword.php?token="+data;
			else
				$('#action_ver').html('<div class="alert alert-danger"><a href="javascript:;" class="close" data-dismiss="alert">&times;</a><strong>Error!</strong> wrong verification code.</div>');					
		});
	});
	
});