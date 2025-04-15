import random
import csv

class Card:
    def __init__(self, face, value):
        self.face = face
        self.value = int(value)

    def __str__(self):
        return self.face


class Deck:
    def __init__(self, filename='deck.csv'):
        self.cards = self.load_deck(filename)

    def load_deck(self, filename):
        cards = []
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for face, value in reader:
                cards.append(Card(face, value))
        return cards

    def draw_card(self):
        return random.choice(self.cards)


class Hand:
    def __init__(self):
        self.cards = []
        self.ace_count = 0

    def add_card(self, card):
        self.cards.append(card)
        if card.value == 11:
            self.ace_count += 1

    def total(self):
        total = sum(card.value for card in self.cards)
        while total > 21 and self.ace_count:
            total -= 10
            self.ace_count -= 1
        return total

    def is_bust(self):
        return self.total() > 21

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)


class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.balance = 0

    def play_round(self, bet):
        player_hand = Hand()
        dealer_hand = Hand()

        for _ in range(2):
            player_hand.add_card(self.deck.draw_card())
        dealer_card = self.deck.draw_card()
        dealer_hand.add_card(dealer_card)

        print(f"\nYour hand: {player_hand} (Total: {player_hand.total()})")
        print(f"Dealer shows: {dealer_card}")

        while player_hand.total() < 21:
            choice = input("Hit or Stand? [H/S]: ").lower()
            if choice == 's':
                break
            elif choice == 'h':
                new_card = self.deck.draw_card()
                player_hand.add_card(new_card)
                print(f"You drew: {new_card} (Total: {player_hand.total()})")
                if player_hand.is_bust():
                    break
            else:
                print("Invalid choice.")

        while dealer_hand.total() < 17:
            dealer_hand.add_card(self.deck.draw_card())

        print(f"\nFinal hands:")
        print(f"Your hand: {player_hand} (Total: {player_hand.total()})")
        print(f"Dealer's hand: {dealer_hand} (Total: {dealer_hand.total()})")

        if player_hand.is_bust():
            print(f"You busted! You lose ${bet}.")
            self.balance -= bet
        elif dealer_hand.is_bust() or player_hand.total() > dealer_hand.total():
            print(f"You win! You earn ${bet}.")
            self.balance += bet
        elif player_hand.total() < dealer_hand.total():
            print(f"You lose ${bet}.")
            self.balance -= bet
        else:
            print("Push! No money lost or won.")

    def run(self):
        print("Welcome to Blackjack Simulator!\n")
        try:
            bet = float(input("Enter your bet per round: $"))
            rounds = int(input("How many rounds would you like to play? "))
        except ValueError:
            print("Invalid input.")
            return

        for i in range(1, rounds + 1):
            print(f"\n=== Round {i} ===")
            self.play_round(bet)

        print("\n=== Game Over ===")
        if self.balance > 0:
            print(f"Net win: ${self.balance}")
        elif self.balance < 0:
            print(f"Net loss: ${-self.balance}")
        else:
            print("You broke even.")


if __name__ == "__main__":
    game = BlackjackGame()
    game.run()
