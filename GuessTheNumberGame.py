import random

max = int(input('What is max number?\n'))
min = int(input('What is min number?\n'))

while min > max :
    print('最小値が最大値以下になるように入力してください')
    max = int(input('What is max number?\n'))
    min = int(input('What is min number?\n'))

for i in range(1, 10):
    randomNumber = random.randint(min, max)

    userAns = int(input('Please enter your answer.'))

    if userAns == randomNumber:
        print("That's correct!")
        break
    else:
        print('Incorrect!:' + str(randomNumber))