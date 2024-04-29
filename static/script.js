var prevScrollpos = window.scrollY || window.pageYOffset;
var header = document.querySelector(".header");
var navbar = document.querySelector(".navbar");

window.addEventListener("scroll", function() {
    var currentScrollPos = window.scrollY || window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        header.style.top = "0";
        navbar.style.opacity = "1";
    } else {
        header.style.top = "-100px"; // Adjust the value based on the height of your header
        navbar.style.opacity = "10";
    }
    prevScrollpos = currentScrollPos;
});

