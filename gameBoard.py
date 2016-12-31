import itertools
import random


suits = ['C','H','S','D']
nums = ['0','1','2','3','4','5','6','7','8','9','J','Q','K']

inputdata = [suits,nums]

def get_board(s):
	cards = list(itertools.product(*inputdata))
	for i in range(len(cards)):
		cards[i] = cards[i][0]+cards[i][1]

	random.seed(s)
	random.shuffle(cards)
	
	# Construct game board as described in the instructions.
        
        board = []               # Create a board list
        
        # For each of the 13 piles, crate a list: 
              # 1. append the current last card in cards list - try using the pop()
              #    function without an argument to get the last card in a list AND
              #    remove it from the list simultaneously!
              # 2. once the pile has 4 cards in it, append it to the board list.
        pile = []
        while len(cards) > 0: 
              pile.append(cards.pop())
              if len(pile) == 4: 
                   board.append(pile)
                   pile = []

        # Once all 13 piles are complete, the cards list should have length 0
        if not cards: 
                print ("Operations are done!")
        
		
	return board

def check_board(board):
	# Count the total number of cards on the board.
	# If there are no remaining cards on the board, return win message
	# If not, return loss message with number of cards left
	total = 0
        win = 'You win!'
        loss = 'You lost - only %d cards were left!'
        for i in range(len(board)):
                total += len(board[i])
        if total == 0: 
                return win
        else: 
                return (loss %(total))                


def print_board(board):
	print "*************************************** Top"
	# Fill in this part to achieve the exactly same output to the sample output
        # For each possible pile position, starting at the end and going to the begining:
        #     1. For each pile in the board: 
        #         1. Is this pile long enough to have this position? If not, print two space 
        #         2. If this pile IS long enough, print the card at that position
        #     2. Once you've printed all the cards at that position in the pile, start a new line
        
        for j in range(4): 
             for i in range(len(board)):
                     print board[i].pop(), 
                     if i == 12: 
                         print "   \n"
             
        print "*************************************** Bottom"
	print "00 01 02 03 04 05 06 07 08 09 10 11 12  Pile"

def is_empty_pile(board, i):
	# Check if the pile (on the board) indexed by i is empty.
	# If that pile is empty, return True.
	# If not, return False.
        for i in range(len(board)):
                if len(board[i]) == 0: 
                   return 1
                else: 
                   return 0 
		
def num_on_card(card):
	# See the number on card.
	# It it is a number N, return int(N)
	# If it is 'J', return 10
	# If it is 'Q', return 11
	# If it is 'K', return 12
        for i in len(card):
                if card[1] == 'J':
                   return 10
                elif card[1] == 'Q':
                   return 11
                elif card[1] == 'K':
                   return 12
                else: 
                   return int(card[1])
