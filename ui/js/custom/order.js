var productPrices = {};

$(function () {
    $.get(productListApiUrl, function (response) {
        productPrices = {};
        if(response) {
            var options = '<option value="">--Select--</option>';
            $.each(response, function(index, product) {
                options += '<option value="'+ product.product_id +'">'+ product.name +'</option>';
                productPrices[product.product_id] = product.price_per_unit;
            });
            $(".product-box").find("select").empty().html(options);
        }
    });
});

$("#addMoreButton").click(function () {
    var row = $(".product-box").html();
    $(".product-box-extra").append(row);
    $(".product-box-extra .remove-row").last().removeClass('hideit');
    $(".product-box-extra .product-price").last().val('0.0');
    $(".product-box-extra .product-qty").last().val('1');
    $(".product-box-extra .product-total").last().val('0.0');
});

$(document).on("click", ".remove-row", function (){
    $(this).closest('.row').remove();
    calculateValue();
});

$(document).on("change", ".cart-product", function (){
    var product_id = $(this).val();
    var price = productPrices[product_id];
    $(this).closest('.row').find('#product_price').val(price);
    calculateValue();
});

$(document).on("change", ".product-qty", function (){
    calculateValue();
});

function calculateValue() {
    var grandTotal = 0.0;
    $(".product-box-extra .row").each(function(){
        var price = parseFloat($(this).find("#product_price").val() || 0);
        var qty = parseFloat($(this).find(".product-qty").val() || 1);
        var total = price * qty;
        $(this).find("#item_total").val(total.toFixed(2));
        grandTotal += total;
    });
    $("#product_grand_total").val(grandTotal.toFixed(2));
}

$("#saveOrder").on("click", function(){
    var customerName = $("#customerName").val().trim();
    var grandTotal = $("#product_grand_total").val();

    var orderDetails = [];
    var hasInvalidRow = false;
    var errorMessage = "";

    $(".product-box-extra .row").each(function(){
        var product_id = $(this).find(".cart-product").val();
        var qty = $(this).find(".product-qty").val();
        var total = $(this).find("#item_total").val();

        if (!product_id) {
            hasInvalidRow = true;
            errorMessage = "Please select a valid product for all items.";
            return false; // breaks each loop
        }

        if (!qty || parseFloat(qty) <= 0) {
            hasInvalidRow = true;
            errorMessage = "Quantity must be greater than zero for all products.";
            return false;
        }

        orderDetails.push({
            product_id: product_id,
            quantity: qty,
            total_price: total
        });
    });

    if (customerName === "") {
        alert("Customer name cannot be empty.");
        return;
    }

    if (orderDetails.length === 0) {
        alert("Please add at least one product to the order.");
        return;
    }

    if (hasInvalidRow) {
        alert(errorMessage);
        return;
    }

    var requestPayload = {
        customer_name: customerName,
        grand_total: grandTotal,
        order_details: orderDetails
    };

    console.log("Sending order payload:", requestPayload);

    fetch(orderSaveApiUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(requestPayload)
    })
    .then(response => {
        if (!response.ok) throw new Error("Network error: " + response.statusText);
        return response.json();
    })
    .then(data => {
        console.log("Order saved successfully", data);
        alert("Order placed successfully!");
        location.reload();
    })
    .catch(error => {
        console.error("Failed to save order:", error);
        alert("Failed to place order.");
    });
});
