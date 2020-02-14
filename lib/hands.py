"""
Created on Mon Feb 10 10:13:40 2020

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

This is the class library for Hands. It requires Card objects that each Hand
type will store. Decks normally store Cards objects before being dealt, but
dealing cards is not included in these classes. Those methods are part of
Table classes.

The classes in this library are:

    Class AbstractHand: Abstract hand class.
        Subclass RegHand: stores cards that form a player's staring blackjack
            hand and bets on the hand.
        Subclass SplitHand: stores and models cards for a player's hands after
            a pair from the original hand has been split into two hands.
        Subclass DealerHand: stores and models cards for the dealer's hand.
"""
from decks import Ace
from decks import FaceCard as FC
from decks import NumberCard as NC


class AbstractHand(list, ABC):
    """
    AbstractHand(ante, **kwrds):

    This sets up the principal methods that the three subclasses need to
    perform their operations.  The hand is a list and inherits all of the list
    methods to make handling Card objects easier. It also has extra attributes
    to store data about the hand.

    Methods
    -------
        __init__: Creates an empty hand. Initializes all integer attributes to
            zero. All boolean attributes are intialized to False.
            Note: bet is not an attibute of this class, as Dealers do not need
            to track bets on their hands. Bet calculations be handled by
            player Hand subclasses instead.
            Note: blackjack is not handled either, as it is does not apply to
                split hands. It only applies to the dealer's hand or the
                player first hand.
            Note: Pairs are only handled in RegularHand since it only applies
                to the type of hand.
        __str__: Prints of user friendly version of the cards in the hand,
            using the Card.__str__() method.
        __Len__: inherited from list
        __repr__: inherited from list
        receive_card: adds a Card object to the hand, updating attributes as
            needed
        print_score: prints out the actual score of the hand, accounting for
            aces

    Attributes
    ==========
        score: integer, score of the hand without accounting for aces.
        has_ace: boolean, starts False, True if an ace was received by
            receive_card().
        busted: boolean, starts False, True if all possible scores for the
            hand are over 21.
    """

    def __init__(self, **kwrds):
        """
        AbstractHand()

        Parameters
        ----------
        **kwrds : None, but this is a placeholder in case we need to pass
            keyward arguments around.

        Returns
        -------
        Empty Hand object with 0 score and False has_ace and busted attributes
        """
        self.score = 0
        self.has_ace = False
        self.busted = False
        return self

    def __str__(self):
        """
        Print the contents of the hand.

        Returns
        -------
        String: output of the contents and score of the hand.
        """
        if len(self) == 0:
            output = "Empty hand"
        else:
            output = "Hand contains: "
            output = output.join([print(card, end=' ') for card in self])
        output = output.join(['\n', "Hand score is: {self.print_score()}\n"])
        return output

    def receive_card(self, card):
        """
        Add a Card to the Hand and update all attributes appropriately.

        Parameters
        ----------
        card : Card object of type Ace, NumberCard, or FaceCard. These types
            are loaded Ace, NC, or FC.

        Returns
        -------
        None.

        """
        # Add the new card to the hand.
        self.append(card)
        if type(card) == Ace:
            self.has_ace = True
        self.score += card.value
        if self.print_score() > 21:
            self.busted = True

    def print_score(self):
        """
        Return the "best" score for this hand.

        Returns
        -------
        Integer: returns self.score unless an Ace is in the hand

        """
        high_score = self.score + 10
        if self.has_ace and high_score < 21:
            return high_score
        else:
            return self.score
