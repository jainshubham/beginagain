var menu = document.getElementById("menu");

function showMenu() {
   menu.classList.add("open-menu");
}

function showCreateProfile() {
   var createProfileBtn = document.getElementById("create-profile-dialog");

   createProfileBtn.classList.add("open-create-profile");
   menu.classList.toggle("open-menu");
}

function showAccountMenu(){
   var accountDropdown = document.querySelector('.account-dropdown');
   accountDropdown.classList.toggle("account-dropdown-open")
}