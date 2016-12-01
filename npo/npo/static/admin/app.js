
var app = angular.module("App", []).run(function($rootScope) {
});

app.config(function($interpolateProvider, $httpProvider) {

    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');

});

app.controller("AppController", function($scope, $http) {

    var map = L.map('map').setView([50.975183, 3.791357], 15);

    var baselayer1 = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {maxZoom: 18, attribution: '<a href="https://www.openstreetmap.org" target="_blank">OpenStreetMap</a>'});
    var baselayer2 = L.tileLayer('http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {maxZoom: 18, attribution: '<a href="http://www.esri.com" target="_blank">ESRI</a>'});
    baselayer1.addTo(map);
    baselayers = {'Kaart': baselayer1, 'Satelliet': baselayer2}

    function onEachFeature(feature, layer) {
            layer.bindPopup("<b>" + feature.properties.CAPAKEY + "</b></br>" + feature.properties.OPPERVL + "m²");
        };

    var style0 = {
        "weight": 1,
        "opacity": 1,
        "fillOpacity": 0,
    };

    var style1 = {
        "weight": 1,
        "opacity": 1,
    };

    var styleN2000 = {
        "weight": 2,
        "color": '#33a02c',
        "opacity": 1,
        "fill": false,
    };

    var style_ven = {
        "weight": 2,
        "color": '#ff7f00',
        "opacity": 1,
        "fill": false,
    };

    var layer_control = L.control.layers(baselayers, null, {collapsed: false});
    layer_control.addTo(map);

    $http.get('/static/data/gebieden1.geojson').success(function(data) {

        var total_area = 0;
        for (var i in data.features) {
            var obj = data.features[i];
            total_area += obj.properties.OPPERVL;
        }
        $scope.total_area = total_area / 10000;

        var gebieden1 = L.geoJson(data, {onEachFeature: onEachFeature, style: style1});
        gebieden1.addTo(map);

    });

    $http.get('/static/data/gebieden0.geojson').success(function(data) {
        var gebieden0 = L.geoJson(data, {onEachFeature: onEachFeature, style: style0});
        layer_control.addOverlay(gebieden0, "<span id='map_legend'>Visiegebied Gondebeek</span>");
    });

    $http.get('/static/data/Natura2000.geojson').success(function(data) {
        var natura_2000 = L.geoJson(data, {style: styleN2000});
        layer_control.addOverlay(natura_2000, "<span id='map_legend'>Natura 2000</span>");
    });

    $http.get('/static/data/VEN.geojson').success(function(data) {
        var ven = L.geoJson(data, {style: style_ven});
        layer_control.addOverlay(ven, "<span id='map_legend'>VEN</span>");
    });

});

// var app = angular.module("App", ['ui.router']).run(function($rootScope) {
// });

// app.config(function($stateProvider, $locationProvider) {

	// $stateProvider

    // .state('start', {
        // url: "/",
        // templateUrl: 'pages/start.php',
        // controller: 'StartPageController',
    // })

    // .state('areas', {
        // url: "/gebieden",
        // templateUrl: 'pages/areas.php',
        // controller: 'AreasPageController',
    // })

    // .state('amphibians', {
        // url: "/overzet",
        // templateUrl: 'pages/amphibians.php',
        // controller: 'AmphibiansPageController',
    // })

    // $locationProvider.html5Mode(true);

// });

// app.controller("AppController", function($scope, $location) {
    // $.material.init();

    // $(document).ready(function () {
        // $(".navbar-nav li a").click(function(event) {
            // $(".navbar-collapse").collapse('hide');
        // });
    // });

    // $scope.isActiveLink = function (l) {
        // return l === $location.path();
    // };

// });

// app.controller("StartPageController", function($scope) {
// });

// app.controller("AreasPageController", function($scope, $http) {
    
    // var map = L.map('map').setView([50.975183, 3.791357], 15);

    // var baselayer1 = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {maxZoom: 18, attribution: '<a href="https://www.openstreetmap.org" target="_blank">OpenStreetMap</a>'});
    // var baselayer2 = L.tileLayer('http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {maxZoom: 18, attribution: '<a href="http://www.esri.com" target="_blank">ESRI</a>'});
    // baselayer1.addTo(map);
    // baselayers = {'Kaart': baselayer1, 'Satelliet': baselayer2}

    // function onEachFeature(feature, layer) {
            // layer.bindPopup("<b>" + feature.properties.CAPAKEY + "</b></br>" + feature.properties.OPPERVL + "m²");
        // };

    // var style0 = {
        // "weight": 1,
        // "opacity": 1,
        // "fillOpacity": 0,
    // };

    // var style1 = {
        // "weight": 1,
        // "opacity": 1,
    // };

    // var styleN2000 = {
        // "weight": 2,
        // "color": '#33a02c',
        // "opacity": 1,
        // "fill": false,
    // };

    // var style_ven = {
        // "weight": 2,
        // "color": '#ff7f00',
        // "opacity": 1,
        // "fill": false,
    // };

    // var layer_control = L.control.layers(baselayers, null, {collapsed: false});
    // layer_control.addTo(map);

    // $http.get('data/gebieden1.geojson').success(function(data) {

        // var total_area = 0;
        // for (var i in data.features) {
            // var obj = data.features[i];
            // total_area += obj.properties.OPPERVL;
        // }
        // $scope.total_area = total_area / 10000;

        // var gebieden1 = L.geoJson(data, {onEachFeature: onEachFeature, style: style1});
        // gebieden1.addTo(map);

    // });

    // $http.get('data/gebieden0.geojson').success(function(data) {
        // var gebieden0 = L.geoJson(data, {onEachFeature: onEachFeature, style: style0});
        // layer_control.addOverlay(gebieden0, "<span id='map_legend'>Visiegebied Gondebeek</span>");
    // });


    // $http.get('data/Natura2000.geojson').success(function(data) {
        // var natura_2000 = L.geoJson(data, {style: styleN2000});
        // layer_control.addOverlay(natura_2000, "<span id='map_legend'>Natura 2000</span>");
    // });

    // $http.get('data/VEN.geojson').success(function(data) {
        // var ven = L.geoJson(data, {style: style_ven});
        // layer_control.addOverlay(ven, "<span id='map_legend'>VEN</span>");
    // });

// });

// app.controller("AmphibiansPageController", function($scope, $http) {

    // $scope.get = function() {
        // $http.get("/api/overzet/"+$scope.filters.jaar).success(function(response) {
            // $scope.entries = response;
        // });
        // $http.get("/api/overzet/totaal/"+$scope.filters.jaar).success(function(response) {
            // $scope.total = response;
        // });
    // };

    // $scope.add = function() {
        // $http.post("/api/overzet/add", $scope.data).success(function(response) {
            // $scope.data = {'datum': new Date(), 'edit': 0};
            // $scope.get();
        // });
    // };

    // $scope.del = function(id) {
        // $http.post("/api/overzet/"+id+"/verwijder").success(function() {
            // $scope.get();
        // });
    // };

    // $scope.data = {'datum': new Date(), 'edit': 0, 'opmerking': ''};
    // $scope.sort = 'datum';
    // $scope.reverse = true;
    // $scope.filters = {'jaar': '2016'};
    // $scope.get();
    
// });
