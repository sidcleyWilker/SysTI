
$(document).ready(function() {

    $("#id_estado_servico").change(function(){
        show_hide_motivo();
    });

    var show_hide_motivo = function(){

        item = $('#id_estado_servico option:selected').text();

        if (item === 'Cancelado' || item === 'Suspenso'){

            $(".field-motivo_cancel_ou_suspen").show();

        }else {
            $(".field-motivo_cancel_ou_suspen").hide();
        }
    }

show_hide_motivo();

});