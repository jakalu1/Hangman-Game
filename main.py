"""
Hangman
*this file includes the front-end and backend to the hangman game that I created.
"""
import pygame
import nltk
from nltk.corpus import words
import random
import string


def __init__():
    letters_guessed_right = ''
    letters_guessed_wrong = ''
    total_wrong = 6
    wrong_guesses = 0
    english_words = (words.words()) #assigns the word list from nltk.corpus to english_words
    random.shuffle(english_words) #shuffle the list of words so that it isn't alphabetical ordered!
    random_word = english_words[random.randint(0, len(english_words)-1)] #picks a random number from 0 - len(english_words) which then is used as an index to pick 1 random word!
    while '-' in random_word or ' ' in random_word: #as long as there is a - or ' ' in a word, pick a different word so that we can work with it
        random_word = english_words[random.randint(0, len(english_words)-1)]
    letters = list(random_word.lower())   
    return english_words, random_word.lower(), letters, letters_guessed_right, letters_guessed_wrong, total_wrong, wrong_guesses

wrong_letter_positions = [(450, 75), (500, 150), (550, 240), (600, 75), (650, 180), (700, 100)] #fixed positions for the wrong letters

#all initialized backend variables that we need to use in the program!
english_words, random_word, letters, letters_guessed_right, letters_guessed_wrong, total_wrong, wrong_guesses = __init__()


pygame.init() #pygame initializer
pygame.font.init() #font initializer
width = 800 #width and height of the screen in pixels
height = 800 
white = pygame.Color('white')
grey = pygame.Color('grey')
black = pygame.Color('black')

screen = pygame.display.set_mode((width, height)) #set up the screen with ur dimension variables!
pygame.display.set_caption('HangMan')

entered_letter = ''
running = True



while running:
    #when starting the game loop, clear the screen first!
    screen.fill(white)
    
    #initializing font settings  
    font = pygame.font.Font(None, 36)
    font2 = pygame.font.Font(None, 30)
    font3 = pygame.font.Font(None, 80) 

    starting_cor = [430, 330]
    for each_letter in random_word:
        underscore = font.render(' _ ', True, black)
        screen.blit(underscore, (starting_cor[0], starting_cor[1]))
        if each_letter in letters_guessed_right:
            letter_color = black
        else:
            letter_color = white     
        hidden_letter = font.render(each_letter, True, letter_color) #we are making it grey just to test it out
        screen.blit(hidden_letter, (starting_cor[0], starting_cor[1]))
        starting_cor[0] += 20

    entering_the_letter = font2.render(entered_letter, True, black) #entering the letter 
    screen.blit(entering_the_letter, (653, 753))

    for event in pygame.event.get():#for every single key pressed, get the pygame event for that key, and render/blit the key onto the screen in real time!
        if event.type == pygame.QUIT: #putting this here so that the user can exit the game. when the user htis the X (close) button
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                entered_letter = entered_letter[:-1]  # Remove the last character if backspace is pressed  
            else:
                char = event.unicode #assign the letter thats pressed to char (#event.unicode is attribute that represents the actual key being pressed. the computer reads the key press event as many different things describing what happened and unciode just assigns that to a letter)
                if char.isalpha() and len(char) == 1:#only allow the input if char is a letter and if its ONLY 1 letter
                    if char.lower() not in letters_guessed_right + letters_guessed_wrong: #only proceed in the program if the entered letter hasn't been entered yet!


                        entered_letter = char.lower() #makes it so that it is only 1 letter being inputted each guess      
                        if not entered_letter in letters:
                            wrong_guesses += 1 
                            letters_guessed_wrong += entered_letter
                            #below, in later parts, we both add the letters_guessed_wrong to the wrong guesses box and we also change the hangman drawing because of the letters_guessed_wrong incremeneted here
                        
                        elif entered_letter in letters:
                            letters_guessed_right += entered_letter

      
    
    tries_left = font.render(f'Tries Left: {total_wrong-wrong_guesses}', True, black)
    screen.blit(tries_left, (500, 710)) #the tries left

    right_letters = font2.render(f'Right Guesses: ', True, black)
    screen.blit(right_letters, (500, 300)) #right letters
    
    enter_letter = font.render('Enter Letter: ', True, black)
    screen.blit(enter_letter, (500, 750)) #the enter letter 
    


    word_box = pygame.draw.rect(screen, white, (400, 25, 350, 250)) #the word box
    pygame.draw.rect(screen, black, word_box, 2) #since the wordbox is white, we draw a black line over it so that it can be visible!

    word_box_area = font2.render(f'Wrong Guesses', True, black) #the Guesses Wrong box
    screen.blit(word_box_area, (500, 40)) 

    letters_guessed_wrong_list = list(letters_guessed_wrong)
    wrong_letters_list = []
    for each_letter in letters_guessed_wrong_list:
        wrong_letters = font2.render(each_letter, True, black) #renders each wrong letter that is in the list
        wrong_letters_list.append(wrong_letters) #now we have a list of letters that are ready to be blitted

    index = 0
    for each_letter in wrong_letters_list:
        screen.blit(each_letter, wrong_letter_positions[index])
        index += 1
    
    #draw the hangstand, and hangman 6 parts
    pygame.draw.rect(screen, black, (20, 50, 200, 10))  # Hang stand
    pygame.draw.line(screen, black, (20, 800), (20, 50), 7) #the bottom part of hangstand
    pygame.draw.line(screen, black, (220, 50), (220, 150), 8) #the hang pole

    if wrong_guesses == 1:
        pygame.draw.circle(screen, black, (220, 195), 45, 3) #the head
    
    elif wrong_guesses == 2:
        pygame.draw.circle(screen, black, (220, 195), 45, 3) #the head
        pygame.draw.line(screen, black, (220, 237), (220, 470), 5) #the body

    elif wrong_guesses == 3:
        pygame.draw.circle(screen, black, (220, 195), 45, 3) #the head
        pygame.draw.line(screen, black, (220, 237), (220, 470), 5) #the body
        pygame.draw.line(screen, black, (220, 300), (300, 320), 5) #the right arm
    
    elif wrong_guesses == 4:
        pygame.draw.circle(screen, black, (220, 195), 45, 3) #the head
        pygame.draw.line(screen, black, (220, 237), (220, 470), 5) #the body
        pygame.draw.line(screen, black, (220, 300), (300, 320), 5) #the right arm
        pygame.draw.line(screen, black, (220, 300), (140, 320), 5) #the left arm
    
    elif wrong_guesses == 5:
        pygame.draw.circle(screen, black, (220, 195), 45, 3) #the head
        pygame.draw.line(screen, black, (220, 237), (220, 470), 5) #the body
        pygame.draw.line(screen, black, (220, 300), (300, 320), 5) #the right arm
        pygame.draw.line(screen, black, (220, 300), (140, 320), 5) #the left arm        
        pygame.draw.line(screen, black, (220, 465), (300, 550), 5) #the right leg
    
    elif wrong_guesses == 6:
        pygame.draw.circle(screen, black, (220, 195), 45, 3) #the head
        pygame.draw.line(screen, black, (220, 237), (220, 470), 5) #the body
        pygame.draw.line(screen, black, (220, 300), (300, 320), 5) #the right arm
        pygame.draw.line(screen, black, (220, 300), (140, 320), 5) #the left arm        
        pygame.draw.line(screen, black, (220, 465), (300, 550), 5) #the right leg
        pygame.draw.line(screen, black, (220, 465), (140, 550), 5) #the left leg
        screen.fill(white)
        game_over = font3.render(f'GAME OVER!', True, (pygame.Color('red')))
        screen.blit(game_over, (250, 300))

    if set(letters) == set(letters_guessed_right): #convert it to sets because in lists, the guessed order has to be the exact same for this statement to be true but it doesn't have to be in sets!
        screen.fill(white)
        winner_winner = font3.render('WINNER!', True, pygame.Color('red'))    
        screen.blit(winner_winner, (268, 325))     

    #constantly update the display
    pygame.display.flip()

#stop the pygame program
pygame.quit()
