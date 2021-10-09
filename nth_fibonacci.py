# program that returns the nth number in the fibonacci sequence

def nth_fib(n):
    previous = 0
    current = 1
    list = []
    for i in range(n):
        list.append(current)
        current += previous                                     # new current number by adding two preceeding numbers
        previous = current - previous                   # updates previous number by subtracting previous from current
    return list[n-1]                                                 # returns the nth number in the sequence

print(nth_fib(1))
print(nth_fib(20))
print(nth_fib(100))
print(nth_fib(1000))
