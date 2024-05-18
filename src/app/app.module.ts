import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './pages/home/home.component';
import { MapComponent } from './components/map/map.component';

@NgModule({
  declarations: [AppComponent, HomeComponent, MapComponent],
  imports: [BrowserModule, AppRoutingModule,HttpClientModule,],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
