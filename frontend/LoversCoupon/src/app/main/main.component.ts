import { Component, OnInit } from '@angular/core';
import { HandlerService } from "../handler.service";
import {Router} from '@angular/router';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  constructor(private service: HandlerService, private router: Router) {}

  setUser(_user: number){
    this.service.user = _user;
    console.log(this.service.user);
  }

  navigateToTicket() {
    this.router.navigateByUrl('/tickets');
 }

  ngOnInit(): void {
  }

}
