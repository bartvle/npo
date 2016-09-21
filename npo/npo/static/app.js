
var app = angular.module("App", ['ui.router', 'ngSanitize', 'ngAnimate', 'ngResource']).run(function($rootScope) {
});

app.config(function($interpolateProvider, $httpProvider) {

    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

});


app.controller("AppController", function($scope) {

    $scope.date = new Date();

    $(document).ready(function () {
        $(".navbar-nav li a").click(function(event) {
            $(".navbar-collapse").collapse('hide');
        });
    });

});


app.controller("StartPageController", function($scope, $http) {
    $http.get("/api/activities").success(function(response) {
        $scope.activities = response;
        console.log($scope.activities);
    });
});


app.controller("MagazinePageController", function($scope, $http) {
    $http.get("/api/magazine").success(function(response) {
        $scope.newsletters = response;
    });
});


app.controller("NewsletterController", function($scope, $http) {
    $scope.post = false;
    $scope.data = {}
    $scope.send = function () {
        $http.post("/api/newsletter/subscribe", $scope.data).success(function(response) {
            $scope.post = true;
            $scope.answer = response;
        });
    }
});










app.factory('NewsItem', function ($resource) {
      return $resource('/api/news/:id');
  });


app.factory('News', function ($resource) {
      return $resource('/api/news/:date/:link');
  });


app.factory('Activity', function ($resource) {
      return $resource('/api/activities/:date/:link');
  });



app.controller("GalleryController", function($scope) {
    $('.parent-container').magnificPopup({
      delegate: 'a', // child items selector, by clicking on it popup will open
      type: 'image',
      gallery:{enabled:true}
      // other options
    });
});


app.controller("MainMapController", function($scope, $http) {

    map = L.map('main_map', {scrollWheelZoom: false}).setView([50.937494, 3.798325], 12);

    var baselayer1 = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {maxZoom: 18, attribution: '<a href="https://www.openstreetmap.org" target="_blank">OpenStreetMap</a>'});
    var baselayer2 = L.tileLayer('http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {maxZoom: 18, attribution: '<a href="http://www.esri.com" target="_blank">ESRI</a>'});
    baselayer1.addTo(map);

    L.marker([50.910762, 3.807238]).addTo(map).bindPopup("<a href='/natuurgebieden'>Vosbroeken</a>");
    L.marker([50.976058, 3.790630]).addTo(map).bindPopup("<a href='/natuurgebieden'>Gondebeek</a>");
    L.marker([50.912186, 3.817297]).addTo(map).bindPopup("<a href='/natuurgebieden'>Heidebos</a>");

    $http.get('/static/data/oosterzele.geojson').success(function(data) {
        var oosterzele = L.geoJson(data, {style: {"weight": 2, "color": 'red', "opacity": 0.75, "fill": false,}});
        oosterzele.addTo(map);
        //layer_control.addOverlay(natura_2000, "<span id='map_legend'>Natura 2000</span>");
    });
});


app.controller("MapController", function($scope) {
    map = L.map('natuurgebieden_kaart').setView([50.937494, 3.798325], 11);
    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {maxZoom: 18}).addTo(map);
    L.marker([50.910762, 3.807238]).addTo(map).bindPopup("Vosbroeken");
    L.marker([50.976058, 3.790630]).addTo(map).bindPopup("Gondebeek");
    L.marker([50.912186, 3.817297]).addTo(map).bindPopup("Heidebos");
});
