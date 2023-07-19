// document.querySelector('#test').innerHTML = 'Afrik_Kitchen';
// to store the ti
let hours  = 6;
let hoursnow = new Date.getTime(); // to get time when the user uses application
let checkTime = localStorage.getting('checkTime');

if (checkTime == null){
    localStorage.setItem('checkTime', now) // to store the varable in the browse of the user
}
else {
    if(hoursnow - checkTime > hours*60*60*1000) {
        localStorage.clear();
        localStorage.setItem('checkTime', now);

    }
}

