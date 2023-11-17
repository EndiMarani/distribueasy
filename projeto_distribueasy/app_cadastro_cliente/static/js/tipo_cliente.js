        document.addEventListener('DOMContentLoaded', function () {
            var tipoClienteSelect = document.getElementById('id_tipo_cliente');
            var cpfCnpjContainer = document.querySelector('.hidden.form-control');
            var allInfoContainers = document.querySelectorAll('.all-info');
            var cpfLabel = cpfCnpjContainer.querySelector('label[for=id_cliente_cpf_cnpj]');
            var nomeLabel = cpfCnpjContainer.querySelector('label[for=id_cliente_nome]');
    
            function toggleVisibility(selectedValue) {
                if (selectedValue === 'PF' || selectedValue === 'PJ') {
                    if (selectedValue === 'PF') {
                        showContainer(cpfCnpjContainer);
                        cpfLabel.textContent = 'CPF:';
                        nomeLabel.textContent = 'Nome:';
                    } else if (selectedValue === 'PJ') {
                        hideContainer(cpfCnpjContainer);
                        cpfLabel.textContent = 'CNPJ:';
                        nomeLabel.textContent = 'Empresa:';
                    }
    
                    allInfoContainers.forEach(function (container) {
                        showContainer(container);
                    });
                } else {
                    hideContainer(cpfCnpjContainer);
    
                    allInfoContainers.forEach(function (container) {
                        hideContainer(container);
                    });
                }
            }
    
            function showContainer(container) {
                container.classList.remove('hidden');
            }
    
            function hideContainer(container) {
                container.classList.add('hidden');
            }
    
            // Adicionando um listener para chamar a função quando o valor do tipo de cliente muda
            tipoClienteSelect.addEventListener('change', function () {
                toggleVisibility(tipoClienteSelect.value);
            });
    
            // Chamar a função inicialmente com o valor atual do tipo de cliente
            toggleVisibility(tipoClienteSelect.value);
        });
