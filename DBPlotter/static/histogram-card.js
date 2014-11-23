
function getRandomColor() {
    var letters = '0123456789ABCDEF'.split('');
    var color = '#';
    for (var i = 0; i < 6; i++ ) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

// Part 2 (graph on left)

var dataset = [ 5, 10, 13, 19, 21, 25, 22, 18, 15, 13,
                11, 12, 15, 20, 18, 17, 16, 18, 23, 25 ];

//SVG Width and height
var w = 500;
var h = 100;
var spaceBetweenBars = 1;

console.log("histogram card code running");

//Create SVG element
var svg = d3.select("#graphHistogram")
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
