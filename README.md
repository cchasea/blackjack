# Blackjack Simulator (Python)

A simple command-line Blackjack simulator written in Python.

## Features
-Interactive text-based game
-Simulates a real Blackjack deck using values from 'deck.csv'
-Handles player options 'Hit' and 'Stand'
-Dynamic Ace (1 or 11)
-Bet tracking and Net gain/loss tracker
-Run multiple hands 
-Uses object orienteted programming

## Example Run
Welcome to Blackjack Simulator!


Enter your bet per round: $100

How many rounds would you like to play? 2


=== Round 1 ===

Your hand: 9, K (Total: 19)

Dealer shows: 7

Hit or Stand? [H/S]: s


Final hands:

Your hand: 9, K (Total: 19)

Dealer's hand: 7, 2, 5, 10 (Total: 24)

You win! You earn $100.0.


=== Round 2 ===

Your hand: 8, 2 (Total: 10)

Dealer shows: 9

Hit or Stand? [H/S]: h

You drew: 2 (Total: 12)

Hit or Stand? [H/S]: h

You drew: Q (Total: 22)


Final hands:

Your hand: 8, 2, 2, Q (Total: 22)

Dealer's hand: 9, 5, Q (Total: 24)

You busted! You lose $100.0.


=== Game Over ===

You broke even.

## Future Improvements 
-Add support for splitting and double down.
-Gui
-Deck without csv
-Automatic simulation with different playstyles

## Open source and free to use

## Made with Python by Cameron Arruda
