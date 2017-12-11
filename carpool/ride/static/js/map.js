$(document).ready(function() {
  function loadMap() {
    var address = $("#home").text()
    var addressWork = $("#away").text()

    var geocoder = new google.maps.Geocoder();

    geocoder.geocode({
      'address': address
    }, function(results, status) {
      var locati = results[0].geometry.location;
      // alert('LAT: ' + locati.lat() + ' LANG: ' + locati.lng());

      var mapOptions = {
        center: new google.maps.LatLng(locati.lat(), locati.lng()),
        zoom: 12
      }
      var map = new google.maps.Map(document.getElementById("map"), mapOptions);
      var marker = new google.maps.Marker({
        position: new google.maps.LatLng(50.9, -1.3),
        map: map,
      });
      var marker = new google.maps.Marker({
        position: new google.maps.LatLng(locati.lat(), locati.lng()),
        map: map,
      });
    });

  }
  google.maps.event.addDomListener(window, 'load', loadMap);
  loadMap()
})
