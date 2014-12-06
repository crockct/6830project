$(document).ready(function() {
    filepathBtnEvent();
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
                for (i in data){
                    table_names.push('<li><a href="yourlink?id=' + data[i] + '">' + data[i] + '</a></li>');
                }
                $('#tables-list').html(table_names.join(''));
            }
        })
    });
}