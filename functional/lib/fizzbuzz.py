def if_ver(num):
    if num % 3 == 0 and num % 5 == 0:
        result = "FizzBuzz"
    elif num % 3 == 0:
        result = "Fizz"
    elif num % 5 == 0:
        result = "Buzz"
    else:
        result = str(num)
    return result

def ternary_ver(num):
    result = "FizzBuzz" if num % 3 == 0 and num % 5 == 0 else "Fizz" if num % 3 == 0 else "Buzz" if num % 5 == 0 else str(num)
    return result

# for i in range(1, 101):
#     print if_ver(i)
#
# for i in range(1, 101):
#     print ternary_ver(i)
