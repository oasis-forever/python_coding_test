class FizzBuzz:
    def __init__(self):
        self

    def if_ver(self, num):
        if num % 3 == 0 and num % 5 == 0:
            result = "FizzBuzz"
        elif num % 3 == 0:
            result = "Fizz"
        elif num % 5 == 0:
            result = "Buzz"
        else:
            result = str(num)
        return result

    def ternary_ver(self, num):
        result = "FizzBuzz" if num % 3 == 0 and num % 5 == 0 else "Fizz" if num % 3 == 0 else "Buzz" if num % 5 == 0 else str(num)
        return result
