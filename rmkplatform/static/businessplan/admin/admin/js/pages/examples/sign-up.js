$(function () {
    $('#sign_upform').validate({
        rules: {
			"email":{
				required: true,
				email:true,
				remote:{
					url:"checkusername.php", //check if email already exists
					type:'POST'
				}},
        },
        highlight: function (input) {
            console.log(input);
            $(input).parents('.form-line').addClass('error');
        },
        unhighlight: function (input) {
            $(input).parents('.form-line').removeClass('error');
        },
        errorPlacement: function (error, element) {
            $(element).parents('.input-group').append(error);
            $(element).parents('.form-group').append(error);
        },
	messages: {
		 email:
		{
			required: "email field is required",
			remote:"this user is already registered."
		},	
		
	} 		
    });	
    $('#contactForm').validate({
        rules: {

        },
        highlight: function (input) {
            console.log(input);
            $(input).parents('.form-line').addClass('error');
        },
        unhighlight: function (input) {
            $(input).parents('.form-line').removeClass('error');
        },
        errorPlacement: function (error, element) {
            $(element).parents('.input-group').append(error);
            $(element).parents('.form-group').append(error);
        },
	messages: {
	
		
	} 	
    });	
});