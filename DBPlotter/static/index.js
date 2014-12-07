$(document).ready(function() {
    filepathBtnEvent();
});

// sends the DB filepath to the server and requests the list of table names for the given DB
var filepathBtnEvent = function() {
    $("#filepath-btn").on("click", function(e) {
        e.preventDefault();
        $.ajax({
            type: "GET",
            url: "/get_tables/",
            data: {
                "f": $('#filepath').val()
            },
            success: function(data) {
                table_names = [];
                table_names.push('<li><button class="table-name">tablename1</button></li>');
                for (i in data) {
                    // table_names.push('<li><a href="tablecard?id=' + data[i] + '">' + data[i] + '</a></li>');
                    table_names.push('<li><button class="table-name" id="' + data[i] + '">' + data[i] + '</button></li>');
                }
                $('#tables-list').html(table_names.join(''));
                tableNameBtnEvent();
            }
        })
    });
}

// this function is called every time a table name is clicked on--
// it hides the instructions and displays the cards for the selected table
var tableNameBtnEvent = function() {
    $(".table-name").on("click", function(e) {
        e.preventDefault();
        // hide instructions
        $("#instructions").hide();
        // display cards
        $("#cards").show();
        var tablename = $(this).text();
        console.log("getting card info for table: " + tablename);
        getPieChartInfo(tablename);
        // getWordCloudInfo(tablename);
        // getHistogramInfo(tablename);
    })
}

// request all info needed to display the pie chart card for the given table
var getPieChartInfo = function(tablename) {
    $.ajax({
        // type: "GET",
        dataType: "json",
        url: "/pie_chart/",
        data: {
            "tablename": tablename
        },
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

// request all info needed to display the word cloud card for the given table
var getWordCloudInfo = function(tablename) {
    $.ajax({
        // type: "GET",
        dataType: "json",
        url: "/word_cloud/",
        data: {
            "tablename": tablename
        },
        success: function(data) {}
    })
}

// request all info needed to display the histogram card for the given table
var getHistogramInfo = function(tablename) {
    $.ajax({
        // type: "GET",
        dataType: "json",
        url: "/histogram/",
        data: {
            "tablename": tablename
        },
        success: function(data) {}
    })
}