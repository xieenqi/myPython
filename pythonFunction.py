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
# # global语句被用来声明x是全局的——因此，当我们在函数内把值赋给x的时候，这个变化也反 映在我们在主块中使用x的值的时候。
# def localFunction2():
#     global x
#     print('x是：',x)
#     x=23
#     print('x变成：',x)
#
# x=56
# localFunction2();
# print ('Value of x is', x)

# 函数的默认参数值
def say(message, times=1):
    print(message * times)


say('Hello');
say('World', 5)
