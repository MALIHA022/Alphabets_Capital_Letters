'''J'''

size = int(input("Enter the size of your alphabet: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        if row == 1 or row == num or (col==1 and row== num-1) or col == num:
            sign = "*"
            if (row==num and col==num) or (row==num and col==1):
                sign = " "
            
        else:
            sign = " "
        print(sign, end="")
        
    print()
