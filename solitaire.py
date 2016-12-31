import time
import gameBoard

board = gameBoard.get_board(0)
print "Currently, the game board is,"
gameBoard.print_board(board)
print
print "Game start"
turn = int(raw_input("To begin, pick a pile: "))
while not gameBoard.is_empty_pile(board,turn):
	print board[turn][-1],
	card = board[turn].pop()

	print "is picked up from pile " + str(turn)
	gameBoard.print_board(board)
	print

	turn = gameBoard.num_on_card(card)
	time.sleep(.75)

print
print gameBoard.check_board(board)
