'''D'''
size = int(input("Enter a number: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):

        if row == 1 or col == 1 or col == num or row == num:
            sign = "*"
            
            if col == num and (row==1 or row == num):
                sign = " "
            
            print(sign ,end="")
            
        else:
            print("",end=" ")
    print()
