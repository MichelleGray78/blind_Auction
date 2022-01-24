from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

# List to store the bidder info
bidder_info = {}


# Method to add a bidder
def add_Bidder(name, bid):
    bidder_info[name] = bid
    # print(bidder_info)


add_Bidder(name=input("What is your name?: "),
           bid=input("What is your bid?: $"))

# while other bidders = yes, keep calling and adding to the list
other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
while other_bidders == "yes":
    clear()
    add_Bidder(name=input("What is your name?: "),
               bid=input("What is your bid?: "))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if other_bidders == "no":
        # check values for highest value
        highest_value = max(bidder_info, key=bidder_info.get)
        print(f"The highest bidder was: {highest_value} with a bid of {max(bidder_info.values())}")
