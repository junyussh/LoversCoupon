import { Component, OnInit, NgModule } from '@angular/core';
import { HandlerService } from "../handler.service";
import {Router, ActivatedRoute, RouterModule} from '@angular/router';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  constructor(private service: HandlerService, private router: Router, private RA: ActivatedRoute) {}

  navigateToTicket(_user: number) {
    this.router.navigate(['/tickets'], { queryParams: {user: _user}});
 }

  ngOnInit(): void {
  }

}
