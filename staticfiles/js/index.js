window.addEventListener('load', () => {
    const hamburguer = document.querySelector('.hamburguer')
    const navbar = document.querySelector('.navbar')

    const closeButon = document.querySelector('.close-button')
    if (hamburguer && navbar) {
        hamburguer.addEventListener('click', () => {
            navbar.classList.add('active')
        })
    }
    if (closeButon && navbar) {
        closeButon.addEventListener('click', () => {
            navbar.classList.remove('active')
        })
    }
})