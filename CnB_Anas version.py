import random
import re

name = 0;
name = raw_input("What's your name?\n")
print "\nOk",name,", let's play Cows n Bulls! \n"

instructions  =  """
Instructions:
	1. The computer will generate a random 4 digit number.
	2. You have to guess what number it is. Choose numbers between 1000 and 9999 only!
	3. For every digit which is correct, you get a cow!
	4. For every digit which is incorrect, you get a bull!
	5. The total number of your cattle will be display at the end!
	6. Hit '-1' if you wish to quit!
"""

print (instructions)

Cnum = str(random.randint(1000,9999))
Unum = 0
guess = 0
#print ("Cnum : ", Cnum)

while (Unum != Cnum):
	Unum = str(raw_input("Make a guess!\n"))
	
	try:
		re.match(r'^\d{4}$', Unum).group(0)
	except Exception:
		print("Cheater!\n")
		continue

	if Unum == "-1":
		break

	guess = guess + 1
	cows = 0
	bulls = 4
	i = 0

	for char in Unum:
		if char == Cnum[i]:
			cows += 1
			bulls -= 1
		i += 1

	print ("Cows: {0}\nBulls: {1}\n".format(cows, bulls))

if Unum == Cnum:
	print "\nIt took you", guess, "guesses!"
elif Unum == "-1":
	print "\nDo play again! :)"