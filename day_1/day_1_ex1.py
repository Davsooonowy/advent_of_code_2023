#1st start exercise

f = open("ex1text.txt", "r")
digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
digit_arr = []
content = f.readlines()
for i in range(len(content)):
    result = ''.join(char for char in content[i] if char in digits)
    digit_arr.append(result)
f.close()
res = 0
for i in digit_arr:
    if len(i) == 1:
        j = int(i)
        res += 10*j + j
    else:
        res += 10 * int(i[0]) + int(i[-1])
print(res)
