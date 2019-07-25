<!DOCTYPE html>
<html>
  <head>
    <style>
       #map {
        height: 400px;
        width: 100%;
       }
	   .markerImg
	   {
		   width:100%;
		   height:140px;
	   }
	   .markerPanel
	   {
		   width:350px;
	   }
    </style>
  </head>
  <body>
    <div id="map"></div>
<script src="assets/js/jquery-2.0.0.js"></script>	
<script async defer
    src="https://maps.googleapis.com/maps/api/js?key=
AIzaSyC-BCgMaGr36-CRW-Mkb4Gtxiximvecuh0
&callback=initMap">
    </script>
    <script>
	$(document).ready(function(){

		
	});

	
      function initMap() {
        var options = {
          zoom: 12,
          center: new google.maps.LatLng(-23.896171, 29.448626),
		  mapTypeId: google.maps.MapTypeId.ROADMAP
        };
		var map = new google.maps.Map(document.getElementById('map'),options);
		
		var results = jQuery.ajax({
			type: "POST",
			url: 'mapMarkers.php',
			cache: false,
			dataType:'json',
			async: false,
			success: function(response)
			{
				results = response;
			}  
		}).responseText;
		
		
		$.each($.parseJSON(results), function(i, item) {
			latLng = new google.maps.LatLng(item.latitude, item.longitude); 
			// Creating a marker and putting it on the map
			var marker = new google.maps.Marker({
				position: latLng,
				map: map
				//title: item.name
			});
			var imgfile = 'admin/sites_images/'+item.id+'-'+item.img;
			var infoWindow = new google.maps.InfoWindow({
				content:'<div class="markerPanel"><img class="markerImg" src="'+imgfile+'"><h3>'+item.name+'</h3><span>'+item.address+'<a class="btn btn-sm btn-link" href="siteInfo.php?siteid="'+item.id+'>Read More...</a></span></div>' 
			});
			
			marker.addListener('click',function(){
				infoWindow.open(map,marker);
			});
		});		
		
      }
    </script>
	 

	<script src="assets/js/jquery-migrate-1.1.1.js"></script>
	
  </body>
</html>