# # 就像Java引用类
# import myModule
#
# myModule.sayhi()
# print('Version', myModule.version)

# from..import  使用from..import语法的版本。
# from myModule import sayhi,version #部分引用
from myModule import *  #全部引用

sayhi()
print('Version', version)