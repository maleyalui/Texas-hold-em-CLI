import random   # Used for shuffling the deck randomly


# ---------------- CARD CLASS ----------------
class Card:
    # Represents a single playing card
    def __init__(self, suit, rank):
        pass      # Card suit (Hearts, Spades etc.)
                  # Card value (2–A)

    # Controls how the card prints when displayed
    def __str__(self):
        return f"{self.rank} of {self.suit}"


# ---------------- DECK CLASS ----------------
class Deck:
    # Represents a full deck of 52 cards
    def __init__(self):

        # All possible suits
        pass

        # All possible ranks
        pass

        pass  # Stores all card objects

        # Create all 52 card combinations
        pass

    # Randomizes the order of cards
    def shuffle(self):
        pass

    # Removes and returns the top card
    def deal(self):
        pass


# ---------------- PLAYER CLASS ----------------
class Player:

    # Represents a game participant (human or computer)
    def __init__(self, name, chips=100):

        pass         # Player name
                     # Stores player's 2 cards
                     # Starting chips
                     # Tracks round bet
                    # Player fold status

    # Adds a card to player's hand
    def add_card(self, card):
        pass

    # Displays player's cards
    def show_hand(self):
        pass

    # Resets player for next round
    def clear_hand(self):

        pass            # Remove old cards
                        # Reset fold state
                        # Reset bet


# ---------------- GAME CLASS ----------------
class Game:

    # Dictionary to convert card ranks into numeric values
    # Makes comparing cards easier
    rank_values = {}

    # Initializes game state
    def __init__(self):

       pass                     # Create deck
                                # Human player
                                # AI player
                                # Shared table cards
                                # Chips to win

    # ----------- DEALING -----------
    def deal_cards(self):

        # Shuffle before dealing
        pass

        # Each player gets 2 cards
        pass

    # ----------- COMMUNITY CARDS -----------

    # First 3 community cards
    def flop(self):

        pass

    # Fourth community card
    def turn(self):

        pass

    # Fifth community card
    def river(self):

        pass

    # ----------- DISPLAY -----------

    # Shows community cards on table
    def show_community(self):
        pass

    # ----------- BETTING -----------

    # Simple betting system
    def betting_round(self):

      pass

        # Get player decision
      

        # Player forfeits round
       

        # Fixed bet (simple implementation)
        

        # Deduct chips from both players
        

        # Add to pot
        

    # ----------- HAND EVALUATION -----------

    # Determines strength of player's hand
    def evaluate_hand(self, player):

        # Combine player cards + community cards
     
        # Convert ranks into numbers
        

        # Sort values for easier evaluation
        

        # Count occurrences of each value
        

        # Track hand patterns
        

        # Detect pairs and three of a kind
       

        # Return ranking score
        # (higher number = stronger hand)

        # Three of a kind
        

        # Two pair
        

        # One pair
       

        # High card
        

    # ----------- WINNER -----------

    # Compares player and computer hands
    def determine_winner(self):

        # Computer wins automatically if player folds
       

        # Get hand scores
       

        # Compare scores
        

        # Tie case
       

    # ----------- RESET -----------

    # Prepares game for next round
    def reset(self):

                               # New deck
                               # Clear table

        # Reset players
       

                      # Reset pot

    # ----------- GAME ROUND -----------

    # Controls one full round of poker
    def play_round(self):

        # Deal player cards
        pass

        # Betting phase
        
        # Stop round if player folds
        

        # Flop phase
        

        # Turn phase
        
        # River phase
       

        # Decide winner
       

        # Handle draw
        

        # Winner gets chips
        

        # Show remaining chips
        


# ---------------- MAIN PROGRAM ----------------

# Create game object
game = Game()

# Game loop
while True:

    # Play one round
    game.play_round()

    # Ask if player wants another round
    again = input("\nPlay again? yes/no: ")

    # Exit condition
    if again.lower() != "yes":
        break

    # Reset game state
    game.reset()