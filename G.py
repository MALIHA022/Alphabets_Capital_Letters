'''G'''
size = int(input("Enter a number: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        
        if row == 1 or col == 1 or row ==num or (row == 2 and col == num) or (row == (num-1) and col==num) or (row==(num-1) and (col== num-1 or col==num or col== num-2)):
            sign = "*"
            
            if (row == (num+1)//2 and col ==num) or (row == 1 and col== num) or (row == num and col == num) or (row==1 and col==1) or (row==num and col==1): 
               sign = " "
               
            print(sign, end="")
        else:
            print(" ",end="")
    print()
