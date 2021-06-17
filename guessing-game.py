# guess a number. If the number is too low or too high, continue to loop
from random import randint

play = "y"

while play == "y":
	rand_num = randint(1, 10)
	low = int(input("Choose a low number:\n"))
	high = int(input("Choose a high number:\n"))
	guess = int(input(f"Guess a number between {low} and {high}\n"))

	while guess != rand_num:
		if guess < rand_num:
			guess = int(input("Too low! Guess again\n"))
		elif guess > rand_num:
			guess = int(input("Too high! Guess again\n"))
	print(f"You got it! The answer was {rand_num}")
	play = input("Would you like to play again? y/n\n")
