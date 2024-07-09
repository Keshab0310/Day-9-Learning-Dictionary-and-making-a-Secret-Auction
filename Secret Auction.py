import os #This import is used to import clear function.
from art import logo
print(logo) #Here I had uploded art file and imported the logo and print it on the console.

bids = {} #Here I am creating the dictionary.
bidding_finished = False

def find_highest_bidder (bidding_record): #This function finds the highest bidder from the dictionary.
    highest_bid = 0 # We are declaring the higgest bid as 0  because it is the minimum bid.
    winner = "" # Simillarly the winner as empty string to replace it as per the highest bidder.
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
            
while not bidding_finished:
    name = input("What is your Name?: ")
    price = int(input("What is your bidding price?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system("cls")
    else:
        exit()
    