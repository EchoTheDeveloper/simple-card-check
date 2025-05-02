import sys  

num = input("Enter Card Number: ")

if len(num) != 16:
    print("Card number is not a valid card number! Must be 16 digits!")
    sys.exit()

r_num = num[::-1]
total = 0

for i in range(0, len(r_num)):
    digit = int(r_num[i])
    if i % 2 == 0:
        total = total + (digit * 2)
    else:
        total = total + int(digit)

if total % 1 == 0:
    print("This is a valid card number")
else:
    print("This is not a valid card number")

