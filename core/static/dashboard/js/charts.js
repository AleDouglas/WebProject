


const dados_1 = [
    ['Mês/Ano', 'Nº de Vendas'],
    ['09/2022',  1000],
    ['10/2022',  1170],
    ['11/2022',  660],
    ['12/2022',  1030],
]
const dados_2 = [
    ['Mês/Ano', 'Nº de Vendas'],
    ['09/2022',  323],
    ['10/2022',  554],
    ['11/2022',  513],
    ['12/2022',  865],
]
const dados_3 = [
    ['Mês/Ano', 'Nº de Vendas'],
    ['09/2022',  10010],
    ['10/2022',  11730],
    ['11/2022',  6630],
    ['12/2022',  15030],
]
const dados_4 = [
    ['Mês/Ano', 'Nº de Vendas'],
    ['09/2022',  4000],
    ['10/2022',  5170],
    ['11/2022',  4360],
    ['12/2022',  7030],
]

//Criando gráfico em LINHA através de dados inseridos
function produtoDestaque(dados, nome, idName){
    //google.charts.load('current', {'packages':['corechart']});
    google.load('visualization', '1.0', {'packages':['corechart']});
    google.setOnLoadCallback(drawChart);
    //google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = google.visualization.arrayToDataTable(
            dados
        );
        
        var options = {
            title: nome,
            curveType: 'function',
            legend: { position: 'bottom' }
        };
        
        var chart = new google.visualization.LineChart(document.getElementById(idName));
        
        chart.draw(data, options);
        }
}
var produto_1 = produtoDestaque(dados_1, 'PRODUTO 01', 'curve_chartA')
var produto_2 = produtoDestaque(dados_2, 'PRODUTO 02', 'curve_chartB')
var produto_3 = produtoDestaque(dados_3, 'PRODUTO 03','curve_chartC')
var produto_4 = produtoDestaque(dados_4, 'PRODUTO 04','curve_chartD')

//Caso mude resolução da página
$(window).resize(function(){
    var produto_1 = produtoDestaque(dados_1, 'PRODUTO 01', 'curve_chartA')
    var produto_2 = produtoDestaque(dados_2, 'PRODUTO 02', 'curve_chartB')
    var produto_3 = produtoDestaque(dados_3, 'PRODUTO 03','curve_chartC')
    var produto_4 = produtoDestaque(dados_4, 'PRODUTO 04','curve_chartD')
});




const dadosGeral_1 = [
    ['Ano', 'Vendas ( R$ )'],
    ['2018',  54554],
    ['2019',  45354],
    ['2021',  35454],
    ['2022',  75554]
]
function geralChart(dados, nome, idName){
    google.load('visualization', '1.0', {'packages':['corechart']});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
    var data = google.visualization.arrayToDataTable(
        dados
    );

    var options = {
        title: nome,
        hAxis: {title: 'Ano',  titleTextStyle: {color: '#333'}},
        vAxis: {minValue: 0}
    };

    var chart = new google.visualization.AreaChart(document.getElementById(idName));
    chart.draw(data, options);
    }
}

var geral_1 = geralChart(dadosGeral_1, 'VENDAS GERAIS', 'area_chartA')

//Caso mude resolução da página
$(window).resize(function(){
    var geral_1 = geralChart(dadosGeral_1, 'VENDAS GERAIS', 'area_chartA')
});

function geralMapa(idName){
    google.load('visualization', '1.0', {'packages':['geochart']});
    google.setOnLoadCallback(drawRegionsMap);

    function drawRegionsMap() {
    var data = google.visualization.arrayToDataTable([
        ['País', 'Número de Lojas'],
        ['Germany', 25],
        ['United States', 37],
        ['Brazil', 54],
        ['Canada', 2],
        ['France', 4],
        ['RU', 1]
    ]);

    var options = {};

    var chart = new google.visualization.GeoChart(document.getElementById(idName));

    chart.draw(data, options);
    }
}

var geral_Regiao = geralMapa('Regiao_chartA')

//Caso mude resolução da página
$(window).resize(function(){
    var geral_Regiao = geralMapa('Regiao_chartA')
});
