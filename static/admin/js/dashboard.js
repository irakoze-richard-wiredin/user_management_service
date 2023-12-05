(function($) {
  'use strict';
  $(function() {
    Chart.defaults.global.defaultFontFamily = "'Karla', sans-serif";
    Chart.defaults.global.defaultFontSize = 14;
    Chart.defaults.global.defaultFontColor = '#333';
    Chart.defaults.global.elements.rectangle.backgroundColor = 'rgba(255, 0, 0, 0.6)';
    Chart.defaults.global.elements.rectangle.borderColor = 'rgba(255, 0, 0, 1)';

    var densityCanvas = document.getElementById("densityChart");

    var densityData = {
      label: 'DataSet 1',
      data: [23.1, 11.0, 3.7, 9.8, 3.7, 12.0, 8.9, 9.0],
      yAxisID: "y-axis-density",
      backgroundColor: '#679467'   // primary
    };
     
    var gravityData = {
      label: 'DataSet 2',
      data: [3.7, 8.9, 9.8, 3.7, 23.1, 9.0, 8.7, 11.0],
      yAxisID: "y-axis-density",
      backgroundColor: '#D2C538'   // warning
    };
     
    var set3Data = {
      label: 'DataSet 3',
      data: [23.1, 3.7, 8.9, 8.7, 11.0, 9.8, 3.7, 9.0],
      yAxisID: "y-axis-density",
      backgroundColor: '#00451F'   // default
    };
     
    var planetData = {
      labels: ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"],
      datasets: [densityData, gravityData, set3Data]
    };
    
    var chartOptions = {
      scales: {
        xAxes: [{
          barPercentage: 0.9,
          categoryPercentage: 0.4,
          gridLines: {
            display: false
          },
          ticks: {
            display: false
          }
        }],
        yAxes: [{
          id: "y-axis-density",
          ticks: {
            beginAtZero: true,
            fontColor: '#333',
            fontSize: 12
          },
          gridLines: {
            color: 'rgba(0, 0, 0, 0.1)'
          }
        }]
      },
      legend: {
        display: false
      }
    };
    
    
    var barChart = new Chart(densityCanvas, {
      type: 'bar',
      data: planetData,
      options: chartOptions
    });






    // Donut chart


    // Sample data for the doughnut chart
    var doughnutData = {
      labels: ['Category 1', 'Category 2', 'Category 3', 'Category 4'],
      datasets: [{
        data: [40, 10, 35, 15],
        backgroundColor: ['#00451F', '#D2C538', '#046222', '#67B16B'],     // default, warning, light-dark, success
        hoverBackgroundColor: ['#00451F', '#D2C538', '#046222', '#67B16B']     // default, warning, light-dark, success
      }]
    };

    // Get the context of the canvas element
    var ctx = document.getElementById('myDoughnutChart').getContext('2d');

    var donutOptions = {
      cutoutPercentage: 70,
      legend: {
        display: false
      }
    };

    // Create the doughnut chart
    var myDoughnutChart = new Chart(ctx, {
      type: 'doughnut',
      data: doughnutData,
      options: donutOptions
    });

  });
})(jQuery);
