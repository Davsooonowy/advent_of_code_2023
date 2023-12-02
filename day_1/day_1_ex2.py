    #2 exercise from 1.12

f = open("ex1text.txt", "r")
digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
text_to_number = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
digit_arr = []
content = f.readlines()
for i in range(len(content)):
        for word, number in text_to_number.items():
            content[i] = content[i].replace(word, word[0] + number + word[-1])
print(content)
for i in range(len(content)):
    result = ''.join(char for char in content[i] if char in digits)
    digit_arr.append(result)
f.close()
print(digit_arr)
res = 0
for i in digit_arr:
    if len(i) == 1:
        j = int(i)
        res += 10*j + j
    else:
        res += 10 * int(i[0]) + int(i[-1])
print(res)

