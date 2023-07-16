def problem_2(a):
    b = ''
    for i in range(a):
        b = b + str(((2*i) + 1)) + ','
    print(b[:-1])

a = int(input())
problem_2(a)
