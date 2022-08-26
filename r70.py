
#print('cs' + 'ip' if '234'.isdigit() else 'IT' + '-402')



#71
def fib(n):
    p, q = 0, 1
    while(p < n):
        yield p
        p, q = q, p + q
x = fib(10

