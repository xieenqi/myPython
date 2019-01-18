from pip._vendor.distlib.compat import raw_input

coke=0
hen=0
chieck=0
for x in range(0,20+2):
    for y in range(0,34):
        for z in range(0,301,3):
            sum=x*5+3*y+z/3
            count=x+y+z
            zz=z/3
            if sum==100 and count==100:
                print('公鸡：'+str(x)+',母鸡：'+str(y)+'小鸡：'+str(z))

# if else  流程控制
number = 23
guess = int(raw_input('Enter an integer : '))
if guess == number:
    print ('Congratulations, you guessed it.') # New block starts here print "(but you do not win any prizes!)" # New block ends here
elif guess < number:
    print ('No, it is a little higher than that') # Another block # You can do whatever you want in a block ...
else:
    print ('No, it is a little lower than that')
# you must have guess > number to reach here
