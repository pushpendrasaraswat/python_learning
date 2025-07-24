import random
from art import logo

print(logo)
print("\n\n\n")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
dealer_cards = []

def deal_card(is_user):
    card = random.choice(cards)
    if is_user:
        user_cards.append(card)
    else:
        dealer_cards.append(card)

def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")

while start_game.lower() == "y":
    user_cards.clear()
    dealer_cards.clear()

    for i in range (2):
        deal_card(True)
        deal_card(False)

    print(f"Your cards: {user_cards} , current score: {sum(user_cards)}")
    print(f"YComputer's first card: {dealer_cards[0]}")

    new_input = input("Type 'y' to get another card, type 'n' to pass:")
    while new_input.lower() == "y":
        deal_card(True)
        deal_card(False)
        if sum(user_cards) <= 23 and sum(dealer_cards) <= 23:
            print(f"Your cards: {user_cards} , current score: {sum(user_cards)}")
            print(f"Computer's first card: {dealer_cards[0]}")
        else:
            new_input = "n"
            break;

        new_input = input("Type 'y' to get another card, type 'n' to pass:")

    print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
    print(f"Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
    print(compare(sum(user_cards), sum(dealer_cards)))


    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")

