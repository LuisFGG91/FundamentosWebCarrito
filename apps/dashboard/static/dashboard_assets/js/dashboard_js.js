function loadJson(selector) {
    return JSON.parse(document.querySelector(selector).getAttribute('data-json'));
}

const p = document;

p.addEventListener("DOMContentLoaded", function(event) {


    //Apex Charts
    //Main Chart


    var chart = new ApexCharts(document.querySelector("#chart"), options);
    if (document.getElementById('chart')) {
        chart.render();
    }

    // Weekly Sales Chart
    var optionsWeeklySalesChart = {
        series: [{
            name: 'Sales',
            data: [32, 44, 37, 47, 42, 55, 47, 65]
        }],
        chart: {
            type: 'bar',
            width: "100%",
            height: 260,
            sparkline: {
                enabled: true
            }
        },
        theme: {
            monochrome: {
                enabled: true,
                color: '#31316A',
            }
        },
        plotOptions: {
            bar: {
                columnWidth: '20%',
                borderRadius: 5,
                radiusOnLastStackedBar: true,
                horizontal: false,
                distributed: false,
                endindShape: 'rounded',
                colors: {
                    backgroundBarColors: ['#F2F4F6', '#F2F4F6', '#F2F4F6', '#F2F4F6'],
                    backgroundBarRadius: 5,
                },
            }
        },
        labels: [1, 2, 3, 4, 5, 6, 7, 8],
        xaxis: {
            categories: ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 'Week 7', 'Week 8'],
            crosshairs: {
                width: 1
            },
        },
        tooltip: {
            fillSeriesColor: false,
            onDatasetHover: {
                highlightDataSeries: false,
            },
            theme: 'light',
            style: {
                fontSize: '12px',
                fontFamily: 'Inter',
            },
            y: {
                formatter: function(val) {
                    return "$ " + val + "k"
                }
            }
        },
    };

    var weeklySalesChartEl = document.getElementById('chart-weekly-sales');
    if (weeklySalesChartEl) {
        var weeklySalesChart = new ApexCharts(weeklySalesChartEl, optionsWeeklySalesChart);
        weeklySalesChart.render();
    }

    //Customers Chart
    var optionsCustomersChart = {
        series: [{
            name: 'Clients',
            data: [120, 160, 200, 470, 420, 150, 470, 750, 650, 190, 140]
        }],
        labels: ['01 Feb', '02 Feb', '03 Feb', '04 Feb', '05 Feb', '06 Feb', '07 Feb', '08 Feb', '09 Feb', '10 Feb', '11 Feb'],
        chart: {
            type: 'area',
            width: "100%",
            height: 140,
            sparkline: {
                enabled: true
            }
        },
        theme: {
            monochrome: {
                enabled: true,
                color: '#31316A',
            }
        },
        tooltip: {
            fillSeriesColor: false,
            onDatasetHover: {
                highlightDataSeries: false,
            },
            theme: 'light',
            style: {
                fontSize: '12px',
                fontFamily: 'Inter',
            },
        },
    };

    var customersChartEl = document.getElementById('chart-customers');
    if (customersChartEl) {
        var customersChart = new ApexCharts(customersChartEl, optionsCustomersChart);
        customersChart.render();
    }

    //Today Users Chart
    var optionsUsersChart = {
        series: [{
            name: 'Users',
            data: [520, 560, 500, 570, 520, 550, 570, 550, 550, 590, 540]
        }],
        labels: ['06PM', '02 Feb', '03 Feb', '04 Feb', '05 Feb', '06 Feb', '07 Feb', '08 Feb', '09 Feb', '10 Feb', '11 Feb'],
        chart: {
            type: 'area',
            width: "100%",
            height: 140,
            sparkline: {
                enabled: true
            }
        },
        theme: {
            monochrome: {
                enabled: true,
                color: '#31316A',
            }
        },
        tooltip: {
            fillSeriesColor: false,
            onDatasetHover: {
                highlightDataSeries: false,
            },
            theme: 'light',
            style: {
                fontSize: '12px',
                fontFamily: 'Inter',
            },
        },
    };

    var usersChartEl = document.getElementById('chart-users');
    if (usersChartEl) {
        var usersChart = new ApexCharts(usersChartEl, optionsUsersChart);
        usersChart.render();
    }


    // Revenue Chart
    var optionsRevenueChart = {
        series: [{
            name: 'Sales',
            data: [34, 29, 32, 38, 39, 35, 36]
        }],
        chart: {
            type: 'bar',
            width: "100%",
            height: 140,
            sparkline: {
                enabled: true
            }
        },
        theme: {
            monochrome: {
                enabled: true,
                color: '#31316A',
            }
        },
        plotOptions: {
            bar: {
                columnWidth: '25%',
                borderRadius: 5,
                radiusOnLastStackedBar: true,
                colors: {
                    backgroundBarColors: ['#F2F4F6', '#F2F4F6', '#F2F4F6', '#F2F4F6'],
                    backgroundBarRadius: 5,
                },
            }
        },
        labels: [1, 2, 3, 4, 5, 6, 7],
        xaxis: {
            categories: ['01 Feb', '02 Feb', '03 Feb', '04 Feb', '05 Feb', '06 Feb', '07 Feb'],
            crosshairs: {
                width: 1
            },
        },
        tooltip: {
            fillSeriesColor: false,
            onDatasetHover: {
                highlightDataSeries: false,
            },
            theme: 'light',
            style: {
                fontSize: '12px',
                fontFamily: 'Inter',
            },
            y: {
                formatter: function(val) {
                    return "$ " + val + "k"
                }
            }
        },
    };

    var revenueChartEl = document.getElementById('chart-revenue');
    if (revenueChartEl) {
        var revenueChart = new ApexCharts(revenueChartEl, optionsRevenueChart);
        revenueChart.render();
    }

    //Traffic volumes
    var optionsTrafficVolumesChart = {
        series: [{
            name: 'Direct',
            data: [7100, 9600, 10000, 8700, 12000, 15400, 19000]
        }, {
            name: 'Refferals',
            data: [4100, 6800, 7000, 6700, 7200, 14000, 12000]
        }, {
            name: 'Organic',
            data: [1100, 3200, 4500, 3200, 3400, 5200, 4100]
        }],
        colors: ['#4D4AE8', '#FD8E7A', '#06A77D', '#51449E'],
        chart: {
            height: 420,
            type: "line",
            fontFamily: 'Inter',
            foreColor: '#4B5563',
            toolbar: {
                show: true,
                offsetX: 0,
                offsetY: 0,
                tools: {
                    download: false,
                    selection: false,
                    zoom: false,
                    zoomin: true,
                    zoomout: true,
                    pan: false,
                    reset: false | '<img src="/static/icons/reset.png" width="20">',
                    customIcons: []
                },
                export: {
                    csv: {
                        filename: undefined,
                        columnDelimiter: ',',
                        headerCategory: 'category',
                        headerValue: 'value',
                        dateFormatter(timestamp) {
                            return new Date(timestamp).toDateString()
                        }
                    }
                },
                autoSelected: 'zoom'
            },
        },
        dataLabels: {
            enabled: false
        },
        stroke: {
            curve: 'smooth'
        },
        grid: {
            show: true,
            borderColor: '#f2f2f2',
            strokeDashArray: 1,
        },
        xaxis: {
            categories: ['01 Feb', '02 Feb', '03 Feb', '04 Feb', '05 Feb', '06 Feb', '07 Feb'],
            labels: {
                style: {
                    fontSize: '12px',
                    fontWeight: 500,
                },
            },
            axisBorder: {
                color: '#ffffff',
            },
            axisTicks: {
                color: '#ffffff',
            }
        },
        yaxis: {
            labels: {
                style: {
                    colors: ['#4B5563'],
                    fontSize: '12px',
                    fontWeight: 500,
                },
            },
        },
        legend: {
            show: true,
            fontSize: '14px',
            fontFamily: 'Inter',
            fontWeight: 400,
            height: 60,
            tooltipHoverFormatter: undefined,
            offsetY: 20,
            markers: {
                width: 14,
                height: 14,
                strokeWidth: 1,
                strokeColor: '#fff',
                radius: 50,
            },
        },
        responsive: [{
            breakpoint: 768,
            options: {
                yaxis: {
                    show: false,
                }
            }
        }]
    };

    var trafficVolumesChartEl = document.getElementById('traffic-volumes-chart');
    if (trafficVolumesChartEl) {
        var trafficVolumesChart = new ApexCharts(trafficVolumesChartEl, optionsTrafficVolumesChart);
        trafficVolumesChart.render();
    }

    // Sales by Product
    var optionsTrafficShareChart = {
        series: [{
            name: 'Visits',
            data: [4, 7, 9, 29, 51]
        }],
        chart: {
            type: 'bar',
            height: 500,
            foreColor: '#4B5563',
            fontFamily: 'Inter',
        },
        plotOptions: {
            bar: {
                horizontal: true,
                distributed: false,
                barHeight: '90%',
                borderRadius: 10,
                colors: {
                    backgroundBarColors: ['#fff'],
                    backgroundBarOpacity: .2,
                    backgroundBarRadius: 10,
                },
            }
        },
        colors: ['#4D4AE8'],
        dataLabels: {
            enabled: true,
            textAnchor: 'middle',
            formatter: function(val, opt) {
                return opt.w.globals.labels[opt.dataPointIndex]
            },
            offsetY: -1,
            dropShadow: {
                enabled: false,
            },
            style: {
                fontSize: '12px',
                fontFamily: 'Inter',
                fontWeight: '500',
            }
        },
        grid: {
            show: false,
            borderColor: '#f2f2f2',
            strokeDashArray: 1,
        },
        legend: {
            show: false,
        },
        yaxis: {
            labels: {
                show: false
            },
        },
        tooltip: {
            fillSeriesColor: false,
            onDatasetHover: {
                highlightDataSeries: false,
            },
            theme: 'light',
            style: {
                fontSize: '12px',
                fontFamily: 'Inter',
            },
            y: {
                formatter: function(val) {
                    return val + "%"
                }
            },
        },
        xaxis: {
            categories: ['Mail', 'Social', 'Organic', 'Referrals', 'Direct'],
            labels: {
                style: {
                    fontSize: '12px',
                    fontWeight: 500,
                },
                offsetY: 5
            },
            axisBorder: {
                color: '#ffffff',
            },
            axisTicks: {
                color: '#ffffff',
                offsetY: 5
            },
        }
    };

    var trafficShareChartEl = document.getElementById('traffic-share-chart');
    if (trafficShareChartEl) {
        var trafficShareChart = new ApexCharts(trafficShareChartEl, optionsTrafficShareChart);
        trafficShareChart.render();
    }

    // Total Orders Chart
    var optionsAppRankingChart = {
        series: [{
            name: 'Travel & Local',
            data: [44, 55, 57, 56, 61, 58, 63, 60, 66]
        }, {
            name: 'Widgets',
            data: [76, 85, 101, 98, 87, 105, 91, 114, 94]
        }],
        chart: {
            type: 'bar',
            height: '400px',
            fontFamily: 'Inter',
            foreColor: '#4B5563',
        },
        colors: ['#f0bc74', '#31316A'],
        plotOptions: {
            bar: {
                horizontal: false,
                columnWidth: '40%',
                borderRadius: 10,
                colors: {
                    backgroundBarColors: ['#fff'],
                    backgroundBarOpacity: .2,
                    backgroundBarRadius: 10,
                },
            },
        },
        grid: {
            show: false,
        },
        dataLabels: {
            enabled: false
        },
        legend: {
            show: true,
            fontSize: '14px',
            fontFamily: 'Inter',
            fontWeight: 500,
            height: 40,
            tooltipHoverFormatter: undefined,
            offsetY: 10,
            markers: {
                width: 14,
                height: 14,
                strokeWidth: 1,
                strokeColor: '#ffffff',
                radius: 50,
            },
        },
        stroke: {
            show: true,
            width: 2,
            colors: ['transparent']
        },
        xaxis: {
            categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
            labels: {
                style: {
                    fontSize: '12px',
                    fontWeight: 500,
                },
            },
            axisBorder: {
                color: '#EBE3EE',
            },
            axisTicks: {
                color: '#f1f1f1',
            }
        },
        yaxis: {
            show: false,
        },
        fill: {
            opacity: 1
        },
        responsive: [{
            breakpoint: 1499,
            options: {
                chart: {
                    height: '400px',
                },
            },
        }]
    };

    var appRankingChartEl = document.getElementById('chart-app-ranking');
    if (appRankingChartEl) {
        var appRankingChart = new ApexCharts(appRankingChartEl, optionsAppRankingChart);
        appRankingChart.render();
    }

    if (d.getElementById('loadOnClick')) {
        d.getElementById('loadOnClick').addEventListener('click', function() {
            var button = this;
            var loadContent = d.getElementById('extraContent');
            var allLoaded = d.getElementById('allLoadedText');

            button.classList.add('btn-loading');
            button.setAttribute('disabled', 'true');

            setTimeout(function() {
                loadContent.style.display = 'block';
                button.style.display = 'none';
                allLoaded.style.display = 'block';
            }, 1500);
        });
    }

    var scroll = new SmoothScroll('a[href*="#"]', {
        speed: 500,
        speedAsDuration: true
    });

    // SVG Map
    if (d.querySelector('#map')) {
        new svgMap({
            targetElementID: 'map',
            colorMin: '#FCE1C3',
            colorMax: '#F8BD7A',
            flagType: 'emoji',
            data: {
                data: {
                    visitors: {
                        name: 'Visitors',
                        format: '{0} visitors',
                        thousandSeparator: ',',
                        thresholdMax: 500000,
                        thresholdMin: 0
                    },
                    change: {
                        name: 'Change by month',
                        format: '{0} %'
                    }
                },
                applyData: 'visitors',
                values: {
                    US: { visitors: 272109, change: 4.73 },
                    CA: { visitors: 160064, change: 11.09 },
                    DE: { visitors: 120048, change: -2.3 },
                    GB: { visitors: 110048, change: 3.3 },
                    FR: { visitors: 100048, change: 1.3 },
                    ES: { visitors: 90048, change: 1.5 },
                    JP: { visitors: 56022, change: 3.5 },
                    IT: { visitors: 48019, change: 1 },
                    NL: { visitors: 40016, change: 2 },
                    RU: { visitors: 30016, change: 3.4 },
                    CN: { visitors: 50016, change: 6 },
                    IN: { visitors: 140016, change: 2 },
                    BR: { visitors: 40016, change: 5 },
                    // ...
                }
            }
        });
    }

});