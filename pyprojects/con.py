guess = input('Enter your Guess')

answer = 42

if guess == answer :
	msg = 'congrats'
elif guess < answer :
	msg = 'low :P'
else:
	msg = 'High'

print msg
