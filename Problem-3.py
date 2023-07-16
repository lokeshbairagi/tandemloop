def problem_3(a):
    b = ''
    if a % 2 == 0:
        a = a-1
    for i in range(a):
        b = b + str(((2*i) + 1)) + ','
    print(b[:-1])

a = int(input())
problem_3(a)
