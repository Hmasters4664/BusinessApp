$(function() {
    $('#find').click(function() {
        $.ajax({
            url: "{% url 'search' %}",
           data: {'search': document.getElementById('txtSearch').value,},
            type: 'GET',
            success: function(data) {

                data = JSON.parse(data);
                $('#searchBody').html('');
                for (i in data){
                $('#searchBody').append(
                    "<tr>" +
                    "<td>" + data[i][0] + "</td>" +
                    "<td>" + data[i][1] + "</td>" +
                    "<td>" + data[i][2] + "</td>" +
                    "<td>" + data[i][3] + "</td>" +
                    "<td>" + data[i][4] + "</td>" +
                    "<td>" + data[i][5] + "</td>" +
                    "<td>" + data[i][6] + "</td>" +
                    "<td>" + data[i][7] + "</td>" +
                    "<td>" + data[i][8] + "</td>" +
                    "</tr>");
                    console.log(data);
                };
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});

