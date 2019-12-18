var gauche = document.getElementById("gauche");
var droite = document.getElementById("droite");
var porte = document.getElementById("porte");
var CS = document.getElementById("CS");
var vitesse = 3;


var largeurG = parseFloat(getComputedStyle(gauche).width);
var largeurD = parseFloat(getComputedStyle(droite).width);
var xMax = parseFloat(getComputedStyle(porte).width);

var animID = null;



function open(){

    var xGauche = parseFloat(getComputedStyle(gauche).left);
    var xDroite = parseFloat(getComputedStyle(droite).left);


    var xMax = parseFloat(getComputedStyle(porte).width);

    
    var progress = (xDroite+largeurG/2.5)/xMax*2;
    CS.style.opacity = progress;

    var trans = parseFloat(getComputedStyle(porte).opacity)

        
    if ((xDroite+largeurG/2) <= xMax){

        gauche.style.left =(xGauche - vitesse) +"px";
        droite.style.left =(xDroite + vitesse) +"px";


        animID = requestAnimationFrame(open);
    }
    else{
        cancelAnimationFrame(animID);
    }
}
animID = requestAnimationFrame(open);