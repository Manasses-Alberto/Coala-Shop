for (let card of document.querySelectorAll('.card')) {
    console.log(card.innerHTML)
    card.addEventListener('mouseover', () => {
        card.style.transform = 'scale(1.03)'
        card.querySelector('.card-title').style.color = '#B4BEC9'
        card.querySelector('p').style.color = '#B4BEC9'
    })

    card.addEventListener('mouseleave', () => {
        card.style.transform = 'scale(1)'
        card.querySelector('.card-title').style.color = '#002333'
        card.querySelector('p').style.color = '#002333'
    })
}
