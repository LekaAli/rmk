// JavaScript Document
$(document).ready(function() 
{	
$.validator.addMethod("id", function(id) {	
    var i, c,
        even = '',
        sum = 0,
        check = id.slice(-1);

    if (id.length != 13 || id.match(/\D/)) {
        return false;
    }
    id = id.substr(0, id.length - 1);
    for (i = 0; c = id.charAt(i); i += 2) {
        sum += +c;
        even += id.charAt(i + 1);
    }
    even = '' + even * 2;
    for (i = 0; c = even.charAt(i); i++) {
        sum += +c;
    }
    sum = 10 - ('' + sum).charAt(1);
    return ('' + sum).slice(-1) == check;
});	
		   
$("#formRegister").validate({	
					
	errorElement: 'div',
	rules:{	
			"fnames":{required: true},	
			"surname":{required: true },
			"email":{
				required: true,
				email:true,
				remote:{
					url:"checkemail.php", //check if email already exists
					type:'POST'
					}},
			"cell":{required: true },			
			"pwd1":{
				required: true ,
			  	minlength:8
			  },
			"pwd2":{
				required:true,
				equalTo: ".pwd1"
		},			  
		},
	
	messages: {
		fnames:
		{
			required: "full names field is required"
		},
		 cell:
		{
			required: "cellphone is required"
		},
		 email:
		{
			required: "email field is required",
			remote:"this user is already registered, try other username."
		},	
		pwd1: 
		{
			 required: "password is required",
			 minlength: "password must be 8 or more characters"
		},
     	pwd2: {
             required: "confirmation password is required",
             equalTo: "Please enter the same password as above"
        },		
	}  
 
  }); 
 
/*
$("#add_personal").validate({
	errorElement: 'div',
	rules:{	
			"id":{
					id:true,
					 remote:{url:"check.php",
					 type:'POST'}
				},
			"email":{email:true,}
		},
messages: {
		id:
		{
			id:"Enter a valid SA ID Number",
			remote:"ID number is already in the system."
		},
		email:
		{
			email:"Enter a valid email address",
		}		
},
});

$(".bank").validate({
	errorElement: 'div',
	rules:{	
			"bnkname":{required: true},	
			"branchcode":{required: true },	
			"accno":{required: true},	
			"acctype":{required: true },	
			"accholder":{required: true}							
		},
messages: {
		bnkname:
		{
			required: "Bank name field is required"
		},
		 branchcode:
		{
			required: "Branch code field is required",
		}		
},
});
  
  
	$('#acceptloan').live("click",function() {	
		var dataString = $('#loancalc').serialize()+"&clid="+$('#clid').val();	
		jQuery.ajax({
			type: "POST",
			url: "process_loan.php",
			data: dataString,
			dataType: 'html',
			cache: false,
			success: function(response)
			{	
				alert(response)
				//location.reload();
			}	
		});
		return false;
		
	});	
	
		$('#updateLoan').live('click',function(){
			var pday = $('#pday').val();
			var otherday = $('#otherday').val();
			var ptype = $('#ptype').val();
			var dp1 = $('#dp1').val();
			var creditor = $('#creditor').val();
			var clid = $('#clid').val();
			$.post('process_loan.php?pday='+pday+'&otherday='+otherday+'&ptype='+ptype+
			'&dp1='+dp1+'&creditor='+creditor+'&clid='+clid,function(response){
				alert(response)
				location.reload();
			});
		});		


$("#savelevels").live("click",function()
{
	if ($("#add_user").valid())
	{
		var dataString = $('#add_user').serialize();;
		jQuery.ajax({
			type: "POST",
			url: "process_user.php",
			data: dataString,
			dataType: 'html',
			cache: false,
			success: function(response)
			{
				//alert(response);
				$('#success').html(response);
				$('form[name="add_user"]')[0].reset();
			}
			
		});					
	}
});
function regClient(dataString,disp)
{
	
	jQuery.ajax({
		type: "GET",
		url: "http://localhost/Loans/process_pdf.php",
		data: dataString,
		dataType: 'html',
		cache: false,
		success: function(response)
		{
			
			if (response.length > 0 && response.length< 3)
			{
				window.parent.client(response);
			}
			$(disp).val(response);
		}
			
	});		
}
var dataString, disp = "";

$("#svpersonal").live("click",function()
{ 
	if ($("#add_personal").valid())
	{
		var dataString = $('#add_personal').serialize();
		disp = '#client_id';
		regClient(dataString,disp);
	}
});
$('#svfiles').live('click', function() {
	var clid = $("#client_id").val();
	var fnames = $("#inptfiles").val();
	var dataString = "clid="+clid+"&fnames="+fnames;
	disp = '';
	regClient(dataString,disp);		
});

$('#svemp').live("click",function()
{ 
	var clid = $("#client_id").val();
	var dataString = $('.employment').serialize()+"&clid="+clid;
	disp = '';
	regClient(dataString,disp);
});	
$('#svincome').live("click",function()
{ 	
	var clid = $("#client_id").val();
	var dataString = $('#frmincome').serialize()+"&clid="+clid;
	disp = '';
	regClient(dataString,disp);
});
$('#sub_client').live("click",function()
{ 	
	if ($(".bank").valid())
	{
		var clid = $("#client_id").val();
		var dataString = $('.bank').serialize()+"&clid="+clid;
		disp = '';
		regClient(dataString,disp);
	}
	
});*/
	
});