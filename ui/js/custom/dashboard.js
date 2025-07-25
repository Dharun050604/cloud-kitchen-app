$(function () {
    console.log("Dashboard loaded!");

    $.get(orderListApiUrl, function (response) {
        console.log("Orders loaded:", response);
        if (response) {
            var table = '';
            var totalCost = 0;
            $.each(response, function (index, order) {
                totalCost += parseFloat(order.total);
                table += '<tr>' +
                    '<td>' + order.datetime + '</td>' +
                    '<td>' + order.order_id + '</td>' +
                    '<td>' + order.customer_name + '</td>' +
                    '<td>' + order.total.toFixed(2) + ' Rs</td>' +
                    '</tr>';
            });
            table += '<tr><td colspan="3" style="text-align: end"><b>Total</b></td><td><b>' + totalCost.toFixed(2) + ' Rs</b></td></tr>';
            $("#ordersTableBody").html(table);
        }
    });
});
