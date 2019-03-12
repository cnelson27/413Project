console.log("Here");

$(
    (function(context) {
    return function() {
        var containers = $('.product-container');
        console.log(111, containers);
        containers.each(function(i, container) {
            console.log(222, container);
            console.log(333, $(container));
            var pid = $(container).attr('data-product-id');
            console.log(444, pid);
            $.ajax({
                url: "/catalog/product.tile/" + pid,
            }).done(function(content) {
                $(container).html(content);
            });
        });
    };
})(DMP_CONTEXT.get())
);