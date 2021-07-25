def facto():
    i, fact = 1, 1
    while i > 0:
        fact *= i
        yield fact                  # Yields each factorial value once a time 
        i += 1

x = facto()             # generator object

for i in range(7):
    print(next(x))                  # next() --> helps to print the value for generator object

def fibo():
    a,b = 0,1
    while a+b > 0:
        yield a
        a,b = b, a+b

y = fibo()

print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
