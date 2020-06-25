# Express the status of "crazy" with '!'

def go_crazy_if_ver(num):
    if num % 3 == 0 or "3" in str(num):
        result = str(num) + "!"
    else:
        result = str(num)
    return result

def go_crazy_ternary_ver(num):
    result = str(num) + "!" if num % 3 == 0 or "3" in str(num) else str(num)
    return result

# for i in range(1, 41):
#     print go_crazy_if_ver(i)
#
# for i in range(1, 41):
#     print go_crazy_ternary_ver(i)
