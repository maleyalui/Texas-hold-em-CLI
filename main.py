import random   # Used for shuffling the deck randomly


# ---------------- CARD CLASS ----------------
class Card:
    # Represents a single playing card
    def __init__(self, suit, rank):
        self.suit = suit      # Card suit (Hearts, Spades etc.)
        self.rank = rank          # Card value (2–A)

    # Controls how the card prints when displayed
    def __str__(self):
        return f"{self.rank} of {self.suit}"


# ---------------- DECK CLASS ----------------
class Deck:
 
    def __init__(self):

        # All possible suits
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    # All possible ranks
        ranks = ['2', '3', '4', '5', '6', '7', '8',
                 '9', '10', 'J', 'Q', 'K', 'A']

        self.cards = []   # Stores all card objects

    # Create all 52 card combinations
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

# Randomizes the order of cards
    def shuffle(self):
        random.shuffle(self.cards)

# Removes and returns the top card
    def deal(self):
        return self.cards.pop()

# ---------------- PLAYER CLASS ----------------
class Player:

    def __init__(self, name, chips=100):

        self.name = name           # Player name
        self.hand = []             # Stores player's 2 cards
        self.chips = chips         # Starting chips
        self.current_bet = 0       # Tracks round bet
        self.folded = False        # Player fold status

# Adds a card to player's hand
    def add_card(self, card):
        self.hand.append(card)

# Displays player's cards
    def show_hand(self):
        for card in self.hand:
            print(card)

# Resets player for next round
    def clear_hand(self):

        self.hand = []            # Remove old cards
        self.folded = False       # Reset fold state
        self.current_bet = 0      # Reset bet

# ---------------- GAME CLASS ----------------
class Game:

    # Dictionary to convert card ranks into numeric values
    # Makes comparing cards easier
    rank_values = {
    '2':2,'3':3,'4':4,'5':5,'6':6,
    '7':7,'8':8,'9':9,'10':10,
    'J':11,'Q':12,'K':13,'A':14
    }

    # Initializes game state
    def __init__(self):

        self.deck = Deck()                 # Create deck
        self.player = Player("Human")      # Human player
        self.computer = Player("Computer") # AI player
        self.community_cards = []          # Shared table cards
        self.pot = 0                       # Chips to win

    # ----------- DEALING -----------
    def deal_cards(self):

        # Shuffle before dealing
        self.deck.shuffle()

        # Each player gets 2 cards
        for i in range(2):

            self.player.add_card(self.deck.deal())

            self.computer.add_card(self.deck.deal())

    # ----------- COMMUNITY CARDS -----------

    # First 3 community cards
    def flop(self):

        for i in range(3):
            self.community_cards.append(self.deck.deal())

    # Fourth community card
    def turn(self):

        self.community_cards.append(self.deck.deal())

    # Fifth community card
    def river(self):

        self.community_cards.append(self.deck.deal())

    # ----------- DISPLAY -----------

    # Shows community cards on table
    def show_community(self):

        print("\nCommunity Cards:")

        for card in self.community_cards:
            print(card)

    # ----------- BETTING -----------

    # Simple betting system
    def betting_round(self):

        print("\nYour turn:")

        # Get player decision
        choice = input("check / call / fold: ").lower()

        # Player forfeits round
        if choice == "fold":
            self.player.folded = True
            return

        # Fixed bet (simple implementation)
        bet = 10

        # Deduct chips from both players
        self.player.chips -= bet
        self.computer.chips -= bet

        # Add to pot
        self.pot += bet * 2

        print("Both players added 10 chips")

    # ----------- HAND EVALUATION -----------

    # Determines strength of player's hand
    def evaluate_hand(self, player):

        # Combine player cards + community cards
        cards = player.hand + self.community_cards

        values = []

        # Convert ranks into numbers
        for card in cards:
            values.append(self.rank_values[card.rank])

        # Sort values for easier evaluation
        values.sort()

        # Count occurrences of each value
        counts = {}

        for v in values:

            if v in counts:
                counts[v] += 1

            else:
                counts[v] = 1

        # Track hand patterns
        pairs = 0
        three = False

        # Detect pairs and three of a kind
        for v in counts:

            if counts[v] == 2:
                pairs += 1

            if counts[v] == 3:
                three = True

        # Return ranking score
        # (higher number = stronger hand)

        # Three of a kind
        if three:
            return (3,max(values))

        # Two pair
        if pairs == 2:
            return (2,max(values))

        # One pair
        if pairs == 1:
            return (1,max(values))

        # High card
        return (0,max(values))

    # ----------- WINNER -----------

    # Compares player and computer hands
    def determine_winner(self):

        # Computer wins automatically if player folds
        if self.player.folded:
            return self.computer

        # Get hand scores
        p_score = self.evaluate_hand(self.player)
        c_score = self.evaluate_hand(self.computer)

        # Compare scores
        if p_score > c_score:
            return self.player

        if c_score > p_score:
            return self.computer

        # Tie case
        return None

    # ----------- RESET -----------

    # Prepares game for next round
    def reset(self):

        self.deck = Deck()          # New deck

        self.community_cards = []   # Clear table

        # Reset players
        self.player.clear_hand()
        self.computer.clear_hand()

        self.pot = 0                # Reset pot

    # ----------- GAME ROUND -----------

    # Controls one full round of poker
    def play_round(self):

        # Deal player cards
        self.deal_cards()

        print("\nYour Cards:")

        self.player.show_hand()

        # Betting phase
        self.betting_round()

        # Stop round if player folds
        if self.player.folded:
            print("You folded")
            return

        # Flop phase
        self.flop()
        self.show_community()

        # Turn phase
        self.turn()
        self.show_community()

        # River phase
        self.river()
        self.show_community()

        # Decide winner
        winner = self.determine_winner()

        # Handle draw
        if winner == None:

            print("\nDraw!")

            return

        # Winner gets chips
        winner.chips += self.pot

        print("\nWinner is:", winner.name)

        print("Pot was:", self.pot)

        # Show remaining chips
        print("\nChip count:")

        print("You:", self.player.chips)

        print("Computer:",self.computer.chips)

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