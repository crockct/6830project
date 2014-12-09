$(document).ready(function() {
    $.ajax({
        url: "/close/",
        async: false,
        success: function(data) {
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
            async: false,
            data: {
                "f": $('#filepath').val()
            },
            success: function(data) {
                var table_names = [];
                for (var i in data) {
                    var table_name = data[i];
                    table_names.push('<li><button class="table-name" id="' + table_name + '">' + table_name + '</button></li>');
                    // add the table name to the hash map of table names to cards
                    tableCards[table_name] = {};
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
        $(".selected-table-name").text(table_name);
        var savedTableCards = tableCards[table_name];
        // if there are no saved cards for a table, request cards from the server
        if ($.isEmptyObject(savedTableCards)) {
            $.ajax({
                type: "GET",
                url: "/make_queries/",
                async: false,
                data: {
                    "table_name": table_name
                },
                success: function(data) {
                    $.each(data, function(card_type, card_query) { // add a new blank card to the UI
                        var newCard = addCard(card_type, card_query, 'new');
                        executeQuery(newCard, card_type, card_query);
                    });
                }
            });
        } else {
            var savedtableCards = tableCards[table_name];
            $.each(savedtableCards, function(card_id, info) {
                var newCard = addCard(info.card_type, info.card_query, 'old');
                executeQuery(newCard, info.card_type, info.card_query);
            });
        }
    });
};