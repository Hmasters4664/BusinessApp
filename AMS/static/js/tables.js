$(document).ready(function() {
    var dt_table = $('#tb1').dataTable({
         language: dt_language,  // global variable defined in html
        order: [[ 0, "desc" ]],
        lengthMenu: [[25, 50, 100, 200], [25, 50, 100, 200]],
        columnDefs: [
            {orderable: true,
             searchable: true,
             className: "data",
             targets: [0, 1]
            },
            {
                name: 'acquisition_date',
                targets: [0]
            },
            {
                name: 'asset_id',
                targets: [1]
            }
        ],
        searching: true,
        processing: true,
        serverSide: true,
        stateSave: true,
        ajax:"{% url 'asset_list' %}",
        columns: [
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


