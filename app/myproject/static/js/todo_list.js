function checked(id) {
  var checked_green = document.getElementById("check" + id);
  checked_green.classList.toggle("selected_task");
  var strike_unstrike = document.getElementById("strike" + id);
  strike_unstrike.classList.toggle("strike_none");
}
