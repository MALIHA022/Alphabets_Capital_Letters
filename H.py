'''H'''
size = int(input("Enter the size of your alphabet: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        if col == 1 or col == num or row == ((num+1)//2):
            sign = "*"
            
        else:
            sign = " "
        print(sign, end="")
        
    print()
