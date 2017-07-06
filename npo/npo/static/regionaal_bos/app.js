
var app = angular.module("App", []).run(function($rootScope) {
});


app.config(function($interpolateProvider, $httpProvider) {

    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');

});


app.controller("AppController", function($scope, $http) {

    var map = L.map('map').setView([50.961886, 3.760017], 12);

    var baselayer1 = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {maxZoom: 18, attribution: '<a href="https://www.openstreetmap.org" target="_blank">OpenStreetMap</a>'});
    var baselayer2 = L.tileLayer('http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {maxZoom: 18, attribution: '<a href="http://www.esri.com" target="_blank">ESRI</a>'});
    baselayer1.addTo(map);
    baselayers = {'Kaart': baselayer1, 'Satelliet': baselayer2}

    function onEachFeature(feature, layer) {
            layer.bindPopup("<b>" + feature.properties.CAPAKEY + "</b></br>" + feature.properties.OPPERVL + "m²");
        };

    var style_perimeter = {
        "weight": 2,
        "opacity": 1,
        // "fillOpacity": 0,
    };

    var style_natura_2000 = {
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

    $http.get('/static/data/Perimeter.geojson').success(function(data) {
        var perimeter = L.geoJson(data, {style: style_perimeter});
        perimeter.addTo(map);
    });

    $http.get('/static/data/Natura2000.geojson').success(function(data) {
        var natura_2000 = L.geoJson(data, {style: style_natura_2000});
        layer_control.addOverlay(natura_2000, "<span id='map_legend'>Natura 2000</span>");
    });

    $http.get('/static/data/VEN.geojson').success(function(data) {
        var ven = L.geoJson(data, {style: style_ven});
        layer_control.addOverlay(ven, "<span id='map_legend'>VEN</span>");
    });

});
