var myPieChart;
var myHistogramChart;

$(document).ready(function() {
    flipCardButtonEvent();
})

function getRandomColor() {
    var letters = '0123456789ABCDEF'.split('');
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

function runQuery(chartType) {
    document.getElementById("execute-button").innerHTML = '<i class="fa fa-spinner"></i>';

    $.ajax({
        dataType: "json",
        url: "/pie_chart/?d=".concat($('#dbfile').val()).concat("&q=").concat($('#query').val().replace(/\n/g, " ").replace(";", "")),
        success: function(data) {
            var pie_data = [];

            $.each(data, function(key, val) {
                pie_data.push({
                    value: val,
                    label: key,
                    color: getRandomColor()
                });
            });

            document.getElementById("execute-button").innerHTML = '<i class="fa fa-line-chart"></i>';
            //document.getElementById("results-title-span").textContent = 'Pie Chart of Results';

            document.querySelector(".flipper").classList.toggle("flip")
            var canvas = document.getElementById("myChart");
            var ctx = canvas.getContext("2d");
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            myPieChart = new Chart(ctx).Pie(pie_data, {});
        }
    });

}

function runQueryPieChart() {
    document.getElementById("execute-button").innerHTML = '<i class="fa fa-spinner"></i>';

    $.ajax({
        dataType: "json",
        url: "/pie_chart/?d=".concat($('#dbfile').val()).concat("&q=").concat($('#query').val().replace(/\n/g, " ").replace(";", "")),
        success: function(data) {
            var pie_data = [];

            $.each(data, function(key, val) {
                pie_data.push({
                    value: val,
                    label: key,
                    color: getRandomColor()
                });
            });

            document.getElementById("execute-button").innerHTML = '<i class="fa fa-line-chart"></i>';
            //document.getElementById("results-title-span").textContent = 'Pie Chart of Results';

            document.querySelector(".flipper").classList.toggle("flip")
            var canvas = document.getElementById("myPieChart");
            var ctx = canvas.getContext("2d");
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            myPieChart = new Chart(ctx).Pie(pie_data, {});
        }
    });
}

function runQueryWordCloud() {
    document.getElementById("execute-button").innerHTML = '<i class="fa fa-spinner"></i>';

    $.ajax({
        dataType: "json",
        url: "http://127.0.0.1:8000/pie_chart/?d=".concat($('#dbfile').val()).concat("&q=").concat($('#query').val().replace(/\n/g, " ").replace(";", "")),
        success: function(data) {
            var pie_data = [];

            $.each(data, function(key, val) {
                pie_data.push({
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

function runQueryHistogram() {
    document.getElementById("execute-button").innerHTML = '<i class="fa fa-spinner"></i>';

    $.ajax({
        dataType: "json",
        url: "http://127.0.0.1:8000/pie_chart/?d=".concat($('#dbfile').val()).concat("&q=").concat($('#query').val().replace(/\n/g, " ").replace(";", "")),
        success: function(data) {
            var hist_data = [];

            $.each(data, function(key, val) {
                hist_data.push({
                    value: val,
                    label: key,
                    color: getRandomColor()
                });
            });

            document.getElementById("execute-button").innerHTML = '<i class="fa fa-line-chart"></i>';
            //document.getElementById("results-title-span").textContent = 'Pie Chart of Results';

            document.querySelector(".flipper").classList.toggle("flip")
            var canvas = document.getElementById("myHistogram");
            var ctx = canvas.getContext("2d");
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            myHistogramChart = new Chart(ctx).Bar(hist_data, {});
        }
    });
}


function flipCardButtonEvent() {
    $('.edit-button').on('click', function(e) {
        e.preventDefault();
        $(this).closest('.flipper').toggleClass("flip");
    })
}


var addPieChart = function addPieChart() {
	$('#cardcontainer').prepend('<div class="container">  <div class="flipper flip"> <div class="card"> <div class="front"> <div class="card-instructions" id="back-instructions"><span id="results-title-span" class="results-title"></span><span class="edit-button"><i class="fa fa-terminal"></i></span></div><div class="pie-chart"><canvas id="myPieChart" width="520" height="260"></canvas></div> </div><div class="back"><div class="card-instructions" id="front-instructions">SQL Query<span id="execute-button" class="run-button" onclick="runQueryPieChart()"><i class="fa fa-line-chart"></i></span></div><textarea id="query" spellcheck="false">Enter a query...</textarea></div></div></div></div>');
}


//TODO fix chart type in html
var addBarChart = function addBarChart() {
	$('#cardcontainer').prepend('<div class="container">  <div class="flipper flip"> <div class="card"> <div class="front"> <div class="card-instructions" id="back-instructions"><span id="results-title-span" class="results-title"></span><span class="edit-button"><i class="fa fa-terminal"></i></span></div><div class="pie-chart"><canvas id="myPieChart" width="520" height="260"></canvas></div> </div><div class="back"><div class="card-instructions" id="front-instructions">SQL Query<span id="execute-button" class="run-button" onclick="runQueryPieChart()"><i class="fa fa-line-chart"></i></span></div><textarea id="query" spellcheck="false">Enter a query...</textarea></div></div></div></div>');
}

// TODO fix chart type in html
var addLineChart = function addLineChart() {
	$('#cardcontainer').prepend('<div class="container">  <div class="flipper flip"> <div class="card"> <div class="front"> <div class="card-instructions" id="back-instructions"><span id="results-title-span" class="results-title"></span><span class="edit-button"><i class="fa fa-terminal"></i></span></div><div class="pie-chart"><canvas id="myPieChart" width="520" height="260"></canvas></div> </div><div class="back"><div class="card-instructions" id="front-instructions">SQL Query<span id="execute-button" class="run-button" onclick="runQueryPieChart()"><i class="fa fa-line-chart"></i></span></div><textarea id="query" spellcheck="false">Enter a query...</textarea></div></div></div></div>');
}

var removeChart = function removeChart() {
	console.log("remove chart!");
}