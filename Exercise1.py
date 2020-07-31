# Game Of Numbers.Take input from user to guess a pre defined number(18 in this case) within 5 times.
# else the game is over. Ask the user to try again if they answer wrong and also prompt
# them of the attempts left.
print('Welcome to the game of choice where you have 5 attempts to guess the correct answer')
choice = input('Do you want to play?\t')
chance = 5
if  choice in ('yes','YES','Y','y'):
    while chance >0:
        num = 18
        guess = int(input('Enter a number'))
        if guess == num:
            print('Congratulation you Entered the right number')
            break
        if guess != num:
            print('Wrong Answer')
            chance-=1
            print('You Have %d Attempts Left'%chance)
            continue
print('GAME OVER')