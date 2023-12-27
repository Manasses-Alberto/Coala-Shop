let like_btn = document.querySelector('#like-btn')
let dislike_btn = document.querySelector('#dislike-btn')
let icon_like = document.querySelector('#icon-like')
let icon_dislike = document.querySelector('#icon-dislike')

like_btn.addEventListener('click', () => {
    if (icon_dislike.classList.contains('bi-hand-thumbs-down-fill') === true) {
        icon_dislike.classList.replace('bi-hand-thumbs-down-fill', 'bi-hand-thumbs-down')
        icon_like.classList.replace('bi-hand-thumbs-up', 'bi-hand-thumbs-up-fill')
    } else if (icon_like.classList.contains('bi-hand-thumbs-up-fill') === true) {
        icon_like.classList.replace('bi-hand-thumbs-up-fill', 'bi-hand-thumbs-up')
    } else if (icon_dislike.classList.contains('bi-hand-thumbs-down') === true) {
        icon_like.classList.replace('bi-hand-thumbs-up', 'bi-hand-thumbs-up-fill')
    }
})

dislike_btn.addEventListener('click', () => {
    if (icon_like.classList.contains('bi-hand-thumbs-up-fill') === true) {
        icon_like.classList.replace('bi-hand-thumbs-up-fill', 'bi-hand-thumbs-up')
        icon_dislike.classList.replace('bi-hand-thumbs-down', 'bi-hand-thumbs-down-fill')
    } else if (icon_dislike.classList.contains('bi-hand-thumbs-down-fill') === true) {
        icon_dislike.classList.replace('bi-hand-thumbs-down-fill', 'bi-hand-thumbs-down')
    } else if (icon_like.classList.contains('bi-hand-thumbs-up') === true) {
        icon_dislike.classList.replace('bi-hand-thumbs-down', 'bi-hand-thumbs-down-fill')
    }
})

document.querySelector('button#send-feedback-modal').addEventListener('click', () => {
    document.body.style.overflowY = 'hidden'
    document.querySelector('header').style.pointerEvents = 'none'
    document.querySelector('article').style.pointerEvents = 'none'
    document.querySelector('footer').style.pointerEvents = 'none'
    document.querySelector('header').style.opacity = '0'
    document.querySelector('article').style.opacity = '0'
    document.querySelector('footer').style.opacity = '0'
    document.querySelector('div#feedback-area').classList.remove('visually-hidden')
    document.querySelector('div#feedback-area').style.opacity = '1'
})

document.querySelector('button#close-modal-feedback').addEventListener('click', () => {
    document.querySelector('header').style.pointerEvents = 'all'
    document.querySelector('article').style.pointerEvents = 'all'
    document.querySelector('footer').style.pointerEvents = 'all'
    document.querySelector('header').style.opacity = '1'
    document.querySelector('article').style.opacity = '1'
    document.querySelector('footer').style.opacity = '1'
    document.body.style.overflowY = 'auto'
    document.querySelector('div#feedback-area').classList.add('visually-hidden')
    document.querySelector('div#feedback-area').style.opacity = '0'
})

document.querySelector('#send-complaint-modal').addEventListener('click', () => {
    document.querySelector('header').style.pointerEvents = 'none'
    document.querySelector('article').style.pointerEvents = 'none'
    document.querySelector('footer').style.pointerEvents = 'none'
    document.querySelector('header').style.opacity = '0'
    document.querySelector('article').style.opacity = '0'
    document.querySelector('footer').style.opacity = '0'
    document.body.style.overflowY = 'hidden'
    document.querySelector('#complaints-area').classList.remove('visually-hidden')
    document.querySelector('#complaints-area').style.opacity = '1'
})

document.querySelector('#close-modal-complaint').addEventListener('click', () => {
    document.querySelector('header').style.pointerEvents = 'all'
    document.querySelector('article').style.pointerEvents = 'all'
    document.querySelector('footer').style.pointerEvents = 'all'
    document.querySelector('header').style.opacity = '1'
    document.querySelector('article').style.opacity = '1'
    document.querySelector('footer').style.opacity = '1'
    document.body.style.overflowY = 'auto'
    document.querySelector('#complaints-area').classList.add('visually-hidden')
    document.querySelector('#complaints-area').style.opacity = '0'
})
