linechartoptions = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.0)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 60,
            suggestedMax: 125,
            padding: 20,
            fontColor: "#9a9a9a"
          }
        }],

        xAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(225,78,202,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#9a9a9a"
          }
        }]
      }
    };
gradientBarChartConfiguration = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{

          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 60,
            suggestedMax: 120,
            padding: 20,
            fontColor: "#9e9e9e"
          }
        }],

        xAxes: [{

          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#9e9e9e"
          }
        }]
      }
    };


var int data = "{{data}}";

var overall = "{{overall}}";

//first line chart polarity_line

let ctx = document.getElementById('polarity_date');
var gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);
gradientStroke.addColorStop(1, 'rgba(29,140,248,0.2)');
gradientStroke.addColorStop(0.4, 'rgba(29,140,248,0.0)');
gradientStroke.addColorStop(0, 'rgba(29,140,248,0)'); //blue colors
let massPopChart = new Chart(ctx,{
   type:'line',
   data:{
      labels:data[0],
      datasets:[{
        label:"",
        data:parseInt(data[1]),
        fill: true,
        backgroundColor:gradientStroke,
        borderColor: '#1f8ef1',
        borderWidth: 2,
        borderDash: [],
        borderDashOffset: 0.0,
        pointBackgroundColor: '#1f8ef1',
        pointBorderColor: 'rgba(255,255,255,0)',
        pointHoverBackgroundColor: '#00d6b4',
        pointBorderWidth: 20,
        pointHoverRadius: 4,
        pointHoverBorderWidth: 15,
        pointRadius: 4,
        }]
    },
    options:linechartoptions
});

var myChart = new Chart(ctx, {
      type: 'bar',
      responsive: true,
      legend: {
        display: false
      },
      data: {
        labels: ['Positive', 'Negative', 'Neutral'],
        datasets: [{
          label: "",
          fill: true,
          backgroundColor: gradientStroke,
          hoverBackgroundColor: gradientStroke,
          borderColor: '#1f8ef1',
          borderWidth: 2,
          borderDash: [],
          borderDashOffset: 0.0,
          data: [53, 20, 10, 80, 100, 45],
        }]
      },
      options: gradientBarChartConfiguration
    });



    /*function loaddata(canid, lable1, lable2, lable3, lable4, lable5, lable6){
        this.canid = canid;
        this.lable1 = lable1;
        this.lable2 = lable2;
        this.lable3 = lable3;
        this.lable4 = lable4;
        this.lable5 = lable5;
        this.lable6 = lable6;
        var x = 100;//parseInt("{{positive}}");
        var y =  600;//parseInt("{{negative}}");
        var z =  700;//parseInt("{{neutral}}");
        var sad = 600;//parseInt("{{sad}}");
        var ang = 800;//parseInt("{{ang}}");
        var joy = 900;//parseInt("{{joy}}");
        var total = x+y+z+sad+ang+joy;
        var type = 'line';
        var all = [x,y,z,sad,ang,joy];
        var bg1 = ['#003333','#E62727','#10375C'];
        var bg2 = ['#2A0033','#CC3300','#F3C623'];
        Chart.defaults.global.responsive=true;
        //Chart.defaults.global.defaultFontSize='2px';


        let massPopChart = new Chart(ctx,{
         type:type,
            data:{
                labels:labels,
                datasets:[{
                    barPercentage:0.5,
                    categoryPercentage: 0.7,
                 label:"",
                 data:data,
                 fill: true,
            backgroundColor:gradientStroke,
            borderColor: '#1f8ef1',
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            pointBackgroundColor: '#1f8ef1',
            pointBorderColor: 'rgba(255,255,255,0)',
            pointHoverBackgroundColor: '#00d6b4',
            pointBorderWidth: 20,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 15,
            pointRadius: 4,
        }]
    },
    options:linechartoptions
});}*/