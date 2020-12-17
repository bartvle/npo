var baselayer1 = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {maxZoom: 18, attribution: '<a href="https://www.openstreetmap.org" target="_blank">OpenStreetMap</a>'});
var baselayer2 = L.tileLayer('http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {maxZoom: 18, attribution: '<a href="http://www.esri.com" target="_blank">ESRI</a>'});

var baselayers = {
    'Kaart': baselayer1,
    'Satelliet': baselayer2
    };

var ettingebos_parcels = L.geoJson(JSON.parse('{{ ettingebos_parcels | escapejs }}'));

var map = L.map('map', {layers: [baselayer1]}).setView([50.935947946491716, 3.8066584080819594], 15);
map.addLayer(ettingebos_parcels);
