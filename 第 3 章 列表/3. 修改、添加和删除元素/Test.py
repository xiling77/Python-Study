bicycles = ['trek','cannodale','redline','specialized']

#修改：
bicycles[0] = 'ducati'

#添加：
bicycles.append('ducati')               #列表中可以有两个值相同的元素

#插入
bicycles.insert(0,'ducati')             #将列表中的元素插入在索引处

#删除
del bicycles[0]                          #将索引处元素删除

#pop删除
poped_bicycle = bicycles.pop()          #弹出列表最末端元素并返回

#pop删除x处
x = 1
poped_bicycle = bicycles.pop(x)          #弹出列表 x 处元素并返回

#根据值删除,只删除第一个指定的值
bicycles.remove('redline')

print(bicycles)