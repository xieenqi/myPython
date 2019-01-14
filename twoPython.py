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
