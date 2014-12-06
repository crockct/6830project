$(document).ready(function() {
    filepathBtnEvent();
})

var filepathBtnEvent = function() {
    $("#filepath-btn").on("click", function(e) {
        e.preventDefault();
        $.ajax({
            type: "GET",
            // contentType: "application/json; charset=utf-8",
            // dataType: "json",
            url: "/get_tables/",
            // url: "http://127.0.0.1:8000/get_tables/?f=".concat($('#filepath').val()),
            data: {
                "filepath": $('#filepath').val()
            },
            success: function(data) {
                table_names = [];
                for (i in data){
                    table_names.push('<li><a href="yourlink?id=' + data[i] + '">' + data[i] + '</a></li>');
                }
                $('#tables-list').html(table_names.join(''));
            }
        })
    });
}