document.addEventListener("keydown", function(event) {
    let wordsWrapper = 'prompt-0'
    const correctLetter = 'correct-letter'
    const incorrectLetter = 'incorrect-letter'
    const incompleteLetter = 'incomplete-letter'
    const incompleteWord = 'incomplete-word'
    const completeLetter = 'complete-word'
    const continueHidden = 'continue-hidden'
    const continueVisible = 'continue-visible'
    const inactivePrompt = 'inactive-prompt'
    const activePrompt = 'active-prompt'

    let promptNumber = 0

    if(event.which == 8){
      backspace()
      return;
    }  
    if(event.which == 13){
        pressEnter()
        return;
    }
    if (invalidCode()) { return; }
    typingLetter()
  
    function backspace(){
      var div = document.getElementById(wordsWrapper);
      var words = div.getElementsByTagName('div')
      hideContinue()
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
      var div = document.getElementById(wordsWrapper);
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
      showContinue()
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
  
    function showContinue(){
        document.getElementById('continue-prompt').className = continueVisible
    }

    function hideContinue(){
        document.getElementById('continue-prompt').className = continueHidden
    }

    function pressEnter(){
        if(document.getElementById('continue-prompt').className == continueVisible){
            var div = document.getElementById(wordsWrapper);
            div.className = inactivePrompt
            promptNumber++;
            wordsWrapper = `prompt-${promptNumber}`
            var div = document.getElementById(wordsWrapper);
            div.className = activePrompt
            document.getElementById('continue-prompt').className == continueHidden
        }
    }
    });
  