import { Component, OnInit, NgModule, DoCheck } from '@angular/core';
import { HandlerService } from "../handler.service";
import { Router, ActivatedRoute, RouterModule } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { LCConfig } from "../Config/config";
import { FormsModule } from "@angular/forms"
 
@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})

export class MainComponent implements OnInit, DoCheck {
  password: string;

  constructor(private service: HandlerService, private router: Router, private RA: ActivatedRoute, /*private HttpClient: HttpClient*/) {
    //this.ApiUrl = 
  }

  navigateToTicket(_user: number) {
    this.router.navigate(['/tickets'], { queryParams: { user: _user } });
  }

  Auth(event) {
    //let auth_response = this.HttpClient.get<boolean>(`APIURL${event.target.value}`);
    //alert(event.target.value);
    console.log(event.target.value);
  }

  ngOnInit(): void {
  }

  ngDocheck(event): void{
    this.password = event.target.value;
    console.log(event.target.value);
  }

}
