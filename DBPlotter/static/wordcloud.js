var diameter = 960,
    format = d3.format(",d"),
    color = d3.scale.category20c();

var bubble = d3.layout.pack()
    .sort(null)
    .size([diameter, diameter])
    .padding(1.5);

var svg = d3.select("body").append("svg")
    .attr("width", diameter)
    .attr("height", diameter)
    .attr("class", "bubble");

// from http://bl.ocks.org/mbostock/4063269 
d3.json("flare.json", function(error, root) {
  var node = svg.selectAll(".node")
      .data(bubble.nodes(classes(root))
      .filter(function(d) { return !d.children; }))
    .enter().append("g")
      .attr("class", "node")
      .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

  node.append("title")
      .text(function(d) { return d.className + ": " + format(d.value); });

  node.append("circle")
      .attr("r", function(d) { return d.r; })
      .style("fill", function(d) { return color(d.packageName); });

  node.append("text")
      .attr("dy", ".3em")
      .style("text-anchor", "middle")
      .text(function(d) { return d.className.substring(0, d.r / 3); });
});

// Returns a flattened hierarchy containing all leaf nodes under the root.
function classes(root) {
  var classes = [];

  function recurse(name, node) {
    if (node.children) node.children.forEach(function(child) { recurse(node.name, child); });
    else classes.push({packageName: name, className: node.name, value: node.size});
  }

  recurse(null, root);
  return {children: classes};
}

d3.select(self.frameElement).style("height", diameter + "px");

function runQueryWordCloud() {
    document.getElementById("execute-button").innerHTML = '<i class="fa fa-spinner"></i>';

    $.ajax({
        dataType: "json",
        url: "http://127.0.0.1:8000/pie_chart/?d=".concat($('#dbfile').val()).concat("&q=").concat($('#query').val().replace(/\n/g, " ").replace(";", "")),
        success: function(data) {
            var word_data = [];

            $.each(data, function(key, val) {
                word_data.push({
                    value: val,
                    label: key,
                    color: getRandomColor()
                });
            });

            document.getElementById("execute-button").innerHTML = '<i class="fa fa-line-chart"></i>';
            //document.getElementById("results-title-span").textContent = 'Pie Chart of Results';

            document.querySelector(".flipper").classList.toggle("flip")
            var canvas = document.getElementById("myWordCloud");
            var ctx = canvas.getContext("2d");
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            myPieChart = new Chart(ctx).Pie(pie_data, {});
        }
    });
}