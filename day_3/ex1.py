def is_valid_position(i, l, n):
    return 0 <= i + n[0] < len(content) and 0 <= l + n[1] < len(content[i])


def is_valid_symbol(i, l, n):
    return content[i + n[0]][l + n[1]] not in digits and content[i + n[0]][l + n[1]] != '.'


def solution(content, digits, vectors, adjective_numbers):
    for i in range(len(content)):
        j = 0
        while j < len(content[i]):
            if content[i][j] in digits:
                digit_len, start = 1, j
                while j < len(content[i]) - 1 and content[i][j + 1] in digits:
                    digit_len += 1
                    j += 1
                flag = False
                for l in range(start, start + digit_len):
                    for n in vectors:
                        if is_valid_position(i, l, n) and is_valid_symbol(i, l, n):
                            adjective_numbers.append(int(content[i][start: start + digit_len]))
                            flag = True
                            break
                    if flag:
                        break
            j += 1
    return sum(adjective_numbers)


with open("input.txt", "r") as f:
    content = f.readlines()

content = [line.strip() for line in content]
digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
vectors = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
adjective_numbers = []