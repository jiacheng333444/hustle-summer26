

# ============================================================
# LAB 7  -  MY OWN ORDERING APP
# Week 7  -  Hack the Hood
# ============================================================
# Name: Jia Cheng Ouyang
#
# This is YOUR app. YOU write the code.
# Do the tickets IN ORDER from the Lab 7 sheet.
# Run this file after EVERY ticket to check your work.
#
# My store sells: Figurines
# ============================================================


# ============================================================
# DAY 1  -  BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint
#   A class for your item. Every item has a name and a price.
#   Write your class below.

class Figurine:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def set_price(self, price):
        if price >= 1:
            set_price = price 
        else:
            print("Item price not valid!")
    
    def display_action(self):
        print(f"{self.name} is a figurine!")
    def display(self):
        print(f"{self.name} - ${self.price}")
    


# TICKET 2: Make your real items
#   Make 2 or 3 real items with YOUR OWN names and prices.
#   PREDICT what print(item1.name) shows: ______________

item1 = Figurine("Hatsune-Miku", 50)
item2 = Figurine("Kasane-Teto", 60)
item3 = Figurine("Akita-Neru", 40)
item4 = Figurine("Megurine-Luka", 70)

print(item1.name)
# I think it will print Hatsune-Miku

# TICKET 3: The price guard
#   Add a set_price method INSIDE your class above.
#   It should say no to a price below zero.
#   BREAK ON PURPOSE: after you build it, try item1.set_price(-5)
#   PREDICT what happens: _______it will say "Item Price Not Valid!"_______
#   Paste the message you see here: _____jia@Jias-MacBook-Neo hustle-summer2026 % python3 lab7_jia.py
#Hatsune-Miku
#Item price not valid!_________
item1.set_price(-5)


# TICKET 4: A second kind of item
#   A new class that copies (inherits from) your first class.
#   Write it below.

class AnimeFigurine(Figurine):
    def display_action(self):
        print(f"{self.name} is gathering dust. Go wipe it off!")

class RamenFigurine(Figurine):
    def display_action(self):
        print(f"{self.name} needs to be put on top of cup ramen!")




# TICKET 5: Each item's own action
#   Give each class its own method (deliver, serve, play...).
#   Same method name, different message.
#   EXPLAIN why the same name can do two things: __________I think it can use the same method name but it executes their own message depedning on which object calls it.____





# ============================================================
# DAY 2  -  BUILD YOUR STORE
# ============================================================

# TICKET 6: My cart
#   A class that holds items in a list and can check out.
#   Write your Cart class below.

class Cart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item.name} to the cart!")
    
    def checkout(self):
        if not self.items:
            print("Your cart is empty!")
        
        print("--- Checkout ---")
        total = 0
        for item in self.items:
            item.display()
            total += item.price

        print(f"Total Price: ${total}")
        print("Thank you For Your Purchase!")





    
    

# TICKET 7: My menu and my cart
#   A dictionary that gives each item a number, and one empty cart.

store = {
    1: item1,
    2: item2,
    3: item3,
    4: item4,
}

my_cart = Cart()


# TICKET 8: Let customers shop
#   Use input() and a loop to keep adding picks until "done".
#   PREDICT what happens when you pick 1: ______i think i need to use int and will give me error________
while True:
    choice = input("Enter the item number you want to buy (or type 'done' to finish!):")

    if choice.lower() == "done":
        break
    
    try:
        item_number = int(choice)

        if item_number in store:
            selected_item = store[item_number]
            my_cart.add_item(selected_item)
        else:
            print("That item number isn't in stock!")

    except ValueError:
            print("Please enter a valid number or 'done'!")
    
    
        
        

# TICKET 9: Checkout  (add this method INSIDE your Cart class)
#   Deliver every item and add up the total.

my_cart.checkout()

# TICKET 10: Test the whole app
#   Run it start to finish. PREDICT the full output first,
#   then check it against what really prints.

# I think my code will run fine, ask you what you want, add it, write done, then will checkout 


# ============================================================
# CHALLENGE: add a THIRD kind of item, or your own feature!
# ============================================================
i added 2 more figures and the checkout title thing
