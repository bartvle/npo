
var app = angular.module("App", []).run(function($rootScope, $http) {
});


app.config(function($interpolateProvider, $httpProvider) {

    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');

    // $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    // $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

});


app.controller("AppController", function($scope) {

    $(document).ready(function () {
        $(".navbar-nav li a").click(function(event) {
            $(".navbar-collapse").collapse('hide');
        });
    });

});


app.controller("MapController", function($scope, $http) {
    map = L.map('natuurgebieden_kaart').setView([50.937494, 3.798325], 11);
    
    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {maxZoom: 18, attribution: '<a href="https://www.openstreetmap.org" target="_blank">OpenStreetMap</a>'}).addTo(map);

    L.marker([50.910762, 3.807238]).addTo(map).bindPopup("Vosbroeken");
    L.marker([50.976058, 3.790630]).addTo(map).bindPopup("Gondebeek");
    L.marker([50.912186, 3.817297]).addTo(map).bindPopup("Heidebos");

    $http.get('/static/data/oosterzele.geojson').success(function(data) {
        var oosterzele = L.geoJson(data, {style: {"weight": 2, "color": 'red', "opacity": 0.75, "fill": false,}});
        oosterzele.addTo(map);
    });
});
