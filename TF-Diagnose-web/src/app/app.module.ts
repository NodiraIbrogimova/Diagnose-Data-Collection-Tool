import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ChartsModule } from 'ng2-charts';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AppLogoComponent } from './parts/app-logo/app-logo.component';
import { SignInComponent } from './pages/sign-in/sign-in.component';
import { HeaderComponent } from './parts/header/header.component';
import { FooterComponent } from './parts/footer/footer.component';
import { SidebarComponent } from './parts/sidebar/sidebar.component';
import { ViewComponent } from './pages/view/view.component';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { StatisticsComponent } from './pages/statistics/statistics.component';
import { ContactComponent } from './pages/contact/contact.component';
import { IconHeartbeatComponent } from './parts/icon-heartbeat/icon-heartbeat.component';
import { IconTemperatureComponent } from './parts/icon-temperature/icon-temperature.component';
import { IconCountComponent } from './parts/icon-count/icon-count.component';
import { IconBloodPressureComponent } from './parts/icon-blood-pressure/icon-blood-pressure.component';
import { IconAdminComponent } from './parts/icon-admin/icon-admin.component';
import { BarChartComponent } from './parts/charts/bar-chart/bar-chart.component';
import { DoughnutChartComponent } from './parts/charts/doughnut-chart/doughnut-chart.component';
import { PieChartComponent } from './parts/charts/pie-chart/pie-chart.component';

@NgModule({
  declarations: [
    AppComponent,
    AppLogoComponent,
    SignInComponent,
    HeaderComponent,
    FooterComponent,
    SidebarComponent,
    ViewComponent,
    DashboardComponent,
    StatisticsComponent,
    ContactComponent,
    IconHeartbeatComponent,
    IconTemperatureComponent,
    IconCountComponent,
    IconBloodPressureComponent,
    IconAdminComponent,
    BarChartComponent,
    DoughnutChartComponent,
    PieChartComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ChartsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
