from pip._vendor.distlib.compat import raw_input

# 猜数字 while循环
number = 23
running = True
while running:
    guess = int(raw_input('Enter an integer : '))
    if guess == number:
        print('Congratulations, you guessed it.')
        running = False  # this causes the while loop to stop
    elif guess < number:
        print('No, it is a little higher than that')
    else:
        print('No, it is a little lower than that')
else:
    print('The while loop is over.')
# Do anything else you want to do here
print('Done')

# 使用break语句
while True:
    s = raw_input('Enter something')
    if s == 'quit':
        break
    print('''Length of the string's''', len(s))
print('Done')

# 使用continue语句
while True:
    s = raw_input('Enter somthing')
    if s == 'quit':
        break
    if len(s) < 5:
        continue
    print('Input is of sufficient length')
