import os


#MY CODE
bidders = {}
x = "yes"

while x== "yes":
    x = input("TYPE yes TO ADD MORE BIDEERS OR TYPE no TO END\n")
    if x== "no": 
        break
    else:
        os.system("cls") #used to clear the screen 
        name = input("what is bidders name?:")
        bid = int(input("what is your bid?:"))
        bidders[name] =bid

print(bidders)

highest_bid = 0
winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
for bidder in bidders:
    bid_amount = bidders[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
print(f"The winner is {winner} with a bid of ${highest_bid}")


# MAAMS CODE
# bids = {}
# bidding_finished = False

# def find_highest_bidder(bidding_record):
#   highest_bid = 0
#   winner = ""
#   # bidding_record = {"Angela": 123, "James": 321}
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bid: 
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")

# while not bidding_finished:
#   name = input("What is your name?: ")
#   price = int(input("What is your bid?: $"))
#   bids[name] = price
#   should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#   if should_continue == "no":
#     bidding_finished = True
#     find_highest_bidder(bids)
#   elif should_continue == "yes":
#     os.system("cls")
  