let promptNumber = 0
let wordsWrapper = `prompt-${promptNumber}`
let continuePrompt = `continue-prompt-${promptNumber}`
const correctLetter = 'correct-letter'
const incorrectLetter = 'incorrect-letter'
const incompleteLetter = 'incomplete-letter'
const incompleteWord = 'incomplete-word'
const completeWord = 'complete-word'
const continueHidden = 'continue-hidden'
const continueVisible = 'continue-visible'
const inactivePrompt = 'inactive-prompt'
const activePrompt = 'active-prompt'
const extraLetter = 'extra-letter'

var correctLetters = 0
var incorrectLetters = 0
var promptFinished = false

document.addEventListener("keydown", function(event) {
    //checkEmptyPrompt()
    if(event.which == 8){
      backspace()
      return;
    }  
    if(event.which == 13){
        pressEnter()
        return;
    }
    if(event.which == 32){
      event.preventDefault()
    }

    if (invalidCode()) { return; }
    if(!promptFinished){
      console.log("stupid tyler")
      typingLetter()
    }
  
    function backspace(){
      var div = document.getElementById(wordsWrapper);
      var words = div.getElementsByTagName('div')
      hideContinue()
      for(i = words.length - 1; i >= 0; i--){
        var letters = words[i].getElementsByTagName('div')
        console.log(letters)
        for(j = letters.length - 1; j >= 0; j--){
          console.log(letters[j].innerText)

          if(letters[j].className == extraLetter){
            extraDivs = document.getElementsByClassName(extraLetter)
            extraDivs[extraDivs.length - 1].remove()
            return
          }
          else if(letters[j].className == correctLetter || letters[j].className == incorrectLetter){
            letters[j].className = incompleteLetter
            words[i].className = incompleteWord
            promptFinished = false
            return;
          }
        }
      }
    }
  
    function typingLetter(){
      console.log("top tpying")
      hideContinue()
      var div = document.getElementById(wordsWrapper);
      //div = div.getElementsByTagName('div')
      //var words = div.getElementsByTagName('div')
      var words = div.getElementsByClassName(incompleteWord)
      console.log(words.length)
      console.log(words)
      for(i = 0; i < words.length; i++){
        console.log("infinity")
        var letters = words[i].getElementsByTagName('div')
        console.log(letters.length)
        if(words[i].className == incompleteWord){
          
          for(j = 0; j < letters.length; j++){
            //console.log(letters[j].innerText)
            console.log("inner infinity")
            if(letters[j].className == incompleteLetter){
              
              if(letters[j].innerText === event.key){
                letters[j].className = correctLetter
                correctLetters++
              } else{
                letters[j].className = incorrectLetter
                incorrectLetters++
              }
              if(i == words.length - 1 && j == letters.length - 1){
                console.log("here")
                words[words.length - 1].className = completeWord
                showContinue()
              }
              
              return;
            }
          }
          if(event.which == 32){
            console.log("space")
            words[i].className = completeWord
            return
          } else {
            console.log("here")
            var newDiv = document.createElement('div')
            newDiv.className = extraLetter
            newDiv.innerText = event.key
            words[i].appendChild(newDiv)
            return
          }
        }
      }
      // if(words[words.length - 1].className == completeWord){
      //   showContinue()
      // }
    }
  
    function invalidCode(){
      return event.which != 32 && event.which != 222 && (event.which < 48 || (event.which > 90 && event.which < 186) || event.which > 192)
      // for reference https://css-tricks.com/snippets/javascript/javascript-keycodes/
    }
  
    function isSpace(){
        // Stop the space bar from scrolling the page down
        //event.preventDefault();
        return event.which === 32
    }
  
    function showContinue(){
        document.getElementById(continuePrompt).className = continueVisible
        if(timer.isRunning){
            timer.stop()
        }
        promptFinished = true
    }

    function hideContinue(){
        document.getElementById(continuePrompt).className = continueHidden
        if(!timer.isRunning){
            timer.start()
        }
        promptFinished = false
    }

    function pressEnter(){
        if(document.getElementById(continuePrompt).className == continueVisible){
            // this is bad and needs to be refactored

            var div = document.getElementById(wordsWrapper);
            document.getElementById(continuePrompt).className = continueHidden
            div.className = inactivePrompt
            promptNumber++;
            wordsWrapper = `prompt-${promptNumber}`
            continuePrompt = `continue-prompt-${promptNumber}`
            var div = document.getElementById(wordsWrapper);
            div.className = activePrompt
            var words = div.getElementsByTagName('div')
            var letters = words[0].getElementsByTagName('div')
            console.log(letters.length)
            if(letters.length <= 0){
              console.log("Trying to post")
              finished()
              return
          }
        }
        hideContinue()
        timer.stop()
    }

    function finished(){
        let data = {
            elapsedTime: timer.getTime().toString(),
            correctLetters: correctLetters,
            incorrectLetters: incorrectLetters
        }
        let url = document.URL
        fetch(url, {
            method: "POST", 
            body: JSON.stringify(data)
          }).then(res => {
            console.log("Request complete! response:", res);
          });
    }
    });

    //https://stackoverflow.com/questions/29971898/how-to-create-an-accurate-timer-in-javascript
    class Timer {
        constructor () {
          this.isRunning = false;
          this.startTime = 0;
          this.overallTime = 0;
        }
      
        _getTimeElapsedSinceLastStart () {
          if (!this.startTime) {
            return 0;
          }
        
          return Date.now() - this.startTime;
        }
      
        start () {
          if (this.isRunning) {
            return console.error('Timer is already running');
          }
      
          this.isRunning = true;
      
          this.startTime = Date.now();
        }
      
        stop () {
          if (!this.isRunning) {
            return console.error('Timer is already stopped');
          }
      
          this.isRunning = false;
      
          this.overallTime = this.overallTime + this._getTimeElapsedSinceLastStart();
        }
      
        reset () {
          this.overallTime = 0;
      
          if (this.isRunning) {
            this.startTime = Date.now();
            return;
          }
      
          this.startTime = 0;
        }
      
        getTime () {
          if (!this.startTime) {
            return 0;
          }
      
          if (this.isRunning) {
            return this.overallTime + this._getTimeElapsedSinceLastStart();
          }
      
          return this.overallTime;
        }
      }
      
      const timer = new Timer();
      //timer.start();
      setInterval(() => {
        const timeInSeconds = Math.round(timer.getTime() / 10);
        document.getElementById('time').innerText = timeInSeconds;
      }, 100)