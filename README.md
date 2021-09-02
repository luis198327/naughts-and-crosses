# Naughts and Crosses Game

## Code Institute Mile Stone 3 Project - Command-Line Application In Python

The Code Institute project brief was to build a command-line application using Python, that allows users to manage a common dataset about a particular domain.

Naughts and Crosses game (or sometimes known as tic tac toe) is a 2 player game which runs in the Code Institute mock terminal on Heroku.

This project is for educational use only.  

The deployed version of my game is here -> [https://naughts-and-crosses-game.herokuapp.com/](https://naughts-and-crosses-game.herokuapp.com/ 

![alt text](https://github.com/luis198327/naughts-and-crosses/blob/main/assets/images/responsive-site.JPG)

## User Experience

### Strategy - User Stories
#### Site Owners Goals
+ The Naughts and Crosses game is played on a 3 x 3 grid in which each player takes it in turn to place either a 'X' or 'O' character onto the grid.  The objective of the game is to get 3 of the same characters in a row/column/diagonal before their opponent, or at the very least to block their opponent from winning and enforcing a draw. 
+ The application provides a platform for a two player input/gaming facility.

#### External User Goals
+ The application user wants to play a logic game.
+ The application user wants to be able to challenge their friend.

### Process Flow
I used MS Publisher to create a basic process flow of the game to identify key steps/functions required throughout the game. This has been saved as a PDF when adding to the assets directory.

The process flow can be found [here](https://github.com/luis198327/naughts-and-crosses/blob/main/assets/images/process_flow.pdf).

### How to Play
The game area is a 3 x 3 grid.  Each player in turn will be asked to input a number between 1 - 9.  The inputted number corresponds to the numbers as showwn in the grid below:

 1 | 2 | 3 
 4 | 5 | 6 
 7 | 8 | 9 

To win the game, a player must place three of their charatcters (either an 'X' or 'O') in a horizontal, vertical, or diagonal row.
If the game is won, a message will be displayed to confirm which player has won.  The game will check this when each input has been accepted into the game area.  If all 9 game slots are filled and no one has won, a message will display to confirm the game has ended in a draw.

Player 1 will use the character 'X' and Player 2 will use the character 'O'.

The players then have the option to either restart the game or to quit. 

## Features
+ A welcome message and rules in how to play.

![alt text](https://github.com/luis198327/naughts-and-crosses/blob/main/assets/images/game-welcome.JPG)

+ A gaming grid to show the gaming area, which updates and is shown once a valid entry is provided by the player.

+ A message to confirm who's turn it is each time.
+ Input validation.  Warnings will be provided to the user if their input:
    + Is off the grid and will provide a relevant message to confirm this and to ask for a new selection from the player

    ![alt text](https://github.com/luis198327/naughts-and-crosses/blob/main/assets/images/validation-out-of-range1.JPG)

    + Is an invalid type (e.g a string). In other words, will only allow integers between 1-9, and not any other characters.

    ![alt text](https://github.com/luis198327/naughts-and-crosses/blob/main/assets/images/validation-non-integer-value.JPG)

    + Has been previously selected, and will provide a message to confirm position already selected and to retry.

    ![alt text](https://github.com/luis198327/naughts-and-crosses/blob/main/assets/images/validation-position-taken.JPG)

+ Message to display the result of the game - either a player has won or the game has been drawn.

![alt text](https://github.com/luis198327/naughts-and-crosses/blob/main/assets/images/winning-move-across.JPG)

+ Option to restart the game or to quit.

### Features Left To Implement
Additional features that I would like to include in a future release would be to:

+ Make it a one player game so the user can play against the computer.
+ Create the game so it has a better graphical representation of the game, Nautghts and Crosses.
+ Include a scoring system to track the scores when multiple games are played in the same session before the exit game option is selected.
+ Add a quit game option throughout should either player wishes to forfeit.
+ For the code to be able to recognise a drawn game has been reached earlier, to prevent all 9 grid slots from having to be entered.

## Technologies Used
### Languages Used
+ Python

### Frameworks Libraries And Programs Used
+ [GitPod](https://www.gitpod.io/) - used as the development environment for my website. I also used Git for Version Control in the project.
+ [GitHub](https://github.com/) - used to store the projects code after being pushed from GitPod.
+ [Heroku](https://id.heroku.com/login) - used to deploy the game
+ [MS Publisher](https://www.microsoft.com/en-gb/microsoft-365/publisher) - used to create the basic process diagram in the design process of my game.
+ [W3Schools](https://www.w3schools.com/) - used for additional support and to get ideas for how to use code in my game. 
+ [PEP8 Online](http://pep8online.com/) - used to check the validity of my Python code in my project.
+ [Python Tutor](http://www.pythontutor.com/) - used to check my Python code in the project. 
+ [Ecotrust](https://ecotrust-canada.github.io/markdown-toc/) - used to create contents page for README.md file.
+ [Python course](https://www.python-course.eu/python3_global_vs_local_variables.php).

## Testing
### Testing User Stories From User Experience Section
#### Site Owners Goals
+ The Naughts and Crosses game is played on a 3 x 3 grid in which each player takes it in turn to place either a 'X' or 'O' character onto the grid.  The objective of the game is to get 3 of the same characters in a row/column/diagonal before their opponent, or at the very least to block their opponent from winning and enforcing a draw. 
    + The app deployed to Heroku will show the grid game and ask for user input and provide feedback throughout.
    + The code has been created so that it meets conventional rules of naughts and crosses. A winning move can therefore be achieved in one of 3 rows, 3 columns or in the 2 possible diagonals.

+ The application provides a platform for a two player input/gaming facility.
    + The game allows valid inputs from two players. The players turn is shown each time until the game has been completed.
    + It is a terminal base game using deployed via Heroku.

#### External User Goals
+ The application user wants to play a logic game.
    + The user is able to play a standard naughts and crosses game using logic and skill in order to beat their opponent. 
+ The application user wants to be able to challenge their friend.
    + The game is a 2 player game, and allows each player to enter their move in turn until the game finishes.
    + The game can be restarted at the game conclusion so the player(s) can continue to challenge one another.

### Further Testing


#### Validation
I used the PEP8online.com validation service to check the validity of my code.

I used these during and at the end of the project to regularly identify issues.  Screenshots are as shown for each file:

<<<provide screenshot>>>>


<<Review to see if this is needed>>
I have tested this on Google Chrome, Firefox, and Microsoft Edge browsers and no issues with the code/behaviour of the quiz were found.  I have also tested this in production using an Android mobile. A relative has also tested this on an IPad too.  
Google Chrome Dev tools have been used and the responsiveness seems to be fine on all mobile and table devices provided as part of Dev Tools, and a general responsiveness check with different widths and heights also seem fine.  I have checked the screen width as low as a Galaxy Fold set at 280px wide.

#### Issues I Overcome
+ I kept receiving the error of "Assigning result of a function call, where the function has no return" and was getting confused.  I was convinced this was missing code somewhere and was adding additional functionality to the logic of the game but was failing to remove this error.  But I then realised that the check_if_winner function was setting a local variable of win_by_row for example, where the result of check_row function wasn't returning a value, which I believe what was meant by this error message.  I then added an if/else statement to the check_row function so that this outputs the character in the winning grid slot(s), depending on the winning row etc.  The error then was removed, apart from standard syntax rules i forgot to apply such as removing white space and 4 spaces for indention.
+ After fixing the above issue, I was able to run the game but after inputting the first grid slot integer, the game was declared as a draw. I realised that it must have recognised the dash "-" as a valid game character.  I therefore added the not equal to (!=) condition to the same 3 functions as in the first issue i overcame above.

When i then ran the game following this fix, it didn't immediate prompt the game had been drawn which was great.  However, when I had then entered 3 grid slots, to mean a winning row was achieved, the message printed back was still a draw.  I realised that I had to update the if/else statement in the play_game function so that the character of X or O had a space either side ie... " X " rather than "X", so this matches the exact grid spacing.  When running the game again, the issue was fixed and the message correctly displayed Player X had won.

+ I was having trouble in setting the validation within function current_player_input to only allow numbers 1-9 to be entered. It wasn't allowing me to run the while loop correctly. I have had to re-write the initial step to leave the input as a string before converting this to an integer. This appears to now be working ok. I may revisit this to look at a way to shorten the code (rather than using a list of all valid strings).

+ I wanted to implement a restart game function. This would mean a better user experience giving them the option challenge their opponnent again. I was having troubles implementing this as researching online I was finding suggestions on how to do this but these were not working or were only partially working. For example, I managed to code the game to restart but this would keep the original game grid and therefore immediately print the previous game result. Having tried a few different solutions I managed to set this function correctly, although there might be an easier and better way to code this. Something maybe to consider in a future release.  I used and combined a couple of solutions that I found online.  These can be found in the code section below.

+ Minor issue i overcome was when setting the change_player logic, and then running the game the player's character didn't change as expected from ' X ' to ' O '. I realised I had forgotton to remove the ' X ' variables set in the current_player function. 

### Known Bugs And Improvements   
+ 

## Constraints
As this used the Code Institute mock terminal, the deployed terminal is set to 80 columns by 24 rows. This means each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

## Deployment
My project was developed using the IDE, Gitpod. I regularly commited my changes using the following git commands:
+ git add - adds new or changed files in my working directory to the Git staging area.
+ git commit - creates a commit, which are snapshots of my entire repository at specific times. 
+ git push - uploads all local branch commits to the corresponding remote branch.

The site was deployed to GitHub pages. The project was deployed using Code Institute's mock terminal for Heroku.  

Steps to deploy are as follows:

<<<<NEED TO REVIEW STEPS>>>>

+ Within Heroku, select:
    + Create new app from the dashboard page
    + Set the name of the app you are creating and the region you are in.
    + Select create app.
    + Once this has been created, select the Settings tab and set the following:
        + Navigate to the Config Vars section.  For this deployment, no creds.json file was created. But in order to use the Code Institute template via Heroku, to improve compatibility a Config Var of Key = PORT, and Value = 8000 was added to the settings.
        + Under Buildpacks section add the following dependancies that are needed outside of any saved under the requirements.txt file (saving each one in turn and ensuring they are in the following order):
            + Python
            + Nodejs
    + Scroll up and select the Deploy tab and set the following:
        + Under the Deployment Method, select GitHub.
        + Then enter the GitHub repository name and click search.
        + Once the repository is listed, click connect to link up the Heroku app to the Github repository code.
        + Then choose whether to Automatically or Manually deploy the branch to this app. 
        + The deployed URL is [here](https://naughts-and-crosses-game.herokuapp.com/)
        <<<check before submitting>>>
        + Every push to main will deploy a new version of this app. Deploys happen automatically but be sure that this branch in GitHub is always in a deployable state and any tests have passed before you push.

### Making A Local Clone
You can clone this repository by:
+ Logging into GitHub and locate the GitHub Repository luis198327/naughts-and-crosses.
+ Under the repository name and with the Code tab displayed by default, click the dropdown "Code" option.
+ This will give you the option to copy the repository using HTTPS by clicking the copy button.
+ Open Git Bash.
+ Change the current working directory to the location where you want the cloned directory to be made.
+ Type git clone and paste the URL i.e. $ git clone https://github.com/luis198327/naughts-and-crosses.git.
+ Press Enter, and your local clone will be created.

## Credits
### Content
+ All content was written by the developer, unless referenced below.

### Code
+ Googled how to try and define an if statement where it does not contain a piece of code to assist with the logic of setting the function if the game is drawn. Found the 'not in' statement to include from [Code Grepper](https://www.codegrepper.com/code-examples/python/python+string+not+contains) to write my code.
+ In order to get the restart game function to work succesfully, I used and combined a couple of resources I found online.  These were:

    + [Edueka](https://www.edureka.co/community/21051/how-to-exit-a-python-script-in-an-if-statement) - to set the if statement correctly inside a while loop which I wasn't doing in previous attempts, and 
    + [Code Grepper](https://www.codegrepper.com/code-examples/python/os.execl%28sys.executable%2C+sys.executable%2C+%2Asys.argv%29) - to fully restart the game, although I also reinserted the grid list manually too to get the restart function to work correctly.

### Resources
I used the following resources to obtain ideas for the game:

+ [Google](https://www.google.com/) - used for general searching
+ [Wikipedia](https://en.wikipedia.org/wiki/Tic-tac-toe)
+ [Code Grepper](https://www.codegrepper.com)
+ [Edueka](https://www.edureka.co/

I also used a couple of youtube videos to bring inspiration on creating a command-line Python game:

+ [Youtube](https://www.youtube.com/watch?v=n2o8ckO-lfk)
+ [Youtube](https://www.youtube.com/watch?v=BHh654_7Cmw&t=3176s)
+ [Youtube]https://www.youtube.com/watch?v=tf3ezjeTpfI)

### Acknowledgements
+ I used the Code Institute GitHub template as a basis for setting up my repository, which will allow the game to played using the Code Institute mock terminal on Heroku
+ I used W3Schools to assist with some features and to develop my understanding.
+ I would like to thank my mentor Spencer Barriball for his review and ongoing support with this project.
+ This project is for educational use only and was created for the Code Institute Module of a command-line application using Python.

### Comments
If you wish to open an external link in a different tab in this README.md file, please press Crtl or Command + Click to do this.  Github prevents/doesn't allow those links to open in a new tab by default.