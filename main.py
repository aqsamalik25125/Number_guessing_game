# using while loop to keep the program running forever
while True :
	# importing random library
	import random
	# telling the library it's range of numbers
	number = random.randint(1,20)
	# taking the user's guess
	guess = int(input('Enter your guess:'))
	# defining the conditions
	if guess == number :
		print('Congratulations!, You won!')
	else:
		print('Try Again!')