'''Z'''

value = int(input("Enter a number: "))
num = value

for row in range(1,num+1):
    for col in range(1,num+1):
        hint = row+col
        if hint == num+1 or row == 1 or row == num:
            print("*" , end="")
        else:
            print(" ",end="")
    
    print()
