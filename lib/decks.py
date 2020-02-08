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
        SubClass Face: Stores face cards with their constant value of 10
        SubClass Card: Stores cards with numberical values on the face that
            match the card's score value 
    
    Class Deck: Object containing 52 cards, randomly shuffled with extra
        entropy
        SubClass CardShoe: A multideck (2-8 decks) also fully shuffled
            with extra entropy.

Both classes require Abstract Base Class. The Deck class requires the
random package in addition.
"""

import random as rd
from abc import ABC, abstractmethod, abstractstaticmethod

# Constants:
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
SUITS = ('S', 'D', 'H', 'C')

class AbstractCard(ABC):
    '''
    This class sets up how cards are initialized.

    Methods:
        __init__: puts the rank and suit into the correct attributes, value
            is handled in the subclasses. Valid rank and suit checkes are
            made and will raise ValueError if incorrect. Used by super().
        __str__ : abstractmethod, overridden in subclasses
        __repr__: abstractmethod, overridden in subclasses

    Attributes:
        self.rank: This is the rank of the card. Valid values are found in
            RANKS constant.
        self.suit: This is the card suit (Spades, Diamonds, Hearts, Clubs),
            represented by the first character of the name of the suit.
            Valid values are in SUITS constant.
        self.value: Initialized by subclasses only.
    '''

 