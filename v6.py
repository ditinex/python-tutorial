'''
Program #2
-----------
Check whether given year is a leap year or not
'''

year = int(input("Enter year : "))

if year%4 == 0:
	if year%100 == 0:
		if year%400 == 0:
			print("{} is a leap year.".format(year))
		else:
			print(str(year) + " is a not leap year.")
	else:
		print("%d is a leap year." % (year))
else:
	print(year,"not a leap year.")

'''
s – strings
d – decimal integers (base-10)
f – floating point display
c – character
b – binary
o – octal
x – hexadecimal with lowercase letters after 9
X – hexadecimal with uppercase letters after 9
e – exponent notation
'''