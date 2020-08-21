import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule ,Routes} from "@angular/router";

import { AppComponent } from './app.component';
import { AddComponent } from './add/add.component';
import { MainComponent } from "./main/main.component";
import { TicketsComponent } from './tickets/tickets.component';
 
const routes: Routes = [
  {path: "", component: MainComponent},
  {path: "add", component: AddComponent},
  {path: "tickets", component: TicketsComponent}
]

@NgModule({
  declarations: [
    AppComponent,
    AddComponent,
    TicketsComponent
  ],
  imports: [BrowserModule,  RouterModule.forRoot(routes)],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
