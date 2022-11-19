'''B'''

size = int(input("Enter a number: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        value = (num+1)//2
        if row == 1 or col == 1 or col ==num or row==value or row == num:
            sign = "*"
            if col == num and (row==1 or row == num or row == (num+1)//2):
                sign = " "
                
            if size%2 == 0:
                var = value +1  
                row == var 
            else:
                var = value
                row == var
            print(sign , end="")
            
        else:
            print(" ",end="")
    print()
