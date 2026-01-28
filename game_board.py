from __future__ import annotations
from card import Card
from random_gen import RandomGen
from config import Config
from data_structures import *

from data_structures.array_list import ArrayList

__author__ = "Divyana (Divi) Ahuja"

class GameBoard:
    """
    GameBoard class to store cards in draw pile and discard pile
    """

    def __init__(self, cards: ArrayList[Card]):
        """
        Constructor for the GameBoard class

        Args:
            cards (ArrayList[Card]): The list of cards to be used in the game

        Returns:
            None

        Complexity:
        -where n is the number of cards in the deck
            Best Case Complexity:o(n)
            Worst Case Complexity:o(n)
            - push the cards into the stack giving a overal complexity of o(n)

        """
        # intialising piles 
        self.draw_pile = ArrayStack(Config.DECK_SIZE)
        self.discard_pile = ArrayStack(Config.DECK_SIZE)

        # pushing the into the draw stack in reverse so they are in right order when drawing 
        
        for i in range(len(cards)-1,-1,-1):
            
            self.draw_pile.push(cards[i])
            
        
        
        

    def discard_card(self, card: Card) -> None:
        """
        Discards the specified card from the player's hand.

        Args:
            card (Card): The card to be discarded.

        Returns:
            None

        Complexity:
            Best Case Complexity:o(1)
            Worst Case Complexity:o(1)
            - overall complexity is pushing a card which is one at 
            the end of the deck and adding to the length
        """
        
       
        self.discard_pile.push(card)
        


    def reshuffle(self) -> None:
        """
        Reshuffles cards from the discard pile and add them back to the draw pile.

        Args:
            None

        Returns:
            None

        Complexity
        where n is the number of cards in discard pile
            Best Case Complexity: O(NlogN)
            Worst Case Complexity: O(NlogN)
        overall complexity is o(n)+o(n)+O(NlogN) which is o(n) for both worst and case case,
        since we need to pop of the cards from the dec into an array list then shuffle them. 
        shuffleing has a complexity of O(NlogN). Then we reshuffle them back into the dec o(n). 
        Since O(NlogN) is more dominineering  O(NlogN) is the overall complexity
        """
        #intiallising variables and array
        tempArray = ArrayList(len(self.discard_pile))
        cardIndex = 0 

        #removing cards from discard pile into list to shuffle
        
        while not self.discard_pile.is_empty(): # Complxity: o(n):where n is the number of cards in discard pile
            card = self.discard_pile.pop() # stack so can only pop one at a time
            if not (card) :
                raise AttributeError("Card is none")
            
            
            tempArray.append(card) 
            cardIndex +=1
        RandomGen.random_shuffle(tempArray)

        # taking the shuffled list of cards and pushing them into the stack 
        # Complxity: o(n):where n is the number of cards in discard pile
        while cardIndex !=0: 
            cardIndex -=1
            self.draw_pile.push(tempArray.delete_at_index(cardIndex))

    def draw_card(self) -> Card:
        """
        Draws a card from the draw pile.

        Args:
            None

        Returns:
            Card: The card drawn from the draw pile.

        Complexity:
        -where n is the number of cards in the discard pile 
            Best Case Complexity:o(1)
            Worst Case Complexity:O(NlogN)
             
            worst case complexity is if reshuffling is needed,
              whereby having an overal complexity of O(NlogN)
            
            in the best case the drawpile is not empty and we just pop 
            a card from the csard pile which has a complexity of o(1)
        """
        if self.draw_pile.is_empty():
            
            self.reshuffle()
        return self.draw_pile.pop()
