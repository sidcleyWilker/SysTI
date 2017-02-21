$(document).ready(function() {

    $("#id_motivo_transferencia").change(function(){

        show_hide_chamado_anexo();
    });

    var show_hide_chamado_anexo = function() {

        item = $('#id_motivo_transferencia option:selected').text();

        if(item === "Chamado") {
            $(".field-chamado").show(100);
            $(".field-anexo_motivo").hide(100);

        } else {
            $(".field-chamado").hide(100);
            $(".field-anexo_motivo").show(100);
        }
    }

    show_hide_chamado_anexo();

});