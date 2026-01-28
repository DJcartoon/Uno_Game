from __future__ import annotations
from enum import auto, IntEnum
from config import Config
from data_structures import *

__author__ = "Divyana (Divi) Ahuja"
class CardColor(IntEnum):
    """
    Enum class for the color of the card
    """

    RED = 0
    BLUE = auto()
    GREEN = auto()
    YELLOW = auto()
    BLACK = auto()
    '''
    def __str__(self) -> str:
        """
        Method to return the string representation of the CardColor

        Args:
            None

        Returns:
            str: The string representation of the CardColor
        """
        pass

    '''
class CardLabel(IntEnum):
    """
    Enum class for the value of the card
    """

    ZERO = 0
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    SKIP = auto()
    REVERSE = auto()
    DRAW_TWO = auto()
    CRAZY = auto()
    DRAW_FOUR = auto()
    '''
    def __str__(self) -> str:
        """
        Method to return the string representation of the CardLabel

        Args:
            None

        Returns:
            str: The string representation of the CardLabel
        """
        pass
        '''

class Card:
    def __init__(self, color: CardColor, label: CardLabel) -> None:
        """
        Initialize the card with the given color and value.

        Args:
            color (CardColor): The color of the card.
            value (CardValue): The value of the card.

        Returns:
            None

        Complexity:
            Best Case:o(1)
            Worst Case:o(1)
        """
        self.color = color
        self.label = label
    
    def __str__(self) -> str:
        """
        Return a string representation of the card.

        Optional method for debugging.
        """
        return f'colour:{self.color}, label:{self.label}'
    

    def __repr__(self) -> str:
        """
        Method to return the string representation of the Card

        Args:
            None

        Returns:
            str: The string representation of the Card
        """
        return str(self)

    def __eq__(self, other: Card) -> bool:
        """
        Check if this card is equal to another card.

        Args:
            other (Card): The other card to compare to.

        Returns:
            bool: True if this card is equal to the other card, False otherwise.
        """
        return self.color == other.color and self.label == other.label
