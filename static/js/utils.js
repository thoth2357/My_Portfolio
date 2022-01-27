// ** start code blocks used for setting terminal icon to blink on home section ** 
var icon = document.getElementById('terminal_blink');

var interval = window.setInterval(function(){
    if(icon.style.visibility == 'hidden'){
        icon.style.visibility = 'visible';
    }else{
        icon.style.visibility = 'hidden';
    }
}, 500);
// ** End code blocks used for setting terminal icon to blink on home section ** 