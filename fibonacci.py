

def caching_fibonacci(cache=None):
    if cache is None:
        cache = {}  #створення кешу
    def fibonacci(n):
     # Базові випадки 
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        # якщо значення вже обчислено,повертаємо його з кешу
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)   # Рекурсивний розрахунок з кешуванням
        return cache[n]
    return fibonacci

def main():
    fib = caching_fibonacci()
    print(fib(10))

if __name__=="__main__":
    main()
