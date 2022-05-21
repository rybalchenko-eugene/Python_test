print ("input a decimal number: ")
num10 = int(input())
print ("input a base of conversion (from 2 to 9): ")
basenum = int (input ())
num2 = ''
while num10 > 0:
    num2 = str(num10 % basenum) + num2
    num10 = num10 // basenum
print (num2)
