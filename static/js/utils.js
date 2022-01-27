// ** start code blocks used for setting terminal icon to blink on home section ** 
var icon = document.getElementById('terminal_blink');
var icon_switch = icon.getAttribute('name');

var interval = window.setInterval(function(){
    if (icon_switch == 'True'){
        if(icon.style.visibility == 'hidden'){
            icon.style.visibility = 'visible';
        }else{
            icon.style.visibility = 'hidden';
        }
    } 
    else{
        icon.style.visibility = 'visible';
    }
    
}, 300);
// ** End code blocks used for setting terminal icon to blink on home section ** 