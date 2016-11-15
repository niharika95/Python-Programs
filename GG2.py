import random

name=0;
name=raw_input("What's your name?\n")
print "\nOk",name,", let's play the guessing game! \n"
#Instructions
print "Instructions:"
print "1. The computer generates a random number between 1 to 50."
print "2. While guessing, please select numbers from 1 to 50 only!"
print "3. Your score will be displayed at the end of the game."
print "4. Hit '-1' if you wish to quit!\n\n"

Cnum=random.randint(1,50)
#print ("Cnum : ", Cnum)
points=100;
Unum=0;
c=0;

Unum=eval(raw_input("Make a guess!\n"))

while Unum!=Cnum or points!=0:

	if Unum==-1:
		print "\nDo play again!\n"
		break

	elif Unum==Cnum:
		print "\nCongratulations",name,"! Your score is ",points,"!\n"
		break

	elif Cnum<Unum:
		print "\nTry a lesser number!"
		points=points-5;
		Unum=eval(raw_input("\n"))

	elif Cnum>Unum:
		print "\nTry a greater number!"
		points=points-5;
		Unum=eval(raw_input("\n"))

if points==0:
	print "\nUh-oh! You lost! A correct guess would've been",Cnum,"!\n"

ex=raw_input("Press anything to end.")
end