document.addEventListener('DOMContentLoaded', function() {
  const signInBtn = document.getElementById("signIn");
  const signUpBtn = document.getElementById("signUp");
  const container = document.querySelector(".container");
  const signUpButton = document.querySelector(".container--signup .btn");
  const loginForm = document.getElementById("loginForm");

  signInBtn.addEventListener("click", () => {
    container.classList.remove("right-panel-active");
  });

  signUpBtn.addEventListener("click", () => {
    container.classList.add("right-panel-active");
  });

  signUpButton.addEventListener("click", showPopup);

  const loginButton = document.querySelector(".container--signin .btn");
  loginButton.addEventListener("click", () => {
    container.classList.add("right-panel-active");
  });

  function showPopup() {
    var popupContainer = document.getElementById('popupContainer');
    popupContainer.style.display = 'block';
  }
});
