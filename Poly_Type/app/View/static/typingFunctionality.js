let promptNumber = 0
let wordsWrapper = `prompt-${promptNumber}`
let continuePrompt = `continue-prompt-${promptNumber}`
const correctLetter = 'letter correct-letter'
const incorrectLetter = 'letter incorrect-letter'
const incompleteLetter = 'letter incomplete-letter'
const incompleteWord = 'incomplete-word'
const completeWord = 'complete-word'
const continueHidden = 'continue continue-hidden'
const continueVisible = 'continue continue-visible'
const inactivePrompt = 'inactive-prompt'
const activePrompt = 'active-prompt'
const extraLetter = 'letter extra-letter'

var correctLetters = 0
var incorrectLetters = 0
var extraLetters = 0
var promptFinished = false

document.addEventListener("keydown", async function(event) {
    //checkEmptyPrompt()
    if(event.which == 8){
      backspace()
      return
    }  
    if(event.which == 13){
        await pressEnter()
        return
    }
    if(event.which == 32){
      event.preventDefault()
    }

    if (invalidCode()) { return }
    if(!promptFinished){
      typingLetter()
    }
  
    function backspace(){
      var div = document.getElementById(wordsWrapper)
      var words = div.getElementsByTagName('div')
      hideContinue()
      for(i = words.length - 1; i >= 0; i--){
        var letters = words[i].getElementsByTagName('div')
        
        for(j = letters.length - 1; j >= 0; j--){
          

          if(letters[j].className == extraLetter){
            extraDivs = document.getElementsByClassName(extraLetter)
            extraDivs[extraDivs.length - 1].remove()
            extraLetters--
            return
          }
          else if(letters[j].className == correctLetter || letters[j].className == incorrectLetter){
            if(letters[j].className == correctLetter){
              correctLetters--
            } else{
              incorrectLetters--
            }
            letters[j].className = incompleteLetter
            words[i].className = incompleteWord
            promptFinished = false
            return
          }
        }
      }
    }
  
    async function typingLetter(){
      
      hideContinue()
      var div = document.getElementById(wordsWrapper)
      //div = div.getElementsByTagName('div')
      //var words = div.getElementsByTagName('div')
      var words = div.getElementsByClassName(incompleteWord)
      
      
      for(i = 0; i < words.length; i++){
        
        var letters = words[i].getElementsByTagName('div')
        
        if(words[i].className == incompleteWord){
          
          for(j = 0; j < letters.length; j++){
            //
            
            if(letters[j].className == incompleteLetter){
              
              if(letters[j].innerText === event.key){
                letters[j].className = correctLetter
                correctLetters++
              } else{
                letters[j].className = incorrectLetter
                incorrectLetters++
              }
              if(i == words.length - 1 && j == letters.length - 1){
                
                words[words.length - 1].className = completeWord
                showContinue()
              }
              
              return
            }
          }
          if(event.which == 32){
            
            words[i].className = completeWord
            return
          } else {
            
            var newDiv = document.createElement('div')
            newDiv.className = extraLetter
            newDiv.innerText = event.key
            words[i].appendChild(newDiv)
            extraLetters++
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
        //event.preventDefault()
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

    async function pressEnter(){
        if(document.getElementById(continuePrompt).className == continueVisible){
            // this is bad and needs to be refactored

            var div = document.getElementById(wordsWrapper)
            document.getElementById(continuePrompt).className = continueHidden
            div.className = inactivePrompt
            promptNumber++
            if(promptNumber > 4){
              await finished()
            }
            wordsWrapper = `prompt-${promptNumber}`
            continuePrompt = `continue-prompt-${promptNumber}`
            var div = document.getElementById(wordsWrapper)
            div.className = activePrompt
            var words = div.getElementsByTagName('div')
            var letters = words[0].getElementsByTagName('div')
            if(letters.length <= 0){
              await finished()
              return
          }
        }
        hideContinue()
        timer.stop()
    }
    });

    //https://stackoverflow.com/questions/29971898/how-to-create-an-accurate-timer-in-javascript
    class Timer {
        constructor () {
          this.isRunning = false
          this.startTime = 0
          this.overallTime = 0
        }
      
        _getTimeElapsedSinceLastStart () {
          if (!this.startTime) {
            return 0
          }
        
          return Date.now() - this.startTime
        }
      
        start () {
          if (this.isRunning) {
            return console.error('Timer is already running')
          }
      
          this.isRunning = true
      
          this.startTime = Date.now()
        }
      
        stop () {
          if (!this.isRunning) {
            return console.error('Timer is already stopped')
          }
      
          this.isRunning = false
      
          this.overallTime = this.overallTime + this._getTimeElapsedSinceLastStart()
        }
      
        reset () {
          this.overallTime = 0
      
          if (this.isRunning) {
            this.startTime = Date.now()
            return
          }
      
          this.startTime = 0
        }
      
        getTime () {
          if (!this.startTime) {
            return 0
          }
      
          if (this.isRunning) {
            return this.overallTime + this._getTimeElapsedSinceLastStart()
          }
      
          return this.overallTime
        }
      }
      
      const timer = new Timer()
      //timer.start()
      setInterval(() => {
        const timeInSeconds = Math.round(timer.getTime() / 1000)
        document.getElementById('time').innerText = timeInSeconds
      }, 100)



async function finished(){
  let data = {
      elapsedTime: timer.getTime().toString(),
      correctLetters: correctLetters,
      incorrectLetters: incorrectLetters,
      extraLetters: extraLetters
  }
  let url = document.URL
  await fetch(url, {
      method: "POST", 
      body: JSON.stringify(data)
    }).then(res => {
      console.log("Request complete! response:", res)
    });
    window.location.replace(document.URL.replace("take_challenge", "results"))
}