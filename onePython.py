# end = input("你想要打印乘法表是:")

# end =9
# col=1
# row=1
# while col<=end:
#     while row<=end:
#         print(str(col) +'x'+str(row)+'='+str(row * col)+"\t"),
#         row+=1
#         print ('')
#         if row>col:
#           col+=1
for i in range(1,10):
    for j in range(1,1+i):
        print('%s*%s=%s' %(i,j,i*j),end=' \t ')
    print()

print(''' wiod fsfndsf 'This' is a multi-line string. This is the first line. This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond." ''')

print('''What\'s your name?''')

print("Newlines are indicated by \n")
print(r"Newlines are indicated by \n")