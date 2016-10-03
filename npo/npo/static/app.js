
var app = angular.module("App", ['ui.router', 'ngSanitize', 'ngAnimate', 'ngResource']).run(function($rootScope) {
});


app.config(function($interpolateProvider, $httpProvider) {

    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');

    $http.get("/api/activities").success(function(response) {
    });

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


app.controller("ActivityPageController", function($scope, $stateParams, $http) {
    var $activity = $stateParams.activity;
    var $date = $activity.substring(0, 10);
    var $slug = $activity.substring(11);
    $http.get("/api/activities", {params: {date: $date, slug: $slug}}).success(function(response) {
        $scope.activity = response[0];
    });
});


app.controller("MagazinePageController", function($scope, $http) {
    $http.get("/api/magazine").success(function(response) {
        $scope.newsletters = response;
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
