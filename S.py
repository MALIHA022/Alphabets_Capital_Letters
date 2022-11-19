'''S'''

size = int(input("Enter a size: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        tip = (num+1)//2
        if row==1 or row==num or row==tip or (col==1 and row<=tip) or (col==num and row>=tip):            
            sign = "*"
            if (row==1 and col==1) or (col==num and  row==num):
                sign = " "
            print(sign,end="")
        else:
            sign = " "
            print(sign,end="")
    print()  
