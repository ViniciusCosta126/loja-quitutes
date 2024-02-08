window.addEventListener('load', () => {
    //Menu hamburguer
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

    const arrow = document.querySelector('.arrow')
    const submenu = document.querySelector('.sub-menu')
    console.log(arrow)
    console.log(submenu)

    if (arrow && submenu) {
        arrow.addEventListener('click', () => {
            arrow.classList.toggle('active')
            submenu.classList.toggle('active')
        })
    }

})