
This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
# Naughts and Crosses Game

## Code Institute Mile Stone 3 Project - Command-Line Application In Python

The Code Institute project brief was to build a command-line application using Python, that allows users to manage a common dataset about a particular domain.

Naughts and Crosses game (or sometimes known as tic tac toe) is a 2 player game which runs in the Code Institute mock terminal on Heroku.

This project is for educational use only.  

The deployed version of my game is here -> PROVIDE LINK 

<<screen shot>>

## User Experience

### Strategy - User Stories
#### Site Owners Goals
+ The Naughts and Crosses game is played on a 3 x 3 grid in which each player takes it in turn to place either an 'X' or 'O' character onto the grid.  The objective of the game is to get 3 of the same characters in a row/column/diagonal before their opponent, or at the very least to block their opponent from winning and enforcing a tie game. 
+ The application provides a platform for a two player input/gaming facility.

#### External User Goals
+ The application user wants to play a logic game.
+ The application user wants to be able to challenge their friend.

### Process Flow
I used MS Publisher to create a basic process flow of the game to identify key steps/functions required throughout the game.

The process flow can be found [here](<<link to flow charts>>>

### How to Play
The game area is a 3 x 3 grid.  Each player in turn will be asked to input a number between 1 - 9.  The inputted number corresponds to the numbers as showwn in the grid below:

 1 | 2 | 3 
 4 | 5 | 6 
 7 | 8 | 9 

To win the game, a player must place three of their charatcters (either an 'X' or 'O') in a horizontal, vertical, or diagonal row.
If the game is won, a message will be displayed to confirm which player has won.  The game will check this when each input has been accepted into the game area.  If all 9 game slots are filled and no one has won, a message will display to confirm the game has ended in a draw.

Player 1 will use the character 'X' and Player 2 will use the character 'O'.

## Features
<<<Add features>>>
+ Input validation.  Warnings will be provided to the user if their input:
    + Is off-grid and to ask for a new selection
    + Is an invalid type (e.g a string)
    + Has been previously selected

### Features Left To Implement
Additional features that I would like to include in a future release would be to:

+ To make it a one player game so the user can play against the computer.
+ To create the game so it has a better graphical representation of the game, Nautghts and Crosses.

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


#### External User Goals


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

+ Within the GitHub repository, navigate to the Settings tab.
+ Then select the Pages sub-menu option on the left, which takes you to GitHub Pages. 
+ Within the source section drop-down menu, select Main (or Master Branch) and click on save.
+ Once this has been saved, the page will confirm that the site is ready to be published and provides the URL address.
+ Refreshing the page will confirm the website has been deployed, again providing the URL address.
+ The deployed URL is <<<provide URL>>

The deployed site will update automatically upon new commits to the main (or master) branch. For the site to deploy correctly on GitHub pages, the landing page must be named index.html.

<<<<NEED TO REVIEW STEPS>>>>

### Making A Local Clone
You can clone this repository by:
+ Logging into GitHub and locate the GitHub Repository luis198327/olympics-quiz-game
+ Under the repository name and with the Code tab displayed by default, click the dropdown "Code" option.
+ This will give you the option to copy the repository using HTTPS by clicking the copy button.
+ Open Git Bash.
+ Change the current working directory to the location where you want the cloned directory to be made.
+ Type git clone and paste the URL i.e. $ git clone <<link to deployed site>>>.
+ Press Enter, and your local clone will be created.

Or simply clone this repository directly into the editor of your choice by pasting $ git clone https://luis198327.github.io/olympics-quiz-game/ into your terminal. To cut ties with this GitHub repository, type git remote rm origin into the terminal.


## Credits
### Content
+ All content was written by the developer, unless referenced below.

### Code
+ 

### Resources
I used the following resources to obtain ideas for the game:

+ [Google](https://www.google.com/) - used for general searching
+ [Wikipedia](https://en.wikipedia.org/wiki/Tic-tac-toe)

I also used the following resources to bring inspiration on creating a command-line Python game:
+ 

### Acknowledgements
+ I used the Code Institute GitHub template as a basis for setting up my repository, which will allow the game to played using the Code Institute mock terminal on Heroku
+ I used W3Schools to assist with some features and to develop my understanding.
+ I would like to thank my mentor Spencer Barriball for his review and ongoing support with this project.
+ This project is for educational use only and was created for the Code Institute Module of a command-line application using Python.

### Comments
If you wish to open an external link in a different tab in this README.md file, please press Crtl or Command + Click to do this.  Github prevents/doesn't allow those links to open in a new tab by default.