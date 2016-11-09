'use strict';

var s = function(p) {

    var canvas;
    var gridPoints = [];
    var segmentWidth = 80;
    var segmentHeight = 80;
    var noiseScale = 0.0005;
    var time = 0;
    var ticks = 0;

    function renderCircle(x, y) {
        var rot = p.map(p.noise(x * noiseScale, y * noiseScale, time), 0, 1, -p.TWO_PI, p.TWO_PI) * 2;
        p.push();
        p.noStroke();
        p.translate(x, y);
        p.rotate(rot);
        p.scale(2.25);
        p.fill(p.map(y, 0, canvas.height, 220, 255), 150);
        p.arc(0, 0, segmentWidth, segmentHeight, 0, p.PI);
        p.fill(p.map(y, 0, canvas.height, 200, 255), 150);
        p.arc(0, 0, segmentWidth, segmentHeight, p.PI, 0);
        p.pop();
    }

    function renderScene() {
        ticks++;
        time += p.map(ticks, 0, 200, 0.003, 0);
        p.background(255);
        for (var j = 0; j < gridPoints.length; j++) {
            renderCircle(gridPoints[j][0], gridPoints[j][1]);
        }
    }

    function init() {
        canvas = p.createCanvas(window.innerWidth, window.innerHeight);
        canvas.parent('background-sketch');
        gridPoints = [];
        for (var ix = -segmentWidth; ix <= canvas.width + segmentWidth; ix += segmentWidth) {
            for (var iy = -segmentHeight * 2; iy <= canvas.height; iy += segmentHeight) {
                gridPoints.push([ix, iy]);
            }
        }
        renderScene();
    }

    p.setup = function() {
        p.pixelDensity(1);
        p.createCanvas(p.windowWidth, p.windowHeight);
        p.background(255, 255, 255);
        init();
    };

    p.draw = function() {
        if (ticks <= 200) {
            renderScene();
        }
    };

    window.onresize = function() {
        init();
    };

    window.onscroll = function() {
        ticks = 0;
    };

};

var myp5 = new p5(s);