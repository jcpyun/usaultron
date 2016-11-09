// // d3.select("p").text("wow");
// // d3.select("body").append("p").style("color","red").text("hi whats up");

// // https://www.youtube.com/watch?v=_4BGBXTHKsA
// var dataArray=[20,40,50];

// var canvas= d3.select("body")
//     .append("svg")
//     .attr("width",500)
//     .attr("height",500);
// var bars=canvas.selectAll("rect")
//     .data(dataArray)
//     .enter()
//         .append("rect")
//         .attr("width",function(d){ return d*10;})
//         .attr("height",50)
//         .attr("y",function(d,i){return i*100 });
// // // var circle = canvas.append("circle")
// //     .attr("cx",250)
// //     .attr("cy",250)
// //     .attr("r",50)
// //     .attr("fill","red");
// // var rect= canvas.append("rect")
// //     .attr("width",100)
// //     .attr("height",50);
// // var line= canvas.append("line")
// //     .attr("x1",0)
// //     .attr("y1",100)
// //     .attr("x2",400)
// //     .attr("y2",400)
// //     .attr("stroke","green")
// //     .attr("stroke-width",10)