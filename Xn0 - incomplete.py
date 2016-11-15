name=0;
print "\nLet's play X n 0! \n"
#Instructions
instructions = """
Instructions:
  1. The computer will generate a random 4 digit number.
  2. You have to guess what number it is. Choose numbers between 1000 and 9999 only!
  3. For every digit which is correct, you get a cow!
  4. For every digit which is incorrect, you get a bull!
  5. The total number of your cattle will be display at the end!
  6. Hit '-1' if you wish to quit!\n
"""

print (instructions)

name1=0
name2=0
name1=str(raw_input("Name of Player 1: "))
name2=str(raw_input("Name of Player 2: "))

for i in range(0,3):
	for j in range(0,3):
		print ('0',end="")
	print "\n"

print board
"""
	first_row=str(raw_input("Player 1 row: "))
	first_col=str(raw_input("Player 1 col: "))
	
	board[first_row,first_col]

	second_row=str(raw_input("Player 2 row: "))
	second_col=str(raw_input("Player 2 col: "))

	board[second_row,second_col]
	"""