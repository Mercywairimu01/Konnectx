let menuIcon = document.querySelector('.hamburger-menu')

let navbar = document.querySelector(".navbar")

menuIcon.addEventListener('click', () => {
  navbar.classList.toggle("change")
})