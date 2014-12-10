/*var data = [
	{"text": "chicken", "count": 10}, 
	{"text": "dog", "count": 30},
	{"text": "rabbit", "count": 100},
	{"text": "human", "count": 1}];
console.log(data);
*/

var Bubbles = function() {
  var chart, clear, click, collide, collisionPadding, connectEvents, force, gravity, hashchange, height, idValue, jitter, label, margin, maxRadius, minCollisionRadius, mouseout, mouseover, node, rScale, rValue, textValue, tick, transformData, update, updateActive, updateLabels, updateNodes, width;
  width = 980;
  height = 510;
  node = null;
  label = null;
  margin = {
    top: 5,
    right: 0,
    bottom: 0,
    left: 0
  };
  maxRadius = 65;
  
  // scale used to size the bubbles
  rScale = d3.scale.sqrt().range([0, maxRadius]);
  rValue = function(d) {
	console.log("d count - should be int: " + d.count);
	var intD = parseInt(d.count);
	if (isNaN(intD)){
		intD = 0;
	}
    return intD;
  };
  
  //function to define the 'id' of a data element
  //  - used to bind the data uniquely to the force nodes
  //   and for url creation
  //  - should make it easier to switch out dataset
  //  for your own
  idValue = function(d) {
    return d.text;
  };
  
  //function to define what to display in each bubble
  //again, abstracted to ease migration to 
  //  a different dataset if desired
  textValue = function(d) {
    return d.text;
  };
  
  // collision constants 
  collisionPadding = 4;
  minCollisionRadius = 12;
  
  // force layout variables
  jitter = 0.5;
   
  /*
   tick callback function will be executed for every
   iteration of the force simulation
   - moves force nodes towards their destinations
   - deals with collisions of force nodes
   - updates visual bubbles to reflect new force node locations
  */
  tick = function(e) {
    var dampenedAlpha;
    dampenedAlpha = e.alpha * 0.1;
    node.each(gravity(dampenedAlpha)).each(collide(jitter)).attr("transform", function(d) {
      return "translate(" + d.x + "," + d.y + ")";
    });
    return label.style("left", function(d) {
      return ((margin.left + d.x) - d.dx / 2) + "px";
    }).style("top", function(d) {
      return ((margin.top + d.y) - d.dy / 2) + "px";
    });
  };
  
  /* The force variable is the force layout controlling the bubbles
  # here we disable gravity and charge as we implement custom versions
  # of gravity and collisions for this visualization */
  force = d3.layout.force().gravity(0).charge(0).size([width, height]).on("tick", tick);
  
  /* ---
  # Creates new chart function. This is the 'constructor' of our
  #  visualization
  # Check out http://bost.ocks.org/mike/chart/ 
  #  for a explanation and rational behind this function design */
  chart = function(selection) {
    return selection.each(function(rawData) {
	  console.log("selection: ");
	  console.log(selection);
	  console.log("rawdata");
	  console.log(rawData);
      var maxDomainValue, svg, svgEnter;
      maxDomainValue = d3.max(data, function(d) {
        return rValue(d);
      });
      rScale.domain([0, maxDomainValue]);
	  
	  
	  // set up svg element
      svg = d3.select(this).selectAll("svg").data([data]);
      svgEnter = svg.enter().append("svg");
      svg.attr("width", width + margin.left + margin.right);
      svg.attr("height", height + margin.top + margin.bottom);
	  
	  // node used to group the bubbles
      node = svgEnter.append("g").attr("id", "bubble-nodes").attr("transform", "translate(" + margin.left + "," + margin.top + ")");
      node.append("rect").attr("id", "bubble-background").attr("width", width).attr("height", height).on("click", clear);
      
	  label = d3.select(this).selectAll("#bubble-labels").data([data]).enter().append("div").attr("id", "bubble-labels");
      update();
      hashchange();
      return d3.select(window).on("hashchange", hashchange);
    });
  };
  update = function() {
    /* add a radius to our data nodes that will serve to determine
    # when a collision has occurred. This uses the same scale as
    # the one used to size our bubbles, but it kicks up the minimum
    # size to make it so smaller bubbles have a slightly larger 
    # collision 'sphere' */
    data.forEach(function(d, i) { // i seems to be an index
	  console.log(d); 
	  console.log("that was d, next is i");
	  console.log(i);
      return d.forceR = Math.max(minCollisionRadius, rScale(rValue(d)));
    });
    force.nodes(data).start();
    updateNodes();
    return updateLabels();
  };
  updateNodes = function() {
    node = node.selectAll(".bubble-node").data(data, function(d) {
      return idValue(d);
    });
    node.exit().remove();
    return node.enter().append("a").attr("class", "bubble-node").attr("xlink:href", function(d) {
      return "#" + (encodeURIComponent(idValue(d)));
    }).call(force.drag).call(connectEvents).append("circle").attr("r", function(d) {
      return rScale(rValue(d));
    });
  };
  updateLabels = function() {
    var labelEnter;
    label = label.selectAll(".bubble-label").data(data, function(d) {
      return idValue(d);
    });
    label.exit().remove();
    labelEnter = label.enter().append("a").attr("class", "bubble-label").attr("href", function(d) {
      return "#" + (encodeURIComponent(idValue(d)));
    }).call(force.drag).call(connectEvents);
    labelEnter.append("div").attr("class", "bubble-label-name").text(function(d) {
      return textValue(d);
    });
    labelEnter.append("div").attr("class", "bubble-label-value").text(function(d) {
      return rValue(d);
    });
    label.style("font-size", function(d) {
      return Math.max(8, rScale(rValue(d) / 2)) + "px";
    }).style("width", function(d) {
      return 2.5 * rScale(rValue(d)) + "px";
    });
    label.append("span").text(function(d) {
      return textValue(d);
    }).each(function(d) {
      return d.dx = Math.max(2.5 * rScale(rValue(d)), this.getBoundingClientRect().width);
    }).remove();
    label.style("width", function(d) {
      return d.dx + "px";
    });
    return label.each(function(d) {
      return d.dy = this.getBoundingClientRect().height;
    });
  };
  gravity = function(alpha) {
    var ax, ay, cx, cy;
    cx = width / 2;
    cy = height / 2;
    ax = alpha / 8;
    ay = alpha;
    return function(d) {
      d.x += (cx - d.x) * ax;
      return d.y += (cy - d.y) * ay;
    };
  };
  collide = function(jitter) {
    return function(d) {
      return data.forEach(function(d2) {
        var distance, minDistance, moveX, moveY, x, y;
        if (d !== d2) {
          x = d.x - d2.x;
          y = d.y - d2.y;
          distance = Math.sqrt(x * x + y * y);
          minDistance = d.forceR + d2.forceR + collisionPadding;
          if (distance < minDistance) {
            distance = (distance - minDistance) / distance * jitter;
            moveX = x * distance;
            moveY = y * distance;
            d.x -= moveX;
            d.y -= moveY;
            d2.x += moveX;
            return d2.y += moveY;
          }
        }
      });
    };
  };
  connectEvents = function(d) {
    d.on("click", click);
    d.on("mouseover", mouseover);
    return d.on("mouseout", mouseout);
  };
  clear = function() {
    return location.replace("#");
  };
  click = function(d) {
    location.replace("#" + encodeURIComponent(idValue(d)));
    return d3.event.preventDefault();
  };
  hashchange = function() {
    var id;
    id = decodeURIComponent(location.hash.substring(1)).trim();
    return updateActive(id);
  };
  updateActive = function(id) {
    node.classed("bubble-selected", function(d) {
      return id === idValue(d);
    });
    if (id.length > 0) {
      return d3.select("#status").html("<h3>The word <span class=\"active\">" + id + "</span> is now active</h3>");
    } else {
      return d3.select("#status").html("<h3>No word is active</h3>");
    }
  };
  mouseover = function(d) {
    return node.classed("bubble-hover", function(p) {
      return p === d;
    });
  };
  mouseout = function(d) {
    return node.classed("bubble-hover", false);
  };
  chart.jitter = function(_) {
    if (!arguments.length) {
      return jitter;
    }
    jitter = _;
    force.start();
    return chart;
  };
  chart.height = function(_) {
    if (!arguments.length) {
      return height;
    }
    height = _;
    return chart;
  };
  chart.width = function(_) {
    if (!arguments.length) {
      return width;
    }
    width = _;
    return chart;
  };
  chart.r = function(_) {
    if (!arguments.length) {
      return rValue;
    }
    rValue = _;
    return chart;
  };
  return chart;
};

plotData = function(selector, data, plot) {
  return d3.select(selector).datum(data).call(plot);
};

var makeBubbleChartFunction = function(data) {
  console.log("make bubble chart function");
  console.log(data);
  var plot = Bubbles();
  console.log(plot);
  var display = function(data) {
    var x = plotData("#vis", data, plot);
	console.log(x);
	return x;
  };
  console.log(display);

  d3.select("#jitter").on("input", function() {
    return plot.jitter(parseFloat(this.output.value));
  });
 
};