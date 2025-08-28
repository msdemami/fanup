def is_prime(number):
    
    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True

# تست تابع
num=int(input(" number : "))
result = is_prime(num)

print(f"ورودی: {num}")
print(f"خروجی: {result}")

test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for n in test_numbers:
    print(f"{n}: {is_prime(n)}")