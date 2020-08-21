import { Component, OnInit } from '@angular/core';
import { HandlerService } from "../handler.service";

@Component({
  selector: 'app-tickets',
  templateUrl: './tickets.component.html',
  styleUrls: ['./tickets.component.css']
})
export class TicketsComponent implements OnInit {

  constructor(private service: HandlerService) { }

  ngOnInit(): void {
  }

  dataList = this.service.dataList;
  username = this.getUserName();
  UserAlias = this.service.UA;

  getUserName(){
    return this.service.username;
  }

}
