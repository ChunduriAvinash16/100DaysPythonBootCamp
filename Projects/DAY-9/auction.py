from art import logo

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        amount = bidding_record[bidder]
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

print(logo)
print("Welcome to the secret auction program.")
bid={}

any_bidders_further = True
while any_bidders_further:
    name = input("What is your name?:")
    bid_amount = int(input("What's your bid?: $"))
    bid[name]=bid_amount
    any_bidders = input("Are there any other bidders?Type 'yes' or 'no'.\n")
    if any_bidders == 'yes':
        any_bidders_further = True
    else:
        any_bidders_further = False
        find_highest_bidder(bid)
