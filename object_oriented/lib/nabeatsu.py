# Express the status of "crazy" with '!'

class Nabeatsu:
    def __init__(self):
        pass

    def go_crazy_if_ver(self, num):
        if num % 3 == 0 or "3" in str(num):
            result = str(num) + "!"
        else:
            result = str(num)
        return result

    def go_crazy_ternary_ver(self, num):
        result = str(num) + "!" if num % 3 == 0 or "3" in str(num) else str(num)
        return result
