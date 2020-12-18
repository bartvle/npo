var baselayer1 = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {maxZoom: 18, attribution: '<a href="https://www.openstreetmap.org" target="_blank">OpenStreetMap</a>'});
var baselayer2 = L.tileLayer('http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {maxZoom: 18, attribution: '<a href="http://www.esri.com" target="_blank">ESRI</a>'});

var baselayers = {
    'Kaart': baselayer1,
    'Satelliet': baselayer2
    };

style_npo = {
    "weight": 3,
    "color": '#1f78b4',
    "fillOpacity": 0.5,
};

style_anb = {
    "weight": 3,
    "color": '#33a02c',
    "fillOpacity": 0.5,
};

style_ilvo = {
    "weight": 3,
    "color": '#ff7f00',
    "fillOpacity": 0.5,
};

style_go = {
    "weight": 3,
    "color": '#fdbf6f',
    "fillOpacity": 0.5,
};

style_gondebeek = {
    "weight": 1,
    "color": '#000000',
    "fillOpacity": 0.,
};

style_gondebeek_perimeter = {
    "weight": 3,
    "color": '#ff0000',
    "fillOpacity": 0.,
};

function loadSpecialOwnerships() {
    var jqxhr_npo = $.get("/admin/eigenaar/49", function(data) {
        window.npo_parcels = data;
    });
    var jqxhr_anb = $.get("/admin/eigenaar/51", function(data) {
        window.anb_parcels = data;
    });
    var jqxhr_ilvo = $.get("/admin/eigenaar/8", function(data) {
        window.ilvo_parcels = data;
    });

    var jqxhr = $.when(jqxhr_npo, jqxhr_anb, jqxhr_ilvo)

    return jqxhr
}

function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        "weight": 3,
        "color": 'red',
        "fillOpacity": 0.5,
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }
}

function resetHighlight(e) {
    if (window.npo_parcels.includes(e.target.feature.properties.CAPAKEY)) {
        e.target.setStyle(style_npo);
    } else if (window.anb_parcels.includes(e.target.feature.properties.CAPAKEY)) {
        e.target.setStyle(style_anb);
    } else if (window.ilvo_parcels.includes(e.target.feature.properties.CAPAKEY)) {
        e.target.setStyle(style_ilvo);
    } else if (e.target.feature.properties.Eigenaar == 'GO!') {
        e.target.setStyle(style_go);
    } else {
        e.target.setStyle(style_gondebeek);
    };
}

function showData(e) {
    e.target.bindPopup("Loading...", {maxWidth: 560}).openPopup();
    // console.log(e.target.feature.properties);
    var popup = e.target.getPopup();
    var str = e.target.feature.properties.CAPAKEY;
    var res = str.replace("/", "-");
    var url = "/admin/perceel/" + res;
    $.get(url, function(data) {

        var n = e.target.feature.properties.CAPAKEY
        var s = '<div id="key"><b>' + n + '</b></div>'
        var data = data.replace('<div id="key"></div>', s);

        var n = e.target.feature.properties.OPPERVL.toString()
        var s = '<div id="size">Oppervlakte: ' + n + ' m2</div>'
        var data = data.replace('<div id="size"></div>', s);
        // console.log(data);
        popup.setContent(data);
        popup.update();
    });
}

function onEachFeature(feature, layer) {
    if (window.npo_parcels.includes(feature.properties.CAPAKEY)) {
        layer.setStyle(style_npo);
    } else if (window.anb_parcels.includes(feature.properties.CAPAKEY)) {
        layer.setStyle(style_anb);
    } else if (window.ilvo_parcels.includes(feature.properties.CAPAKEY)) {
        layer.setStyle(style_ilvo);
    } else if (feature.properties.Eigenaar == 'GO!') {
        layer.setStyle(style_go);
    } else {
        layer.setStyle(style_gondebeek);
    };
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        click: showData,
    });
}
