import random

name=0;
name=raw_input("What's your name?\n")
print "\nOk",name,", let's play Cows n Bulls! \n"
#Instructions
print "Instructions:"
print "1. The computer will generate a random 4 digit number."
print "2. You have to guess what number it is. Choose numbers between 1000 and 9999 only!"
print "3. For every digit which is correct, you get a cow!"
print "4. For every digit which is incorrect, you get a bull!"
print "5. The total number of your cattle will be display at the end!"
print "6. Hit '-1' if you wish to quit!\n\n"

Cnum=str(random.randint(1000,9999))
Unum=0
guess=0
#print ("Cnum : ", Cnum)

while (Unum!=Cnum):
	Unum=str(eval(raw_input("Make a guess!\n")))

	if Unum=="-1":
		break

	guess=guess+1
	i=0
	j=i+4
	cows=0
	bulls=0
	joi=Cnum+Unum

	for i in range(0,4):
		if joi[i]==joi[j]:
			cows=cows+1
		else:
			bulls=bulls+1

		j=j+1

	print "\ncows:",cows, "\nbulls:",bulls,"\n"

if Unum==Cnum:
	print "\nIt took you",guess,"guesses!"
elif Unum=="-1":
	print "\nDo play again! :)"

ex=raw_input("Press anything to end.")
end