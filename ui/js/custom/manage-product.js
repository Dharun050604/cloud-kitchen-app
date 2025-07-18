var productModal = $("#productModal");
var selectedProductId = null;

$(function () {
    // Load all products
    $.get("http://127.0.0.1:5000/getProducts", function (response) {
        if(response) {
            var table = '';
            $.each(response, function(index, product) {
                table += '<tr data-id="'+ product.product_id +'" data-name="'+ product.name +'" data-unit="'+ product.uom_id +'" data-price="'+ product.price_per_unit +'">' +
                    '<td>'+ product.name +'</td>'+
                    '<td>'+ product.uom_name +'</td>'+
                    '<td>'+ product.price_per_unit +'</td>'+
                    '<td>'+
                        '<span class="btn btn-xs btn-primary edit-product">Edit</span> '+
                        '<span class="btn btn-xs btn-danger delete-product">Delete</span>'+
                    '</td></tr>';
            });
            $("table").find('tbody').empty().html(table);
        }
    });
});

// Save Product (Insert or Update)
$("#saveProduct").on("click", function () {
    var requestPayload = {
        product_id: selectedProductId,
        product_name: $("#name").val(),
        uom_id: $("#uoms").val(),
        price_per_unit: $("#price").val()
    };

    var url = selectedProductId ? "http://127.0.0.1:5000/updateProduct" : "http://127.0.0.1:5000/insertProduct";

    $.ajax({
        url: url,
        type: "POST",
        data: JSON.stringify(requestPayload),
        contentType: "application/json",
        success: function(res) {
            console.log("Saved:", res);
            window.location.reload();
        }
    });
});

// Delete Product
$(document).on("click", ".delete-product", function (){
    var tr = $(this).closest('tr');
    var productId = tr.data('id');
    var isDelete = confirm("Are you sure to delete "+ tr.data('name') +"?");

    if (isDelete) {
        $.ajax({
            url: "http://127.0.0.1:5000/deleteProduct",
            type: "POST",
            data: JSON.stringify({ product_id: productId }),
            contentType: "application/json",
            success: function(res) {
                console.log("Deleted:", res);
                window.location.reload();
            }
        });
    }
});

// Edit Product - populate modal
$(document).on("click", ".edit-product", function (){
    var tr = $(this).closest('tr');
    selectedProductId = tr.data('id');
    $("#name").val(tr.data('name'));
    $("#price").val(tr.data('price'));
    $("#productModal").find('.modal-title').text('Edit Product');

    // Load UOMs and set selected
    $.get("http://127.0.0.1:5000/getUOM", function (response) {
        if(response) {
            var options = '<option value="">--Select--</option>';
            $.each(response, function(index, uom) {
                options += '<option value="'+ uom.uom_id +'" '+(uom.uom_id==tr.data('unit') ? 'selected' : '')+'>'+ uom.uom_name +'</option>';
            });
            $("#uoms").empty().html(options);
            productModal.modal('show');
        }
    });
});

// Reset modal on close
productModal.on('hide.bs.modal', function(){
    selectedProductId = null;
    $("#name, #price").val('');
    $("#uoms").empty();
    productModal.find('.modal-title').text('Add New Product');
});

// Populate UOM on opening add modal
productModal.on('show.bs.modal', function(){
    if(!selectedProductId) {
        $.get("http://127.0.0.1:5000/getUOM", function (response) {
            if(response) {
                var options = '<option value="">--Select--</option>';
                $.each(response, function(index, uom) {
                    options += '<option value="'+ uom.uom_id +'">'+ uom.uom_name +'</option>';
                });
                $("#uoms").empty().html(options);
            }
        });
    }
});
