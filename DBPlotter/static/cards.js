var tableCards = {};

// adds a blank card to the UI for the given type
var addCard = function(card_type, card_query, status) {
    var table_name = $(".selected-table-name").text();
    var card_id = table_name + "-card-" + getRandomColor();
    var newCard;
    $.ajax({
        url: 'card.html',
        async: false,
        success: function(data) {
            newCard = $(data);
        }
    });
    newCard.attr('id', card_id);
    newCard.addClass('col-xs-7');
    newCard.attr('data-card-type', card_type);
    newCard.find(".execute-button").attr('data-card-type', card_type);
    newCard.find(".query-text").text(card_query);
    newCard.find(".chart-type").text(card_type);
    attachCardBtnListeners(newCard);
    $("#cards").prepend(newCard);
    if (status == 'new') {
        tableCards[table_name][card_id] = {
            "card_type": card_type,
            "card_query": card_query
        };
    }
    newCard.find(".query-text").focus().select();
    return newCard;
};

// sends a card type and SQL query to the server
// receives all data necessary to render the SQL query for the given card type
var executeQuery = function(card, card_type, card_query) {
    var chart_data;
    $.ajax({
        type: "GET",
        url: "/process_query/",
        async: false,
        data: {
            "chart_type": card_type,
            "query": card_query
        },
        success: function(data) {
            title = data.title;
            chart_data = data.data;
        }
    });
    addChart(card, card_type, chart_data, title);
    showChart(card);
};

// render the chart on the card given the data
var addChart = function(card, card_type, data, title) {
    card.find(".chart-title").text(title);
    card.find(".canvas-div").html('<canvas class="canvas" width="520" height="260"></canvas>');
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
};

// returns random colors
var getRandomColor = function() {
    var letters = '0123456789ABCDEF'.split('');
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
};

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
var addHistogram = function(data, newCard) {
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

// attach listeners for the remove, flip, edit query, and execute query buttons on a card
var attachCardBtnListeners = function(card) {
    removeCardBtnEvent(card);
    flipCardButtonEvent(card);
    executeQueryBtnEvent(card);
    editQueryBtnEvent(card);
};

// attach listener to the remove button on a card
var removeCardBtnEvent = function(card) {
    var removeCardBtn = card.find(".remove-button");
    removeCardBtn.on('click', function(e) {
        e.preventDefault();
        card.remove();
    });
};

// flip the card over
var flipCard = function(card) {
    card.find(".query").toggleClass('hide');
    card.find(".chart").toggleClass('hide');
    if (!card.find(".query").hasClass('hide')) {
        // put focus on the query textarea
        card.find(".query-text").focus().select();
    }
};

// if the chart is not already shown, flip the card
var showChart = function(card) {
    card.find(".query").addClass('hide');
    card.find(".chart").removeClass('hide');
};

// if the query textarea is not already shown, flip the card
var showQuery = function(card) {
    card.find(".query").removeClass('hide');
    card.find(".chart").addClass('hide');
    // put focus on the query textarea
    card.find(".query-text").focus().select();
};

// attach listener to the flip button on a card
var flipCardButtonEvent = function(card) {
    var flipCardButton = card.find(".flip-button");
    flipCardButton.on('click', function(e) {
        e.preventDefault();
        flipCard(card);
    });
};

// attach listener to the execute query button on a card
var executeQueryBtnEvent = function(card) {
    var executeQueryBtn = card.find(".execute-button");
    executeQueryBtn.on('click', function(e) {
        e.preventDefault();
        var table_name = $(".selected-table-name").text();
        var card_id = card.attr('id');
        var card_type = card.data("card-type");
        var card_query = card.find(".query-text").val();
        tableCards[table_name][card_id]['card_query'] = card_query;
        executeQuery(card, card_type, card_query);
    });
};

// attach listener to the edit query button on a card
var editQueryBtnEvent = function(card) {
    var editQueryBtn = card.find(".edit-button");
    editQueryBtn.on('click', function(e) {
        e.preventDefault();
        // flip the card over to display the query
        showQuery(card);
    });
};

// everything below this is used for testing card.html
// $(document).ready(function() {
// 	var card = $(".card");
// 	attachCardBtnListeners(card);
// });