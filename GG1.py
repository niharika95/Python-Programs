import random

print "Let's play! \n \n"

Cnum=random.randint(1,10)

for i in range (1,5):
	Unum=eval(raw_input("Guess a number between 1 to 10! \n \n"))
	#print ("Unum: ", Unum)
	#print ("Cnum : ", Cnum)
	if Unum==Cnum:
		print "Congratulations!"
		break

	elif Unum<Cnum or Unum>Cnum:
		if i<4:
			print "Try again!"

		elif i==4:
			print "\n\nUh oh! You lost!"
			break