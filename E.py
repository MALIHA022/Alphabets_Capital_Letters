'''E'''    
size = int(input("Enter a number: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        
        value = (num+1)//2
        if (row == 1 ) or col == 1 or row==var or row == num:
            if size%2 == 0:
                var = value +1  
                row == var 
            else:
                var = value
                row == var
            print("*" , end="")

        else:
            print(" ",end="")
    print()
