from random import randint
words_list = ['apple', 'pineapple', 'watermelon', 'kiwi', 'peach', 'banana', 'strawberry', 'melon', 'cherry', 'mango', 'durian', 'coconut']
word = words_list[randint(0, len(words_list)-1)]
characters = ''
rem_chance = 5
blank = '_'*len(word)


def chance(rem_chance):
    if rem_chance == 4:
        print(
'''
⎡‾‾‾‾‾‾‾‾‾‾⎤
⎜          ┼
⎜          O
⎜
⎜
⎜
⎜
⎜
⎜
''')
        print(rem_chance, 'Left.')

    elif rem_chance == 3:
        print(
'''
⎡‾‾‾‾‾‾‾‾‾‾⎤
⎜          ┼
⎜          O
⎜          ⎜
⎜
⎜
⎜
⎜
⎜
''')
        print(rem_chance, 'Left.')

    elif rem_chance == 2:
        print(
'''
⎡‾‾‾‾‾‾‾‾‾‾⎤
⎜          ┼
⎜          O
⎜          ⎟
⎜         /⎟\ 
⎜
⎜
⎜
⎜
''')
        print(rem_chance, 'Left.')

    elif rem_chance == 1:
        print(
'''
⎡‾‾‾‾‾‾‾‾‾‾⎤
⎜          ┼
⎜          O
⎜          ⎟
⎜         /⎟\ 
⎜          ⎟
⎜
⎜
⎜
''')
        print(rem_chance, 'Left.')

    elif rem_chance == 0:
        print(
'''
⎡‾‾‾‾‾‾‾‾‾‾⎤
⎜          ┼
⎜          O
⎜          ⎟
⎜         /⎟\\
⎜          ⎟
⎜         ⎰⎱
⎜
⎜
''')
        print('Fail!')

while rem_chance > 0:
    # print(' '.join(blank))
    input_letter = input('type letter: ').lower()

    characters = ''

    if input_letter in characters:
        print("You've already guessed that letter.")
        continue

    if input_letter in word:
        for i in range(len(word)):
            if word[i] == input_letter:
                blank = blank[:i] + input_letter + blank[i+1:]
    else:
        rem_chance -= 1
        chance(rem_chance)

    if '_' not in blank:
        print('Congratulations! You guessed the word:', word)
        break