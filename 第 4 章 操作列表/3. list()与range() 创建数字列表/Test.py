numbers = list(range(1,6))

print(numbers)


#2表示步长为2
step = 2
even_numbers = list(range(2,11,step))
print(even_numbers)


#例：将十个数的平方加入列表中
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

#例：
squares_1 = []
for value in range(1,11):
    squares_1.append(value ** 2)
print(squares_1)