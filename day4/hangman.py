# Missing validations
# Missing Random Choice Words (import not working)
# Missing ending the game if user guesses the word


class Hangman():

    def __init__(self, name):
        self.name = name
        self.lives = 6
        self.letters_guessed = []
        self.word_to_guess = ''
        self.result = ''
        self.count = 0
    def __str__(self):
        pass

    def __repr__(self):
        pass

    def generate_word(self):
        self.word_to_guess = 'word'
        self.show_word(self.word_to_guess)

    def show_word(self, word):
        sep_word = [" _ " if letter not in self.letters_guessed else f' {letter} ' for letter in self.word_to_guess] 
        print(f'\n{"".join(sep_word)}\n')

    def guess_letter(self, letter):
        if letter in self.word_to_guess:
            print(f'\n"{letter}" is in the word. Nice job!')
            self.count += 1
            self.show_word (self.word_to_guess)
        else:
            print(f'\nAww. "{letter}" is not in the word.')
            self.lives -= 1
        self.list_of_letters(letter)
        print(f'\nThese are the letters you\'ve guessed: {self.letters_guessed}')
    
    def guess_word(self, word):
        if word == self.word_to_guess:
            print(f'\n"{word}" is the right word. Nice job!')
            for letter in [*word]:
                self.list_of_letters(letter)
            self.show_word (self.word_to_guess)
            self.count = len(self.word_to_guess)
        else:
            print(f'\nAww. "{word}" is not correct.')
            self.lives -= 1
            for letter in word:
                self.list_of_letters(letter)
        print(f'\nThese are the letters you\'ve guessed: {self.letters_guessed}')

    def list_of_letters(self, letter):
        if letter not in self.letters_guessed:
            self.letters_guessed.append(letter)
        return self.letters_guessed
    
    def game_status(self):
        if self.count < len(self.word_to_guess):
            if self.lives > 1:
                print(f'You have {self.lives} lives left.')
            elif self.lives == 1:
                print(f'You have 1 life left.')
            else:
                print(f'It\s game over :(')
                play_again = input('Would you like to play again? y/n ')
                if play_again == 'y':
                    pass # random choice word new word and lives back to 6
                elif play_again == 'n':
                    game = 'off'
        else:
            print(f'YAY, {self.name}! You won.')
            game = 'off'
    
# -------------------------------------------- GAME -------------------------------------------- #

def game():
    name = input('What\'s your name? ') 
    hangman = Hangman(name)
    game = 'on'
    while game == 'on':
        
        hangman.generate_word()
        hangman.game_status()
        guess = input(f'\nWould you like to guess a letter or the word?\n\t1. letter\n\t2. word \n\t3. quit\n')
        
# -------------------------------------------- OPTIONS -------------------------------------------- #

        if guess == '1' or guess == 'letter':
            letter_user = input(f'\nEnter a letter: ')
            hangman.guess_letter(letter_user)
        elif guess == '2' or guess == 'word':
            word_user = input('Enter a word: ')
            hangman.guess_word(word_user)
        elif guess == '3' or guess == 'quit':
            print(f'\nThank you for playing, {hangman.name}.\n')
            break

# -------------------------------------------- CALL -------------------------------------------- #

game()


