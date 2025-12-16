import math
calculations = []

line_chars_len = 0
with open("input.txt", "r") as file:
    for line in file:
        line = line.rstrip("\n")
        line_chars_len = len(line)
        calculations.append(line)
        
total = 0
current_sign = None
nums = []

for i in range(line_chars_len):
    dig_1 = calculations[0][i]
    dig_2 = calculations[1][i]
    dig_3 = calculations[2][i]
    dig_4 = calculations[3][i]
    sign = calculations[4][i]

    if dig_1 == dig_2 == dig_3 == dig_4 == sign == " ":

        if current_sign == "+":
            total += sum(nums)
        else:
            total += math.prod(nums)
        
        current_sign = None
        nums = []
        continue
            
    if current_sign is None:
        current_sign = sign
    
    digits = []
        
    if dig_1 != " ":
        digits.append(int(dig_1))
        
    if dig_2 != " ":
        digits.append(int(dig_2))
        
    if dig_3 != " ":
        digits.append(int(dig_3))
        
    if dig_4 != " ":
        digits.append(int(dig_4))


    if len(digits) == 1:
        number = (digits[0])
        
    elif len(digits) == 2:
        number = (digits[0] * 1 + digits[1] * 10)
        
    elif len(digits) == 3:
        number = (digits[0] * 1 + digits[1] * 10 + digits[2] * 100)
        
    else:
        number = (digits[0] * 1 + digits[1] * 10 + digits[2] * 100 + digits[3] * 1000)

    number = int(str(number)[::-1])
    nums.append(number)
        
if current_sign == "+":
    total += sum(nums)
else:
    total += math.prod(nums)
    
print(total)
