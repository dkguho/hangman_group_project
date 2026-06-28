import turtle
import random
import time

#Madisons welcome screen
def welcomeScreen():
    turtle.clear()
    for i in range (10): #shows welcome screen for aprox 7 seconds
        turtle.hideturtle()
        turtle.bgcolor("black")
        turtle.color("white")
        turtle.penup()
        turtle.write("Welcome to Hangman", align="center", font=('Arial','25','normal'))
        turtle.goto(0,-100)
        turtle.write("Guess letters to fill in the dashs.", align="center", font=('Arial','16','normal'))
        turtle.goto(0,-150)
        turtle.write("If wrong letter is guessed part of stick figure will be drawn.", align="center", font=('Arial','16','normal'))
        turtle.goto(0,-200)
        turtle.write("Game is lost if the entire stick figure is drawn", align="center", font=('Arial','16','normal'))
        turtle.color("black")
        turtle.goto(0,0)
        

#Madisons function to draw the hangman
def drawMan(count):
    if count == 1:
        #draw head
        turtle.goto(0,0)
        turtle.pendown()
        turtle.circle(30)
        turtle.penup()
        
    elif count == 2:
        #draw torso
        turtle.goto(0,0)
        turtle.right(90)
        turtle.pendown()
        turtle.forward(70)
        turtle.penup()
        
    elif count == 3:
        #draw 1st arm
        turtle.goto(0,-10)
        turtle.pendown()
        turtle.left(45)
        turtle.forward(50)
        turtle.penup()
        
    elif count == 4:
        #draw second arm
        turtle.goto(0,-10)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(50)
        turtle.penup()
        
    elif count == 5:
        #draw first leg
        turtle.goto(0,-70)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(50)
        turtle.penup()
        
    elif count == 6:
        #draw second leg
        turtle.penup()
        turtle.goto(0,-70)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(50)
        turtle.penup()

    else:
        None

#Kushal's function to send a message to the screen
def warning(value):
    #Making a new turtle screen allows for clearing just the words in this portion
    window = turtle.Screen()
    turtle2 = turtle.Turtle()
    turtle2.shape("turtle")
    turtle2.color("white")
    turtle2.hideturtle()
    turtle2.penup()
    turtle2.goto(-150,200)
    turtle2.pendown()

    if value == "double":
        turtle2.write("Please write only one letter at a time.",font=('Arial', '20', 'bold'))
        time.sleep(2)
        turtle2.clear()

    elif value == "nothing":
        turtle2.write("Please write a letter for continue.",font=('Arial', '20', 'bold'))
        time.sleep(2)
        turtle2.clear()

    elif value == "character":
        turtle2.write("You write some non-character letter.",font=('Arial', '20', 'bold'))
        time.sleep(2)
        turtle2.clear()

    elif value == "used":
        turtle2.write("You guessed this letter already.",font=('Arial', '20', 'bold'))
        time.sleep(2)
        turtle2.clear()

#Kushal's input validation function; Paul helped slightly.
def inputVal():
    #Declare variables
    play_input = str()
    player_input = str()

    window = turtle.Screen()
    
    player_input = window.textinput("Enter letter", "Enter letter: ")
        
    if len(player_input) > 1: #If player provide 2 or more letters at a time then his answer will count as a wrong answer
        warning("double")
        return None

    elif len(player_input) == 0: #If player doesn't write anything, then this part of code will run and count it as a wrong answer
        warning("nothing")
        return None
 
    else:
        if player_input.isalpha(): #This isalpha method help to prevent any other character, like numeric, special character or foreign language
            return player_input.lower()
        else:   
            warning("character")
            #Paul wrote this return
            return "nonchar"

    
#Pauls function; draws the letters if the user guesses correct
def drawLetter(index, value, letter, word):
    #Declare variables
    x = float()
    
    x = 20 - (70/2*len(word))+index*70

    if letter in value:
        turtle.goto(x,-290)
        turtle.write(f"{letter}", align="center", font=('Arial', '30', 'bold'))
        
    
#Paul/Matt; function that draws the line on the screen
def drawLines(word):
    #Declare variables
    x = int()

    turtle.penup()
    turtle.right(90)

    """
     The x variable allows for dynamic drawing of the dashed lines at the center of
     the turtle screen; we can split that in half and have an equal number of dash
     lines on each half..
    """
    
    x = 0 - (70/2*len(word))

    turtle.goto(x,-300)

    #Draws each dash line
    for letter in word:
        turtle.pendown()
        turtle.forward(40)
        turtle.penup()
        x+=70
        turtle.goto(x,-300)

#Matt's function; gets a random word for the game   
def bank():
    #Declare variable
    wordlist = list()
    
    wordlist = ["apple","orange","pear","pineapple", "bear",
                "cranberry", "sunshine", "time", "enigma"]

    return random.choice(wordlist)

#Matt's function; a fun function if the user wins
def celebrate():
    #Declare variables
    colors = list()

    turtle.speed(7)
    turtle.clear()
    turtle.speed(0)
    turtle.penup()

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    #i is known to temporarily assign a value in the range of the loop. It is being used as a counter.
    for i in range(30):
        turtle.penup()
        turtle.color(random.choice(colors))
        turtle.penup()
        turtle.goto(random.randint(-200, 200), random.randint(-200, 200))
        turtle.write("you win :)", align="left", font=('Arial', '30', 'bold'))
        turtle.goto(random.randint(-200, 200), random.randint(-200, 200))
        turtle.write("congrats!", align="right", font=('Arial', '50', 'bold'))
        turtle.pendown()

    restartScreen()

#Matt's function; a not so fun function if the user looses
def failure():
    #Declare variables
    colors = list()

    turtle.speed(7)
    turtle.clear()
    turtle.goto(0,0)
    turtle.write("loser.", align="center", font=('Arial','16','normal'))
    for i in range(30):
        colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        turtle.goto(random.randint(-200, 200), random.randint(-200, 200))
        turtle.color(random.choice(colors))
        turtle.write("haha", align="center", font=('Arial','16','normal'))

    restartScreen()

#Paul's function; detects mouse click
def onClickScreen(x,y):
    #Onlys for only one click
    turtle.onscreenclick(None)
    main()

#Paul's function; gets screen ready to determine if the user wants to play again
def restartScreen():
    turtle.reset()
    turtle.bgcolor("black")
    turtle.color("white")
    turtle.goto(0,0)
    turtle.write("Click anywhere on the screen to play again.", align="center", font=('Arial','16','normal'))
    turtle.onscreenclick(onClickScreen)

#Paul did main function        
def main():
    #Declare variables
    count = int()
    word = list()
    used_letter = list()

    welcomeScreen()
    
    #Sets the background color, turtle size, and draws the two posts
    turtle.showturtle()
    turtle.clear()
    turtle.bgcolor("black")
    turtle.color("white")
    turtle.penup()
    turtle.goto(300,-200)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(260)
    turtle.left(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.penup()

    #Get word from bank
    word = list(bank())

    #Start the counter
    count = 0
    
    #Draw the lines based on number of letters in the word
    drawLines(word)

    """
    Regarding the while loop, the user has 7 tries to guess the correct word.
    For each wrong letter guess, the user will get +1 in the count variable. Word.count("")
    counts the number of empty strings inside the list of words from the bank. If the word.count("")
    equals the length of the word, then the user wins.


    Regarding the enumerate (word), what is happening is this function is getting the value and the
    index of the value inside the list of the chosen word. So, if the letter guessed by the user is correct,
    we get the index value so we can use it to draw the word on the screen, and we switch the correct guess
    of the letters inside the list and replace them with empty strings.    
    """

    #Letter = None, allows for the user to not put in the same letter twice, when
    #using the inputVal() function
    letter = None
    used_letter = []
    
    #Pauls while loop
    while count < 6 and word.count('') != len(word):
        while letter is None:

            #If the user puts in an acceptable letter, then that letter becomes a variable
            letter = inputVal()
            if letter == "nonchar":
                break
            #Appendeds the letter into a list, so we can keep track of guessed letters
            elif letter not in used_letter:
                used_letter.append(letter)
            #If letter is in the list used_letters, then our program will not accept that letter
            #and it will ask for a new letter
            else:
                warning("used")
                letter = None
        
        #If the user guesses a letter in the word
        if letter in word:
            #Gets the value and the index of the value in the list of the word
            for index, value in enumerate(word):
                drawLetter(index,value,letter,word)
                #Changes the value of the letter to an empty string
                if value == letter:
                    word[index] = ''    

        elif letter == "nonchar":
            print("")
        
        else:
            count+=1
            drawMan(count)

        letter = None

    #User looses
    if count == 6:
        time.sleep(1)
        failure()
    #User wins
    else:
        time.sleep(1)
        celebrate()
  
    turtle.mainloop()

#Allows user to restart game without using loop  
if __name__ == "__main__":
    main()
    



