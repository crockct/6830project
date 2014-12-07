$(document).ready(function() {
    filepathBtnEvent();
    tableClickedEvent();
})



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
                table_names.push('<li><a class="tablename">' + "tablename1" + '</a></li>');
                for (i in data) {
                    table_names.push('<li><a href="tablecard?id=' + data[i] + '">' + data[i] + '</a></li>');
                }
                $('#tables-list').html(table_names.join(''));
            }
        })
    });
}
// called when a table is clicked. Requests that the server make charts for table table_name
// server returns list/array of tuples (chart_type, chart_id)
var tableClickedEvent = function() {
    $(".tablename").on("click", function(e) {
        e.preventDefault();
        $.ajax({
            type: "GET",
            url: "/make_charts/",
            data: {
                "table_name": $(this).text()
            },
            success: function(data) {
                for (i in data) {
                    requestChart(i[0], i[1]);
                }
            }
        })
    });
}

var requestChart = function(chart_type, chart_id) {	
	console.log("requesting chart. chart type, chart id: ");
	console.log(chart_type);
	console.log(chart_id);
	 $.ajax({
            type: "GET",
            url: "/get_chart/",
            data: {
                "id": chart_id
            },
            success: function(data) {
                for (i in data) {
                    console.log(i);
                }
                $('#tables-list').html(table_names.join(''));
            }
        })
}

/*
var tableNameBtnEvent = function() {
    $(".tablename").on("click", function(e) {
        e.preventDefault();
        // get info needed to populate pie chart card
        $.ajax({
            type: "GET",
            url: "/tablecard/",
            data: {
                "tablename": $(this).text()
            },
            success: function(data) {
                table_names = [];
                table_names.push('<li><a class="tablename" href="table?id=' + "tablename1" + '">' + "tablename1" + '</a></li>');
                for (i in data) {
                    table_names.push('<li><a href="table?id=' + data[i] + '">' + data[i] + '</a></li>');
                }
                $('#tables-list').html(table_names.join(''));
            }
        })
    })

}
*/