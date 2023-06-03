import random
import os
from graphic import hangman_graphics #opcja grafiki z pliku

#Lub można nie komplikować i dodać dictionary w tym miejscu
# hangman_graphics = {
# 0:"""STAGE 1/6
#     ┌
#     |
#     |
#     |
#     |
#     |
#  ___|___
# """,
# 1:"""STAGE 2/6
#     ┌--------┐
#     |        |
#     |
#     |
#     |
#     |
#  ___|___
# """,
# 2:"""STAGE 3/6
#     ┌--------┐
#     |        |
#     |        O
#     |        ┼
#     |
#     |
#  ___|___
# """,
# 3:"""STAGE 4/6
#     ┌--------┐
#     |        |
#     |        O
#     |       -┼-
#     |
#     |
#  ___|___
# """,
# 4:"""STAGE 5/6
#     ┌--------┐
#     |        |
#     |        O
#     |       -┼-
#     |        ┴
#     |
#  ___|___
#  """,
# 5:"""STAGE 6/6
#     ┌--------┐
#     |        |
#     |        O
#     |       -┼-
#     |       ┌┴┐
#     |                SORRY YOU'RE DEAD
#  ___|___
#  """
# }

print("Witaj w grze wisielec")
print("Kategorie: \n1. animals \n2. fruits")


def words_input():
    filename = input('Podaj nazwe kategorii (bez rozszerzenia txt): ')
    if os.path.isfile(f'{filename}.txt'):
        with open(f'{filename}.txt', encoding='utf-8') as f:

            load_words = f.read().splitlines()
        return load_words
    else:
        print('Nie ma takiej kategori :(')


def read_words(filename) -> list:
    with open(filename, encoding='utf-8') as fp:
        content = fp.read().splitlines()
    return content


words_game = words_input()
if words_game is None:
    exit()

words_ask = []
words_list = []
game_chances = 10


def generate(words_to_generate):
    guess = random.choice(words_to_generate)
    words = [guess]
    for i in range(len(words[0])):
        words_list.append(words[0][i])
    for i in range(len(words[0])):
        words_ask.append('-')
    return guess


secret_word = generate(words_game)
print(secret_word)  # wyświetla do sprawdzenia działania kodu


def main(guess_word, game_chances):
    print('Długość słowa', len(words_ask))
    stage = 0
    while game_chances > 0:
        letter = (input(f'Podaj literę lub słowo aby odgadnąć hasło, masz {game_chances} szans: '))
        letter = letter.lower()
        game_chances -= 1
        if letter == guess_word:
            print('ZGADŁEŚ HASŁO PO SŁOWIE GRATULACJE, wylosowane hasło to:', guess_word)
            break
        else:
            found = False
            for x in range(len(words_list)):
                if words_list[x] == letter:
                    words_ask[x] = letter
                    found = True

            print(words_ask)
            if words_ask == words_list:
                print('Hasło odgadnięte, wylosowane hasło to:', guess_word)
                break

            elif not found:
                print(hangman_graphics[stage])
                stage += 1

            if stage == 6:
                print('Koniec gry, skończyły się Tobie życia, hasło to :', guess_word)
                break
            if game_chances == 0:
                print('Koniec gry, skończyły się Tobie szanse, hasło to :', guess_word)
                break


if __name__ == '__main__':
    main(secret_word, game_chances)
