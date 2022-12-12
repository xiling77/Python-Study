filename = "C:\\Users\\48783\\Desktop\\OJ\\Python\\第 10 章 文件\\2. 逐行读取\\in.txt"

with open(filename) as file_object:
    lines =file_object.readlines()
    
for line in lines:
    print(line.rstrip())