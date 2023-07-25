shop_name = 'That Annoying Wine Shop'
payment = 'pending'
shop = 'open'
welcome = f'Welcome to {shop_name}!'
total_cart = 0
cart = {}

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

freebies = ['wine glass', 'coaster', 'colored lightbulb']

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
                
def view_cart():
    if cart == {}:
        print('\nYour shopping cart is empty. Time to put some wine there :)\n')
    else:
        print('\n(Qty) Item - Price\n')
        for key,value in cart.items():
            qty = int(cart[key].get('quantity'))
            art_price = int(cart[key].get('price'))
            print(f"({qty}) {key.title()} - ${art_price}\n\tTotal: ${art_price * qty}\n")
        total()
        
def total():
    global total_cart
    sum = 0
    for key, value in cart.items():
        sum += cart[key]['price'] * int(cart[key]['quantity'])
    total_cart = sum
    print(f"\nYour total is: ${total_cart:.2f}")
    
def find_price(add_art):
    if add_art in articles['wine']['red']:
        return articles['wine']['red'][add_art]['price']
    elif add_art in articles['wine']['white']:
        return articles['wine']['white'][add_art]['price']
    elif add_art in articles['wine']['rose']:
        return articles['wine']['rose'][add_art]['price']
    elif add_art in articles['cheese']:
        return articles['cheese'][add_art]
    elif add_art in articles['accessories']:
        return articles['accessories'][add_art]
    
def freebie():
    print(freebies)
    
    select_freebie = input('What freebie would you like? 1, 2, or 3? ')
    
    while select_freebie not in {'1', '2', '3'}:
        select_freebie = input('Select a valid freebie: 1, 2, or 3? ')
    
    cart[freebies[int(select_freebie) -1]] = {'price': 0, 'quantity': 1}

def add():
    while True:
        display_articles()
        
        add_art = input('What article would you like to add? ').lower().strip()
#         PENDING Need to validate entry but code below is not working yet
#         PENDING while add_art not in {display_articles()}:
#         PENDING    add_art = input('Select a valid article from the list').title().strip()


# PENDING if article already in cart, add to quantity

        if add_art in {'wine', 'red', 'white', 'rose'}:
            display_wines()
            add_art = input('\nWhat wine would you like to buy? ').lower().strip()
        elif add_art == 'cheese':
            display_article('cheese')
            add_art = input('\nWhat type of cheese would you like to buy? ').lower().strip()
        elif add_art == 'accessories':
            display_article('accessories')
            add_art = input('\nWhat accessory would you like to buy? ').lower().strip()
            
        add_art_num = input('How many articles would you like to add to your cart? Enter a number: ').strip()

#         while not add_art_num.isdigit():
#             add_art_num = int(input('Enter a valid number: ').strip())
            
        # PENDING add_art_num needs a validation for numbers only
        
        print("If you add two more, I'll throw in a random freebie for you!")
        add_art_more = input('add two more article y/n? ').lower().strip()
        if add_art_more == 'y':
            add_art_num = int(add_art_num) + 2
            freebie()

        # append to the cart
        cart[add_art] = {'quantity': add_art_num, 'price': find_price(add_art)}
    
        view_cart()
        
        add_art_cont = input('Would you like to add more articles to your cart? y/n: ').lower().strip()
        
        while add_art_cont not in {'y', 'n'}:
            add_art_cont = input('select a valid option. add more articles? y/n: ').lower().strip()
            
        if add_art_cont == 'n':
            break

def delete():

    if cart == {}:
        print('\nYour shopping cart is empty. Time to put some wine there :)')
    else:
        view_cart()

        del_art = input('What article would you like to delete? ')

        while del_art not in cart:
               del_art = input('Enter an article in your cart: ')

        del_art_num = input('How many would you like to delete? ')
        del_conf = input("are you sure you'd like to delete this many articles from your shopping cart? y/n ")

        if int(cart[del_art]['quantity']) - int(del_art_num) == 0:
            del cart[del_art]
            return print(f"You've deleted {del_art} from your cart")
        else:
            cart[del_art]['quantity'] = int(cart[del_art]['quantity']) - int(del_art_num)
        view_cart()


def pay():
    print('Your cart:\n')
    view_cart()
    total() 
    
    while True:
        method_of_payment = input('Method of payment - credit card, apple pay, or cash? ')
        if method_of_payment == 'credit card' or method_of_payment == 'apple pay':
            all_set()
            break    
        elif method_of_payment == 'cash':

                cash = input('Enter the amount of cash: ')
                if int(cash) == total_cart:
                    return all_set()
                elif int(cash) > total_cart:
                    print(f'\nThank you for the tip!\n')
                    return all_set()
                else: 
                    print("\nThat's not enough cash.")

def all_set():
    print('You are all set. Thank you for shopping at That Annoying Wine Shop\n')
    print('Here is your Annoying Receipt:')
    view_cart()
    global shop
    shop = 'closed'

def leave():

    if cart == {}:
        print(f'Thank you for coming to {shop_name}. I hope I can annoy you more soon!')
        shop == 'closed'
    else:   
        if payment == 'done':
            all_set()
        else:
            print('\nRemember to pay :)\n')
            pay()

def main():
    print(f'{welcome}\n')
    
    while shop == 'open':
        action = input('What would you like to do? Add, Delete, View Cart, Pay, Leave: ').lower().strip()

        while action not in {'add', 'delete', 'view cart', 'pay', 'leave'}:
            action = input('Please, select a valid option: Add, Delete, View Cart, Pay, Leave: ').lower().strip()

        if action == 'add':
            add()
        elif action == 'delete':
            delete()
        elif action in 'view cart':
            view_cart()
        elif action == 'pay':
            pay()
        elif action == 'leave':           
            leave()
            cart = {}
            return print(f'\nLet me annoy you again soon!')
        
main()