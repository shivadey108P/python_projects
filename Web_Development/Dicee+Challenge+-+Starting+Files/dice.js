var click_me = document.querySelector('h1');



click_me.addEventListener('click', function(){
    randomNumber1 = Math.floor(Math.random()* 6)+1;
    randomNumber2 = Math.floor(Math.random()* 6)+1;
    document.querySelector('.img1').setAttribute('src', "images/dice"+randomNumber1+".png")
    document.querySelector('.img2').setAttribute('src', "images/dice"+randomNumber2+".png")
    if(randomNumber1 > randomNumber2){
        click_me.innerHTML = '🥇 Player 1 Wins!'
    }
    else if(randomNumber2 > randomNumber1){
        click_me.innerHTML = 'Player 2 Wins! 🥈'
    }
    else{
        click_me.innerHTML = "It's a draw"
    }
});