// function redirectTo404() {
//     window.location.href = "404.html";
// }


//   function initMap() {
//     var location = { lat: 53.073635, lng: 8.806422 };
//     var map = new google.maps.Map(document.getElementById('map'), {
//       zoom: 14,
//       center: location
//     });
//     var marker = new google.maps.Marker({
//       position: location,
//       map: map
//     });
//   }

// initMap();

function initMap() {
    // Specify the latitude and longitude of your location
    var myLatLng = { lat: 53.073635, lng: 8.806422 };
  
    // Create a map centered at your location
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 10,
      center: myLatLng
    });
  
    // Add a marker at your location
    var marker = new google.maps.Marker({
      position: myLatLng,
      map: map,
      title: 'Afrik Kitchen'
    });
  }
  