'''X'''

value = int(input("Enter a number: "))
num = value

for row in range(1,num+1):
    for col in range(1,num+1):
        hint = row+col
        if row == col or hint == num+1:
            print("*" , end="")
        else:
            print(" ",end="")
    
    print()
