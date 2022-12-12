number = input()
number = int(number)

if(number % 2 == 0):
    print("\nThe number " + str(number) + " is even.")          #输出时必须是string 格式
else:
    print("\nThe number " + str(number) + " is odd.")