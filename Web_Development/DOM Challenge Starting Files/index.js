var last_ul = document.querySelector('ul').lastElementChild
last_ul.innerHTML = "Shiva's Website"


var google_link = document.querySelector('.list a')
google_link.style.color = "red"

var click_me_btn = document.querySelector('#btn')
click_me_btn.style.backgroundColor = 'yellow'

var hello_text = document.querySelector('h1')



click_me_btn.addEventListener('click', function(){
    hello_text.classList.toggle('huge');
    // hello_text.innerHTML = '<em> Good Bye </em>' 
});