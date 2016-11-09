//https://mathiasbynens.be/notes/xhr-responsetype-json

xmlhttp=new XMLHttpRequest();
xmlhttp.open("GET", "http://127.0.0.1:8000/media/drone.json", false);
xmlhttp.send();
var parseddata = JSON.parse(xmlhttp.responseText);
console.log(parseddata);
console.log(parseddata.strike.length)
console.log(parseddata.strike[0].lat)




//alert("I am an alert box!");

var mymap = L.map('mapid', { attributionControl:false }).setView([21.47, 55.9754], 4);
//, { attributionControl:false } this deletes bottom watermark

//var mymap = L.map('mapid').setView([35.9908385, -78.9005222], 8);
L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.dark',
    accessToken: 'pk.eyJ1IjoiamNweXVuIiwiYSI6ImNpdXExNzkxejAyMGcydHFteDhrNXAwc20ifQ.gY2JiAMFphomRoFfGMKVEg'
}).addTo(mymap);


/*
function test(){
    for (var i = 0; i < dronedata.length; i ++){
        var circle= L.circle(dronedata[i],{
            color: 'red',
            fillColor: '#f03',
            fillOpacity: 0.5,
            radius: 3000
            }).addTo(mymap);
    }
}*/
//test();
var customOptions =
        {
        'maxWidth': '300',
        'className' : 'custom',
        'popupAnchor': '[-3, -76]',
        }

function dataToMap(n){
    for (var i=0;i<parseddata.strike.length;i++){
        if (parseddata.strike[i].lat != "" && parseddata.strike[i].lon!= ""){
            var customPopup = "<h1>"+parseddata.strike[i].location+"</h1>"
                                +"Date: "+parseddata.strike[i].date.substring(0, 10) +"</br>"
                                +"Injuries: "+parseddata.strike[i].injuries +"</br>"
                                +"Deaths: "+parseddata.strike[i].deaths +"</br>"
                                +"Description: "+parseddata.strike[i].narrative +"</br>"
                                +"Target: "+parseddata.strike[i].target+"</br>"
                                +"Source: "+"<a href="+parseddata.strike[i].bij_link+"/>"+parseddata.strike[i].bij_link;
            var circle= L.circle([parseddata.strike[i].lat,parseddata.strike[i].lon],{
                color: 'red',
                fillColor: '#f03',
                fillOpacity: 0.5,
                radius: 3000
                }).addTo(mymap);
            circle.bindPopup(customPopup,customOptions);
        }
    }
}
dataToMap(parseddata);
//////////////
/*
var popup = L.popup();

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(mymap);
}
var itslit=false;
mymap.on('click', onMapClick);
*/
function onClick(e) {alert(this.getLatLng());}
mymap.on('popupopen', function (e) {
     document.getElementById("moreinfo").innerHTML=e.popup._source
     console.log(e.popup)
     
});



///////////
// disabler
/////////

//http://www.coffeegnome.net/control-button-leaflet/
var buttonstat=false
var customControl =  L.Control.extend({
  options: {
    position: 'topleft'
  },
  onAdd: function (mymap) {
    var container = L.DomUtil.create('div', 'leaflet-bar leaflet-control leaflet-control-custom');

    container.style.backgroundColor = 'white';     
    container.style.backgroundImage = "url()";
    container.style.backgroundSize = "30px 30px";
    container.style.width = '30px';
    container.style.height = '30px';

    container.onclick = function(){
        if (buttonstat==false){
            mymap.dragging.disable();
            buttonstat=true
            






            
        }
        else{
            mymap.dragging.enable();
            buttonstat=false
        }
    }

    return container;
  }
});
mymap.addControl(new customControl());
////////
////////////////////////////////////////////////////////////////////
// Watermark

////////////////////////////////////////////////////////////////////

