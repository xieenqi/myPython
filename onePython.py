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
for i in range(1, 10):
    for j in range(1, 1 + i):
        print('%s*%s=%s' % (i, j, i * j), end=' \t ')
    print()

print(''' wiod fsfndsf 'This' is a multi-line string. This is the first line. This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond." ''')

print('''What\'s your name?''')

print("Newlines are indicated by \n")
print(r"Newlines are indicated by \n")
# 计算表达
print(2 + 3)
print('幂:',2 ** 5)
print('取整除:', 60 // 7)
print('左移:', 2 << 2,'(2 << 2得到8。——2按比特表示为10)',)
print('右移:', 11 >> 1,'(11 >> 1得到5。——11按比特表示为 1011，向右移动1比特后得到101，即十 进制的5。)',)


length = 5
breadth = 2
area = length * breadth
print ('Area is', area)
print ('Perimeter is', 2 * (length + breadth))