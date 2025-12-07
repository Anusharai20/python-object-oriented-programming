"""
Python Object-Oriented Programming Class Example
"""

class Card:
    # initialize card with value and suit and it is also a constructor    
    def __init__(self, value, suit):
        # attributes assignment
        self.value = value
        self.suit = suit

# function/method to represent the card as a string
    def __repr__(self):
        # string representation of the card
        return f"{self.value} of {self.suit}"


if __name__ == "__main__":
    # create two card objects
    card1 = Card("Ace", "Spades") 
    card2 = Card("Queen", "Hearts")
    card3 = Card("King", "Daimonds")
    card4 = Card("Six", "Spades")

    print(card1)
    print(card2)
    print(card3)
    print(card4)
