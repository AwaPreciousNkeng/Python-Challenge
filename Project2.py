from replit import clear

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner is {winner}")
print("Welcome to the auction program.")
while not bidding_finished:
    name = input("What's your name: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders Type 'yes' or 'no'. \n")
    if should_continue.lower() == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue.lower() == 'yes':
        clear()