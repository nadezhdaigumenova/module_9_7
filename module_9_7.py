
def is_prime(func):
    def wrapper(*args):
        summ = func(*args)
        k = 0
        for i in range(2, summ // 2 + 1):
            if (summ % i == 0):
                k = k + 1
        if (k <= 0):
           print("Простое")
           return summ
        else:
            print('Составное')
            return summ
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2,3,6)
print(result)