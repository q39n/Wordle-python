import random, sys, nltk, replit
from termcolor import colored
from nltk.corpus import words

base = [
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ']
]

def print_board():
    print(f'''
┏━━━┳━━━┳━━━┳━━━┳━━━┓
┃ {base[0][0]} ┃ {base[0][1]} ┃ {base[0][2]} ┃ {base[0][3]} ┃ {base[0][4]} ┃
┣━━━╋━━━╋━━━╋━━━╋━━━┫
┃ {base[1][0]} ┃ {base[1][1]} ┃ {base[1][2]} ┃ {base[1][3]} ┃ {base[1][4]} ┃
┣━━━╋━━━╋━━━╋━━━╋━━━┫
┃ {base[2][0]} ┃ {base[2][1]} ┃ {base[2][2]} ┃ {base[2][3]} ┃ {base[2][4]} ┃
┣━━━╋━━━╋━━━╋━━━╋━━━┫
┃ {base[3][0]} ┃ {base[3][1]} ┃ {base[3][2]} ┃ {base[3][3]} ┃ {base[3][4]} ┃
┣━━━╋━━━╋━━━╋━━━╋━━━┫
┃ {base[4][0]} ┃ {base[4][1]} ┃ {base[4][2]} ┃ {base[4][3]} ┃ {base[4][4]} ┃
┗━━━┻━━━┻━━━┻━━━┻━━━┛
''')

def print_menu():
    print("Let's play Wordle:")
    print("Type a 5 letter word and hit enter!")

nltk.data.path.append('/work/words')
word_list = words.words()
words_five = [word for word in word_list if len(word) == 5]

replit.clear()
print_board()

word = random.choice(words_five)
for i in range(5):
    guess = input().lower()
    
    for index ,letter in enumerate(guess):
        try:
            if letter == word[index]: 
                base[i][index] = colored(letter, 'green')
            elif letter not in word:
                base[i][index] = colored(letter, 'red')
            elif letter in word:
                base[i][index] = colored(letter, "yellow")
        except:
            pass
    print_board()
    if guess == word:
        print(f"Gongrats You Won in {i + 1} attempts !")
        break
    elif i == 5:
        print("")