function card_hover_effect(over, leave) {
    if (over) {
        card.style.transform = 'scale(1.03)'
        card.querySelector('.card-title').style.color = '#B4BEC9'
        card.querySelector('p').style.color = '#B4BEC9'
    }

    if (leave) {
        card.style.transform = 'scale(1)'
        card.querySelector('.card-title').style.color = '#002333'
        card.querySelector('p').style.color = '#002333'
    }
}

for (let card of document.querySelector('#products-datas').querySelectorAll('.card')) {
    card.querySelector('.card-title').addEventListener('mouseover', () => {
        card_hover_effect(over=true, leave=false)
    })

    card.querySelector('.card-img-top').addEventListener('mouseover', () => {
        card_hover_effect(over=true, leave=false)
    })

    card.querySelector('p').addEventListener('mouseover', () => {
        card_hover_effect(over=true, leave=false)
    })

    card.querySelector('.card-title').addEventListener('mouseleave', () => {
        card_hover_effect(over=false, leave=true)
    })

    card.querySelector('.card-img-top').addEventListener('mouseleave', () => {
        card_hover_effect(over=false, leave=true)
    })

    card.querySelector('p').addEventListener('mouseleave', () => {
        card_hover_effect(over=false, leave=true)
    })

    card.addEventListener('click', () => {
        let product_id = card.getAttribute('id')
        location.href = `/product/${product_id}/`
    })
}

document.querySelector('#account-actions-modal-xbtn').addEventListener('click', () => {
    document.querySelector('header').style.opacity = '1'
    document.querySelector('header').style.pointerEvents = 'auto'
    document.querySelector('article').style.opacity = '1'
    document.querySelector('article').style.pointerEvents = 'auto'
    document.querySelector('footer').style.opacity = '1'
    document.querySelector('footer').style.pointerEvents = 'auto'
    document.body.style.overflowY = 'auto'
    document.querySelector('#modal-account-actions').style.opacity = '0'
    document.querySelector('#modal-account-actions').classList.add('visually-hidden')
})

document.querySelector('#login-btn').addEventListener('click', () => {
    location.href = '/auth/login/'
})

document.querySelector('#register-btn').addEventListener('click', () => {
    location.href = '/auth/register/'
})
