// $(document).ready(function() {
//     flipCardButtonEvent();
// });

// function runQuery(chartType) {
//     document.getElementById("execute-button").innerHTML = '<i class="fa fa-spinner"></i>';

//     $.ajax({
//         dataType: "json",
//         url: "/pie_chart/?d=".concat($('#dbfile').val()).concat("&q=").concat($('#query').val().replace(/\n/g, " ").replace(";", "")),
//         success: function(data) {
//             var pie_data = [];

//             $.each(data, function(key, val) {
//                 pie_data.push({
//                     value: val,
//                     label: key,
//                     color: getRandomColor()
//                 });
//             });

//             document.getElementById("execute-button").innerHTML = '<i class="fa fa-line-chart"></i>';
//             //document.getElementById("results-title-span").textContent = 'Pie Chart of Results';

//             document.querySelector(".flipper").classList.toggle("flip");
//             var canvas = document.getElementById("myChart");
//             var ctx = canvas.getContext("2d");
//             ctx.clearRect(0, 0, canvas.width, canvas.height);
//             myPieChart = new Chart(ctx).Pie(pie_data, {});
//         }
//     });
// }

// function flipCardButtonEvent(flipCardButton) {
//     flipCardButton.on('click', function(e) {
//         e.preventDefault();
//         $(this).closest('.flipper').toggleClass("flip");
//     });
// }

// var removeChart = function removeChart() {
// 	console.log("remove chart!");
// };