print ("input a decimal number: ")
num10 = int(input())
num2 = ''
while num10 > 0:
    num2 = str(num10 % 2) + num2
    num10 = num10 // 2
print (num2)
