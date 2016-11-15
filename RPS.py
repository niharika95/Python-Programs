import getpass

name=0;
print "\nLet's play Rock-Paper-Scissors! \n"
#Instructions
print "Instructions:"
print "1. The players have to choose among 'Rock (R || r)', 'Paper (P || p)', 'Scissor (S || s)'"
print "2. Domination:\n Paper > Rock \n Rock > Scissor \n Scissor > Paper"
print "3. The choice made by players will be hidden from user's view."
print "4. The winner is declared at the end of the game."

P1=0
P2=0
game=0

name1=0
name2=0
name1=str(raw_input("\nName of Player 1: "))
name2=str(raw_input("Name of Player 2: "))

print "\n"

for i in range (0,5):
	if P1==3 or P2==3:
		break

	print "Game",(game+1)
	first=str(getpass.getpass("Player 1: "))
	second=str(getpass.getpass("Player 2: "))

	if (first=="r" or first=="R") and (second=="p" or second=="P"):
		P2=P2+1
	elif (first=="p" or first=="P") and (second=="r" or second=="R"):
		P1=P1+1
	elif (first=="r" or first=="R") and (second=="s" or second=="S"):
		P1=P1+1
	elif (first=="s" or first=="S") and (second=="r" or second=="R"):
		P2=P2+1
	elif (first=="s" or first=="S") and (second=="p" or second=="P"):
		P1=P1+1
	elif (first=="p" or first=="P") and (second=="s" or second=="S"):
		P2=P2+1

	print "\n"
	game=game+1

if P1>P2:
	print "The winner is",name1,"!"
elif P2>P1:
	print "The winner is",name2,"!"
elif P1==P2:
	print "The result of the game is a tie between",name1,"and",name2,"!"

print "Do play again! :)"

ex=raw_input("Press anything to end.")
end