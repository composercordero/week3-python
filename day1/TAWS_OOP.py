class Cart():

    def __init__(self, shop_name, payment, shop, total_cart, cart, freebies):
        self.shop_name = shop_name
        self.payment = payment
        self.shop = shop
        self.total_cart = total_cart
        self.cart = cart
        self.freebies = freebies

    def add(self):
        while True:
            Cart.display_articles()
            
            add_art = input('What article would you like to add? ').lower().strip()

            if add_art in {'wine', 'red', 'white', 'rose'}:
                Cart.display_wines()
                add_art = input('\nWhat wine would you like to buy? ').lower().strip()
            elif add_art == 'cheese':
                Cart.display_article('cheese')
                add_art = input('\nWhat type of cheese would you like to buy? ').lower().strip()
            elif add_art == 'accessories':
                Cart.display_article('accessories')
                add_art = input('\nWhat accessory would you like to buy? ').lower().strip()
                
            add_art_num = input('How many articles would you like to add to your cart? Enter a number: ').strip()
            
            print("If you add two more, I'll throw in a random freebie for you!")
            add_art_more = input('add two more article y/n? ').lower().strip()
            if add_art_more == 'y':
                add_art_num = int(add_art_num) + 2
                Cart.freebie(self)

            self.cart[add_art] = {'quantity': add_art_num, 'price': Cart.find_price(add_art)}

            wine_pairing = articles['wine']['red'][add_art]["pairing"]

            if add_art in articles['wine']['red'] or add_art in articles['wine']['white'] or add_art in articles['wine']['rose']:
                print(f'I see you added {add_art} which goes perfect with {wine_pairing}')
                add_pairing = input(f'add {wine_pairing} to your cart for free? y/n ').lower().strip()
                if add_pairing == 'y':
                    self.cart[wine_pairing] = {'quantity': 1, 'price': 0}
            
            Cart.view_cart(self)
            
            add_art_cont = input('Would you like to add more articles to your cart? y/n: ').lower().strip()
            
            while add_art_cont not in {'y', 'n'}:
                add_art_cont = input('select a valid option. add more articles? y/n: ').lower().strip()
                
            if add_art_cont == 'n':
                break

    def delete(self):
        if self.cart == {}:
            print('\nYour shopping cart is empty. Time to put some wine there :)')
        else:
            Cart.view_cart(self)

            del_art = input('What article would you like to delete? ')

            while del_art not in self.cart:
                del_art = input('Enter an article in your cart: ')

            del_art_num = input('How many would you like to delete? ')
            del_conf = input("are you sure you'd like to delete this many articles from your shopping cart? y/n ")

            if int(self.cart[del_art]['quantity']) - int(del_art_num) == 0:
                del self.cart[del_art]
                return print(f"You've deleted {del_art} from your cart")
            else:
                self.cart[del_art]['quantity'] = int(self.cart[del_art]['quantity']) - int(del_art_num)
            Cart.view_cart(self)

    def pay(self):
        print('Your cart:\n')
        Cart.view_cart(self)
        Cart.total(self) 
        
        while True:
            method_of_payment = input('Method of payment - credit card, apple pay, or cash? ')
            if method_of_payment == 'credit card' or method_of_payment == 'apple pay':
                Cart.all_set(self)
                break    
            elif method_of_payment == 'cash':

                    cash = input('Enter the amount of cash: ')
                    if int(cash) == total_cart:
                        return Cart.all_set(self)
                    elif int(cash) > total_cart:
                        print(f'\nThank you for the tip!\n')
                        return Cart.all_set(self)
                    else: 
                        print("\nThat's not enough cash.")

    def all_set(self):
        print('You are all set. Thank you for shopping at That Annoying Wine Shop\n')
        print('Here is your Annoying Receipt:')
        Cart.view_cart(self)
        global shop
        self.shop = 'closed'

    def leave(self):

        if self.cart == {}:
            print(f'Thank you for coming to {self.shop_name}. I hope I can annoy you more soon!')
            self.shop == 'closed'
        else:   
            if self.payment == 'done':
                Cart.all_set(self)
            else:
                print('\nRemember to pay :)\n')
                Cart.pay(self)

    # Display

    def display_articles():
        for key,value in articles.items():
            print(key.title())
            for k,v in value.items():
                print(f'\t{k}')

    def display_wines():
        for key,value in articles.items():
            if key == 'wine':
                for k,v in value.items():
                    print(k.title())
                    for a,b in v.items():
                        print(f'\t{a}')
                
    def display_article(article):
        for key,value in articles.items():
            for k,v in value.items():
                if key == article:
                    print(k.title())
                    
    def view_cart(self):
        if self.cart == {}:
            print('\nYour shopping cart is empty. Time to put some wine there :)\n')
        else:
            print('\n(Qty) Item - Price\n')
            for key,value in self.cart.items():
                qty = int(self.cart[key].get('quantity'))
                art_price = int(self.cart[key].get('price'))
                print(f"({qty}) {key.title()} - ${art_price}\n\tTotal: ${art_price * qty}\n")
            Cart.total(self)
            
    def total(self):
        global total_cart
        sum = 0
        for key, value in self.cart.items():
            sum += self.cart[key]['price'] * int(self.cart[key]['quantity'])
        total_cart = sum
        print(f"\nYour total is: ${total_cart:.2f}")
        
    def find_price(item):
        if item in articles['wine']['red']:
            return articles['wine']['red'][item]['price']
        elif item in articles['wine']['white']:
            return articles['wine']['white'][item]['price']
        elif item in articles['wine']['rose']:
            return articles['wine']['rose'][item]['price']
        elif item in articles['cheese']:
            return articles['cheese'][item]
        elif item in articles['accessories']:
            return articles['accessories'][item]
        
    def freebie(self):
        print(self.freebies)
        
        select_freebie = input('What freebie would you like? 1, 2, or 3? ')
        
        while select_freebie not in {'1', '2', '3'}:
            select_freebie = input('Select a valid freebie: 1, 2, or 3? ')
        
        self.cart[self.freebies[int(select_freebie) -1]] = {'price': 0, 'quantity': 1}

articles = {
    'wine':{
        'red':{
            'cabernet': {
                'price': 23,
                'pairing': 'aged gouda',
                'year': 2013
            },
            'pinot noir': {
                'price': 22,
                'pairing': 'brie',
                'year': 2019
            }
        },
        'white':{
            'chardonnay':{
                'price': 10,
                'paring': 'cheddar',
                'year': 2021                
            },
            'sauvignon blanc': {
                'price': 12,
                'paring': 'aged gouda',
                'year': 2022
            }
        },
        'rose':{
            'malbec rose':{
                'price': 13,
                'paring': 'cheddar',
                'year': 2020                
            },
            'pinot grigio rose': {
                'price': 20,
                'paring': 'brie',
                'year': 2018
            }
        }
    },
    'cheese':{
        'aged gouda': 4,
        'brie': 3,
        'cheddar': 2
    },
    'accessories':{
        'wine glasses': 12,
        'wine markers': 5,
        'wine breather': 30
    }
}

wine_shop_freebies = ['wine glass', 'coaster', 'colored lightbulb']

def main():
    
    my_cart = Cart('That Annoying Wine Shop', 'pending', 'open',0, {}, wine_shop_freebies)
    print(f'Welcome to {my_cart.shop_name}!\n')
    while my_cart.shop == 'open':
        action = input('What would you like to do? Add, Delete, View Cart, Pay, Leave: ').lower().strip()

        while action not in {'add', 'delete', 'view cart', 'pay', 'leave'}:
            action = input('Please, select a valid option: Add, Delete, View Cart, Pay, Leave: ').lower().strip()

        if action == 'add':
            my_cart.add()
        elif action == 'delete':
            my_cart.delete()
        elif action in 'view cart':
            my_cart.view_cart()
        elif action == 'pay':
            my_cart.pay()
        elif action == 'leave':           
            my_cart.leave()
            return print(f'\nLet me annoy you again soon!')
        
main()