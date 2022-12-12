filename = "C:\\Users\\48783\\Desktop\\OJ\\Python\\第 10 章 文件\\2. 逐行读取\\in.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
        #print(line.rstrip())