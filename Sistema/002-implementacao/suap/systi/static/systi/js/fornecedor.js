$(document).ready(function() {

    $("#id_tipo").change(function(){

        show_hide_tipo();
    });

    var show_hide_tipo = function() {

        item = $('#id_tipo option:selected').text();

        if(item === "Pessoa Jurídica") {
            $(".field-cnpj").show(100);
            $(".field-cpf").hide(100);

        } else {
            $(".field-cnpj").hide(100);
            $(".field-cpf").show(100);
        }
    }

    show_hide_tipo();

});
