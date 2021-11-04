document.addEventListener("keydown", function(event) {
    const wordsWrapper = 'takechallenge-body'
    const correctLetter = 'correct-letter'
    const incorrectLetter = 'incorrect-letter'
    const incompleteLetter = 'incomplete-letter'
    const incompleteWord = 'incomplete-word'
    const completeLetter = 'complete-word'
    let promptFinished = false
    
    if(event.which == 8){
      backspace()
      return;
    }  
    if (invalidCode()) { return; }
    typingLetter()
  
    function backspace(){
      var div = document.getElementById(wordsWrapper);
      var words = div.getElementsByTagName('div')
  
      for(i = words.length - 1; i >= 0; i--){
        var letters = words[i].getElementsByTagName('div')
        console.log(letters)
        for(j = letters.length - 1; j >= 0; j--){
          console.log(letters[j].innerText)
          if(letters[j].className == correctLetter || letters[j].className == incorrectLetter){
            letters[j].className = incompleteLetter
            words[i].className = incompleteWord
            promptFinished = false
            return;
          }
        }
      }
    }
  
    function typingLetter(){
      var div = document.getElementById('takechallenge-body');
      var words = div.getElementsByTagName('div')
      for(i = 0; i < words.length; i++){
        var letters = words[i].getElementsByTagName('div')
        if(words[i].className == incompleteWord){
          for(j = 0; j < letters.length; j++){
            console.log(letters[j].innerText)
            if(letters[j].className == incompleteLetter){
              if(letters[j].innerText === event.key){
                letters[j].className = correctLetter
              } else{
                letters[j].className = incorrectLetter
              }
              return;
            }
          }
          if(isSpace){
            words[i].className = completeLetter
            return
          }
        }
      }
        promptFinished = true// everything is typed
    }
  
    function invalidCode(){
      return !isSpace() && event.which < 48 || (event.which > 90 && event.which < 186) || event.which > 192
      // for reference https://css-tricks.com/snippets/javascript/javascript-keycodes/
    }
  
    function isSpace(){
        // Stop the space bar from scrolling the page down
        event.preventDefault();
        return event.which == 32
    }
  
    });
  