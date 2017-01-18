
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

    show_hide_mais_atributo();
    show_hide_ategoria_do_ativo();
});