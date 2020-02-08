"""
Created in this form 04:04 on 02/09/2020.
Copyright (C) 2017, 2019, 2020  Jeffrey L. Scott

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

This is the class library for Deck and Card classes.  There are a number of 
classes in this library:

    Class AbstractCard: Abstract card class
        SubClass Ace: Store aces and their second value
        SubClass FaceCard: Stores face cards with their constant value of 10
        SubClass NumberCard: Stores cards with numberical values on the face
            that match the card's score value 
    
    Class Deck: Object containing 52 cards, randomly shuffled with extra
        entropy
        SubClass CardShoe: A multideck shoe (2-8 decks) also fully shuffled
            with extra entropy.

Both classes require Abstract Base Class. The Deck class requires the
random package in addition.
"""

import random as rd
from abc import ABC, abstractmethod, abstractstaticmethod

class AbstractCard(ABC):
    """
    This class sets up how cards are initialized.

    Methods:
        __init__: Puts the rank and suit into the correct attributes, value
            is handled in the subclasses. Valid rank and suit checkes are
            made and will raise ValueError if incorrect. Subclasses should
            invoke this wits super().
        __str__ : returns string 'rank-suit'. Subclasses invoke with super().
        __repr__: abstractmethod only

    Attributes:
        self.rank: This is the rank of the card. Valid values are found in
            RANKS constant.
        self.suit: This is the card suit (Spades, Diamonds, Hearts, Clubs),
            represented by the first character of the name of the suit.
            Valid values are in SUITS constant.
        self.value: Initialized by subclasses only.
    """
    # Constants:
    RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    SUITS = ('S', 'D', 'H', 'C')
    FACECARDS = ('J', 'Q', 'K')
    NUMBERCARDS = ('2', '3', '4', '5', '6', '7', '8', '9', '10')

    # Methods
    def __init__(self, rank, suit):
        """
        Usage: AbstractCard(rank, suit). This method will validate the rank
        and suit against constants RANKS and SUITS from the class. The
        card's value as part of a hand is left to subclasses. Invoke this
        abstract base class method via super() method.
        INPUTS: two strings, rank and suit
        OUTPUTS: none outside of creating the card object
        """
        if rank not in self.RANKS:
            print(f"AbstractCard: An invalid rank was supplied {rank}.")
            raise ValueError("Card objects must have a valid rank.") from None
            return None

        if suit not in self.SUITS:
            print(f"AbstractCard: An invalid suit was supplied {suit}.")
            raise ValueError("Card objects must have a valid suit.") from None
            return None
        self.rank = rank
        self.suit = suit
        self.value = None

    def __str__(self):
        """
        Returns a three character string '{rank}-{suit}'
        """
        return "{rank}-{suit} ".format(rank=self.rank, suit=self.suit)

    @abstractmethod
    def __repr__(self):
        pass

class Ace(AbstractCard):
    """
    Usage: Ace(suit). This class uses the methods from AbstractCard and
    adds an extra attribute, high_value, to this object. It only requires
    a suit.
    """

    # Methods
    def __init__(self, suit):
        """
        Usage: Ace(suit). This method calls super().__init__() to run
        checks on the suit and set the rank and suit.
        INPUT: one string, suit
        OUTPUTS: none
        """
        super().__init__(rank='A', suit=suit)
        self.value = 1
        self.high_value = 11
    
    def __str__(self):
        """
        Returns a three character string 'A-{suit}'.
        """
        output = super().__str__()
        return output

    def __repr__(self):
        """
        Returns the class call.
        """
        return 'Ace({suit})'.format(suit=self.suit)

class FaceCard(AbstractCard):
    """
    Usage: FaceCard(rank, suit). This class uses the methods from AbstractCard
    without adding any additional attributes.
    """
    # All face cards have a value of 10 in Blackjack.
    CARDVALUE = 10

    # Methods
    def __init__(self, rank, suit):
        """
        Usage: FaceCard(rank, suit). This method calls super().__init__() to
        run checks on the suit and set the rank and suit. It then sets the
        value attribute.
        """
        if rank not in self.FACECARDS:
            print(f"FaceCard: An invalid rank was supplied {rank}.")
            raise ValueError("FaceCard.rank must be J, Q, or K") from None
            return None
        super().__init__(rank=rank, suit=suit)
        self.value = self.CARDVALUE
    
    def __str__(self):
        """
        Returns a three character string '{rank}-{suit}'.
        """
        output = super().__str__()
        return output

    def __repr__(self):
        """
        Returns the class call.
        """
        return 'FaceCard({rank}, {suit})'.format(rank=self.rank, 
                                                   suit=self.suit)

class NumberCard(AbstractCard):
    """
    Usage: NumberCard(rank, suit). This class uses the methods from
    AbstractCard without adding any additional attributes.
    """
    
    # Methods
    def __init__(self, rank, suit):
        """
        Usage: NumberCard(rank, suit). This method calls super().__init__() to
        run checks on the suit and set the rank and suit. It then sets the
        value attribute.
        """
        if rank not in self.NUMBERCARDS:
            print(f"NumberCard: An invalid rank was supplied {rank}.")
            raise ValueError("NumberCard.rank must be an integer") from None
            return None
        super().__init__(rank=rank, suit=suit)
        self.value = int(self.rank)
    
    def __str__(self):
        """
        Returns a three character string '{rank}-{suit}'.
        """
        output = super().__str__()
        return output

    def __repr__(self):
        """
        Returns the class call.
        """
        return 'NumberCard({rank}, {suit})'.format(rank=self.rank, 
                                                   suit=self.suit)
