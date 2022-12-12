import json

filename = 'C:\\Users\\48783\\Desktop\\OJ\\Python\\第 10 章 文件\\7. 使用json.dump()\\numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
    
print(numbers)