$(document).ready(function () {
    // Função para desativar os campos do endereço
    function desativarCamposEndereco() {
        $('#id_cliente_cidade').prop('readonly', true);
        $('#id_cliente_estado').prop('readonly', true);
        $('#id_cliente_bairro').prop('readonly', true);
        $('#id_cliente_rua').prop('readonly', true);
    }

    $('#id_cliente_cep').on('blur', function () {
        var cep = $(this).val();

        if (cep.length === 8) {
            $.getJSON(`https://viacep.com.br/ws/${cep}/json/`, function (data) {
                if (data.erro) {
                    alert('CEP não encontrado. Verifique se o CEP está correto.');
                    desativarCamposEndereco();
                } else {
                    // Preencher os campos com as informações do CEP
                    $('#id_cliente_cidade').val(data.localidade);
                    $('#id_cliente_estado').val(data.uf);
                    $('#id_cliente_bairro').val(data.bairro);
                    $('#id_cliente_rua').val(data.logradouro);

                    // Desativar os campos após preenchê-los
                    desativarCamposEndereco();
                }
            }).fail(function () {
                alert('Erro ao obter informações do CEP. Tente novamente mais tarde.');
                desativarCamposEndereco();
            });
        }
    });
});


