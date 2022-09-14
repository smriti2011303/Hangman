#importing liberary
import random

#taking user mane
name=input("Please enter your name here:")
print("Good luck!",name)

#creating a list of a words to be guessed
words =['rainbow','blue','animal','teacher','lake','noun','computer','transportation','earthquake','nothing','score','game','kids','school','classes','windows','laptop','keyword','mouse','world','issue','report','screen']

#randomly printing the words
word = random.choice(words)

print("Guess the charaters of the word:")
guesses =''
turn = 10

#condition to check for 10 turn
while turn > 0:
    failed = 0

    for char in word :
        if char in guesses :
            print(char)

        else:
             print("_")
             failed += 1
    if failed  == 0 :
        print("You win! Congratulation!!")
        #print correct word
        print("The word is :", word)
        break
    guess = input("Guess a character:")

    guesses += guess

    if guess not in word :
        turn -= 1
        print("Wrong input, Please try again !")

        print("You have ", turn, "more guesses")

        if turn == 0:
            print("You losses better luck next time")

