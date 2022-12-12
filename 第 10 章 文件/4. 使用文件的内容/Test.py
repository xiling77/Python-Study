filename = "C:\\Users\\48783\\Desktop\\OJ\\Python\\第 10 章 文件\\4. 使用文件的内容\\in.txt"

with open(filename) as file_object:
    lines =file_object.readlines()
    
pi_string = ''
for line in lines:
    #pi_string += line.rstrip()
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))
