from art import logo

print(logo)
bid_dict = {}

any_other_bid = True
while any_other_bid:
    # TODO-1: Ask the user for input
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))

    # TODO-2: Save data into dictionary {name: price}
    bid_dict[name] = price

    # TODO-3: Whether if new bids need to be added
    any_other_bid_input = input("Are there any other bidders? Type 'yes or 'no :")
    if any_other_bid_input.lower() == "no":
        any_other_bid = False

    print("\n \n \n")

print(bid_dict)
# TODO-4: Compare bids in dictionary

winner = ""
max_bid = 0

for name, price in bid_dict.items():
    if price > max_bid:
        max_bid = price
        winner = name

# TODO-5: Print the winner
print(f"The winner is {winner} with a bid of ${max_bid}")


res = max(bid_dict, key=bid_dict.get)
# Using max function to find the key with the maximum value , saying key=bid_dict.get
# means that we are looking for the key with the maximum value in the dictionary bid_dict

print(f"The winner is {res} with a bid of ${bid_dict[res]}")

