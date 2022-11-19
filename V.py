'''V'''

size = int(input("Enter a size: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        hint = row+col
        if row == col:
            print("*" , end="")
        else: 
            print(" ",end="")
    for col in range(1,num+1):
        hint = row+col
        if hint == num+1:
            print("*" , end="")
        else: 
            print(" ",end="")
    print()    
