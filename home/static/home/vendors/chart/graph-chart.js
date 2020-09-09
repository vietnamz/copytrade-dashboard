var randAmount = function () {
    var min = 10;
    var max = 300;
    return Math.floor(Math.random() * (max - min)) + min;
};

var genData = function() {
    var i, dataSet = [];
    for (i = 1; i < 31; i++) {
        dataSet.push([Date.UTC(2018,0,i),randAmount()]);
    };
    return dataSet;
};

jQuery(function () {
    var data = genData();

    var myChart = Highcharts.chart('purchase-graph', {
        chart: {
            zoomType: 'x'
        },
        title: {
            text: ''
        }, 
        yAxis: {
            title: {
                text: ''
            }
        },
        legend: {
            enabled: false
        },
        plotOptions: {
            area: {
                fillColor: { 
                    linearGradient: {
                        x1: 0,
                        y1: 0,
                        x2: 0,
                        y2: 1
                    },
                    stops: [
                        [0, Highcharts.getOptions().colors[0]],
                        [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                    ]
                },
                marker: {
                    radius: 3
                },
                lineWidth: 1,
                lineColor: '#3599ea',
                strokeColor: '#f4f5f9',
                strokeWidth: 1,
                states: { 
                    hover: {
                        lineWidth: 1
                    }
                },
                threshold: null
            }
        },

        series: [{
            type: 'area',
            name: 'Purchase',
            data: data,
        }]
    });
});