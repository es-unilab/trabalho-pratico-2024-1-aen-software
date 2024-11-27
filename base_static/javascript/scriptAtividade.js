   
// Função para exibir os formulários dinamicamente
$(document).ready(function() {
    $('#atividade').on('change', function() {
        let atividadeSelecionada = $(this).val();

        // Verifica se a atividade selecionada é Ensino ou Pesquisa e exibe o formulário correspondente
        if (atividadeSelecionada === 'Ensino') {
            $('#ensino-section').show();
            $('#pesquisa-section').hide();
        } else if (atividadeSelecionada === 'Pesquisa') {
            $('#pesquisa-section').show();
            $('#ensino-section').hide();
        } else {
            $('#ensino-section').hide();
            $('#pesquisa-section').hide();
        }
    });

    // Função para exibir os campos de "Graduação" ou "Pós-Graduação" ao selecionar o tipo de ensino
    $('#tipo_ensino').on('change', function() {
        let tipoEnsinoSelecionado = $(this).val();

        // Verifica se é graduação ou pós-graduação e exibe o formulário correspondente
        if (tipoEnsinoSelecionado === 'graduacao') {
            $('#graduacao-section').show();
            $('#pos-graduacao-section').hide();
        } else if (tipoEnsinoSelecionado === 'pos_graduacao') {
            $('#graduacao-section').hide();
            $('#pos-graduacao-section').show();
        } else {
            $('#graduacao-section').hide();
            $('#pos-graduacao-section').hide();
        }
    });

    // Função para calcular a carga horária total
    $('form').on('change', function() {
        let totalMin = 0;
        let totalMax = 0;

        // Pega os valores dos campos de carga horária
        totalMin += parseInt($('input[name="carga_horaria_min_graduacao"]').val()) || 0;
        totalMax += parseInt($('input[name="carga_horaria_max_graduacao"]').val()) || 0;
        totalMin += parseInt($('input[name="carga_horaria_min_pos_graduacao"]').val()) || 0;
        totalMax += parseInt($('input[name="carga_horaria_max_pos_graduacao"]').val()) || 0;
        totalMin += parseInt($('input[name="carga_horaria_min_pesquisa"]').val()) || 0;
        totalMax += parseInt($('input[name="carga_horaria_max_pesquisa"]').val()) || 0;

        // Atualiza os valores no frontend
        $('#carga-min').text(totalMin);
        $('#carga-max').text(totalMax);
    });
});