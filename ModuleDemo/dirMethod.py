import sys
dir(sys)
dir()
# 列表 list
shoplist = ['apple', 'mango', 'carrot', 'banana']
print ('I have', len(shoplist),'items to purchase.')
shoplist.sort()#列表的sort方法来对列表排序。
print ('Sorted shopping list is', '遍历过后',shoplist)

shoplist.append("我加入购物车是")
print ('The first item I will buy is','数组的第一项', '\'',shoplist[0],'\'')
olditem = shoplist[0]
del shoplist[0]
print ('I bought the','我买了什么，我选择了什么', olditem)
print ('My shopping list is now','现在list有那些了', shoplist)

# 使用元组
zoo=('wolf','elephan','penguin')
print('number of animalsin the zoo is :',len(zoo))
new_zoo=('monkey','dolphin',zoo)
print('number of animalsin the new_zoo is:',len(new_zoo))
print('all animalsion in new_zoo:',new_zoo)
