line = ""
n = 5
for w in range(2 * n - 1):
    if w < n:
        line += "*"
    else:
        line = line[:-1]
    print(line)
