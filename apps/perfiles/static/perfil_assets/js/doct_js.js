SetDatePicker();

$(document).ready(function() {

    tabledetalle = $("#dataDetalleImportaciones").DataTable({
        language: {
            retrieve: true,
            paging: false,
            decimal: "",
            emptyTable: "No hay información",
            info: "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
            infoEmpty: "Mostrando 0 to 0 of 0 Entradas",
            infoFiltered: "(Filtrado de _MAX_ total entradas)",
            infoPostFix: "",
            thousands: ",",
            lengthMenu: "Mostrar _MENU_ Entradas",
            loadingRecords: "Cargando...",
            processing: "Procesando...",
            search: "Buscar:",
            zeroRecords: "Sin resultados encontrados",
            paginate: {
                first: "Primero",
                last: "Ultimo",
                next: "Siguiente",
                previous: "Anterior",
            },
        }

    });


    $(document).ready(function() {
        $("#reenviarMovi div").on("click", "button", function(event) {
            event.preventDefault();
            console.log("form submitted!"); // sanity check
            var data = table.row($(this).parents('tr')).data();

            var tipmov = data[0]
            var codpro = data[1]
            var numdoc = data[2]

            console.log(tipmov, codpro, numdoc)
            reenviarMovimientoAjax(tipmov, codpro, numdoc)
        });

        function reenviarMovimientoAjax(tipmov, codpro, numdoc) {

            var val = $('input[name = csrfmiddlewaretoken]').val()
            console.log(val)


            let $this = $(this);
            console.log($this.serialize())

            let url = 'envioRandom/' + tipmov + '/' + codpro + '/' + numdoc + '/';
            console.log(url)
            let method = "POST";
            $.ajax({

                url: url,
                method: method,
                beforeSend: function(xhr) {
                    xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                },
                //                headers: { "X-CSRFToken": val },
                success: function(data) {

                    if (data.valid !== 'success')
                        notification[data.valid](data.message);

                    if (data.valid === 'success') {
                        if (data.redirect_url) {
                            window.location.replace(data.redirect_url);
                        } else {
                            notification[data.valid](data.message);
                            var item_row = param['btn'].closest('.item-row');
                            item_row.hide('slow', function() {
                                item_row.remove();
                            });
                        }
                    }
                },
                error: function() {
                    console.log("not done")

                }
            });
        };
    })

    // renvioRandom Item
    $('.item-row').on('click', '.reenvio_item', function(event) {
        event.preventDefault();
        var btn = $(this);
        var url = btn.data('href');
        var param = [];
        param['url'] = url;
        param['btn'] = btn;

        console.log(param)

        $.confirm({
            title: 'Warning!',
            content: 'Desea reenviar el movimiento a random ?',
            type: 'red',
            buttons: {
                yes: function() {
                    AjaxRenviaItem(param);
                },
                no: function() {}
            }
        }, );
    });

    // Delete Item
    $('.item-row').on('click', '.delete_item', function(event) {
        event.preventDefault();
        var btn = $(this);
        var url = btn.data('href');
        var param = [];
        param['url'] = url;
        param['btn'] = btn;

        $.confirm({
            title: 'Warning!',
            content: 'Are you sure you want to delete?',
            type: 'red',
            buttons: {
                yes: function() {
                    AjaxRemoveItem(param);
                },
                no: function() {}
            }
        }, );
    });

    // Edit Item by double click
    $('.item-row').dblclick(function(event) {
        event.preventDefault();
        var item = $(this);
        var url = item.data('edit');
        var param = [];
        param['url'] = url;
        param['item'] = item;
        AjaxGetEditRowForm(param);
    });

    // Save form with click button
    $('.item-row').on('click', '.save_form', function(event) {
        event.preventDefault();
        var btn = $(this);
        SaveItem(btn);
    });

    // Save form with ENTER
    $('.item-row').keyup('.importacion', function(event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            var btn = $(this);
            SaveItem(btn);
        }
    });

    // Cancel edit form
    $('.item-row').on('click', '.cancel_form', function(event) {
        event.preventDefault();
        var btn = $(this);
        var item = btn.closest('.item-row');
        var url = item.data('detail');
        var param = [];
        param['url'] = url;
        param['item'] = item;
        AjaxGetEditRowDetail(param);
    });
});


// Functions

function AjaxGetEditRowDetail(param) {
    $.ajax({
        url: param['url'],
        type: 'GET',
        success: function(data) {
            param['item'].html(data.edit_row);
        },
        error: function() {
            notification.error('Error occurred');
        }
    });
}

function AjaxGetEditRowForm(param) {
    $.ajax({
        url: param['url'],
        type: 'GET',
        success: function(data) {
            param['item'].html(data.edit_row);
            SetDatePicker();
        },
        error: function() {
            notification.error('Error occurred');
        }
    });
}

function AjaxPutEditRowForm(param) {
    $.ajax({
        url: param['url'],
        type: 'PUT',
        data: param['query'],
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
        },
        success: function(data) {
            notification[data.valid](data.message);

            if (data.valid === 'success') {
                param['item'].html(data.edit_row);
                SetDatePicker();
            }
        },
        error: function() {
            toastr.error('Error occurred');
        }
    });
}

function AjaxRemoveItem(param) {
    $.ajax({
        url: param['url'],
        type: 'DELETE',
        data: param['query'],
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
        },
        success: function(data) {
            if (data.valid !== 'success')
                notification[data.valid](data.message);

            if (data.valid === 'success') {
                if (data.redirect_url) {
                    window.location.replace(data.redirect_url);
                } else {
                    notification[data.valid](data.message);
                    var item_row = param['btn'].closest('.item-row');
                    item_row.hide('slow', function() {
                        item_row.remove();
                    });
                }
            }
        },
        error: function() {
            toastr.error('Error occurred');
        }
    });
}

function AjaxRenviaItem(param) {
    $.ajax({
        url: param['url'],
        type: 'POST',
        data: param['query'],
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
        },
        success: function(data) {
            if (data.valid !== 'success')
                notification[data.valid](data.message);

            if (data.valid === 'success') {
                if (data.redirect_url) {
                    window.location.replace(data.redirect_url);
                } else {
                    notification[data.valid](data.message);
                    var item_row = param['btn'].closest('.item-row');
                    item_row.hide('slow', function() {
                        item_row.remove();
                    });
                }
            }
        },
        error: function() {
            console.log("not done")

        }
    });
}

function SaveItem(btn) {
    var item = btn.closest('.item-row');
    var url = item.data('edit');
    var param = [];
    param['url'] = url;
    param['item'] = item;
    param['query'] = $('.importacion').serialize();
    AjaxPutEditRowForm(param);
}

function SetDatePicker() {
    var datepickers = [].slice.call(d.querySelectorAll('.datepicker_input'));
    datepickers.map(function(el) {
        return new Datepicker(el, { format: 'yyyy-mm-dd' });
    });
}