def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result < 2:
            print("Составное")
        else:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i ==0:
                    return ("Составное")
                else:
                    return ("Простое")
    return wrapper



@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 10, 6)
print(result)

