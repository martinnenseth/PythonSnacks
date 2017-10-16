import os
import random

#In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary. Download this file and save it in the same directory as your Python code. This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments. Each line in the file contains a single word.

# simple solution: append to array. Better: randomly pop a line from the file without temporarily storing it.
def pick_word():
    lines = []
    with open("sowpods.txt", "r") as file:
        for line in file:
            lines.append(str(line))

        return random.choice(lines)


def guess():
    word = pick_word().lower()
    print(word)
    wrong_guesses = []
    correct_guess = "_" * len(word)
    correct_guess = list(correct_guess)

    while len(word) >= 0:
        letter = input("Guess your letter: ")
        if letter not in word:
            print("Incorrect!")
            wrong_guesses.append(letter)
            continue
        else:
            print("Correct!")
            index = word.index(letter)
            correct_guess[index] = letter
            print(correct_guess)


# TODO: Check if there are several indexes of letter in word. The word is an element too long atm.


def main():
    print("Welcome to Hangman!")
    print("- - - - - - -")


main()
guess()




