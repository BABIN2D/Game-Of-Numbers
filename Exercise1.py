# Game Of Numbers.Take input from user to guess a pre defined number(18 in this case) within 5 times.
# else the game is over. Ask the user to try again if they answer wrong and also prompt
# them of the attempts left.
print('The Rules of The Game are as follows,\n1. You have Five lives\n2. Guess a No. Between 1 and 100\n3. If you guess correct you win the game')
num = 18
guess = 5
while guess >0:
    user_input = int(input('Enter a Number between 1 and 100\t'))
    if user_input > 18:
        print('You have guessed wrong, The Number is too high')
        print('You have',guess-1,'Lives left')
        guess-=1
        continue
    elif user_input < 18:
        print('You have guessed wrong, The Number is too low')
        print('You have',guess-1,'Lives left')
        guess-=1
        continue
    else:
        print('!!!You Won!!!')
        break
print('*** GAME OVER ***')
