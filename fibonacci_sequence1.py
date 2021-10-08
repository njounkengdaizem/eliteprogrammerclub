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
    num_b4 = 0  # preceeding number starting from 0
    num_nw = 1  # current number 1
    total = 0  # total initialized to zero

    while num_nw <= num:
        """While loop computes the sum of all odd numbers in the given series"""
        if num_nw % 2 != 0:
            total = total + num_nw
        num_nw = num_nw + num_b4
        num_b4 = num_nw - num_b4
    return total

def main():

    user_input = int(input("Enter a number to compute the sum of all odd number in that sequence: "))
    odd_total = fib(user_input)
    print("The sum:{} " .format(odd_total))

main()
