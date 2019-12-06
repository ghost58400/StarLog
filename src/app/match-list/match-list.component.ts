import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-match-list',
  templateUrl: './match-list.component.html',
  styleUrls: ['./match-list.component.css']
})
export class MatchListComponent implements OnInit {

  list=[{
    imgSource:"assets/man1.jpg",
    Desc:"Blablabla, les infos",
    Ville:"Bourges",
    Nom:"Jean-Cloud",
    likes:true,
    youLike:true,
    messages:[{
      me:true,
      content:"salut",
      date:"11:07"
    }]
  },{
    imgSource:"assets/girl1.jpg",
    Desc:"Blablabla, les infos",
    Ville:"Bourges",
    Nom:"Jeanine",
    likes:true,
    youLike:true,
    messages:[{
      me:true,
      content:"hellooo",
      date:"15:34"
    }]
  }]
  activeChat=this.list[0];
  isActive=false;
  constructor() { }

  ngOnInit() {
  }

  sendMessage(){
    var input=(<HTMLInputElement>document.getElementById("messageInput")).value;
    var d = new Date();
    this.activeChat.messages.push({me:true,content:input,date:d.getHours()+":"+d.getMinutes()});
    (<HTMLInputElement>document.getElementById("messageInput")).value="";
  }
  closeModal(){
    this.isActive=false;
  }
  openModal(person){
    this.activeChat=person;
    this.isActive=true;
  }
}
