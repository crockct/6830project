var vis = d3.select("#graphRight")
            .append("svg")
.attr("width", 200).attr("height", 200);

var nodes = [
    {x: 10, y: 50},
    {x: 70, y: 10},
    {x: 140, y: 50}   
  ]

vis.selectAll("circle.nodes")
   .data(nodes)
   .enter()
   .append("svg:circle")
   .attr("cx", function(d) { return d.x; })
   .attr("cy", function(d) { return d.y; })
   .attr("r", "10px")
   .attr("fill", "black");
   
   
// Part 2 (graph on left)

var dataset = [ 5, 10, 13, 19, 21, 25, 22, 18, 15, 13,
                11, 12, 15, 20, 18, 17, 16, 18, 23, 25 ];

//SVG Width and height
var w = 500;
var h = 100;
var spaceBetweenBars = 1;

//Create SVG element
var svg = d3.select("#graphLeft")
            .append("svg")
            .attr("width", w)
            .attr("height", h)
			.attr("fill", "teal");
			
svg.selectAll("rect")
   .data(dataset)
   .enter()
   .append("rect")
   .attr("x", function(d, i) {
		return i * (w / dataset.length);
	})
   .attr("y", function(d) {
		return h - d;  //Height minus data value, since we start drawing from the top of the bar
	})
   .attr("width", w / dataset.length - spaceBetweenBars)
   .attr("height", function(d) {
		return d;
	});