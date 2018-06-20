
        $(document).ready(function () {
            $.ajax({
                url: '/getdata',
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    // Prints the retrieved JSON data into a table
                    $('#RetriveTable').DataTable({
                        responsive: true,
                        data: data.rowValues,
                        columns: [
                            { 'data': 'title' },
                            { 'data': 'description' },
                            { 'data': 'client' },
                            { 'data': 'clientPriority' },
                            { 'data': 'targetDate' },
                            { 'data': 'productArea' }
                        ]
                    });
                }
            });
        });