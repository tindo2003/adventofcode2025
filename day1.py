arr = []
with open('/Users/tindo/Downloads/input.txt', 'r') as file:
    for line in file:
        arr.append(line.strip())
# arr = ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]
res, cur = 0 , 50
for op in arr:
    direction = -1 if (op[0] == "L") else 1
    num = int(op[1:])
    new_cur = (cur + direction * num)
    cur = new_cur % 100
    if cur == 0: res += 1
print(res)