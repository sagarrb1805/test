strip_nums = {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:5}


num = int(input('enter the number: '))

strip_count = 0
while num > 0:
    digit = num%10
    if digit in strip_nums.keys():
        strip_count += strip_nums[digit]
    num = num//10
print(strip_count)