
$(document).ready(function() {

    $("#id_tipo_do_usuario").change(function(){
        show_hide_aluno_servidor();
    });

    function dataFormatada() {
      var data = new Date(),
        dia = data.getDate(),
        mes = data.getMonth() + 1,
        ano = data.getFullYear();
      return [dia, mes, ano].join('/');
    }

    $("#id_data_registro").val(dataFormatada);
    $("#id_data_registro").attr('disabled', 'disabled');
    $("#id_data_des_registro").attr('disabled', 'disabled');

    var show_hide_aluno_servidor = function() {

        item = $('#id_tipo_do_usuario option:selected').text();

        if(item === "Aluno") {
            $(".field-servidor").hide(100);
            $('.field-aluno').show();
        } else {
            $(".field-aluno").hide(100);
            $(".field-servidor").show(100);
        }
    }

show_hide_aluno_servidor();

});
