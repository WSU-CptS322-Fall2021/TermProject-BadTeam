document.addEventListener("DOMContentLoaded", function() {
  var divs = document.getElementsByClassName('active-prompt')
  console.log(divs)
  for(i = 0; i < divs.length; i++){
    // var words = divs[i].getElementsByTagName('div')
    // var letters = words[words.length - 1].getElementsByTagName('div')
    // console.log(letters[letters.length - 1])
    // letters[letters.length - 1].innerText = "TYLER IS HERE"
    // letters[letters.length - 1].className = "incorrect-letter"
  }  

  for(i = 1; i < divs.length; i){
    divs[i].className = 'inactive-prompt'
  }
});