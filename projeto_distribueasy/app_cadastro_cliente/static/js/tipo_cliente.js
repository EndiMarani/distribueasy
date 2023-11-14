$(document).ready(function() {
    var tipoClienteSelect = $("#id_tipo_cliente");
    var pfInfo = $(".pf-info");
    var pjInfo = $(".pj-info");
    var allInfo = $(".all-info");

    function toggleInfoFields(selectedValue) {
        $("input[type='text']").prop("disabled", false); // Habilitar todos os campos antes de ocultar

        pfInfo.addClass('hidden');
        pjInfo.addClass('hidden');
        allInfo.addClass('hidden');

        if (selectedValue === "PF") {
            pfInfo.removeClass('hidden');
            allInfo.removeClass('hidden');
            pjInfo.addClass('hidden');
        } else if (selectedValue === "PJ") {
            pjInfo.removeClass('hidden');
            allInfo.removeClass('hidden');
            pfInfo.addClass('hidden');
        }
    }

    tipoClienteSelect.on("change", function() {
        var selectedValue = $(this).val();
        toggleInfoFields(selectedValue);

        // Desabilitar campos não utilizados após ocultar
        $("input[type='text']").not("." + selectedValue + "-info input").prop("disabled", true);
    });

    $("form").submit(function(event) {
        // Habilitar todos os campos antes do envio
        $("input[type='text']").prop("disabled", false);
        return true;
    });
});
