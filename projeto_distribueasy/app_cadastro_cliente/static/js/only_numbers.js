$(document).ready(function(){
    // Adiciona o evento de input ao campo CPF/CNPJ
    $('#id_cliente_cpf_cnpj').on('input', function (e) {
    // Remove qualquer caractere não numérico
        this.value = this.value.replace(/\D/g, '');
    });
});

