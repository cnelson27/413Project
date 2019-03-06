$((function(context) {
    return function() {
        var containers = $('.product-container');
        containers.each(function(i, container) {
            var pid = $(container).attr('data-product-id');
            $.ajax({
                url: "/catalog/product.tile/" + pid,
            });
        });
    }
})(DMP_CONTEXT.get()));