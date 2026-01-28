from __future__ import annotations
from card import Card, CardColor, CardLabel
from config import Config
from data_structures import *
from data_structures.array_list import ArrayList

__author__ = "Divyana (Divi) Ahuja"

class Player:
    """
    Player class to store the player details
    """

    def __init__(self, name: str) -> None:
        """
        Constructor for the Player class

        Args:
            name (str): The name of the player
            position (int): The position of the player

        Returns:
            None

        Complexity:
            Best Case Complexity:o(1)
            Worst Case Complexity:o(1)
        """
        self.name = name
        self.hand = ArrayList(Config.DECK_SIZE)

    def add_card(self, card: Card) -> None:
        """
        Method to add a card to the player's hand

        Args:
            card (Card): The card to be added to the player's hand

        Returns:
            None

        Complexity:
            Best Case Complexity:o(1)
            Worst Case Complexity:o(1)
        """
        
        
        self.hand.append(card)

    def is_empty(self) -> bool:
        """
        Method to check if the player's hand is empty

        Args:
            None

        Returns:
            bool: True if the player's hand is empty, False otherwise

        Complexity:
            Best Case Complexity:o(1)
            Worst Case Complexity:o(1)
        """
        return len(self.hand) ==0

    def cards_in_hand(self) -> int:
        """
        Method to check the number of cards left in the player's hand

        Args:
            None

        Returns:
            int: The number of cards left in the player's hand

        Complexity:
            Best Case Complexity:o(1)
            Worst Case Complexity:o(1)
        """
        return len(self.hand)

    def play_card(
        self, current_color: CardColor, current_label: CardLabel
    ) -> Card | None:
        """
        Method to play a card from the player's hand

        Args:
            current_color (CardColor): The current color of the game
            current_label (CardLabel): The current label of the game

        Returns:
            Card: The first card that is playable from the player's hand

        Complexity:
            -n is the number of cards in a players hand 
            Best Case Complexity:o(n)
            Worst Case Complexity:o(n^2)
            - due to insertion sort  function being need  the worst case of insertion sort is o(n^2) 
            and best case is o(1) of this function 
            - iterating through the hand variable has a complexity of o(n)
            therefore for the best case the complexity is o(n)+o(n) which is o(n) overall 
            and for the worst case it is o(n^2) +o(n) which is o(n^2)
        """
        # if the card is 1. same colour 2.same label or 3.black colour it is playable 
       
        playable_cards = ArrayList(Config.DECK_SIZE)

        for i in range(len(self.hand)): #complexity o(n): iterates through all the cards in a player hand which is n 
            if self.hand[i].color == current_color or self.hand[i].label == current_label or self.hand[i].color == CardColor.BLACK:
                playable_cards.append(self.hand[i])

       
        if not playable_cards:# is it empty 
            return None
        
        # Sort by color first, then by label, then play the frist card and remove it from hand
        
        self.insertion_sort(playable_cards)
            # order them by current colour and current lable
        card_to_play = playable_cards[0]
        self.hand.remove(card_to_play)
        return card_to_play
    
    def insertion_sort(self,cards: ArrayList[Card]) -> None:
        """
        Sorts the list of cards in place using Insertion Sort.
        Sorting priority: Least color first, then least label.

        Args:
            cards (list[Card]): List of playable cards.

        Returns:
            None (Sorts in place)
        complexity 
            - n is the number of cards = len(cards)
            worse:o(n^2)

            
            - reversed sort is the worst case whereby 
            the whole dec is in reverse, thereby we need to go once through the list 
            to sort and annother to check if it is sorted 


            best :o(n)


            the function will go through the whole list once to check if the list 
            is sorted. 
        """
        
        for index in range(1, len(cards)):  # Start from the second element
            temp = cards[index]  # Store the card to be inserted
            i = index - 1
            while index-1 >= 0 and (cards[index-1].color > temp.color or 
                            (cards[index -1].color == temp.color and cards[index -1].label > temp.label)):
                cards[index] = cards[index-1]  # Shift the larger card to the right
                index-= 1
            cards[index] = temp  # Place the temp card in its correct position


    def __str__(self) -> str:
        """
        Return a string representation of the player.

        Optional method for debugging.

        """
        return f"Player {self.name}: {', '.join(map(str, self.hand))}"

    def __repr__(self) -> str:
        """
        Method to return the string representation of the player

        Args:
            None

        Returns:
            str: The string representation of the player
        """
        return str(self)
