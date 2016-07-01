import sys
import click

board = [0] * 9
gameIsWon = False

def display(currentBoard):
	click.clear()
	click.echo((str(currentBoard[0:3])+'\n'+str(currentBoard[3:6])+'\n'+str(currentBoard[6:]))
		.replace("[","|")
		.replace("]","|"))

def getInput(board):
	# Take input
	move = raw_input('Move in form "col,row": ')
	movex = int(move[0])
	movey = int(move[2])
	index = (movex - 1) + (movey - 1) * 3
	# Confirm that it's a legal move
	if board[index] == 0:
		# Update the board list
		board[index] = 1
		return board
	else:
		print "Not a valid move!"
		return getInput(board)

def getAiDecision(board):
	# Get list of possible moves
	spaces = board
	for box in spaces:
		if box != 0:
			box = False
		else:
			box = True
	# if sum of any row == 2
		# go in that row
	# in other cases, you have options -- naive says go where the sum is lowest?

	# Make sure to exclude impossible assignments
	return

def isGameWon(board):
	# Could do this smarter with sums in the array?
	for x in [0,1,2]:
		# Check columns
		if abs(sum([board[x], board[x+3], board[x+6]])) == 3:
			return True
		# Check rows
		elif abs(sum([board[x*3], board[x*3+1], board[x*3+2]])) == 3:
			return True
		# Check diagonals
		elif abs(sum([board[0], board[4], board[8]])) == 3 or abs(sum([board[2], board[4], board[6]])) == 3:
			return True
		else:
			return False

while gameIsWon == False:
	display(board)
	# Player moves
	board = getInput(board)
	# Check if game is won
	gameIsWon = isGameWon(board)
	# Computer moves
	# Check if game is won
	gameIsWon = isGameWon(board)


# Check who won
display(board)
print "Someone won! Game over"
sys.exit()