# # 函数的运用
# def sayHello():
#     print('Hello World!11111113333333333333')  # block belonging to the function
#
#
# sayHello()  # 调用函数

# # 形参函数的运用
# def printMax(x, y):
#     if (x > y):
#         print('x大于y')
#     else:
#         print('x小于y')
#
# printMax(22, 5);

# # 使用局部变量
# def localFunction(x):
#     print('x是：',x)
#     x=23
#     print('x变成：',x)

# localFunction(56);


# # 使用局部变量global
# # global语句被用来声明x是全局的——因此，当我们在函数内把值赋给x的时候，这个变化也反映在我们在主块中使用x的值的时候。
# def localFunction2():
#     global x
#     print('x是：',x)
#     x=23
#     print('x变成：',x)
#
# x=56
# localFunction2();
# print ('Value of x is', x)

# # 函数的默认参数值
# def say(message, times=10):
#     print(message * times)
#
#
# say('Hello');
# say('World', 5)

# # 函数的关键参数
# def keyParameter(a, b=5, c=67):
#     print('a的值：', a, 'b的值：', b, 'c的值：', c)
#
#
# keyParameter(3, 7)
# keyParameter(3, c=77)
# keyParameter(c=87, a=67)

# return语句  和 DocStrings
def maixMin(a,b):
    '''
    Prints the maximum of two numbers.
    DocStrings : 文档描述
    The two values must be integers.'''
    if a>b:
        return a
    else:
        return b

print('最后的最大值是什么：',maixMin(203,67),maixMin.__doc__)
help(maixMin)