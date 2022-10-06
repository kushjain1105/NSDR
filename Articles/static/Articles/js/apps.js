document.addEventListener("DOMContentLoaded", function() {
    console.log("Hello, world!");
    const toggleButton = document.querySelector(".toggle-button");
    const navLinks = document.querySelector(".links");
    toggleButton.onclick = function() {
        navLinks.classList.toggle("active");
    }
});