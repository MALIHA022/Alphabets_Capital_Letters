'''P'''
size = int(input("Enter a size: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        if col==1 or row==1 or row== ((num+1)//2) or col==num :
            sign = "*"
            if (col==num and row> ((num+1)//2)) or (col==num and (row==1 or row==((num+1)//2))):
                sign = " "
            print(sign,end="")
        else:
            sign = " "
            print(sign,end="")
    print()    
    
