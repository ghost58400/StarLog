import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-matcher',
  templateUrl: './matcher.component.html',
  styleUrls: ['./matcher.component.css']
})
export class MatcherComponent implements OnInit {

  list=[{
    imgSource:"assets/man1.jpg",
    Desc:"Blablabla, les infos",
    Ville:"Bourges",
    Nom:"Jean-Cloud",
    likes:true,
    youLike:false,
    messages:[]
  },{
    imgSource:"assets/girl1.jpg",
    Desc:"Blablabla, les infos",
    Ville:"Bourges",
    Nom:"Jeanine",
    likes:true,
    youLike:false,
    messages:[]
  }]
  currentIndex=0;
  show=this.list[this.currentIndex];
  showLikeAlert=false;
  listIsEmpty=false;
  isMatch=false;
  match=this.list[0];
  constructor() { }

  ngOnInit() {
  }
  next(){
    console.log("user next");
    if(this.currentIndex+1<this.list.length){
      this.currentIndex++;
      this.show=this.list[this.currentIndex];
    }else{
      this.listIsEmpty=true;
    }

  }
  like(){
    console.log("user like");
    this.showLikeAlert=true;
    var that=this;
    if(this.show.likes==true){
      var index=this.currentIndex;
      this.list[index].youLike=true;
      this.match=this.list[index];
      this.isMatch=true;
    }
    this.next();
    setTimeout(() => { this.showLikeAlert=false }, 2000);
  }
  closeModal(){
    this.isMatch=false;
  }
}
