



console.log('execution of my file');
var img = document.getElementById("image0");

var img2= new Image();
img2.src=img.src;
console.log(img.src);

img2.setAttribute('crossOrigin', '');
img2.onload=function() {

    console.log('We get into the function');

    drawMyImg(this)
}

function drawMyImg(img) {
    var canvas= document.getElementById("myCanvas");
    var ctx = canvas.getContext('2d');
    ctx.drawImage(img, 0, 0);
    var imageData=ctx.getImageData(0,0, canvas, canvas.width, canvas.height);
    var data=imageData.data;

    var recolorImage= function(oldRed, oldGreen, oldBlue, newRed, newGreen, newBlue){
        // examine every pixel,
    // change any old rgb to the new-rgb
    for (var i = 0; i < data.length; i += 4) {
        // is this pixel the old rgb?
        if (data[i] == oldRed && data[i + 1] == oldGreen && data[i + 2] == oldBlue) {
            // change to your new rgb
            data[i] = newRed;
            data[i + 1] = newGreen;
            data[i + 2] = newBlue;
        }
    }
    console.log('Changed colour of the image');
    ctx.putImageData(imageData, 0, 0);
    }

    var chgColBtn = document.getElementById('change-Color');
    chgColBtn.addEventListener('click', recolorImage);


}


// function recolorImage(oldRed, oldGreen, oldBlue, newRed, newGreen, newBlue) {
//
//     // examine every pixel,
//     // change any old rgb to the new-rgb
//     for (var i = 0; i < data.length; i += 4) {
//         // is this pixel the old rgb?
//         if (data[i] == oldRed && data[i + 1] == oldGreen && data[i + 2] == oldBlue) {
//             // change to your new rgb
//             data[i] = newRed;
//             data[i + 1] = newGreen;
//             data[i + 2] = newBlue;
//         }
//     }
//     console.log('Changed colour of the image');
// }
