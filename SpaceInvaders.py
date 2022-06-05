

# Name: Ashwin Unnithan
# Date: December 20, 2019
# Purpose: To create a game using the pygame module and a variety of python and pygame functions, user-defined functions, loops and control stuctures.


import pygame
# A code used to import a module called easygui that lets the program access and use the module.
# pygame is a graphic-interface module that allows the program to establish game-like graphical interface


from pygame import mixer
# This code is used to import a particular module from pygame which is called mixer.
# The mixer module allows the pygame graphical interface to use/manipulate and play various sound formats.


import random
# This code is used to access and import a module called random
# The random module allows the program to access and store random numbers within a set range.


import math
# This code is used to access and import a module called math.
# The math module allows the program to access and use a variety of mathematical functions and equations.


pygame.init()
# This code is used to intialize the pygame program

# These 2 variables are set to True or False to display the title screen and main game to the user.
title_screen = True
run = False

# A code used to caption the title of the screen to "The Last Frontier"
pygame.display.set_caption("The Last Frontier")

# Setting the dimensions of the pygame window - (width, height).
screen = pygame.display.set_mode((800,600))


# Setting the icon of the game window to a image and displaying the icon
icon = pygame.image.load('Owlman Ship.png') # The Player ship is a original sprite made by me
pygame.display.set_icon(icon)


#Background Space Picture
Background = pygame.transform.scale(pygame.image.load('Space.png'), (800,600)) #Background ripped from internet

# Game Over Explosion Picture
You_Died = pygame.transform.scale(pygame.image.load('You Died.jpg'), (800,600)) # Background ripped from internet

# Title Screen background
Title_Background = pygame.transform.scale(pygame.image.load('Title Background.jpg'), (800,600)) # Background ripped from internet
# 3 of the codes are used to load the corresponding pictures to pygame


# Loading and Playing the Background Music
mixer.music.load('Epic Background Music.wav') # Background music ripped from internet
mixer.music.play(-1)



# Defining and loading the coordinates, values and image Player Ship
Space_Ship = pygame.transform.scale(pygame.image.load('Owlman Ship.png'), (100,100))
PlayerX = 370
PlayerY = 480
PlayerX_Change = 0



# Defining the value lists of the enemy ship
Enemyimg = []
EnemyX = []
EnemyY = []
EnemyX_Change = []
EnemyY_Change = []
Number_Of_Enemies = 30


# Setting the same coordinates, image and coordinate changes to each enemy in the list
for i in range(Number_Of_Enemies):
    Enemyimg.append(pygame.transform.scale(pygame.image.load('Enemy Ship.png'), (64,64))) # This sprite is ripped from internet
    EnemyX.append(random.randint(0,735))
    EnemyY.append(random.randint(0,100))
    EnemyX_Change.append(40)
    EnemyY_Change.append(20)



# Defining and loading the coordinates, values and image Player Ship
Bulletimg = pygame.transform.scale(pygame.image.load('Bullet.png'), (24,32)) # The energy bullet is a original sprite made by me
EnergyBlastX = 0
EnergyBlastY = 480
EnergyBlastX_Change = 0
EnergyBlastY_Change = 60
EnergyBlast_State = "ready"


# Defining the starting score value of the user
Score = 0


# Defining and acessing the various fonts used in the program. All fonts are ripped from internet
font = pygame.font.Font('Star Wars Font.ttf', 32)
You_Lost = pygame.font.Font('You Lost.ttf', 100)
Title_Font = pygame.font.Font('Space Age.ttf', 50)
Title_Font2 = pygame.font.Font('Star Wars Font.ttf', 20)
Result = pygame.font.Font('Azonix.otf', 20)


# Defining the x and y coordinates of the score screen
ScoreX = 30
ScoreY = 10



# Defining the various functions used in the program


# Defining the function used to display the title screen on the game window
def Title_Screen():
    screen.blit(Title_Background, (0,0))
    Starting_Screentxt = Title_Font.render("The Last Frontier",True,(255,0,0))
    Starting_Screentxt2 = Title_Font2.render("Press Space to Protect Axrial",True,(255,255,255))
    screen.blit(Starting_Screentxt, (75,150))
    screen.blit(Starting_Screentxt2, (200,250))



# Making the end score and game over screen global so they can be used in below Game_Over function
global Result_Screen
global Score_Screen




# Defining the function used to tell the user that they lost on the game window
def Game_Over():
    mixer.music.load('Epic Background Music.wav')
    pygame.mixer.pause()
    Result_Screen = Result.render("", True, (0,0,0))
    Score_Screen = font.render("Your Score was " + str(Score), True, (0,0,0))



    Losing_Screen = You_Lost.render("Game Over",True,(255,0,0))

    # if user score is less than 50 when they died, they receive the bollow end screen
    if Score <50:
        Result_Screen = Result.render("OMG, You dont deserve to be a Space Officer", True, (0,0,0))
        Score_Screen = font.render("Your Score was " + str(Score), True, (0,0,0))


    # if user score is greater than or equal to 50 and less than or equal to 100, they receive the bollow end screen
    elif Score >= 50 and Score <= 100:
        Result_Screen = Result.render("You are a Amateur Space Officer, Be Better!", True, (0,0,0))
        Score_Screen = font.render("Your Score was " + str(Score), True, (0,0,0))


    # if user score is greater than 100 and less than or equal to 200, they receive the bollow end screen
    elif Score > 100 and Score <= 200:
        Result_Screen = Result.render("Good Job - You are a Above Average Space Officer!", True, (0,0,0))
        Score_Screen = font.render("Your Score was " + str(Score), True, (0,0,0))


    # if user score is greater than 200, they receive the bollow end screen
    else:
        Result_Screen = Result.render("Smh, You are such a Try Hard Space Officer!", True, (0,0,0))
        Score_Screen = font.render("Your Score was " + str(Score), True, (0,0,0))


    # Displaying the corresponding end screen text and images to the game window
    screen.blit(You_Died, (0,0))
    screen.blit(Losing_Screen, (200,250))
    screen.blit(Result_Screen, (100,150))
    screen.blit(Score_Screen, (200,200))




# Defining the function to display the user score screen on the top-left side of the screen
def PlayerScore(x,y):
    score_screen = font.render("Score:" + str(Score),True,(255,255,255))
    screen.blit(score_screen, (x,y))



# Defining the function to detect the bullet collision of the energy blast with the enemy ship
def HitEnemy(EnemyX,EnemyY,EnergyBlastX, EnergyBlastY):
    Dist = math.sqrt((math.pow(EnemyX - EnergyBlastX,2)) + (math.pow(EnemyY - EnergyBlastY,2)))

    # if the distance between the energy blast and the enemy ship is less than 27, than they collide
    if Dist < 27:
        return True

    # otherwise there is no collision
    else:
        return False



# Defining the function used to display the player's ship on the screen
def Player_Ship(x,y):
    screen.blit(Space_Ship, (x, y))


# Defining the function used to display the enemy ships
def Enemy_Ship(x,y, i):
    screen.blit(Enemyimg[i], (x, y))



# Defining the function used to display the energy blast on the screen
def Fire_Bullet(x,y):
    global EnergyBlast_State
    EnergyBlast_State = "fire"
    screen.blit(Bulletimg, (x + 35,y + 10))




# When the game starts, the title screen is displayed on the screen intially
while title_screen:

    Title_Screen()
    keys = pygame.key.get_pressed()

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            title_screen = False # Flag that we are done so we exit this loop

        # When the Space key is pressed,the title screen disappears and the user transitions to the main game
        elif keys[pygame.K_SPACE]:
                title_screen = False
                run = True


    # updating the game window with the new contents
    pygame.display.update()




# -------- Main Program Loop -----------
while run:


    screen.fill((255,255,255))

    # Displaying our main background on the game window
    screen.blit(Background, (0,0))

    # Drawing the line which represents the main boundary that the enemies can reach
    pygame.draw.line(screen, (0,191,255), (0,400), (800,400), 5)


    # When the user clicks the x icon, the game ends and the window closes
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            run = False # Flag that we are done so we exit this loop




    # Checking for all the usable key presses

    # When the right arrow key is pressed, the player ship moves to the right side of the screen
    if (event.type==pygame.KEYDOWN): #KEYDOWN means a key is pressed
        if (event.key==pygame.K_RIGHT) or event.type == pygame.K_d:
            PlayerX_Change = 12

        # When the left arrow key is pressed, the player ship moves to the left side of the screen
        elif (event.key==pygame.K_LEFT) or event.type == pygame.K_a:
            PlayerX_Change = -12

        # When the space key is pressed, the player ship shoots a energy bullet to the enemy ships.
        elif (event.key==pygame.K_SPACE) or event.type == pygame.K_o :
            if EnergyBlast_State == 'ready':
                Bullet_Sound = mixer.Sound('Energy Blast.wav')
                Bullet_Sound.play()
                EnergyBlastX = PlayerX
                Fire_Bullet(PlayerX, EnergyBlastY)


    elif (event.type==pygame.KEYUP): # Keyup means when the key is pressed and let go
            PlayerX_Change  = 0 # When the user lets go of the key, the player ships stops moving




    # When the right or left arrow is pressed, the x position of the ship changes
    PlayerX += PlayerX_Change

    # Placing a boundary or limit for how much the player ship can move to the left side of the screen, which is the end or 0
    if PlayerX <= 0:
        PlayerX = 0

    # Placing a boundary or limit for how much the player ship can move to the right side of the screen, which is the end or 736
    elif PlayerX >= 736:
        PlayerX = 700


    # For each of the enemy ships
    for i in range(Number_Of_Enemies):


        # When the ships goes beyond the y coordinate of 350, the player loses
        if EnemyY[i] >= 350:
            for j in range(Number_Of_Enemies):
                EnemyY[j] = 2000 # Hides all the enemies when the user loses
                PlayerY = 2000 # Hides the player ship when the user loses
                PlayerX = 2000

            # Calls the game over function to tell the user they lost
            Game_Over()
            break # Breaks the game main loop when player loses



        # The x-coordinate of the enemy changes, causing it to moves to the right side of the screen
        EnemyX[i] += EnemyX_Change[i]
        if EnemyX[i] <= 0:
            EnemyX_Change[i] = 4
            EnemyY[i] += EnemyY_Change[i]

        # If the enemy ships reaches the end of the right side of the screen, it starts moving to the left side
        elif EnemyX[i] >= 736:
            EnemyX_Change[i] = -4
            EnemyY[i] += EnemyY_Change[i]


        # To detect when the energy bullet hits the enemy ship.
        # When the bullet hits the ship, the explosion sound occurs, and another enemy ship respawns in a random x(between 0 and 736) and y coordinate(between 10 and 20).
        collision = HitEnemy(EnemyX[i],EnemyY[i],EnergyBlastX, EnergyBlastY)
        if collision:
                Bullet_Sound = mixer.Sound('Ship Explode.wav')
                Bullet_Sound.play()
                EnergyBlastY = 480
                EnergyBlast_State = 'ready'
                Score += 1
                EnemyX_Change[i] += 10
                EnemyY_Change[i] += 7
                EnemyX[i] = random.randint(0,736)
                EnemyY[i] = random.randint(10,20)

        # Recalling the function for enemy ship to spawn
        Enemy_Ship(EnemyX[i], EnemyY[i], i)



    # Bullet Movement Code
    # If the energy bullet is off the screen, it is resetted back to it's original position of the player's ship
    if EnergyBlastY <=0:
        EnergyBlastY = 480
        EnergyBlast_State = "ready"


    # If the energy bullet is fired,the energy bullet moves toward the enemy ships and the top of the screen with the help of the below functions.
    if EnergyBlast_State == 'fire':
        Fire_Bullet(EnergyBlastX, EnergyBlastY)
        EnergyBlastY -= EnergyBlastY_Change




    # Used to call the functions to display the player's ship and score
    Player_Ship(PlayerX, PlayerY)
    PlayerScore(ScoreX, ScoreY)


    # Updating the screen with the new contents and things we drawn
    pygame.display.update()



