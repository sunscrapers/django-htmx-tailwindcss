var setdate = document.querySelector(".set_date");
var settime = document.querySelector(".set_time");

var date = new Date().toDateString();
setdate.innerHTML = date;

setInterval(function () {
    var time = new Date().toLocaleTimeString();
    settime.innerHTML = time;
}, 500);

function checked(id) {
    var checked_green = document.getElementById("check" + id);
    checked_green.classList.toggle("selected_task");
    var strike_unstrike = document.getElementById("strike" + id);
    strike_unstrike.classList.toggle("strike_none");
}
