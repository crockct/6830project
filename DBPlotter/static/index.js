$(document).ready(function() {
    $.ajax({
        url: "/close/",
        async: false,
        success: function(data) {
            console.log(data);
            filepathBtnEvent();
            $("#filepath").focus().select();
        }
    });
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
                for (var i in data) {
                    table_names.push('<li><button class="table-name" id="' + data[i] + '">' + data[i] + '</button></li>');
                }
                $('#tables-list').html(table_names.join(''));
                tableNameBtnEvent();
            }
        });
    });
};

// this function is called every time a table name is clicked on--
// it hides the instructions and displays the cards for the selected table,
// asks the server to compute an intelligent query for each card type,
// and displays the query result on its respective card
var tableNameBtnEvent = function() {
    $(".table-name").on("click", function(e) {
        e.preventDefault();
        // hide instructions
        $("#instructions").hide();
        // clear out old cards
        $("#cards").html('');
        // display cards
        $("#card-div").show();
        var table_name = $(this).text();
        $.ajax({
            type: "GET",
            url: "/make_queries/",
            data: {
                "table_name": table_name
            },
            success: function(data) {
                $(".selected-table-name").text(table_name);
                $.each(data, function(card_type, card_query) {
                    // add a new blank card to the UI
                    var newCard = addCard(card_type, card_query);
                    executeQuery(newCard, card_type, card_query);
                });
            }
        });
    });
};