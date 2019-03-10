'''
Program #1
-----------
Write a program to asking user about the number of relationship he/she had.
print "good job" and "Dude" in seperate lines, if its an odd number
or print "you will die single" and "wiredo" in seperate lines, if its an even number
less than or equals 10
or print "go to hell" and "baby" in seperate lines if its an even number 
greater than 10
'''

relationship = int(input("Enter your relationship no: "))

if relationship%2 != 0 : #{
	print("Good Job")
	print("Dude")
	#}
elif relationship%2 == 0 and relationship < 10:
	print("You will die single")
	print("Wirdo")
else :
	print("Go to hell")
	print("Baby")