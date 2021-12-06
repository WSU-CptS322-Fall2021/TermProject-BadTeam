# Functional Testing

**Note To Tester:** You are free to test these in any order you choose but we would suggest this following order to streamline the testing process.

- Using Host Functionalities
- Create A Challenge
- Opening A Challenge
- Taking a Challenge
- Typing Behavior
- Closing A Challenge

------

### Typing Behavior

**Precondition:** You are a challenger in a prompt of a challenge where there is enough words to test the text behavior.

- Type a correct character
  - In the text editor for the prompt, while in the middle of a word, type the character that you see in the underlying prompt
  - Confirm the character you typed highlighted is the primary color and overlays the underlying matching character
- Type an incorrect character in the middle of a word
  - In the text editor for the prompt, while in the middle of a word, type a character other than that you see in the underlying prompt
  - Confirm that the correct underlying character turned the error color and that you do not see the character you typed. You should be able to continue typing or backspace. 
- Type an incorrect character at the end of the word
  - In the text editor for the prompt, while at the end of a word, type a character other than that you see in the underlying prompt
  - Confirm that the character you typed was inserted into the underlying text is in the error color. You will not be able to proceed unless you press space.
- Type an incorrect space in the middle of a word
  - In the text editor for the prompt, while in the middle of a word, type a space 
  - Confirm that the same behavior as typing an incorrect character in the middle of a word occurs. 
- Type an correct space after incorrect characters after a word
  - In the text editor for the prompt, while at the end of a word, type a character other than that you see in the underlying prompt then type space 
  - Confirm that you are allowed to proceed to the first character of the next word in the prompt.
- Type a backspace
  - Type a backspace anywhere 
  - Confirm that this allows you to undo the last character, returning to the subtle underlying text or empty space.


------

### Creating A Challenge

**Precondition:** You are a host in the main host home page

- Redirect to challenge creation page
  - Click on the plus button at the end of the list of created challenges
  - Confirm that you are redirected to a challenge creation page - it will have a different layout, header and url. 

- Add text to a prompt
  - Click on the first prompt text input box
  - Confirm that you can type or paste text into the prompt box, and confirm that you see your text in the box. You can add text to up to 5 prompts, if there is no text in a prompt it is not counted as a challenge prompt to show the challenger. 
- Name the challenge
  - Click on the Challenge Title input box
  - Confirm that the name you give it is reflected in the input field. You can do this step before the ones listed before but before you can save the challenge you will need to give it a name. 
- Submit (Save) the challenge
  - Click the Post button at the end of the list of challenges 
  - Confirm that you are redirected to the main host page.
- See new challenge in host home page
  - Confirm that you can see your new challenge with the correct name 
  - Confirm that you can see all challenges in the list of challenges associated with your account.

------

### Using Host Functionalities

**Precondition:** For Login and Update, you must have the right credentials (username and password) to access the account. 

- Register
  - Hover near the log_in text in the index page, and enter in your new username and new password in the lower section denotated by the register text header then click the register button. 
  - Confirm that after clicking the register button, you are redirected into the Host homepage
- Login
  - Hover near the log_in text in the index page, and enter in your username and password into the upper section and click the log in button. 
  - Confirm that you are redirected to the Host homepage.
- Update
  - Click Edit_Account button in the top right corner
  - Confirm that you are redirected to the edit account page
  - Click on edit account text field and enter new name, click update button (which will redirect you to the host homepage)
  - Confirm that the new username is the name at the top of the host homepage


------

### Taking a Challenge

**Precondition:** You are a challenger with the correct challenge code for accessing a challenge

- Redirect to 1st prompt in challenge
  - Enter the correct challenge code and a username
  - Confirm that you are redirected to the 1st prompt in the list of prompts within in the challenge

- Take prompt
  - Start typing
  - Confirm that the timer begins and the typing functionalities are working.

- Redirect to and participate in subsequent prompts in challenge
  - Press Enter after finishing the prompt
  - Confirm that you are redirected to the next prompt if there is any in the challenge
  - Confirm that you can continue typing the prompt and that the timer continues running.

- View challenge results
  - Press Enter after finishing the last prompt
  - Confirm that you are redirected to a results page
  - Confirm that you can see your data for words per minute, number of correct characters, number of mistakes made, and number of extra characters. 


------

### Opening and Closing Challenges

**Precondition:**  You are a host in the main host home page

- Opening 
  - Click on the play button in the challenge's right side bar
  - Confirm that once clicked the challenge's right side bar changes to only display the challenge id and a stop button. 
  - Copy the challenge code, log out, provide this code to the challenge code input box, and a username
  - Confirm that you can join the challenge

- Closing
  - Click on the stop button in the challenge's right side bar
  - Confirm once clicked the challenge's right side bar should change to the initial suite of tool (edit, start, delete, view results) 
  - Log out, using the same code for the previously opened challenge in the challenge code input box, and a username 
  - Confirm that you can't join the challenge.




# User Interface Testing

### On Hover

- Log In Text Box
  - Hover over or near the Log in text in the index page
  - Confirm that the register/log in form fades
  - Confirm that the register/log in form has a darker background shade, and a primary color border
  - Confirm that the register/log in form has the register and log in text has turned to the primary color
- Buttons
  - Hover over a button
  - Confirm that the button's background turns a darker shade
- Input Field Boxes
  - Hover over an input field box
  - Confirm that the box turns a different shade of the background color (lighter or darker based on theme)

### On Click

- Buttons
  - Click on a button
  - Confirm that you are redirected to the correct page
    - Join, if possible, redirects to the 1st prompt of the challenge 
    - [+] redirects to the challenge creation page
    - Post redirects to the host homepage
    - Log in, if with correct credentials, redirects to the host homepage
    - Register, if with all the inputs fields filled out, redirects to the host homepage
    - Log out, redirect to the index page

- Input Field Boxes
  - Click on an input field box
  - Confirm that you are able to add text to the field and that it is saved there when clicked off

### Color Scheme

- Rotating Color Wheel
  - Click on the name of the current theme up in the right hand color
  - Confirm that the program's colors have changed and correspond to the new theme palette.

### Input Validation

- Incorrect Challenge Code
  - Click join or press enter with a username and an incorrect challenge code
  - Confirm that a flash message fades in that says "the room <challenge code> is not open or does not exist"
- Submit A Challenge Without A Title
  - Click the Post button for the form
  - Confirm that there is a small pop up tag that says "Please fill out this field" (the title) before posting
- Sign In With Incorrect Credentials
  - Click Log In with incorrect credentials
  - Confirm that a flash message fades in saying "Invalid Username or Password" in the error color of the theme
- Register with different Passwords
  - Enter in a username and two different passwords then click register in the lower section
  - Confirm the flash message reads "Invalid registration information"

### Open Challenge

- Open Challenge
  - Click the [>] button in the tool suite
  - Confirm that the tool suite switches to just a challenge code and a [S] (stop button)
- Join Challenge
  - Note the challenge code (copy), Log out, enter challenge code and username in correct fields, and Click Join
  - Confirm that you are redirected to the first prompt of the correct challenge 

### Close Challenge

- Close Challenge
  - Click the [S] button in the tool suite
  - Confirm that the tool suite switches to the original "[R]  [E]  [D]  [>]" 
- Join Challenge
  - Note the challenge code (copy), Log out, enter challenge code and username in correct fields, and Click Join
  - Confirm that you get the flash message "the room <challenge code> is not open or does not exist"