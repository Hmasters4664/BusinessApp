$(document).ready(function() {
    var dt_table = $('#tb1').dataTable({
        "processing": true,
        "serverSide": true,
         "ajax":"{% url 'asset_list' %}",
         "columns": [
            { "data": "asset_id" },
            { "data": "acquisition_date" },
            { "data": "asset_name" },
            { "data": "description" },
            { "data": "asset_type" },
            { "data": "asset_barcode" },
            { "data": "asset_serial_number" },
            { "data": "asset_location_id" },
            { "data": "asset_status" },
            { "data": "asset_owner" },
            { "data": "asset_department" },
            { "data": "added_date" },
            {"data":  "modified_date"}
        ]
    });
});


