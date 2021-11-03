import { Component, OnInit } from '@angular/core';
import { Label, MultiDataSet, Color } from 'ng2-charts';
import { ChartType } from 'chart.js';

@Component({
  selector: 'app-doughnut-chart',
  templateUrl: './doughnut-chart.component.html',
  styleUrls: ['./doughnut-chart.component.scss']
})
export class DoughnutChartComponent {
  doughnutChartLabels: Label[] = ['Blood', 'Stool', 'Widal'];
  doughnutChartData: MultiDataSet = [[53, 30, 17]];
  doughnutChartType: ChartType = 'doughnut';
}
