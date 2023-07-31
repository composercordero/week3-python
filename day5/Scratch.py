from random import randint, choice

class BlackJack():

    def __init__(self, name,deck = 48):
        self.name = name
        self.deck = deck
        self.stand = 'off'
        self.game = 'on'
        self.blackjack = 'on'
        
        self.card_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.card_suits = ['Clubs','Diamonds','Hearts','Spades']
        
        self.cards_served = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], \
                             8: [], 9: [], 10: [], 11: [], 12: [], 13: []}
        
        self.card_names = {1: 'Ace', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',\
                            8: '8', 9: '9', 10: '10', 11: 'Jack', 12: 'Queen', 13: 'King'}
        
        self.dealer = Dealer(0, 100, [])
        self.user1 = Player(0, 100, [], name)
        
        print(f'Welcome to That Annoying Wine Shop Casino, {self}!')
        print(f'\nYou have ${self.user1.money} on your account.')
        
    def __str__(self):
        return self.name.title()
    
    # -------------------- Checking the Game -------------------- #
    
    def check_blackjack(self):
        if self.user1.hand == 21:
            print(f'BlackJack!')
            self.reset_game()
        else:
            self.blackjack = 'off'
            
    def game_status(self):
        if self.stand == 'off':
            if self.user1.hand > 21:
                print(f'Busted!')
                self.reset_game()                
        else:
            if self.dealer.hand > 21:
                print(f'Congrats, {self}! Dealer is busted')
                self.reset_game()
            elif self.user1.hand > self.dealer.hand:
                print(f'Congrats, {self}! You won this round.')
                self.reset_game()
            else:
                print(f'You lost this round, {self}.')
                self.reset_game()
               
    def reset_game(self):
        self.stand = 'off'
        self.blackjack = 'on'
        self.user1.deck = []
        self.dealer.deck = []
        self.user1.hand = 0
        self.dealer.hand = 0
    
    def pay(self):
        if self.double_down == 'on':
            self.user1.money += bet * 2 
        else:
            self.user1.money += bet 
                    
    # -------------------- Play -------------------- #
            
    def shuffle_cards(self):
        number = randint(1,13)
        suit = choice(self.card_suits)
        
        while suit in self.cards_served[number]:
            number = randint(1,13)
            suit = choice(self.card_suits)
        self.cards_served[number].append(suit)
        self.deck -= 1
        return number, suit

    def deal_initial_cards(self, target):
        for i in range(1,3):
            tup = self.shuffle_cards()
            if target == 'dealer':
                self.dealer.deck.append(f'{self.card_names[tup[0]]} of {tup[1]}')
                if tup[0] in {1, 11, 12, 13}:
                    self.dealer.hand += 10
                else:
                    self.dealer.hand += tup[0]
            elif target == 'user1':
                self.user1.deck.append(f'{self.card_names[tup[0]]} of {tup[1]}')
                if tup[0] in {1, 11, 12, 13}:
                    self.user1.hand += 10
                else:
                    self.user1.hand += tup[0]
            i += 1
        
    def deal_cards(self):
        tup = self.shuffle_cards()
        if self.stand == 'on':
            self.dealer.deck.append(f'{self.card_names[tup[0]]} of {tup[1]}')
            print(f'\nDealer got a {self.card_names[tup[0]]} of {tup[1]}')
            if tup[0] in {1, 11, 12, 13}:
                self.dealer.hand += 10
            else:
                self.dealer.hand += tup[0]
            print(f'\nDealer deck is: {self.dealer.deck}')            
            print(f'\nDealer count is: {self.dealer.hand}')
        else:
            self.user1.deck.append(f'{self.card_names[tup[0]]} of {tup[1]}')
            print(f'\nYou got a {self.card_names[tup[0]]} of {tup[1]}')
            if tup[0] in {1, 11, 12, 13}:
                self.user1.hand += 10
            else:
                self.user1.hand += tup[0]
            print(f'\nYour Deck is: {self.user1.deck}')
            print(f'\nYour Count is: {self.user1.hand}')
            
#     def deal_cards(self, target):
#         tup = self.shuffle_cards()
#             self.target.deck.append(f'{self.card_names[tup[0]]} of {tup[1]}')
#             print(f'\n{target} got a {self.card_names[tup[0]]} of {tup[1]}')
#             if tup[0] in {11, 12, 13}:
#                 self.target.hand += 10
#             else:
#                 self.target.hand += tup[0]
#             print(f'\n{target} deck is: {self.{target}.deck}')            
#             print(f'\n{target} count is: {self.{target}.hand}')
            
    def dealer_show(self):
        print('\ndealer_show\n')
# ------------------------ Players ------------------------ #
class Dealer():

    def __init__(self, hand, money, deck):
        self.hand = hand
        self.money = money
        self.deck = deck
    
    def __str__(self):
        return {f'The house\'s hand is {self.hand}'}
    
    def __repr__(self):
        return (f'< Dealer | {self.deck} >')
    
class Player(Dealer):
    
    def __init__(self,hand, money, deck, name):
        super().__init__(hand,money,deck)
        self.name = name
        
    def __str__(self, name):
        return {f'Your hand is {self.hand}'}
    
    def __repr__(self):
        return (f'< Player | {self.name} >')

def main():
# ------------------------ Set up ------------------------ #
    name = input('What is your name? ')
    
    blackjack = BlackJack(name)

    blackjack.deal_initial_cards('dealer')
    blackjack.deal_initial_cards('user1')
    
    while blackjack.game == 'on':
# -------------------------- Bet -------------------------- #
        if blackjack.blackjack == 'on':
            bet = input(f'\nHow much would you like to bet, {name}? ')
            while not bet.isdigit() or int(bet) > blackjack.user1.money:
                bet = input(f'Please, {name}, enter a valid number: ')
            blackjack.user1.money -= int(bet)
# -------------------- Shuffle Cards -------------------- #        
        blackjack.shuffle_cards()
        print('='*100)
        print(f'\n{blackjack.cards_served}')
        print('='*100)
# -------------------- Check BlackJack -------------------- #        
        if blackjack.blackjack == 'on':
            blackjack.check_blackjack()
# -------------------------- Info -------------------------- #
        print(f'\nYour deck is: {blackjack.user1.deck}\n')
        print(f'\nYour count is: {blackjack.user1.hand}\n')
# ------------------------ Questions ------------------------ #        
        action = input('Would you like to \
        \n\t1. hit\
        \n\t2. stand\
        \n\t3. double down\
        \n\t4. Insurance\
        \n\t5. Split\
        \n\t6. Quit: ').lower()
        while action not in {'1','hit', '2', 'stand', '3', 'double', 'down', \
                             '5', 'insurancre', '5', 'split', '6', 'quit'}:
            action = input('Select a valid option\
        \n\t1. hit\
        \n\t2. stand\
        \n\t3. double down\
        \n\t4. Insurance\
        \n\t5. Split\
        \n\t6. Quit: ').lower()
# ------------------------ Actions ------------------------ #
        if action in {'1','hit'}:
            blackjack.deal_cards()
        elif action == 'stand' or action == '2':
            blackjack.stand = 'on'
            blackjack.dealer_show()
            while blackjack.dealer.hand < 17:
                blackjack.deal_cards()
        elif action == 'double':
            blackjack.double_down()
        elif action == 'insurance':
            pass
        elif action == 'split':
            pass
        elif action in {'quit','6'} :
            blackjack.game = 'off'
        blackjack.game_status()

main()