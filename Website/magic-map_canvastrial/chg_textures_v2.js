var imgURL=$('#image0');
var img;

URL=imgURL.src;

function setup(){
    canvas=createCanvas(400, 400);
    img=createImg(URL, test); //saem issue: image is in teh "broken" state
    img.hide()
}


function draw(){
    background(0);
    image(img, 0, 0, img.elt.width, img.elt.height);


}