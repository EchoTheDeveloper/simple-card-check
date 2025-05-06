import sys

num = input("Enter Card Number: ")

if len(num) != 16 or not num.isdigit():
    print("Card number is not a valid card number! Must be 16 digits!")
    sys.exit()

r_num = num[::-1]
total = 0

for i in range(len(r_num)):
    digit = int(r_num[i])
    if i % 2 == 1:
        digit *= 2
        if digit > 9:
            digit -= 9
    total += digit

if total % 10 == 0:
    print("This is a valid card number")
else:
    print("This is not a valid card number")
