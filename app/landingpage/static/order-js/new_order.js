$(document).ready(function () {
    // Cargar las opciones del select utilizando AJAX
    load_merengue();
    load_size();
    load_base();
    load_pisos();
    val_telefono();


    var baseLoaded = false;
    var pisosLoaded = false;
    var merengueLoaded = false;
    var sizeLoaded = false;

    var pisos = {}; // Se crea un objeto vacío para almacenar los datos de los pisos
    var base = {}; // Se crea un objeto vacío para almacenar los datos de la base
    var merengue = {}; // Se crea un objeto vacío para almacenar los datos del merengue
    var size = {}; // Se crea un objeto vacío para almacenar los datos del tamaño

    // Función para mostrar información adicional del objeto CakeSample al hacer clic en una imagen
    $('#galeria-imagenes').on('click', 'img', function () {
        // Remueve la clase 'seleccionado' de todas las imágenes
        $('#galeria-imagenes img').removeClass('seleccionado');

        // Agrega la clase 'seleccionado' a la imagen seleccionada
        $(this).addClass('seleccionado');

        // Mueve la imagen seleccionada al centro de la galería
        var galeria = $('#galeria-imagenes');
        var seleccionado = galeria.find('img.seleccionado');
        var offset = seleccionado.offset().left - galeria.offset().left;
        var centro = galeria.width() / 2 - seleccionado.width() / 2;
        galeria.scrollLeft(offset - centro);

        var name = $(this).data('name');
        var description = $(this).data('description');
        var filling = $(this).data('filling');
        var info = '<p><strong>' + name + '</strong></p><p>' + description + '</p><p>Sabor de relleno: ' + filling + '</p>';
        $('#informacion-cake-sample').html(info);
    });

    $('#id_merengue').change(function () {

        var merengueId = $(this).val();
        var url = 'home/get_merengue/?id=' + merengueId;
        enviarAjax(url, 'GET', {}, function (data) {
            merengue = data.merengue;
            baseLoaded = true;
            $('#merengue-imagen').attr('src', data.merengue.image);
            if (baseLoaded && pisosLoaded && merengueLoaded && sizeLoaded) {
                enviarAjax('home/get_cake_sample/', 'POST',
                    {
                        'base_id': base.id,
                        'merengue_id': merengue.id,
                        'size_id': size.id,
                        'layers_id': pisos.id
                    },
                    function (data) {
                        if ('error' in data) {
                            // Se muestra el mensaje de error en un elemento HTML
                            mostrarNotificacion("warning", 'top-start', data.error);
                            $('#galeria-imagenes').empty();

                        } else {
                            $('#galeria-imagenes').empty();
                            $.each(data, function (index, cake_sample) {
                                var img = '<img src="' + cake_sample.image_url + '" alt="' + cake_sample.name + '" data-name="' + cake_sample.name + '" data-description="' + cake_sample.description + '" data-filling="' + cake_sample.filling + '">';
                                $('#galeria-imagenes').append(img);
                            });
                        }
                    },
                    function (xhr, textStatus, errorThrow) {
                        mostrarNotificacion("error", 'top-start', "No se han podido cargar los datos con la muestra del cake");
                        $('#cake_sample-imagen').attr('src', "");
                    });

            }
        }, function (xhr, textStatus, errorThrown) {
            mostrarNotificacion("error", 'top-start', "No se han podido cargar los datos");
        });
    });
    $('#id_base').change(function () {

        var merengueId = $(this).val();
        var url = 'home/get_base/?id=' + merengueId;
        if (merengueId !== '-1') {
            enviarAjax(url, 'GET', {}, function (data) {
                base = data.base;
                pisosLoaded = true;
                $('#base-imagen').attr('src', data.base.image);
                if (baseLoaded && pisosLoaded && merengueLoaded && sizeLoaded) {
                    enviarAjax('home/get_cake_sample/', 'POST',
                        {
                            'base_id': base.id,
                            'merengue_id': merengue.id,
                            'size_id': size.id,
                            'layers_id': pisos.id
                        },
                        function (data) {
                            if ('error' in data) {
                                // Se muestra el mensaje de error en un elemento HTML
                                mostrarNotificacion("warning", 'top-start', data.error);
                                $('#galeria-imagenes').empty();

                            } else {
                                $('#cake_sample-imagen').attr('src', data.image_url);
                                $('#cake_sample_text').text(data.name);
                            }
                        },
                        function (xhr, textStatus, errorThrow) {
                            mostrarNotificacion("error", 'top-start', "No se han podido cargar los datos con la muestra del cake");
                            $('#cake_sample-imagen').attr('src', "");
                        });
                }
            }, function (xhr, textStatus, errorThrown) {
                mostrarNotificacion("error", 'top-start', "No se han podido cargar los datos");
            });
        } else {
            $('#base-imagen').attr('src', "");

        }


    });
    $('#id_size').change(function () {

        var merengueId = $(this).val();
        var url = 'home/get_size/?id=' + merengueId;
        enviarAjax(url, 'GET', {}, function (data) {
            size = data.size;
            merengueLoaded = true;
            $('#size-imagen').attr('src', data.size.image);
            if (baseLoaded && pisosLoaded && merengueLoaded && sizeLoaded) {
                enviarAjax('home/get_cake_sample/', 'POST',
                    {
                        'base_id': base.id,
                        'merengue_id': merengue.id,
                        'size_id': size.id,
                        'layers_id': pisos.id
                    },
                    function (data) {
                        if ('error' in data) {
                            // Se muestra el mensaje de error en un elemento HTML
                            mostrarNotificacion("warning", 'top-start', data.error);
                            $('#galeria-imagenes').empty();

                        } else {
                            $('#cake_sample-imagen').attr('src', data.image_url);
                            $('#cake_sample_text').text(data.name);
                        }
                    },
                    function (xhr, textStatus, errorThrow) {
                        mostrarNotificacion("error", 'top-start', "No se han podido cargar los datos con la muestra del cake");
                        $('#cake_sample-imagen').attr('src', "");
                    });
            }
        }, function (xhr, textStatus, errorThrown) {
            mostrarNotificacion("error", 'top-start', "No se han podido cargar los datos");
        });
    });
    $('#id_pisos').change(function () {
        var merengueId = $(this).val();
        var url = 'home/get_pisos/?id=' + merengueId;
        enviarAjax(url, 'GET', {}, function (data) {
            pisos = data.pisos;
            sizeLoaded = true;
            $('#pisos-imagen').attr('src', data.pisos.image);
            if (baseLoaded && pisosLoaded && merengueLoaded && sizeLoaded) {
                enviarAjax('home/get_cake_sample/', 'POST',
                    {
                        'base_id': base.id,
                        'merengue_id': merengue.id,
                        'size_id': size.id,
                        'layers_id': pisos.id
                    },
                    function (data) {
                        if ('error' in data) {
                            // Se muestra el mensaje de error en un elemento HTML
                            mostrarNotificacion("warning", 'top-start', data.error);
                            $('#galeria-imagenes').empty();

                        } else {

                            $('#cake_sample-imagen').attr('src', data.image_url);
                            $('#cake_sample_text').text(data.name);
                        }

                    },
                    function (xhr, textStatus, errorThrow) {
                        mostrarNotificacion("error", 'top-start', "No se han podido cargar los datos con la muestra del cake");
                        $('#cake_sample-imagen').attr('src', "");
                    });
            }
        }, function (xhr, textStatus, errorThrown) {
            mostrarNotificacion("error", 'top-start', "No se han podido cargar los datos");
        });
    });


    var calendario = document.getElementById("calendario");
    var hoy = new Date(); // Obtiene la fecha actual
    var tresDiasDespues = new Date(hoy.getTime() + (3 * 24 * 60 * 60 * 1000)); // Calcula la fecha tres días después
    var fecha_entrega;
    flatpickr(calendario, {
        inline: true,
        static: true,
        height: "100px",
        width: "10px",
        dateFormat: "d/m/Y",
        minDate: tresDiasDespues,
        defaultDate: tresDiasDespues,
        onValueUpdate: function (selectedDates, dateStr, instance) {
            fecha_entrega = selectedDates[0]; // Almacena la fecha seleccionada en la variable global

        },

    });


    // Manejar el envío del formulario con AJAX
    $('#create-form').submit(function (event) {
        mostrarNotificacion("success", "top-start", "orden para base" + $('#id_base').val() + "Tamaño Ñ" + $('#id_size').val() + "confecha" + fecha_entrega)

        event.preventDefault();
        // enviarAjax("/asd", "", null,
        //     function () {
        //
        //     },
        //     function () {
        //         mostrarNotificacion("error", 'top-start', "Informacion insuficiente")
        //
        //     }
        // )
    });
var images = $('#galeria-imagenes img');

  // Agregar el evento de clic a cada imagen
  images.click(function() {

    // Seleccionar la imagen principal en el contenedor de zoom
    var zoomImage = $('#galeria-zoom .zoom');

    // Mover la imagen seleccionada al principio de la lista de imágenes en la galería
    $(this).parent().prepend($(this));

    // Cambiar la imagen principal por la imagen seleccionada
    zoomImage.attr('src', $(this).attr('src'));
    alert(zoomImage)

    // Activar el plugin de zoom en la imagen principal
    zoomImage.ezPlus({
      zoomType: "inner",
      cursor: "crosshair"
    });
  });
    // const $galeria = $('#galeria-imagenes');
    // const $seleccionado = $('.seleccionado');
    // const $zoom = $('.zoom');
    //
    // $galeria.on('mousemove', '.seleccionado', function (e) {
    //     const seleccionadoRect = this.getBoundingClientRect();
    //     const x = e.pageX - window.pageXOffset;
    //     const y = e.pageY - window.pageYOffset;
    //     const ancho = seleccionadoRect.width;
    //     const alto = seleccionadoRect.height;
    //     const centroX = ancho / 2;
    //     const centroY = alto / 2;
    //     const distanciaX = x - seleccionadoRect.left - centroX;
    //     const distanciaY = y - seleccionadoRect.top - centroY;
    //     const distanciaXPorcentaje = distanciaX / centroX;
    //     const distanciaYPorcentaje = distanciaY / centroY;
    //     const desplazamiento = Math.sqrt(Math.pow(distanciaXPorcentaje, 2) + Math.pow(distanciaYPorcentaje, 2));
    //     if (desplazamiento < 1) {
    //         let zoomX = x - ($zoom.width() / 2) - seleccionadoRect.left;
    //         let zoomY = y - ($zoom.height() / 2) - seleccionadoRect.top;
    //         if (zoomX < 0) {
    //             zoomX = 0;
    //         } else if (zoomX + $zoom.width() > ancho) {
    //             zoomX = ancho - $zoom.width();
    //         }
    //         if (zoomY < 0) {
    //             zoomY = 0;
    //         } else if (zoomY + $zoom.height() > alto) {
    //             zoomY = alto - $zoom.height();
    //         }
    //         const backgroundPosX = -zoomX * (seleccionadoRect.width / $seleccionado.width());
    //         const backgroundPosY = -zoomY * (seleccionadoRect.height / $seleccionado.height());
    //         $zoom.css('transform', `translate(${zoomX}px, ${zoomY}px) scale(${1 + desplazamiento})`);
    //         $zoom.css('background-position', `${backgroundPosX}px ${backgroundPosY}px`);
    //     }
    // });
    //
    // $galeria.on('mouseleave', '.seleccionado', function () {
    //     $zoom.css('transform', 'translate(-50%, -50%) scale(0.8)');
    //     $zoom.css('background-position', '0 0');
    // });
});

function load_base() {
    enviarAjax("home/cargar_base/ ", "GET", null,
        function (data) {
            // Agregar las opciones al select
            $('#id_base').empty();
            $('#id_base').append($('<option>').text("-- Selecciona una").attr('value', -1));
            $.each(data, function (index, obj) {
                $('#id_base').append($('<option>').text(obj.name).attr('value', obj.id));
            });
        },
        function () {
            mostrarNotificacion("error", 'top-start', "No se han podido cargar los datos");
        }
    )
}

function load_size() {
    enviarAjax("home/load_size/ ", "GET", null,
        function (data) {
            // Agregar las opciones al select
            $('#id_size').empty();
            $('#id_size').append($('<option>').text("-- Selecciona una").attr('value', -1));
            $.each(data, function (index, obj) {
                $('#id_size').append($('<option>').text(obj.name).attr('value', obj.id));
            });
        },
        function () {
            mostrarNotificacion("error", 'top-start', "No se han podido cargar los datos");
        }
    )
}

function load_merengue() {
    enviarAjax("home/load_merengue/ ", "GET", null,
        function (data) {
            // Agregar las opciones al select
            $('#id_merengue').empty();
            $('#id_merengue').append($('<option>').text("-- Selecciona una"));
            $.each(data, function (index, obj) {
                $('#id_merengue').append($('<option>').text(obj.name).attr('value', obj.id));
            });
        },
        function () {
            mostrarNotificacion("error", 'top-start', "No se han podido cargar los datos");
        }
    )
}

function load_pisos() {
    enviarAjax("home/cargar_pisos/ ", "GET", null,
        function (data) {
            // Agregar las opciones al select
            $('#id_pisos').empty();
            $('#id_pisos').append($('<option>').text("-- Selecciona una"));
            $.each(data, function (index, obj) {
                $('#id_pisos').append($('<option>').text(obj.name).attr('value', obj.id));
            });
        },
        function () {
            mostrarNotificacion("error", 'top-start', "No se han podido cargar los datos");
        }
    )
}


function val_telefono() {
    var telefonoPrefijo = $('#telefono-prefijo');
    var telefonoResto = $('#telefono-resto');

    telefonoResto.on('input', function () {
        var prefijo = telefonoPrefijo.val();
        var resto = telefonoResto.val();
        var telefono = prefijo + resto;
        telefonoResto.val(resto); // Asegura que el valor del campo de entrada solo contenga el resto del número de teléfono
        telefonoResto.attr('maxlength', 8); // Restringe la longitud máxima del campo de entrada a 7 dígitos
        telefonoPrefijo.val(prefijo); // Establece el valor del select en el prefijo actual
    });

    telefonoPrefijo.on('change', function () {
        var prefijo = telefonoPrefijo.val();
        var resto = telefonoResto.val();
        var telefono = prefijo + resto;
        telefonoResto.attr('maxlength', 8); // Permite que el usuario ingrese el prefijo completo si cambia el valor del select
        telefonoResto.val(''); // Borra el valor actual del campo de entrada para evitar errores
        telefonoPrefijo.val(prefijo); // Establece el valor del select en el prefijo seleccionado
        telefonoResto.focus(); // Enfoca el campo de entrada para que el usuario pueda ingresar el resto del número de teléfono
    });
}
