from art import logo
print(logo)

bids = {}

oneMoreBid = True

def findHiggestBid(bidding_record):
    highestBid = 0
    winner = ""
    for bidder in bidding_record:
        bidAmount = bidding_record[bidder]
        if bidAmount > highestBid:
            highestBid = bidAmount
            winner = bidder
    print(f"The winner is {winner} , they won with a bid of ₹{highestBid}")

while oneMoreBid :
    name = input("What is your name?\n").lower()
    price = int(input("What is your bid? \n ₹"))
    bids[name] = price
    nextBid = input("Any new bidders? Y or N\n").lower()
    if nextBid == "n":
        oneMoreBid = False
        findHiggestBid(bidding_record=bids)
    elif nextBid == "y":
        clear()
    else:
        print("Wrong input please try again")







