##################################################################
# Given a positive integer num, return
# the sum of all odd Fibonacci numbers that are less than or equal to num.
# What is a fibonacci_number: https://en.wikipedia.org/wiki/Fibonacci_number
####################################################################
def fib(num):
    """Function that collects user's number choice an
     computes the sum of odd fibonacci numbers in the sequence
     :param num
     """
    previous = 0  # preceeding number starting from 0
    current = 1  # current number 1
    total = 0  # total initialized to zero
    list = []
    while current <= num:
        list.append(current)
        """While loop computes the sum of all odd numbers in the given series"""
        if current % 2 != 0:
            total = total + current
        current += previous
        previous = current - previous
    return total


def main():

    user_input = int(input("Enter a number to compute the sum of all odd number in that sequence: "))
    odd_total = fib(user_input)
    print("The sum:{} " .format(odd_total))


if __name__ == "__main__":
    main()
