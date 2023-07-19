// function redirectTo404() {
//     window.location.href = "404.html";
// }


  function initMap() {
    var location = { lat: YOUR_LATITUDE, lng: YOUR_LONGITUDE };
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 14,
      center: location
    });
    var marker = new google.maps.Marker({
      position: location,
      map: map
    });
  }

initMap();