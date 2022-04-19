from ast import Not
from cmath import e
from multiprocessing.sharedctypes import Value
from random import randrange
import random
import sys
from tokenize import Number
from contextlib import suppress

try:

# Starting of the game,1 choice
    version = open('version.txt', 'r')
    print (f'Version is:',  *version)
    
    print ('Hello, welcome to python Akinator!')
    print()
    print('Rules:\n I will ask questions, you have to choose answer.\n 1 - Yes\n 2-No \n 3- probably')
    print ()
    start= int(input('If you ready type 1: '))
    print()

    if start != 1:
        print("Incorrect type of input!")
        sys.exit(1)

# Answer variables will do it more easier to read

    Yes = 1
    No = 2

  # All characters
    
    Character1 = ('PewDiePie')
    Character2 = ('MrBeast')
    ch3 = ('Cocomelon')
    ch4 = ('A part of your family')
    ch5 = ('Your close friend')
    ch6 = ('Pikachu')
    ch7 = ('T-Series')
    ch8 = ('Elon Mask')
    ch9 = ('Tokyo Ghoul')
    ch10 = ('Brawl Stars')
    enter = ('\n')
   

# After each question it is a 'if' program which is helping to indefy when variable AllCharacters is empty
# And after each question it is a code which is deleting a character if he has no connection with question    
    q1 = int(input('Is your character real? '))
    print ()
    
    if q1 == No:
        del(Character1)
        del (Character2)
        del  (ch3)
        del (ch4)
        del(ch5)
        del(ch7)
        del(ch8)
        Character1 = []
        Character2 = []
        ch3 = []
        ch4 = []
        ch5 = []
        ch7 = []
        ch8 = []
    
    if q1 == Yes:
        del(ch6)
        del(ch10)
        del(ch9)
        ch6 = []
        ch10 = []
        ch9 = []


    q2 = int(input('Is it an popular (more than 1m subs) Youtuber? '))
    print ()
    
    if q2 == Yes:
        del(ch5)
        del(ch4)
        del(ch6)
        del(ch9)
        del(ch8)
        del(ch10)
        ch4 = []
        ch5 = []
        ch6 = []
        ch8 = []
        ch9 = []
        ch10 = []
    
    
    if q2 == No:
        del(Character1)
        del(Character2)
        del(ch3)
        del(ch7)
        Character1 =[]
        Character2 = []
        ch3 = []
        ch7 = []

   
    q3 = int(input('Is your character Swidish? '))
    print ()
    
    if q3 == Yes:
        del(ch6)
        ch6 = []
        del(ch3)
        ch3 = []
        del(Character2)
        Character2 = []
        del(ch7)
        ch7 = []
        del(ch8)
        ch8 =[]
    if q3 == No:
        del(Character1)
        Character1 = []
    

    q4 = int(input('Have everyone who knows him seen his face? '))
    print ()
    
    if q4 == Yes:
        del(ch3)
        
        del ch10
        del ch7
        ch3 = []
        ch6 = []
        ch10 = []
        ch7 = []
        
    if q4 == No:
        del(Character1)
        del(Character2)
        del(ch4)
        del(ch5)
        del ch8
        del ch9
        ch6 = []
        Character1 = []
        Character2 = []
        ch4 = []
        ch5 = []
        ch8 = [] 
        ch9 = []
        
    
    q5 = int(input('Is your character the most popular gamer-youtuber? '))
    print ()
    
    if q5 == Yes:
        del(Character2)
        del(ch3)
        del(ch4)
        del(ch5)
        del(ch6)
        del(ch7)
        del(ch8)
        del(ch9)
        del(ch10)
        Character2 = []
        ch3 = [] 
        ch4= []
        ch5 = []
        ch6 = []
        ch7 = [] 
        ch8 = [] 
        ch9 = []
        ch10 = []

    if q5 == No:
        del(Character1)
        Character1 = []

    q6 = int(input('Did you met this person? '))
    print ()
    
    if q6 == Yes:
        del(Character1)
        del(Character2)
        del(ch3)
        del(ch6)
        del(ch7)
        del(ch8)
        del(ch9)
        del(ch10)
        Character1 = []
        Character2 =[]
        ch3 = []
        ch6 = []
        ch7 = []
        ch8 = []
        ch9 = []
        ch10 = []
    if q6 == No:
        del(ch4)
        del(ch5)
        ch4 = []
        ch5 = []

    q7 = int(input('Has he a group of people helping him in his work? '))
    print ()
    
    if q7 == Yes:
        del Character1
        Character1 = []
        del ch4
        ch4 = []
        del ch5 
        ch5 = []
        del ch6
        ch6 = []
        del ch8
        ch8 = []
        del ch9
        ch9 = []

    if q7 == No:
        del Character2
        Character2 = []
        del ch3
        ch3 = []

        
        del ch10
        ch10 = []
    q8 = int(input('Is your character American? '))
    print ()
    
    if q8 == Yes:
        del Character1
        Character1 = []
        del ch6
        ch6 = []
        del ch7
        ch7 = []
        del ch9
        ch9 = []
    if q8 == No:
        Character2 = []
        ch3 =[]
        ch10 = []
        ch3 = []          
        ch8 = []
        
        



    q20 = int(input('Is it a game? '))
    print ()
    if q20 == Yes:
       Character1 = []
       Character2 = []
       ch3 = []
       ch4 = []
       ch5 = []
       ch6 = []
       ch7 = []
       ch8 = []
       ch9 = [] 
    if q20 == No:
        del(ch10)
        ch10 = []
    # q9 = int(input('Is he/she older than 30 years old? '))
    # if q9 == Yes:
        # Character2 = []
# 
    # if q9 == No:
        # Character1 =[]

        
        


    q10 = int(input('Does your character live in your home? '))
    print ()
    
    if q10 == Yes:
        ch5 =[]
        Character1 = []
        Character2 = []
        ch3 = []
        ch6 =[]
        ch7 = []
        ch8 = []
        ch9 = []
        ch10 = []
    if q10 == No:
        ch4 = []

   
    q11 = int(input('Is it the most subscribed channel in the world? '))
    print ()
    if q11 == No:
        ch7 = []
    if q11 == Yes:
        ch10 = []
        Character1 =[]
        ch9 = []
        ch8 = []
        ch6 = []
        ch5 = []
        ch4 = []
        ch3 = []
        Character2 = []
    
    q12 = (int(input('Is it the most subscribed channel for kids? ')))
    print ()

    if q11 == No:
        ch3 = []
    if q11 == Yes:
        ch10 = []
        Character1 =[]
        ch9 = []
        ch8 = []
        ch6 = []
        ch5 = []
        ch4 = []
        ch7 = []
        Character2 = []

    q13 = int(input('Is your character connected to anime? '))
    print ()
    
    if q13 == Yes:
        del(ch5)
        ch5 = []
        del(ch4)
        ch4 = []
        del(ch3)
        ch3 = []
        del(Character2)
        Character2 = []
        del(Character1)
        Character1 = []
        del ch10
        ch10 =[]
        ch7 = []
        ch8 = []

    if q13 == No:
        del(ch6)
        del(ch9)
        ch6 = []
        ch9 = []

    q14 = int(input('Does he break his fingers often? '))
    print ()
    if q14 == Yes:
        ch10 = []
        Character1 =[]
        ch6 = []
        ch8 = []
        ch7 = []
        ch5 = []
        ch4 = []
        ch3 = []
        Character2 = []
    if q14 == No:
        ch9 = []
        AllCharacters = [Character2, Character1, ch3, ch4, ch5, ch6, ch7, ch8, ch9, ch10]
        
        
        if Character1 == []:
            AllCharacters.remove (Character1)
        if Character2 == []:
            AllCharacters.remove (Character2)
        if ch3 == []:
            AllCharacters.remove (ch3)
        if ch4 == []:
            AllCharacters.remove (ch4)
        if ch5 == []:
            AllCharacters.remove (ch5)
        if ch6 == []:
            AllCharacters.remove (ch6) 
        if ch7 == []:
            AllCharacters.remove (ch7)
        if ch7 == []:
            AllCharacters.remove (ch8)
        if ch9 == []:
            AllCharacters.remove (ch9)
        if ch10 == []:
            AllCharacters.remove (ch10)
               
    
# And if someone will write incorrect answer, it will show message about error
    
    print ()

    print (f'Your character is: {AllCharacters} ')
    akinator_end = int(input('Type 1 if yes if no type 2: '))
    if akinator_end == 1:
        print('Im glad to hear it!')
        print('Thanks for using!')
        print('If you wanna help my project write characters to reddit u/xandreymo')
        sys.exit()
    elif akinator_end == 2:
        print('Oh, looks like i didnt add this character yet! ')
        characters = input ('What character it was? ')
        with open('characters_from_beta.txt', 'a') as the_file:
            the_file.write(characters)
            the_file.write(enter)
        print('If you wanna help my project write characters to reddit u/xandreymo')
        sys.exit()

# If we will catch an error our program will say about it and crush game 

except ValueError:
    print ('There is no characters match to your answers.\n That means You answered incorretly, or program doesnt have this character\n If its 2nd problem go to u/xs')

except Exception:
    pass
    # print ('ERROR, GAME CRUSHES')
    sys.exit()
# Finally base is working! Only left to add more characters, do it in an app, and do it more beaty!