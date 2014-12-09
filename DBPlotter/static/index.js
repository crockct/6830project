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
                // TODO: remove the line below this
                // table_names.push('<li><button class="table-name">tablename1</button></li>');
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
        var tablename = $(this).text();
        $.ajax({
            type: "GET",
            url: "/make_queries/",
            data: {
                "table_name": $(this).text()
            },
            success: function(data) {
                $.each(data, function(card_type, card_query) {
                    var card_data = getCardData(card_type, card_query);
                    addSmartCard(card_type, card_query, card_data);
                });
            }
        });
    });
};

// sends a card type and SQL query to the server
// receives all data necessary to render the SQL query for the given card type
var getCardData = function(card_type, card_query) {
    var local_data;
    $.ajax({
        type: "GET",
        url: "/process_query/",
        async: false,
        data: {
            "chart_type": card_type,
            "query": card_query
        },
        success: function(data) {
            local_data = data;
        }
    });
    return local_data;
};

// adds a card to the UI and renders the given card_type chart on the card
var addSmartCard = function(card_type, card_query, data) {
    $.get("card.html").done(function(newCard) {
        newCard = $(newCard);
        newCard.attr('id', '').data('card-type', card_type);
        newCard.find(".execute-button").data('card-type', card_type);
        newCard.find("#query").val(card_query);
        newCard.find(".flipper").removeClass("flip");
        attachCardBtnListeners(newCard);
        addChart(card_type, newCard, data);
        $("#cards").append(newCard);
    });
};

function addChart(card_type, card, data) {
    switch (card_type) {
    case "pie_chart":
        card = addPieChart(data, card);
        break;
    case "histogram":
        card = addHistogram(data, card);
        break;
    case "line_chart":
        card = addLineChart(data, card);
        break;
    default:
        console.log("error: cannot render card type '" + card_type + "'");
    }
}

// returns random colors
function getRandomColor() {
    var letters = '0123456789ABCDEF'.split('');
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

// renders a pie chart on a card
var addPieChart = function(data, newCard) {
    var pie_data = [];
    $.each(data, function(key, val) {
        pie_data.push({
            value: val,
            label: key,
            color: getRandomColor()
        });
    });
    var canvas = newCard.find("canvas")[0];
    var ctx = canvas.getContext("2d");
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    var myPieChart = new Chart(ctx).Pie(pie_data, {});
    return newCard;
};

// renders a histogram on a card
var addHistogramChart = function(data, newCard) {
    var canvas = newCard.find("canvas")[0];
    var ctx = canvas.getContext("2d");
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    var myLineChart = new Chart(ctx).Bar(data, {});
    return newCard;
};

// renders a line chart on a card
var addLineChart = function(data, newCard) {
    var canvas = newCard.find("canvas")[0];
    var ctx = canvas.getContext("2d");
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    var myLineChart = new Chart(ctx).Line(data, {});
    return newCard;
};

// adds a card to the UI for the given type
var addCard = function(card_type) {
    $.get("card.html").done(function(newCard) {
        newCard = $(newCard);
        newCard.attr('id', '').data('card-type', card_type);
        newCard.find(".execute-button").data('card-type', card_type);
        attachCardBtnListeners(newCard);
        $("#cards").prepend(newCard);
        newCard.find("#query").focus().select();
    });
};

function attachCardBtnListeners(card) {
    removeCardBtnEvent(card);
    flipCardButtonEvent(card);
    executeQueryBtnEvent(card);
    editQueryBtnEvent(card);
}

function removeCardBtnEvent(card) {
    var removeCardBtn = card.find(".remove-button");
    removeCardBtn.on('click', function(e) {
        e.preventDefault();
        $(this).closest('.chart-card').remove();
    });
}

function flipCardButtonEvent(card) {
    var flipCardButton = card.find(".flip-button");
    flipCardButton.on('click', function(e) {
        e.preventDefault();
        $(this).closest('.flipper').toggleClass("flip");
    });
}

function executeQueryBtnEvent(card) {
    var executeQueryBtn = card.find(".execute-button");
    executeQueryBtn.on('click', function(e) {
        e.preventDefault();
        var card = $(this).closest('.chart-card');
        $(this).closest('.flipper').removeClass("flip");
        var card_type = card.data("card-type");
        var card_query = card.find("#query").val();
        var card_data = getCardData(card_type, card_query);
        addChart(card_type, card, card_data);
    });
}

function editQueryBtnEvent(card) {
    var editQueryBtn = card.find(".edit-button");
    editQueryBtn.on('click', function(e) {
        e.preventDefault();
        var card = $(this).closest('.chart-card');
        $(this).closest('.flipper').addClass("flip");
        card.find("#query").focus().select();
    });
}