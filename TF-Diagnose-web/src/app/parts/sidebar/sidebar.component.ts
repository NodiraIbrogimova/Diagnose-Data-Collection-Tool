import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.scss']
})
export class SidebarComponent implements OnInit {
  navItems = [
    { name: 'Dashboard', link: 'dashboard' },
    { name: 'View Raw Data', link: 'view' },
    { name: 'Statistics', link: 'statistics' },
    { name: 'Contact Us', link: 'contact' }
  ];
  constructor() { }

  ngOnInit(): void {
  }

}
