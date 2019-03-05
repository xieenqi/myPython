import sys

dir(sys)
dir()
# 列表 list
shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(shoplist), 'items to purchase.')
shoplist.sort()  # 列表的sort方法来对列表排序。
print('Sorted shopping list is', '遍历过后', shoplist)

shoplist.append("我加入购物车是")
print('The first item I will buy is', '数组的第一项', '\'', shoplist[0], '\'')
olditem = shoplist[0]
del shoplist[0]
print('I bought the', '我买了什么，我选择了什么', olditem)
print('My shopping list is now', '现在list有那些了', shoplist)

# 使用元组
zoo = ('wolf', 'elephan', 'penguin')
print('number of animalsin the zoo is :', len(zoo))
new_zoo = ('monkey', 'dolphin', zoo)
print('number of animalsin the new_zoo is:', len(new_zoo))
print('all animalsion in new_zoo:', new_zoo)

# 元组与打印语句  打印替代
age = 22
name = 'Swaroop'
print('%s is %d years old' % (name, age))
print('Why is %s playing with that python?' % name)

# 使用字典
db = {'Swaroop': 'swaroopch@byteofpython.info', 'Larry': 'larry@wall.org',
      'Matsumoto': 'matz@ruby-lang.org',
      'Spammer': 'spammer@hotmail.com'}
print('Swaroop的值----', db['Swaroop'])
# Adding a key/value pair增加一个key  value
db['Guido'] = 'guido@python.org'
# Deleting a key/value pair 删除键/值对
del db['Spammer']
print('\nthere are %f contacts in the address \n' % len(db))
for name, address in db.items():
    print('Contact %s at %s ' % (name, address))
if 'Matsumoto' in db:
    print('\n Matsumoto sadress is %s' % db['Matsumoto'])
else:
    print("不在其中》》》》》》》》》。")

# 使用序列
shoplist = ['物品1', '物品2', '物品3', '物品4', '物品5', '物品4', '物品6', '物品47']
# 索引或“订阅”操作
print('第一个item是：', shoplist[0])
print('第2个item是：', shoplist[1])
print('第3个item是：', shoplist[2])
print('第4个item是：', shoplist[3])
print('第-1个item是：', shoplist[-1])
print('第-2个item是：', shoplist[-2])
# 切片列表
print('第1至3项是:', shoplist[1:4])
print('第3至最后项是:', shoplist[2:])

#对象与引用
