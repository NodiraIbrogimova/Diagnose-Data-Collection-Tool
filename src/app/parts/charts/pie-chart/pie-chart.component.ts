import { Component } from '@angular/core';
import { ChartOptions, ChartType } from 'chart.js';
import { Label } from 'ng2-charts';

@Component({
  selector: 'app-pie-chart',
  templateUrl: './pie-chart.component.html',
  styleUrls: ['./pie-chart.component.scss']
})
export class PieChartComponent{
  pieChartOptions: ChartOptions = {
    responsive: true,
    legend: {
      position: 'top'
    },
    tooltips: {
      enabled: true,
      mode: 'single',
      callbacks: {
        label: function(tooltipItems, data:any) {
          return 20 + ' %';
        }
      }
    }
  };

  pieChartLabels: Label[] = ['Diarrhea/Constipation', 'Cough', 'High Fever', 'Loss of Appetite'];

  pieChartData: number[] = [78.09, 20.95, 0.93, 0.03];

  pieChartType: ChartType = 'pie';

  pieChartLegend = true;

  pieChartPlugins = [];

  pieChartColors = [
    {
      backgroundColor: [
        'rgba(50, 168, 82,0.3)',
        'rgba(62, 50, 168,0.3)',
        'rgba(163, 71, 10,0.3)'
      ]
    }
  ];

}
