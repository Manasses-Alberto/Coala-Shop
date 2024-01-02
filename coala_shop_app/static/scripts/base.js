document.querySelector('button#account-actions-modal-btn').addEventListener('click', () => {
    if (document.querySelector('article#products-datas').getAttribute('data-authenticated') === 'False') {
        document.querySelector('header').style.opacity = '0'
        document.querySelector('header').style.pointerEvents = 'none'
        document.querySelector('article').style.opacity = '0'
        document.querySelector('article').style.pointerEvents = 'none'
        document.querySelector('footer').style.opacity = '0'
        document.querySelector('footer').style.pointerEvents = 'none'
        document.body.style.overflowY = 'hidden'
        document.querySelector('#modal-account-actions').classList.remove('visually-hidden')
        document.querySelector('#modal-account-actions').style.opacity = '1'
    } else {
        location.href = `/user-profile/${document.querySelector('article#products-datas').getAttribute('data-user')}/`
    }
})

document.querySelector('button#redirect-to-home-btn').addEventListener('click', () => {
    location.href = '/'
})
