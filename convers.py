# перевод числа из одной систмы счисления в десятиричную
print ("input a decimal number: ")
num10 = int(input())
print ("input a base of conversion (from 2 to 16): ")
basenum = int (input ())
num2 = ''
dic = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
while num10 > 0:
    if (num10 % basenum) < 10:
        num2 = str(num10 % basenum) + num2
    else: num2 = dic[num10 % basenum] + num2
    num10 = num10 // basenum
print (num2)
