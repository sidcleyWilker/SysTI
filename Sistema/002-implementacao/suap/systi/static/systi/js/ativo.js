
$(document).ready(function() {



    $("#id_mais_atributo").change(function(){
            show_hide_mais_atributo();
    });

     $("#id_categoria_do_ativo").change(function(){
            show_hide_ategoria_do_ativo();
    });


    var show_hide_mais_atributo = function(){

        item = $('#id_mais_atributo option:selected').text();

        if (item === 'Não'){
            $("#atributo_set-group").hide(100);
        }else{
            $("#atributo_set-group").show(100);
        }

    }

    var show_hide_ategoria_do_ativo = function(){

        item = $('#id_categoria_do_ativo option:selected').text();

        if(item === 'Hardware'){
            $("#categoriahardware_set-group").show(100);
            $("#categoriasoftware_set-group").hide(100);
            $("#categoriarede_set-group").hide(100);
        }else if (item === 'Software'){
            $("#categoriahardware_set-group").hide(100);
            $("#categoriasoftware_set-group").show(100);
            $("#categoriarede_set-group").hide(100);
        }else if (item === 'Rede'){
            $("#categoriarede_set-group").show(100);
            $("#categoriahardware_set-group").hide(100);
            $("#categoriasoftware_set-group").hide(100);
        }

    }


    var validacaoHardware = function( ){
        $("#id_categoriahardware_set-0-fabricante").attr("required", true);
        $("#id_categoriahardware_set-0-versao").attr("required", true);
    }

    var validacaoSoftware = function(){
        $("#id_categoriasoftware_set-0-nome_software").attr("required", true);
        $("#id_categoriasoftware_set-0-versao_software").attr("required", true);
        $("#id_categoriasoftware_set-0-pago").attr("required", true);
    }

    var validacaoRede = function(){
        $("#id_categoriasoftware_set-0-pago").attr("required", true);
#id_categoriarede_set-0-fabricante
    }
//    $('.default').click(function () {
//
//        //$('#ativo_form').
//
//       item = $('#id_categoria_do_ativo option:selected').text();
//
//       if (item === 'Hardware'){
//
//       }
//    }

     show_hide_mais_atributo();
     show_hide_ategoria_do_ativo();
});