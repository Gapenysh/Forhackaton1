import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { MapComponent } from './components/map/map.component';

const routes: Routes = [
  {
    path:'',
    component:HomeComponent,
    title: 'Home',
  },
  {
    path:'map',
    component:MapComponent,
    title: 'Map',
  },
  {
    path:'**',
    component:HomeComponent,
    redirectTo: '',
  },

  
 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
