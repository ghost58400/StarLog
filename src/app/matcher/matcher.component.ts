import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-matcher',
  templateUrl: './matcher.component.html',
  styleUrls: ['./matcher.component.css']
})
export class MatcherComponent implements OnInit {

  list=[{
    imgSource:"assets/man1.jpg",
    Desc:"Jeuné diplomé, je peux aider autant dans les matières scolaires (méthématiques, physique) que sur des petites astuces pour mieux organiser son travail personnel afin d'être plus efficace.",
    Ville:"Bourges",
    Nom:"Jean-Cloud",
    likes:true,
    youLike:false,
    messages:[]
  },{
    imgSource:"assets/girl1.jpg",
    Desc:"J'habite sur Bourges depuis toujours et je connais tous les établissement dont vous pourriez avoir besoin si vous arrivez juste dans la ville, si vous avez des problèmes financiers, je pourrais vous rediriger vers les organismes qui sauront vous aider facilement",
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
  profileShown=false;
  match=this.list[0];
  constructor() { }
  profil={
    imgSource:"assets/img3.svg",
    Desc:"Jeune Etudiant, je suis nouveau à Bourges et j'aimerais en apprendre d'avantage sur la ville et les facilités réservées aux étudiants",
    Ville:"Bourges",
    Nom:"Louis",
    likes:true,
    youLike:false,
    messages:[]
  }

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
  showProfile(){
    this.profileShown=true;
  }
  hideProfile(){
    this.profileShown=false;
  }
}
