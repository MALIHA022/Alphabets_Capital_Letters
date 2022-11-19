'''Y'''

size = int(input("Enter a size: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        tip = (num+1)//2
        if ((row == col and col <= tip) or ((row+col) == num+1) and col >= tip or (col==tip and row>= tip)):   
            
            sign = "*"
            print(sign,end="")
        else:
            sign = " "
            print(sign,end="")
    print()   
