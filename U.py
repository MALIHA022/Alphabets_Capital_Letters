'''U'''

size = int(input("Enter a size: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        if row== num or col==1 or col==num:   
            sign = "*"
            if row==num and (col==1 or col==num):
                sign = " "
            print(sign,end="")
        else:
            sign = " "
            print(sign,end="")
    print()  
