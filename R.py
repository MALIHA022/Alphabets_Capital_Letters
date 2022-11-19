'''R'''

size = int(input("Enter a size: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        if col==1 or row==1 or row== ((num+1)//2) or col==num or (row>=((num+1)//2) and row==col):
            sign = "*"
            if (col==num and row> ((num+1)//2) and row<num) or (col==num and (row==1 or row==((num+1)//2))):
                sign = " "
            print(sign,end="")
        else:
            sign = " "
            print(sign,end="")
    print()    
