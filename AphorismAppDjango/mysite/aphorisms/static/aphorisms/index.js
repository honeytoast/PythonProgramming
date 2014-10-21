/*#### Grace Hadiyanto
#### e-mail: ifoundparis@gmail.com
#### Assignment 7
#### CS223P
*/

var getFortune = function () { 
    //fortune.innerHTML = marquee1 + aphorism + marquee2;
    //uncomment above for scrolling text but the timing is not very good.
    //can uncomment the block within id="fortune" in index.html for better
    //results instead.

    //uncomment below for text that types out
    fortune.innerHTML = aphorism;
    new TypingText(fortune);
    TypingText.runAll();
}

var openChest = function () {
    chest.src = img;
    window.location.reload();
}

window.onload = getFortune;
chest.onclick = openChest;
