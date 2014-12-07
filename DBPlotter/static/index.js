$(document).ready(function() {
    filepathBtnEvent();
    tableNameBtnEvent();
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