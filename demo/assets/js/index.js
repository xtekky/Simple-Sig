$('#test').click(function() {

    data = 'username=grgrg&password=1234'

    config = {
        headers: {
            ...x(data),
        },
        body   : data,
        method : "POST",
        mode   : "cors",
    }

    fetch("/test", config);

});
