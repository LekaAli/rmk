$(function () {
    $('.js-basic-example').DataTable({
        responsive: true
    });

    //Exportable table
    var table = $('.js-exportable').DataTable({
        dom: 'Bfrtip',
        responsive: true,
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ]
    });
	
     $('#per_status').live('change', function () {
		 if($(this).val() == "Session")
		 {
			$('#tblSession').show();
			$('#tblTrail').hide();	
		 }
		 else	
		 {			 
			table.columns(1).search(this.value).draw();	 
			$('#tblTrail').show();
			$('#tblSession').hide(); 
		 }
	 }); 
	$("#per_status").prop("selectedIndex", 0).change();	
});