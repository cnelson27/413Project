$((function(context) {
    return function() {

        $.ajax({
            "url": "/catalog/index.tile1/"
        }).done(function(data) {
            console.log("IT'S BACK");
            console.log(data)
        });
    }
})(DMP_CONTEXT.get()));