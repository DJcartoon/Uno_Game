from __future__ import annotations
from player import Player
from game_board import GameBoard
from card import CardColor, CardLabel, Card
from random_gen import RandomGen
from config import Config
from data_structures import *
from data_structures.queue_adt import CircularQueue

__author__ = "Divyana (Divi) Ahuja"
class Game:
    """
    Game class to play the game
    """

    def __init__(self) -> None:
        """
        Constructor for the Game class

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity: o(1)
            Worst Case Complexity:o(1)
            since we are just setting the self variables the overall complexity will be o(1)
        """
        self.players = None
        self.current_player = None
        self.current_color = None 
        self.current_label = None
        self.game_board = None


        

    def generate_cards(self) -> ArrayList[Card]:
        """
        Method to generate the cards for the game

        Args:
            None

        Returns:
            ArrayList[Card]: The list of Card objects generated
        """
        list_of_cards: ArrayList[Card] = ArrayList(Config.DECK_SIZE)
        idx: int = 0

        # Generate 4 sets of cards from 0 to 9 for each color
        for color in CardColor:
            if color != CardColor.BLACK:
                # Generate 4 sets of cards from 0 to 9 for each color
                for i in range(10):
                    list_of_cards.insert(idx, Card(color, CardLabel(i)))
                    idx += 1
                    list_of_cards.insert(idx, Card(color, CardLabel(i)))
                    idx += 1

                # Generate 2 of each special card for each color
                for i in range(2):
                    list_of_cards.insert(idx, Card(color, CardLabel.SKIP))
                    idx += 1
                    list_of_cards.insert(idx, Card(color, CardLabel.REVERSE))
                    idx += 1
                    list_of_cards.insert(idx, Card(color, CardLabel.DRAW_TWO))
                    idx += 1
            else:
                # Generate black crazy and draw 4 cards
                for i in range(4):
                    list_of_cards.insert(idx, Card(CardColor.BLACK, CardLabel.CRAZY))
                    idx += 1
                    list_of_cards.insert(
                        idx, Card(CardColor.BLACK, CardLabel.DRAW_FOUR)
                    )
                    idx += 1

                # Randomly shuffle the cards
                RandomGen.random_shuffle(list_of_cards)

                return list_of_cards

    def initialise_game(self, players: ArrayList[Player]) -> None:
        """
        Method to initialise the game

        Args:
            players (ArrayList[Player]): The list of players

        Returns:
            None

        Complexity:
        - n is the number of players 
        -m is the no of cards 
        -k is the no of cards in a players hand 
        
            Best Case Complexity:o(k*n+m*log(m))


            Worst Case Complexity:o(k*n+m*log(m))

            -append waach play to player queue which is o(n)
             - pass the self.generate cards into the game board which is o(m log m) 
             since we are logorithimthically generating cards.
             -then for k the no of cards in a players hand we keep addding these many cards to 
             each player which is o(k*n)
             - drawing a card is o(1)
             - and checking if the frist card is a number card is a constant as 
             even in the worst case complexity all the speacial cards are at the top of the deck
             even so we will not iterate through the whole deck making it a constant complexity
             - futher in the best case the frist card in the deck will be a number card which also 
             makes the complexity o(1)
               since there is only a certain number of speacial cards
            therefore: o(n)+ o(m log m) +o(k*n) +o(1) +o(1) is the finial complexity 
            which simplifies to 

        """
        # setting up players , game board
        self.players = CircularQueue(len(players))

        for player in players:
            self.players.append(player)
            

        self.game_board = GameBoard(self.generate_cards())# o (m log M ) as it only loops M times, where m is the number of cards
        
        
        # while each player not have certain amount of cards in hand 
        for i in range(Config.NUM_CARDS_AT_INIT): # constant complexity o(k*n) runs for a set number of times
            for player in players:
                self.draw_card(player,False)
                                 
      
         # while If the top card is not a number card, 
         # repeat drawing a new one until the top card is a number card. 
                
        draw_card = self.game_board.draw_card() # drawing card from dec 
        while draw_card.label.value > 9:  # complexity: runs a set number of times sine  finding a normal card
            
            self.game_board.discard_card(draw_card) #  discarding the top card 
            draw_card = self.game_board.draw_card()
        
        self.game_board.discard_card(draw_card) 
        self.current_color = draw_card.color
        self.current_label = draw_card.label
        

    def next_player(self) -> Player:
        """
        Method to get the next player

        Args:
            None

        Returns:
            Player: The next player

        Complexity:
            Best Case Complexity: o(1)
            Worst Case Complexity: o(1)

        - if 0 players exist then it will skip the frist if statment which has a complexity of o(1)
        - the peek function is also o(1) complexity since it returns the next item in the list  therefore 
        the overall complexity is o(1)
        """
        if not self.players:
                raise ValueError("no players exisit")
        
        next_player = self.players.peek() # complexity o(1)
        return next_player
                    

    def reverse_players(self) -> None:
        """
        Method to reverse the order of the players

        Args:
            None

        Returns:
            None

        Complexity: 
        -n is the number of players 
            Best Case Complexity: o(n)
            Worst Case Complexity:o(n)

        - at point 1, we push n players in the stack therefore it has a complexity of o(1).
        - at point 2, we append n players into the queue.
        """

        player_store = ArrayStack(len(self.players))

        # pushing the into the draw stack 
        while not self.players.is_empty():#  pushing players in a player storage stack, serving from queue
            player_store.push(self.players.serve())
        
        while not player_store.is_empty():#poping players fro stack back into queue 
            self.players.append(player_store.pop())
        
        
    def skip_next_player(self) -> None:
        """
        Method to skip the next player in the game

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity: o(1)
            Worst Case Complexity:o(1)

            append and serve have a complexity of o(1)
        """
        
        
        next_player = self.players.serve()        
        self.players.append(next_player) # skipping next player 


    def play_draw_two(self) -> None:
        """
        Method to play a draw two card

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity: o(1)
            Worst Case Complexity: o (1)

        the for loop runs for a step number of times, next player has a complexity of o(1)

        """
        
        for i in range(2):
            card_draw = self.game_board.draw_card()
            self.next_player().add_card(card_draw)
        
       

        

    def play_black(self, card: Card) -> None:
        """
        Method to play a crazy card

        Args:
            card (Card): The card to be played

        Returns:
            None

        Complexity:
            Best Case Complexity:o(1)
            Worst Case Complexity:o(1)
            - CardColor(RandomGen.randint(0, 3)) has a complexity of o(1)
            as it returns a number bwteen 0 to 3, the next player getting 4 cards is also o(1) 
            since the overall complexity of the draw_card function is o(1) and next_player 
            function is o(1)
        """
        # Change the game's current color to a random color (excluding black)
        self.current_color = CardColor(RandomGen.randint(0, 3))     
        
        
        # # If the card is a Draw Four card, apply the draw effect and skip the next player
        if card.label == CardLabel.DRAW_FOUR :
            for _ in range(4):
                self.draw_card(self.next_player(),False)
            
            self.skip_next_player()



    def draw_card(self, player: Player, playing: bool) -> Card | None:
        """
        Method to draw a card from the deck

        Args:
            player (Player): The player who is drawing the card
            playing (bool): A boolean indicating if the player is able to play the card

        Returns:
            Card - When drawing a playable card, other return None

        Complexity:
            Best Case Complexity:o(1)
            Worst Case Complexity:o(1)
            - draw a card which has a complexity of 1 if the card is playable 
            it is retuned having a complexity of o(1)
            - else the card is added to the players hand having a complexity of o(1)
        """
        
        drawn_card = self.game_board.draw_card()
        

        if ( drawn_card.color == CardColor.BLACK or drawn_card.color == self.current_color or drawn_card.label == self.current_label) and  playing == True:
            
            # remember to pass the black card through self.play_black when calling this function
            
            return drawn_card
        
        else:
            player.add_card(drawn_card)


    def play_game(self) -> Player:
        """
        Method to play the game

        Args:
            None

        Returns:
            Player: The winner of the game
        """
        
        # starts game intialiseing frist player
        
        self.current_player = self.players.serve()
        self.players.append(self.current_player)
        turn = 0 # number of players played 
        
        while len(self.current_player.hand)  !=0  :# the while loop represents the game, when a player has no cards in hand the loop ends 

            if  turn != 0 :# error occured when placed at the end so only suitable option to iterate through players duing rounds 
                self.current_player = self.players.serve()
                self.players.append(self.current_player)
            turn +=1 


            playable_card = self.current_player.play_card(self.current_color,self.current_label)

            
            if  playable_card is None:# player dosen't have any cards to play pick up CARD
                playable_card = self.draw_card(self.current_player,True) #draw _card 

                
                if playable_card is None  :
                    continue
            
            self.current_color  = playable_card.color # reset current colour and label 
            self.current_label = playable_card.label 
                    

            if playable_card.label <= 9 :# if cards is a number card
            
                self.game_board.discard_card(playable_card)

            elif playable_card.label > 9:#  implementing speacial cards 
                
                if  playable_card.color == CardColor.BLACK:
                    self.play_black(playable_card)

                elif  playable_card.label == CardLabel.DRAW_TWO:
                    self.play_draw_two()
                    
                elif  playable_card.label == CardLabel.REVERSE:
                
                    # after reversing the current player becomes the next frist player 
                    # so we need to skip over the current 

                    self.reverse_players()
                    self.current_player = self.players.serve()
                    self.players.append(self.current_player)
                
                elif  playable_card.label == CardLabel.SKIP:
                    self.skip_next_player()

                else:
                    raise Exception(f"card is playable, but not speacial {playable_card}")
            else:
                raise Exception(f"card playablity failed: {playable_card}")       
        
        
        return  self.current_player
    
        

