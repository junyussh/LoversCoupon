import { Component, OnInit } from '@angular/core';
import { HandlerService } from "../handler.service";

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  constructor(private service: HandlerService) {}

  setUser(_user){
    //this.service.user = _user;
    console.log(this.service.user);
  }

  ngOnInit(): void {
  }

}
