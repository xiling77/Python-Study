import json

numbers = [2,3,5,7,11,13]

#只有U和数字前面需要双斜杠
filename = 'C:\\Users\\48783\\Desktop\\OJ\\Python\\第 10 章 文件\\7. 使用json.dump()\\numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)