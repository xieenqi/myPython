#
# # 使用sys模块
# import sys
#
# print('The command line arguments are--','命令行参数是')
# for i in sys.argv:
#     print(i)
#
# print ('\n\nThe PYTHONPATH is', sys.path, '\n')


# 模块的__name__
if __name__ == '__main__':
    print('This program is being run by itself --- 该程序正在自行运行')
else:
    print("I am being imported from another module --- 我是重另一个模块导入的")
