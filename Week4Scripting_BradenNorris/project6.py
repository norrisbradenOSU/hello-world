iteration = int(input("Iterations: "))
check = 0
x = 1
sign = True
for i in range(iteration):
    check = check + 1 / x if sign else check - 1 / x
    x += 2
    sign = not sign
pi = check * 4
print(pi)