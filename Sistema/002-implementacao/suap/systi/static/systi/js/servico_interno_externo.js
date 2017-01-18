$(document).ready(function() {

    $("#id_motivo_servico").change(function(){

        show_hide_chamado_anexo();
    });

    $("#id_estado_servico").change(function(){
        show_hide_motivo();
    });


    var show_hide_chamado_anexo = function() {

        item = $('#id_motivo_servico option:selected').text();


        if(item === "Chamado") {
            $(".field-chamado").show(100);
            $(".field-anexo_motivo").hide(100);

        } else {
            $(".field-chamado").hide(100);
            $(".field-anexo_motivo").show(100);
        }
    }

    var show_hide_motivo = function(){

        item = $('#id_estado_servico option:selected').text();

        if (item === 'Cancelado' || item === 'Suspenso'){

            $(".field-motivo_cancel_ou_suspen").show();

        }else {
            $(".field-motivo_cancel_ou_suspen").hide();
        }
    }

    show_hide_motivo();


    show_hide_chamado_anexo();

});
