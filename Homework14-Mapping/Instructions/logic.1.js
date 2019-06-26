var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson";

var queryUrl2 = "https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json";


// marker size based on magnitude
function markerSize(mag) {
  return mag*4;
};
// marker color based on magnitude
function markerColor(mag) {
  if (mag > 5) {
    // return (255,69,0)
    return "#FF0000"
  } else if (mag > 4) {
    return "#FF4500"
  } else if (mag > 3) {
    return "#FFA500"
  } else if (mag > 2) {
    return "#F08080"
  } else if (mag > 1) {
    return "#FFFF00"
  } else {
    return "#7FFF00"
  }
  };

// Layer for earthquakes
var earthquakeLayer = new L.LayerGroup();

// Perform a GET request to the query URL
d3.json(queryUrl, function(data) {
  // Once we get a response, send the data.features object to the createFeatures function
  createFeatures(data.features);
});

// Create a GeoJSON layer containing the features array on the earthquakeData object
// Run the onEachFeature function once for each piece of data in the array
function createFeatures(earthquakeData) {
 
  var earthquakes = L.geoJSON(earthquakeData, {
    onEachFeature: function(features,layer) {
      layer.bindPopup("<h3>Place: " + features.properties.place +
      "</h3><hr><p>Time: " + new Date(features.properties.time) + "</p>" +
      "<p>Magnitude: "+ features.properties.mag + "</p>");
    },
    pointToLayer: function(features,latlng) {
      return L.circleMarker(latlng, {radius:markerSize(features.properties.mag)})
    },
    style: function(features) {
      return {
          color: markerColor(features.properties.mag),
          fillColor: markerColor(features.properties.mag),
          fillOpacity: 0.8,
          stroke: false
      }
    }
  }).addTo(earthquakeLayer);

  // Pass the layer to createMap function
  createMap(earthquakes);
}

// Layer for tectonic plates
var tectonicLayer = new L.LayerGroup();

// Perform a GET request to the query URL for tectonic plates
d3.json(queryUrl2, function(data) {
  console.log(data);
  L.geoJSON(data.features, {
    style: function(features) {
      return {
        color: "yellow",
        weight: 2
      }
    }
  }).addTo(tectonicLayer);
});


function createMap(earthquakes) {

    // Define streetmap and darkmap layers
    var satellite = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
      attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
      maxZoom: 18,
      id: "mapbox.satellite",
      accessToken: API_KEY
    });
  
    var grayscale = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
      attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
      maxZoom: 18,
      id: "mapbox.light",
      accessToken: API_KEY
    });
  
    var outdoors = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
      attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
      maxZoom: 18,
      id: "mapbox.outdoors",
      accessToken: API_KEY
    });
  
    // Define a baseMaps object to hold our base layers
    var baseMaps = {
      "Satellite": satellite,
      "Grayscale": grayscale,
      "Outdoor": outdoors
    };
  
    // Create overlay object to hold our overlay layer
    var overlayMaps = {
      Earthquakes: earthquakeLayer,
      "Fault Lines": tectonicLayer
    };
  
    // Create our map, giving it the satellite, earthquakes, fault line layers to display on load
    var myMap = L.map("map", {
      center: [
        37.09, -95.71
      ],
      zoom: 3,
      layers: [satellite, earthquakeLayer,tectonicLayer]
    });

  // Create a layer control
  // Pass in our baseMaps and overlayMaps
  // Add the layer control to the map
    L.control.layers(baseMaps, overlayMaps, {
      collapsed: false
    }).addTo(myMap);
}


  





